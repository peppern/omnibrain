# Investment research desk

Find understandable businesses that can compound per-share value for years, then establish whether the price offers a defensible advantage over a broad market alternative. Long equities are the default; specific portfolio tilts are also possible.

**Workspace status:** review scaffolding installed on 2026-10-17. The recurring pipeline and automated views are planned in [Omniscience epic omni-83b](https://github.com/peppern/omniscience/blob/investment-research-routine/docs/rfcs/investment-research-routine.md). This page is not evidence of a completed research run. There are no screened businesses or actionable recommendations in this workspace yet. The first research run (2026-10-21, `ai-exposure-via-energy-commodities`) answered thesis questions only; no business was assessed.

## Review in this order

Start with **[Portfolio holdings and size bands](portfolio/README.md)** for NHP exposure context. This is a dated, coarse snapshot; current funding, exact weights and allocation constraints still require FamilyFin evidence.

0. **[Latest thesis review packet: Bet on AI through energy and commodities (2026-10-21)](reviews/theses/2026-10-21-ai-exposure-via-energy-commodities.md)**: the one page to read per thesis per cycle (claim, view, new evidence, answers, risks, decision asks). The generated [desk review](reviews/generated-latest-review.md) and [digest](reviews/generated-latest-digest.md) cover all theses.
1. **[Latest review: setup and inherited leads](reviews/2026-10-17-setup.md)** — what exists, what remains unknown, and what comes next.
2. **[Recommendations](recommendations/README.md)** — specific proposed actions, entry conditions, sizing and blockers; proposals await Noah's decision.
3. **[Business assessments](businesses/README.md)** and **[investment expressions](expressions/README.md)** — business quality, alternatives and price discipline.
4. **[Thesis registry](theses/README.md)** — claims, evidence and research questions; preserve existing canonical IDs.
5. **[Evidence inbox](inbox/README.md)** — ambiguous matches and unresolved observations.
6. **[Too difficult](too-difficult/README.md)** — parked cases and the information that could reopen them.
7. **[Decision history](decisions/README.md)** and **[past reviews](reviews/README.md)** — what Noah decided, on which revision, and why.

## Working agreement

Read the [investment mandate](mandate.md), [routine](routine.md), and [templates](templates/README.md). Evidence supports or challenges particular claims; a company mention alone does not establish a relationship. Business quality, valuation, conviction and research priority are separate judgments. Unknowns remain visible.

The existing machine-generated evidence/thesis area is [`research/investment-ideas/`](../investment-ideas/README.md), written by `omni tracks export`. This desk links to those sources rather than creating another writable thesis registry.

## Publication ownership

The mandate, routine and templates are human-maintained. Research pages, review packets and dated recommendation revisions are added through reviewed PRs. Future generated indexes must have explicit ownership and must preserve human content. No recursive deletion of this directory is allowed. The existing content-track exporter does not manage this desk.

Research proposals and owner decisions are distinct. A decision applies to an exact revision. An approved proposal is not a record of an executed transaction.
