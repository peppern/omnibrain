# Evals

> Practices and tools are what the cited sources say (verbatim evidence). **Proposals are the agent's inferences** for Noah's agents/repos, each grounded in at least one quoted source claim.

Theme: `evals` · Sources: 1 · Published 2024-10-04 → 2024-10-04 · First seen by pipeline: 2026-10-16

Evaluators and quality checks for model/agent outputs.

## Practices and patterns

- Garry Tan suggests using o1 plus evals/workflows to write a custom evaluator for each item in a list. — “using o1 and evals/workflow to write custom evaluators for every one of these” (main) [@garrytan, 2024-10-04](https://x.com/garrytan/status/1842100905778544903)

## Proposed improvements (agent inference)

Also in [`improvement-backlog.jsonl`](improvement-backlog.jsonl).

### Per-item grounding evaluators for grok-x summaries (`67fbd5f8adac`)

- Target: `grok-x` · Effort: M
- Hypothesis: A cheap evaluator per summary (every takeaway must have lexical support in the fetched content) catches ungrounded summaries before export.
- Experiment: Write an evaluator that scores each takeaway's overlap with content/<id>*.md and run it on the 74 bookmarks; review the lowest 10.
- Success metric: Finds real ungrounded takeaways with less than 20% false positives in the reviewed set.
- Basis: Custom evaluators per item, built with a model and an eval workflow. — “write custom evaluators for every one of these”


## Evidence log

- `2024-10-04` [@garrytan, 2024-10-04](https://x.com/garrytan/status/1842100905778544903): Garry Tan suggests using o1 plus evals/workflows to write a custom evaluator for each item in a list. — “using o1 and evals/workflow to write custom evaluators for every one of these” (main)
- `2024-10-04` [@garrytan, 2024-10-04](https://x.com/garrytan/status/1842100905778544903): Custom evaluators per item, built with a model and an eval workflow. — “write custom evaluators for every one of these” (main)
