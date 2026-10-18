# Retrieval and RAG

> Practices and tools are what the cited sources say (verbatim evidence). **Proposals are the agent's inferences** for Noah's agents/repos, each grounded in at least one quoted source claim.

Theme: `retrieval-and-rag` · Sources: 1 · Published 2025-06-24 → 2025-06-24 · First seen by pipeline: 2026-10-16

Search/retrieval design for agents and knowledge bases.

## Practices and patterns

- RAG/search fails when every signal (numbers, location, categories) is embedded as text; use specialised encoders or structured handling per data type. — “your search pilot sees the entire world as strings” (main) / “stringifying numbers and feeding them to text models creates unpredictable, noisy results” (main) [@jxnlco, 2025-06-24](https://x.com/jxnlco/status/1937556712287826147)
- Hard filters are overused to approximate soft preferences, and re-ranking is a patch for weak retrieval. — “filters are overused to approximate biases” (main) / “re-ranking is a hack that only works on <1% of your data” (main) [@jxnlco, 2025-06-24](https://x.com/jxnlco/status/1937556712287826147)

## Proposed improvements (agent inference)

Also in [`improvement-backlog.jsonl`](improvement-backlog.jsonl).

### Treat dates, source type and author as structured signals in library search (`4f8b7fd9e0d9`)

- Target: `omniscience` · Effort: M
- Hypothesis: Using published date, source_type and author as structured filters/boosts (instead of embedding them as text) improves retrieval precision for time- or source-scoped questions.
- Experiment: Add optional date-range/source_type/author boosts to library search and compare precision@5 on 20 scoped queries.
- Success metric: precision@5 improves on scoped queries without regressing unscoped ones.
- Basis: Text embeddings don't understand non-text data. — “text embeddings don't understand non-text data”


## Evidence log

- `2025-06-24` [@jxnlco, 2025-06-24](https://x.com/jxnlco/status/1937556712287826147): RAG/search fails when every signal (numbers, location, categories) is embedded as text; use specialised encoders or structured handling per data type. — “your search pilot sees the entire world as strings” (main) / “stringifying numbers and feeding them to text models creates unpredictable, noisy results” (main)
- `2025-06-24` [@jxnlco, 2025-06-24](https://x.com/jxnlco/status/1937556712287826147): Hard filters are overused to approximate soft preferences, and re-ranking is a patch for weak retrieval. — “filters are overused to approximate biases” (main) / “re-ranking is a hack that only works on <1% of your data” (main)
- `2025-06-24` [@jxnlco, 2025-06-24](https://x.com/jxnlco/status/1937556712287826147): Text embeddings don't understand non-text data. — “text embeddings don't understand non-text data” (main)
