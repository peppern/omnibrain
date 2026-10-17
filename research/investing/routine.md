# Investment research routine

**Status:** an implementation contract and manual review guide. The scheduled workflow is not installed yet. [Implementation design and Beads map](https://github.com/peppern/omniscience/blob/investment-research-routine/docs/rfcs/investment-research-routine.md).

## One bounded run

1. Read the mandate, prior successful run, portfolio context and outstanding decisions. Record input cutoffs, budget and source availability.
2. Process new or changed material. Extract source-grounded observations, inspect nearby theses, and attach with a supports/challenges/qualifies/context rationale. Keep unresolved matches in the inbox. Propose a new candidate only for a distinct claim.
3. Prioritize existing work by decision impact, information gain and material change. Seek contrary evidence. Do not keep researching parked cases without a reopening trigger.
4. Answer a bounded question using primary sources and the library where available. Save provenance, source dates and evidence; report missing access instead of treating it as a negative result.
5. Update the relevant business assessment and investment expression. A qualified case proceeds to explicit valuation and portfolio assumptions. If inputs are missing, record a research-only proposal with blockers.
6. Publish dated revisions, a review packet and changed indexes in an Omnibrain PR after validation. Clearly distinguish a proposal from an owner decision and an owner decision from execution.
7. Record failures and the last successfully published checkpoint. Retry safely. A no-change run produces no empty PR or repeated notification.

## Review cadence

| Cadence | Work | Review output |
| --- | --- | --- |
| Daily | Incremental evidence intake, material contradictions, reopening triggers | Changed evidence or exception summary; no digest if nothing changed |
| Weekly | Bounded research on the highest-value questions; shortlist and valuation refresh where needed | Decisions, proposal revisions, watch-price changes, unknowns, new parked cases |
| Quarterly / material event | Business economics, management/capital allocation, financial statements, valuation assumptions | Updated business case and return scenarios; invalidate stale conclusions |

Times, timezone and budgets belong in configuration. Scheduling and notifications ship through Beads; this document does not activate them.

## Existing CLI building blocks

The current Omniscience CLI supports `omni tracks thesis list`, `omni tracks pending`, `omni tracks thesis queue`, task claims, grounded research updates, validation, export and `omni tracks thesis digest --since <date>`. Consult `--help` and the [current content-tracks RFC](https://github.com/peppern/omniscience/blob/main/docs/rfcs/content-tracks.md) for syntax.

The new evidence inbox, business assessments, investment expressions, return models and recommendation approvals are planned capabilities. Until implemented, use the templates as clearly labeled review drafts; do not hand-edit operational JSON to simulate new states. The existing exporter writes `research/investment-ideas/`, not this review workspace.

## Review packet order

Lead with decisions needed and material changes to already-underwritten businesses. Then show specific proposals, watch-price entries, new evidence/counterevidence, answerable questions, newly parked cases and operational failures. Include links and as-of dates. Keep implementation task status in Beads rather than in investment notes.
