# Review packet: Bet on AI through energy and commodities — 2026-10-21

`ai-exposure-via-energy-commodities` · cycle 1 · prepared by Waffle (research agent) · 2026-10-21 11:30 SGT

> **How this page was made.** Agent-written from the validated Omniscience state after research run `research-worker-dc5a3867489c`. Every quote below is verbatim from a saved source and passed `omni tracks work answer` quote verification. The one exception is the correlation table, which is the agent's own calculation from public daily prices (method and code in the [appendix](2026-10-21-ai-exposure-via-energy-commodities-correlations.md)). This packet is hand-assembled for this first cycle; a generator is tracked in beads (see the E2E epic in omniscience `docs/e2e/investment-thesis-e2e.md`). Not investment advice; nothing here is a recommendation or a trade.

Generated companions: [thesis page](../../../investment-ideas/theses/ai-exposure-via-energy-commodities.md) · [current view](../../theses/generated-current-views.md#ai-exposure-via-energy-commodities) · [desk review 2026-10-21](../generated-2026-10-21-review.md) · [digest 2026-10-21](../generated-2026-10-21-digest.md)

## 1. Decisions for Noah

1. **Reframe, keep, or close?** The kill criterion (“AI-related demand turns out to be a small share of power or copper demand growth”) is **triggered for copper** and for global power, **not for US power**. Options:
   - **(a) Reframe (agent's suggestion):** narrow to *“Supply-constrained US power generation and grid equipment is the cleanest liquid AI-infrastructure exposure”*, drop copper, and replace “overlooked” with an explicit valuation test.
   - (b) Keep as is and fund cycle 2 (instrument terms, valuation).
   - (c) Close as invalidated (copper leg wrong, power leg already priced).
2. **Conviction:** none set. Agent confidence in this view is *medium*.
3. **Next cycle scope:** approve the two new research tasks below, and say whether cycle 2 should build business assessments for specific names (VST, CEG, TLN, GEV), which is the step before any recommendation.

Reply in chat (or comment on the Omnibrain PR) with e.g. “reframe (a), conviction low, go cycle 2”. Waffle records it with `--by noah --ref <your message>`.

## 2. Claim and current view

**Claim (owner framing, unchanged):** AI buildout demand for power and materials could make energy and commodities such as copper a simple, liquid and leverageable way to get AI exposure that investors are overlooking.

**Status:** active (promoted 2026-10-21 per Noah's chat instruction to drive this thesis end to end). **View direction:** weakened. **Evidence:** 4 supporting, 3 challenging, 4 qualifying.

**Agent view:** The thesis splits in two. The **US power leg is real but crowded**: data centres are nearly half of US electricity demand growth to 2030, listed power producers hold direct AI contracts, and power equipment is supply-constrained, yet those stocks already trade as high-beta AI proxies (more than -20% on the DeepSeek day). The **copper leg is the reverse**: liquid, leverageable and not crowded, but AI is about 2% of 2030 copper demand and the refined market is in surplus through 2027, so copper is mostly *not* AI exposure.

## 3. What changed this cycle

- Promoted candidate → active (owner, 2026-10-21); 4 research questions seeded alongside the original one; all 5 answered.
- 7 sources saved as research notes; 10 new evidence links (3 challenging, 4 qualifying, 3 supporting) on top of the original bookmark.
- Kill criterion moved from *unknown* to *triggered (copper / global power), not triggered (US power)*.
- 2 new research tasks opened (instrument terms; quarterly kill-criterion monitor).

## 4. Answers to the research questions

**Q1. How big is AI demand relative to total power and copper demand growth?** Big for US power, small for global power and copper.
- IEA: “In the United States, data centres account for nearly half of electricity demand growth between now and 2030.”
- LBNL/DOE: “data centers consumed about 4.4% of total U.S. electricity in 2023 and are expected to consume approximately 6.7 to 12% of total U.S. electricity by 2028”
- IEA (global): “Data centres account for around one-tenth of global electricity demand growth to 2030, less than the share from industrial motors, air conditioning in homes and offices, or electric vehicles.”
- IEA (copper, via The Oregon Group): “2% for copper” and “the absolute volumes in 2030 still reach 512 kilotonnes (kt) of copper”
- BNEF (via MINING.COM): “copper demand from the sector will average around 400,000 tonnes annually over the next decade, peaking at 572,000 tonnes in 2028”

**Q2. Which liquid instruments, and how much of each is really AI?**
- Independent power producers have direct AI contracts. CNBC: “Constellation, for example, has signed a power agreement with Microsoft to restart the Three Mile Island nuclear plant” and “Talen is powering an Amazon data center with electricity from the nearby Susquehanna nuclear plant.”
- Grid and turbine equipment is partial AI exposure. GE Vernova 2Q26 call: of its gas gigawatts under contract, “approximately 80% are traditional customers and 20% are for data centers”; Electrification “data center orders to over $5 billion in the first half of 2026, more than double full-year ’25.”
- Copper futures and ETFs are liquid and leverageable, but at ~2% of demand AI does not drive them. Fees, roll costs and margin were **not** researched yet (new task).

**Q3. Do they trade like AI already?** Power names yes, copper no.
- CNBC, 2025-01-27: “Vistra closed nearly 30% lower, erasing its gains for 2025. Constellation Energy, Talen Energy and GE Vernova tumbled more than 20%”
- Agent calculation, daily returns 2023-01-04 to 2026-10-20 ([appendix](2026-10-21-ai-exposure-via-energy-commodities-correlations.md)):

| Instrument | Corr. with SMH | Beta to SMH | DeepSeek day (2025-01-27) | Total return since Jan 2023 |
| --- | --- | --- | --- | --- |
| GEV | 0.61 | 0.99 | -21.5% | +581% (since its Mar 2024 listing) |
| VST | 0.49 | 0.72 | -28.3% | +608% |
| CEG | 0.48 | 0.64 | -20.8% | +225% |
| URA | 0.52 | 0.60 | -11.2% | +101% |
| COPX | 0.53 | 0.55 | -2.1% | +138% |
| CPER | 0.36 | 0.27 | -1.9% | +74% |
| Copper futures (HG=F) | 0.28 | 0.22 | -2.0% | +76% |
| XLU | 0.10 | 0.05 | -2.3% | +33% |
| *NVDA / SMH (reference)* | | | *-17.0% / -9.8%* | |

**Q4. What constrains supply (where does demand become price)?** Power equipment, not near-term copper.
- IEA: “wait times for critical grid components such as transformers and cables have doubled in the past three years” and “Turbine deliveries for new gas-fired power plants now face lead times of several years”
- GE Vernova: “now have agreements signed into ’31”
- ICSG (Reuters via Mining Weekly, 2026-10-15): “the global refined copper market would remain in surplus through 2027, with it widening from about 104 000 metric tons in 2026 to 368 000 metric tons in 2027”
- Counterpoint, long horizon only: BNEF sees AI “potentially pushing the supply shortfall to 6 million tonnes by 2035”

**Q5. What would prove it wrong?**
- Efficiency: IEA High Efficiency Case, “electricity demand from data centres is 20% lower in 2035 than in the Base Case”, with a 2035 range that “spans from 700 to 1 700 TWh”. DeepSeek showed how fast the market reprices on efficiency news.
- Copper: already near its kill line (2% share, near-term surplus).
- “Overlooked”: fails while power names keep a beta to semis of 0.6–1.0.

## 5. Risks and kill criteria

| Kill criterion / risk | Status | Basis |
| --- | --- | --- |
| AI-related demand turns out to be a small share of power or copper demand growth | **Triggered** for copper and global power; **not triggered** for US power | IEA ~2% copper, ~1/10 of global power growth; ~1/2 of US power growth |
| AI capex slows or is already priced into energy and copper | Partly evidenced (priced) for power equities | DeepSeek-day moves, betas, +225% to +608% returns |
| Commodity prices are driven mostly by factors unrelated to AI | Evidenced for copper | ICSG surplus; AI ~2% of demand |

Suggested sharper kill criteria if reframed (agent proposal, Noah to approve): (1) US utility large-load interconnection requests or hyperscaler capex guidance fall for two consecutive quarters; (2) GE Vernova data-center share of gas gigawatts under contract stops growing; (3) beta of the basket to SMH stays above 0.8 (thesis is just AI beta, not a distinct exposure).

## 6. Sources (saved research notes)

| Note | Source | Published |
| --- | --- | --- |
| `2026-10-21-iea-energy-and-ai` | [IEA, Energy and AI: Executive summary](https://www.iea.org/reports/energy-and-ai/executive-summary) | 2025-04-10 |
| `2026-10-21-doe-lbnl-2024` | [US DOE on the LBNL 2024 data center report](https://www.energy.gov/articles/doe-releases-new-report-evaluating-increase-electricity-demand-data-centers) | 2024-12-20 |
| `2026-10-21-iea-copper-2pct` | [The Oregon Group, quoting IEA Energy and AI](https://theoregongroup.com/commodities/copper/ai-data-centers-to-drive-2-of-global-copper-demand-by-2030/) (secondary) | 2025-04-10 |
| `2026-10-21-bnef-copper-datacenters` | [MINING.COM on BNEF](https://www.mining.com/ai-data-centers-to-worsen-copper-shortage-bnef/) (secondary) | 2025-08-12 |
| `2026-10-21-icsg-surplus` | [Reuters via Mining Weekly on ICSG](https://www.miningweekly.com/article/icsg-sees-global-refined-copper-surplus-widening-in-2027-2026-10-15) (ICSG PDF was gated) | 2026-10-15 |
| `2026-10-21-cnbc-deepseek-power` | [CNBC, power stocks plunge](https://www.cnbc.com/2025/01/27/power-stocks-plunge-as-ai-energy-needs-questioned-due-to-new-china-model.html) | 2025-01-27 |
| `2026-10-21-gev-2q26-call` | [GE Vernova 2Q 2026 call transcript](https://www.gevernova.com/sites/default/files/gev_webcast_transcript_07222026.pdf) | 2026-07-22 |
| origin | [@WillManidis bookmark](https://x.com/WillManidis/status/2112582008010604549) | 2026-10-20 |

Not reached: the Omniscience library (its Postgres database isn't reachable from the box where this ran), so no podcast or earnings-library evidence was searched.

## 7. Next cycle (open research tasks)

- Instrument terms: fees, roll, margin or embedded leverage, liquidity and tax for COMEX copper, CPER, COPX, URA and the IPPs.
- Quarterly monitor: hyperscaler capex guidance, US large-load interconnection requests, IPP data-center contracts.
- Deferred by the worker's budget: `screen-thesis` (find specific businesses for an assessment).
