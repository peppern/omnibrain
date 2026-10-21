# Appendix: correlation of energy and copper instruments with AI equities (agent calculation)

For the [2026-10-21 review packet](2026-10-21-ai-exposure-via-energy-commodities.md) of `ai-exposure-via-energy-commodities`.

> This is Waffle's own calculation, not a quoted source, so it is **not** in the evidence ledger and passed no quote check. Data: Yahoo Finance daily closes, adjusted for splits and dividends, fetched 2026-10-21 11:15 SGT with `yfinance`. Window: 2023-01-04 to 2026-10-20 (GEV from its 2024-03-27 listing). Daily simple returns; correlation and beta are against SMH (semiconductor ETF) unless noted. Past co-movement does not predict future co-movement.

## Full window

| Instrument | Corr. SMH | Corr. NVDA | Corr. SPY | Beta to SMH | Annualised vol | Total return |
| --- | --- | --- | --- | --- | --- | --- |
| Copper futures (HG=F) | 0.28 | 0.18 | 0.25 | 0.22 | 28% | +76% |
| CPER | 0.36 | 0.24 | 0.38 | 0.27 | 27% | +74% |
| COPX | 0.53 | 0.33 | 0.55 | 0.55 | 37% | +138% |
| URA | 0.52 | 0.39 | 0.50 | 0.60 | 41% | +101% |
| XLU | 0.10 | 0.02 | 0.34 | 0.05 | 16% | +33% |
| VST | 0.49 | 0.43 | 0.46 | 0.72 | 53% | +608% |
| CEG | 0.48 | 0.41 | 0.47 | 0.64 | 48% | +225% |
| GEV | 0.61 | 0.52 | 0.55 | 0.99 | 53% | +581% |

## By calendar year (correlation with SMH)

| Year | HG=F | CPER | COPX | URA | XLU | VST | CEG | GEV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2023 | 0.26 | 0.28 | 0.44 | 0.29 | 0.10 | 0.16 | 0.32 | — |
| 2024 | 0.24 | 0.28 | 0.37 | 0.45 | -0.10 | 0.44 | 0.39 | 0.49 |
| 2025 | 0.22 | 0.33 | 0.62 | 0.56 | 0.38 | 0.69 | 0.71 | 0.68 |
| 2026 YTD | 0.46 | 0.52 | 0.63 | 0.65 | 0.02 | 0.44 | 0.37 | 0.63 |

## DeepSeek day, 2025-01-27 (one-day return)

VST -28.3%, GEV -21.5%, CEG -20.8%, NVDA -17.0%, URA -11.2%, SMH -9.8%, XLU -2.3%, COPX -2.1%, HG=F -2.0%, CPER -1.9%, SPY -1.4%.

## Reading

Power producers and turbine/grid equipment moved with AI equities, increasingly so in 2025, and fell harder than NVDA on the DeepSeek efficiency shock: they are already priced as AI beta. Copper futures and CPER have low correlation and beta to semis and barely moved on the DeepSeek day: they are liquid and cheap to hold, but mostly not AI exposure. Copper's correlation with semis rose in 2026, which is worth re-checking next cycle.

## Code

```python
import pandas as pd, yfinance as yf
tickers = ["NVDA","SMH","COPX","CPER","URA","XLU","VST","CEG","GEV","HG=F","SPY"]
d = yf.download(tickers, start="2023-01-01", end="2026-10-21", progress=False, auto_adjust=True)["Close"]
r = d.pct_change(fill_method=None)
cols = ["HG=F","CPER","COPX","URA","XLU","VST","CEG","GEV"]
out = pd.DataFrame({"corr_SMH": r[cols].corrwith(r["SMH"]), "corr_NVDA": r[cols].corrwith(r["NVDA"]),
                    "corr_SPY": r[cols].corrwith(r["SPY"])})
out["beta_SMH"] = [r[c].cov(r["SMH"]) / r["SMH"].var() for c in cols]
out["ann_vol"] = r[cols].std() * 252 ** 0.5
out["total_return"] = [d[c].dropna().iloc[-1] / d[c].dropna().iloc[0] - 1 for c in cols]
print(out.round(2)); print(r.loc["2025-01-27"].round(3))
for y in ["2023","2024","2025","2026"]:
    print(y, r.loc[y, cols].corrwith(r.loc[y, "SMH"]).round(2).to_dict())
```
