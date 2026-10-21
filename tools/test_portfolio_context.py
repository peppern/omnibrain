import json
from pathlib import Path
import sqlite3
import tempfile
import unittest

from refresh_portfolio_context import load_rows, render, summarize


def holding(name, ticker, value, **changes):
    row = dict(name=name, ticker=ticker, value=value, asset_id=name,
               source_kind="statement", investment_type="Stock", currency="USD",
               as_of_date="2026-08-31", account_name="PRIVATE-ACCOUNT-123456",
               quantity=987654, source_file="PRIVATE-STATEMENT.pdf")
    row.update(changes)
    return row


class PortfolioContextTests(unittest.TestCase):
    def summarize(self, rows):
        return summarize(rows, "nhp_2026-08", "test-run", "2026-10-21")

    def test_aggregation_band_boundaries_and_privacy(self):
        rows = [holding("Core", "CORE", 940), holding("Split", "SPLIT", 25),
                holding("Split", "SPLIT", 25), holding("One percent", "ONE", 10)]
        data = self.summarize(rows)
        self.assertIn("provisional", data["size_status"])
        self.assertEqual({p["ticker"]: p["size"] for p in data["positions"]},
                         {"CORE": "large", "SPLIT": "large", "ONE": "medium"})
        for output in (json.dumps(data), render(data)):
            for private in ("PRIVATE-ACCOUNT", "PRIVATE-STATEMENT", "987654"):
                self.assertNotIn(private, output)
        self.assertEqual(set(data["positions"][0]), {"name", "ticker", "size", "source_dates", "basis"})
        self.assertEqual(self.summarize(list(reversed(rows))), data)

    def test_small_and_below_five_percent(self):
        data = self.summarize([holding("Core", "CORE", 951), holding("Medium", "MID", 40),
                               holding("Small", "SML", 9)])
        self.assertEqual({p["ticker"]: p["size"] for p in data["positions"]},
                         {"CORE": "large", "MID": "medium", "SML": "small"})

    def test_real_estate_and_debt_do_not_dilute_financial_asset_bands(self):
        data = self.summarize([holding("Core", "CORE", 95), holding("Other", "OTHER", 5),
                               holding("Private street address", "", 100000, investment_type="Real Estate"),
                               holding("Mortgage", "", 100000, source_kind="state_md_liability")])
        self.assertTrue(all(p["size"] == "large" for p in data["positions"]))
        self.assertNotIn("Private street address", json.dumps(data))
        self.assertEqual(data["excluded_row_counts"]["direct_real_estate"], 1)

    def test_opaque_sleeve_redaction_and_carried_dates(self):
        data = self.summarize([holding("FREC account total (Apex Clearing FREC-123456)", "", 10, source_kind="state_md"),
                               holding("Stripe Stock", "", 90, source_kind="state_md", as_of_date="2026-05-23")])
        self.assertNotIn("123456", json.dumps(data))
        stripe = next(p for p in data["positions"] if p["name"] == "Stripe Stock")
        self.assertEqual(stripe["source_dates"], ["2026-05-23"])
        self.assertIn("unquantified", stripe["basis"][0])

    def test_bad_values_dates_and_currencies_fail_instead_of_becoming_small(self):
        for field, value in [("value", None), ("value", float("nan")), ("value", -1),
                             ("as_of_date", None), ("as_of_date", "2027-01-01"), ("currency", "SGD")]:
            with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                self.summarize([holding("Bad", "BAD", 1, **{field: value})] if field != "value"
                               else [holding("Bad", "BAD", value)])

    def test_load_selects_latest_completed_ingest_and_never_writes_source(self):
        with tempfile.TemporaryDirectory() as temp:
            period = Path(temp)
            (period / "data").mkdir()
            db = period / "data/canonical.db"
            with sqlite3.connect(db) as conn:
                conn.executescript("""
                    CREATE TABLE pipeline_runs (run_id, stage, status, ended_at, started_at);
                    CREATE TABLE validation_issues (ingest_run_id, severity);
                    CREATE TABLE accounts (account_id, name);
                    CREATE TABLE assets (asset_id, name, ticker, asset_type);
                    CREATE TABLE holdings (holding_id, account_id, asset_id, ingest_run_id);
                    INSERT INTO pipeline_runs VALUES ('old', 'ingest', 'completed', '2026-08-01', '2026-08-01');
                    INSERT INTO pipeline_runs VALUES ('new', 'ingest', 'completed', '2026-09-01', '2026-09-01');
                    INSERT INTO pipeline_runs VALUES ('failed', 'ingest', 'failed', '2026-10-01', '2026-10-01');
                    INSERT INTO accounts VALUES ('a', 'secret-account');
                    INSERT INTO assets VALUES ('x', 'Asset', 'X', 'Stock');
                    INSERT INTO holdings VALUES ('one', 'a', 'x', 'old');
                    INSERT INTO holdings VALUES ('two', 'a', 'x', 'new');
                """)
            before = db.read_bytes()
            rows, run_id = load_rows(period)
            self.assertEqual(run_id, "new")
            self.assertEqual([r["holding_id"] for r in rows], ["two"])
            self.assertEqual(db.read_bytes(), before)
            with sqlite3.connect(db) as conn:
                conn.execute("INSERT INTO validation_issues VALUES ('new', 'error')")
            with self.assertRaises(ValueError):
                load_rows(period)

    def test_empty_portfolio_does_not_publish(self):
        with self.assertRaises(ValueError):
            self.summarize([])


if __name__ == "__main__":
    unittest.main()
