# Retrieval and RAG

> Practices and tools are what the cited sources say (verbatim evidence). **Proposals are the agent's inferences** for Noah's agents/repos, each grounded in at least one quoted source claim.

Theme: `retrieval-and-rag` · Sources: 3 · Published 2025-06-24 → 2026-10-19 · First seen by pipeline: 2026-10-16

Search/retrieval design for agents and knowledge bases.

## Practices and patterns

- RAG/search fails when every signal (numbers, location, categories) is embedded as text; use specialised encoders or structured handling per data type. — “your search pilot sees the entire world as strings” (main) / “stringifying numbers and feeding them to text models creates unpredictable, noisy results” (main) [@jxnlco, 2025-06-24](https://x.com/jxnlco/status/1937556712287826147)
- Hard filters are overused to approximate soft preferences, and re-ranking is a patch for weak retrieval. — “filters are overused to approximate biases” (main) / “re-ranking is a hack that only works on <1% of your data” (main) [@jxnlco, 2025-06-24](https://x.com/jxnlco/status/1937556712287826147)
- Have the agent read each source once and link it into what you already have, building a compiled, cross-linked knowledge base instead of accumulating notes. — “a pile of notes isn't memory” (main) / “Claude reads a source once and links it to everything you already have” (main) [@rvaniaaaa, 2026-10-16](https://x.com/rvaniaaaa/status/2111085365171790269)
- Judge a compiled wiki only after feeding it a meaningful corpus (about 50 sources); before that it behaves like plain search. — “feed it your first 50 sources” (main) / “a compiled wiki behaves like a plain search engine” (main) [@rvaniaaaa, 2026-10-16](https://x.com/rvaniaaaa/status/2111085365171790269)
- Start each task from a short handoff file (goal, decisions, paths, open questions, next action) in a fresh conversation instead of carrying a long chat forward. — “Create or update HANDOFF.md for this workflow” (main) / “Keep it under 400 words” (main) [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640)
- Extract only the passages a question needs before analysis, while keeping the full originals and the details (units, dates, billing terms) that change the meaning. — “Extract the passages or fields needed to answer those questions” (main) / “Do not silently truncate required evidence” (main) [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640)
- Run a cheap change check against the last snapshot before a full analysis, and never count a failed check as unchanged. — “A lightweight change check before a full analysis” (main) / “A failed check must never count as unchanged” (main) [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640)
- Store a refresh rule with each saved result so later runs reuse still-valid facts (keeping their original check date) and redo only expired parts. — “Give Completed Work an Expiration Rule” (main) / “Do not relabel old information as newly checked” (main) [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640)
- Give each task one owner, cap a failing operation at two attempts, save progress first, and on resume retry only the unfinished step. — “Allow at most two attempts at the same failing operation” (main) / “Do not restart completed assignments” (main) [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640)
- Define done as a checklist evaluated PASS/FAIL/UNKNOWN against evidence, with one focused correction pass; otherwise return NEEDS REVIEW. — “Mark PASS, FAIL, or UNKNOWN” (main) / “A bot saying “verified” is not evidence” (main) [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640)

## Tools

- **graphify**: Turns a codebase with docs, SQL schemas, configs and PDFs into a queryable knowledge graph. — “turns a codebase with its docs, SQL schemas, configs and PDFs into a queryable knowledge graph” (main) [@rvaniaaaa, 2026-10-16](https://x.com/rvaniaaaa/status/2111085365171790269)
- **Understand-Anything**: Maps a project's code, docs or wiki into a graph searchable from a coding assistant. — “maps a project's code, docs or wiki into a graph you can search and query from your coding assistant” (main) [@rvaniaaaa, 2026-10-16](https://x.com/rvaniaaaa/status/2111085365171790269)
- **claude-obsidian**: Lets Claude Code build and maintain a source-backed Markdown knowledge base in Obsidian. — “lets Claude Code build and maintain a Markdown knowledge base in Obsidian” (main) [@rvaniaaaa, 2026-10-16](https://x.com/rvaniaaaa/status/2111085365171790269)
- **llm-wikid**: An agent compiles raw sources into cross-linked wiki pages in Obsidian. — “an agent compiles your raw sources into cross-linked wiki pages in Obsidian” (main) [@rvaniaaaa, 2026-10-16](https://x.com/rvaniaaaa/status/2111085365171790269)
- **LiteLLM**: Tracks spend and sets budgets on API calls. — “track spending and set budgets for connected API calls” (main) [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640)
- **RouteLLM**: Sends simpler requests to a cheaper model. — “route simpler API requests to a cheaper model” (main) [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640)
- **LLMLingua**: Compresses long inputs before the model reads them. — “compress lengthy inputs before the model reads them” (main) [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640)
- **RTK**: Compresses common command outputs before they enter the conversation. — “compress common command outputs before they enter the conversation” (main) [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640)
- **changedetection.io**: Monitors web pages and sends change notifications. — “changedetection.io can monitor web pages and issue change notifications” (main) [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640)
- **PyBreaker**: Pauses calls to a repeatedly failing service. — “pause calls to a repeatedly failing service” (main) [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640)

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
- `2026-10-21` [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640): Start each task from a short handoff file (goal, decisions, paths, open questions, next action) in a fresh conversation instead of carrying a long chat forward. — “Create or update HANDOFF.md for this workflow” (main) / “Keep it under 400 words” (main)
- `2026-10-21` [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640): Extract only the passages a question needs before analysis, while keeping the full originals and the details (units, dates, billing terms) that change the meaning. — “Extract the passages or fields needed to answer those questions” (main) / “Do not silently truncate required evidence” (main)
- `2026-10-21` [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640): Run a cheap change check against the last snapshot before a full analysis, and never count a failed check as unchanged. — “A lightweight change check before a full analysis” (main) / “A failed check must never count as unchanged” (main)
- `2026-10-21` [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640): Store a refresh rule with each saved result so later runs reuse still-valid facts (keeping their original check date) and redo only expired parts. — “Give Completed Work an Expiration Rule” (main) / “Do not relabel old information as newly checked” (main)
- `2026-10-21` [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640): Give each task one owner, cap a failing operation at two attempts, save progress first, and on resume retry only the unfinished step. — “Allow at most two attempts at the same failing operation” (main) / “Do not restart completed assignments” (main)
- `2026-10-21` [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640): Define done as a checklist evaluated PASS/FAIL/UNKNOWN against evidence, with one focused correction pass; otherwise return NEEDS REVIEW. — “Mark PASS, FAIL, or UNKNOWN” (main) / “A bot saying “verified” is not evidence” (main)
- `2026-10-21` [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640): Tracks spend and sets budgets on API calls. — “track spending and set budgets for connected API calls” (main)
- `2026-10-21` [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640): Sends simpler requests to a cheaper model. — “route simpler API requests to a cheaper model” (main)
- `2026-10-21` [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640): Compresses long inputs before the model reads them. — “compress lengthy inputs before the model reads them” (main)
- `2026-10-21` [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640): Compresses common command outputs before they enter the conversation. — “compress common command outputs before they enter the conversation” (main)
- `2026-10-21` [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640): Monitors web pages and sends change notifications. — “changedetection.io can monitor web pages and issue change notifications” (main)
- `2026-10-21` [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640): Pauses calls to a repeatedly failing service. — “pause calls to a repeatedly failing service” (main)
