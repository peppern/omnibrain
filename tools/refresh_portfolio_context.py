"""Publish coarse portfolio context; keep all balances in FamilyFin."""
from __future__ import annotations

import argparse
from datetime import date
from decimal import Decimal, InvalidOperation
import json
from pathlib import Path
import sqlite3
import sys


def load_rows(period):
    db = period / "data/canonical.db"
    with sqlite3.connect(db.resolve().as_uri() + "?mode=ro", uri=True) as conn:
        conn.row_factory = sqlite3.Row
        run = conn.execute("""
            SELECT run_id FROM pipeline_runs
            WHERE stage = 'ingest' AND status = 'completed'
            ORDER BY ended_at DESC, started_at DESC LIMIT 1
        """).fetchone()
        if not run:
            raise ValueError("Period has no completed ingest; choose a populated period explicitly")
        if conn.execute("""
            SELECT COUNT(*) FROM validation_issues
            WHERE ingest_run_id = ? AND severity = 'error'
        """, (run["run_id"],)).fetchone()[0]:
            raise ValueError("Ingest has unresolved validation errors")
        rows = conn.execute("""
            SELECT h.*, a.name, a.ticker, a.asset_type AS investment_type,
                   ac.name AS account_name
            FROM holdings h
            JOIN assets a ON a.asset_id = h.asset_id
            JOIN accounts ac ON ac.account_id = h.account_id
            WHERE h.ingest_run_id = ? ORDER BY h.holding_id
        """, (run["run_id"],)).fetchall()
        return [dict(row) for row in rows], run["run_id"]


def summarize(rows, period_name, run_id, generated_on):
    groups = {}
    excluded = {"direct_real_estate": 0, "liabilities": 0, "zero_value": 0}
    total = Decimal(0)
    for row in rows:
        if row["source_kind"] == "state_md_liability":
            excluded["liabilities"] += 1
            continue
        # Direct property is outside this financial-assets denominator. REITs remain.
        if row["investment_type"].casefold() == "real estate":
            excluded["direct_real_estate"] += 1
            continue
        try:
            value = Decimal(str(row["value"]))
        except InvalidOperation as exc:
            raise ValueError("Missing or invalid asset value; review in FamilyFin") from exc
        if not value.is_finite() or value < 0:
            raise ValueError("Missing, nonfinite or negative asset value; review in FamilyFin")
        if row["currency"] != "USD":
            raise ValueError("Values must already be in USD; this exporter does not convert FX")
        if value == 0:
            excluded["zero_value"] += 1
            continue
        as_of = row["as_of_date"]
        if not as_of or date.fromisoformat(as_of) > date.fromisoformat(generated_on):
            raise ValueError("Missing or future source date; review in FamilyFin")
        ticker = (row["ticker"] or "").strip().upper()
        name = " ".join(row["name"].split())
        basis = "derived from recorded statement value"
        if row["source_kind"] != "statement":
            basis = "derived from carried manual value; valuation uncertainty unquantified"
        if name.startswith("FREC account total"):
            key, name, ticker = "frec-sleeve", "Frec portfolio (constituents not available)", ""
            basis = "derived from manually transcribed total; date attributed by operator"
        elif ticker == "CASH":
            key, name = "brokerage-cash", "Brokerage cash and accrued income"
        else:
            key = "ticker:" + ticker if ticker else "asset:" + row["asset_id"]
        group = groups.setdefault(key, {"name": name, "ticker": ticker or None,
                                       "dates": set(), "bases": set(), "value": Decimal(0)})
        group["value"] += value
        group["dates"].add(as_of)
        group["bases"].add(basis)
        total += value
    if total <= 0:
        raise ValueError("No positive financial assets to summarize")
    if sum((g["value"] for g in groups.values()), Decimal(0)) != total:
        raise ValueError("Grouped values do not reconcile to eligible source values")
    positions = []
    for group in groups.values():
        weight = group["value"] / total
        band = "large" if weight >= Decimal("0.05") else "medium" if weight >= Decimal("0.01") else "small"
        positions.append({"name": group["name"], "ticker": group["ticker"], "size": band,
                          "source_dates": sorted(group["dates"]), "basis": sorted(group["bases"])})
    order = {"large": 0, "medium": 1, "small": 2}
    positions.sort(key=lambda p: (order[p["size"]], p["ticker"] or p["name"]))
    # An allowlist of output fields prevents balances, quantities, IDs and account
    # details from leaking through a future addition to the canonical query.
    return {"schema_version": 1, "household": "NHP", "generated_on": generated_on,
            "source_period": period_name, "source_ingest_run": run_id,
            "size_basis": "Recorded USD financial assets, including cash and private holdings; excluding direct real estate and liabilities",
            "size_status": "historical and provisional; private-mark uncertainty is unquantified and affects every band through the denominator",
            "coverage_limits": ["Frec and startup-basket constituents are unknown",
                                "Fund look-through and bank balances outside ingest are not represented",
                                "Absence is not proof of no exposure; current holdings and funding require refreshed FamilyFin evidence"],
            "bands": {"large": ">=5%", "medium": ">=1% and <5%", "small": "<1%"},
            "excluded_row_counts": excluded, "positions": positions}


def render(data):
    lines = ["# NHP portfolio holdings", "",
             f"Generated {data['generated_on']} from FamilyFin `{data['source_period']}`. This is a historical snapshot, not live holdings.", "",
             "Large: ≥5% · Medium: ≥1% and <5% · Small: <1% of recorded financial assets. These are descriptive export bands, not approved allocation targets, conviction ratings or trade sizes.", "",
             "Includes retirement accounts, brokerage cash and carried private holdings. Direct real estate and liabilities are excluded. Identical tickers are combined across accounts; share classes remain separate. Cash balances and accrued income are one sleeve. No fund look-through or issuer-level concentration is implied.", "",
             "**Coverage limits:** Frec is an opaque account total, not a security; its underlying holdings are unknown here. Private positions use older manual marks with unquantified uncertainty. Every band is provisional because those marks affect the denominator. Small means small relative to this denominator, not unimportant or low risk. Statement labels may be truncated. Bank accounts outside the ingest and undisclosed constituents are not represented; absence is not proof of no exposure.", "",
             "| Holding / statement label | Ticker or security ID | Position size | Source date(s) |",
             "| --- | --- | --- | --- |"]
    for p in data["positions"]:
        name = p["name"].replace("|", "\\|").replace("\n", " ")
        lines.append(f"| {name} | {p['ticker'] or '—'} | {p['size'].capitalize()} | {', '.join(p['source_dates'])} |")
    lines += ["", "Source and per-position basis: [holdings.json](holdings.json). Refresh and usage: [README](README.md).", ""]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--familyfin", required=True, type=Path)
    parser.add_argument("--period", required=True, help="Explicit NHP period with completed ingest")
    args = parser.parse_args()
    if not args.period.startswith("nhp_") or Path(args.period).name != args.period:
        parser.error("Use a single NHP period directory name")
    sys.path.insert(0, str(args.familyfin.resolve()))
    import pandas as pd
    from report_gen.portfolio_view import collapse_overlapping_statement_snapshots

    rows, run_id = load_rows(args.familyfin / args.period)
    frame, _ = collapse_overlapping_statement_snapshots(pd.DataFrame(rows))
    data = summarize(frame.to_dict("records"), args.period, run_id, date.today().isoformat())
    output = Path(__file__).resolve().parents[1] / "research/investing/portfolio"
    output.mkdir(parents=True, exist_ok=True)
    (output / "holdings.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    (output / "holdings.md").write_text(render(data), encoding="utf-8")
    print(f"Published {len(data['positions'])} coarse holdings to {output}")


if __name__ == "__main__":
    main()
