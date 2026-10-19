# Retrieval and RAG

> Practices and tools are what the cited sources say (verbatim evidence). **Proposals are the agent's inferences** for Noah's agents/repos, each grounded in at least one quoted source claim.

Theme: `retrieval-and-rag` · Sources: 2 · Published 2025-06-24 → 2026-10-16 · First seen by pipeline: 2026-10-16

Search/retrieval design for agents and knowledge bases.

## Practices and patterns

- RAG/search fails when every signal (numbers, location, categories) is embedded as text; use specialised encoders or structured handling per data type. — “your search pilot sees the entire world as strings” (main) / “stringifying numbers and feeding them to text models creates unpredictable, noisy results” (main) [@jxnlco, 2025-06-24](https://x.com/jxnlco/status/1937556712287826147)
- Hard filters are overused to approximate soft preferences, and re-ranking is a patch for weak retrieval. — “filters are overused to approximate biases” (main) / “re-ranking is a hack that only works on <1% of your data” (main) [@jxnlco, 2025-06-24](https://x.com/jxnlco/status/1937556712287826147)
- Have the agent read each source once and link it into what you already have, building a compiled, cross-linked knowledge base instead of accumulating notes. — “a pile of notes isn't memory” (main) / “Claude reads a source once and links it to everything you already have” (main) [@rvaniaaaa, 2026-10-16](https://x.com/rvaniaaaa/status/2111085365171790269)
- Judge a compiled wiki only after feeding it a meaningful corpus (about 50 sources); before that it behaves like plain search. — “feed it your first 50 sources” (main) / “a compiled wiki behaves like a plain search engine” (main) [@rvaniaaaa, 2026-10-16](https://x.com/rvaniaaaa/status/2111085365171790269)

## Tools

- **graphify**: Turns a codebase with docs, SQL schemas, configs and PDFs into a queryable knowledge graph. — “turns a codebase with its docs, SQL schemas, configs and PDFs into a queryable knowledge graph” (main) [@rvaniaaaa, 2026-10-16](https://x.com/rvaniaaaa/status/2111085365171790269)
- **Understand-Anything**: Maps a project's code, docs or wiki into a graph searchable from a coding assistant. — “maps a project's code, docs or wiki into a graph you can search and query from your coding assistant” (main) [@rvaniaaaa, 2026-10-16](https://x.com/rvaniaaaa/status/2111085365171790269)
- **claude-obsidian**: Lets Claude Code build and maintain a source-backed Markdown knowledge base in Obsidian. — “lets Claude Code build and maintain a Markdown knowledge base in Obsidian” (main) [@rvaniaaaa, 2026-10-16](https://x.com/rvaniaaaa/status/2111085365171790269)
- **llm-wikid**: An agent compiles raw sources into cross-linked wiki pages in Obsidian. — “an agent compiles your raw sources into cross-linked wiki pages in Obsidian” (main) [@rvaniaaaa, 2026-10-16](https://x.com/rvaniaaaa/status/2111085365171790269)

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
- `2026-10-16` [@rvaniaaaa, 2026-10-16](https://x.com/rvaniaaaa/status/2111085365171790269): Have the agent read each source once and link it into what you already have, building a compiled, cross-linked knowledge base instead of accumulating notes. — “a pile of notes isn't memory” (main) / “Claude reads a source once and links it to everything you already have” (main)
- `2026-10-16` [@rvaniaaaa, 2026-10-16](https://x.com/rvaniaaaa/status/2111085365171790269): Judge a compiled wiki only after feeding it a meaningful corpus (about 50 sources); before that it behaves like plain search. — “feed it your first 50 sources” (main) / “a compiled wiki behaves like a plain search engine” (main)
- `2026-10-16` [@rvaniaaaa, 2026-10-16](https://x.com/rvaniaaaa/status/2111085365171790269): Turns a codebase with docs, SQL schemas, configs and PDFs into a queryable knowledge graph. — “turns a codebase with its docs, SQL schemas, configs and PDFs into a queryable knowledge graph” (main)
- `2026-10-16` [@rvaniaaaa, 2026-10-16](https://x.com/rvaniaaaa/status/2111085365171790269): Maps a project's code, docs or wiki into a graph searchable from a coding assistant. — “maps a project's code, docs or wiki into a graph you can search and query from your coding assistant” (main)
- `2026-10-16` [@rvaniaaaa, 2026-10-16](https://x.com/rvaniaaaa/status/2111085365171790269): Lets Claude Code build and maintain a source-backed Markdown knowledge base in Obsidian. — “lets Claude Code build and maintain a Markdown knowledge base in Obsidian” (main)
- `2026-10-16` [@rvaniaaaa, 2026-10-16](https://x.com/rvaniaaaa/status/2111085365171790269): An agent compiles raw sources into cross-linked wiki pages in Obsidian. — “an agent compiles your raw sources into cross-linked wiki pages in Obsidian” (main)
