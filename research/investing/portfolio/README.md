# Portfolio context

Read [NHP holdings and position sizes](holdings.md) before researching an existing holding or discussing a new portfolio idea. [holdings.json](holdings.json) is the same compact data for agents, including each position's source dates and sizing basis.

This covers the NHP household only; Robert and Linda's RLP portfolio is separate. The initial export uses the latest populated NHP canonical ingest, August 2026. September has no completed ingest at publication on 2026-10-21. Statement holdings are dated 2026-08-31; Stripe and the undisclosed startup basket retain their 2026-05-23 manual marks. Frec's date was attributed by the operator to an undated screenshot. No current October portfolio is claimed.

Size means share of recorded USD financial assets: **large ≥5%, medium ≥1% and <5%, small <1%**. The denominator includes cash, retirement assets, private positions and the opaque Frec sleeve; direct real estate and liabilities are excluded. These export conventions are descriptive, not family policy or permission to transact. Private-mark uncertainty is unquantified, so the labels are provisional; no claim is made that every label would survive revaluation. Exact weights, balances, quantities, cost bases, tax lots, account identifiers and property addresses stay in FamilyFin.

Frec constituents, individual startup investments and fund look-through are unknown in this view. A ticker missing here can still be held inside a fund or an opaque sleeve. Bank balances outside the holdings ingest are not included. This context helps set research relevance; it cannot establish funding availability, tax effects or an actionable trade size. Consult FamilyFin for those questions and refresh stale evidence first.

## Refresh

The FamilyFin canonical SQLite store remains the source of truth. These two files are generated snapshots, outside the Omniscience content-track exporter; do not hand-edit them. This is an explicit refresh command, not an activated schedule. After a new NHP ingest completes, run from the Omnibrain root, using FamilyFin's environment:

```sh
/Users/np/projects/familyfin/.venv/bin/python tools/refresh_portfolio_context.py \
  --familyfin /Users/np/projects/familyfin --period nhp_2026-08
/Users/np/projects/familyfin/.venv/bin/python -m unittest discover \
  -s tools -p 'test_portfolio_context.py'
```

Replace the period explicitly. The exporter reads the latest completed ingest in that period, refuses ingest errors and invalid values/dates/currencies, reuses FamilyFin's overlapping-statement collapse, combines positions, and writes only coarse fields. It never converts FX, refreshes prices or writes to the source database. Review the generated diff before publishing; a newer empty or incomplete period is not a replacement for a populated one.

Source: [FamilyFin](https://github.com/peppern/familyfin), `<period>/data/canonical.db`, with the selected ingest run recorded in JSON. Private marks and the Frec caveat originate in `<period>/state.md`; statements remain under `<period>/source_data/`.
