# Research agents

> Practices and tools are what the cited sources say (verbatim evidence). **Proposals are the agent's inferences** for Noah's agents/repos, each grounded in at least one quoted source claim.

Theme: `research-agents` · Sources: 2 · Published 2024-11-08 → 2025-06-13 · First seen by pipeline: 2026-10-16

Agents and workflows for research (summarization, document Q&A, citations).

## Practices and patterns

- Nat Friedman asks for the best AI summarizer of long YouTube videos (no answer captured). — “What's the best AI summarizer of long YouTube videos?” (main) [@natfriedman, 2024-11-08](https://x.com/natfriedman/status/1855014700897239545)
- Set up a research space with a master prompt that fixes context and answer format before asking questions. — “I'm going to give this one like a master prompt” (transcript) [@DavidTaggart, 2025-06-13](https://x.com/DavidTaggart/status/1933655565798187274)
- Load primary documents (earnings materials, transcripts) into the space so answers draw on them. — “I'm going to upload some transcripts that are downloaded as well” (transcript) [@DavidTaggart, 2025-06-13](https://x.com/DavidTaggart/status/1933655565798187274)
- Perplexity says it differentiates on trust through citations and easy auditing of data. — “by giving citations and really easy ways to audit all the data” (transcript) [@DavidTaggart, 2025-06-13](https://x.com/DavidTaggart/status/1933655565798187274)

## Tools

- **Perplexity**: Used live as an answer engine for institutional-style equity research. — “use perplexity to try and see how close we can get to what we would deem institutional quality outputs” (transcript) [@DavidTaggart, 2025-06-13](https://x.com/DavidTaggart/status/1933655565798187274)

## Proposed improvements (agent inference)

Also in [`improvement-backlog.jsonl`](improvement-backlog.jsonl).

### Per-theme research spaces for the investment research agent (`244f854bc5c8`)

- Target: `research-agent` · Effort: M
- Hypothesis: Starting each investment research task from the theme dossier as a master prompt, plus uploaded primary documents, gives auditable, cited answers.
- Experiment: For one queue item, build a space: dossier + 10-K/transcripts + a master prompt requiring citations; review answer quality.
- Success metric: Every answer claim has a primary-source citation; the question is closed or narrowed.
- Basis: Master prompt plus uploaded documents in one space. — “now I'm going to start loading a bunch of information to this space”

### Open questions

- [P3] Does omniscience's own transcribe-then-summarize path beat off-the-shelf long-video summarizers? — Decides whether to keep building in-house summarization for YouTube items. (`6e7cf7b2fb54`)


## Evidence log

- `2024-11-08` [@natfriedman, 2024-11-08](https://x.com/natfriedman/status/1855014700897239545): Nat Friedman asks for the best AI summarizer of long YouTube videos (no answer captured). — “What's the best AI summarizer of long YouTube videos?” (main)
- `2025-06-13` [@DavidTaggart, 2025-06-13](https://x.com/DavidTaggart/status/1933655565798187274): Set up a research space with a master prompt that fixes context and answer format before asking questions. — “I'm going to give this one like a master prompt” (transcript)
- `2025-06-13` [@DavidTaggart, 2025-06-13](https://x.com/DavidTaggart/status/1933655565798187274): Load primary documents (earnings materials, transcripts) into the space so answers draw on them. — “I'm going to upload some transcripts that are downloaded as well” (transcript)
- `2025-06-13` [@DavidTaggart, 2025-06-13](https://x.com/DavidTaggart/status/1933655565798187274): Perplexity says it differentiates on trust through citations and easy auditing of data. — “by giving citations and really easy ways to audit all the data” (transcript)
- `2025-06-13` [@DavidTaggart, 2025-06-13](https://x.com/DavidTaggart/status/1933655565798187274): Used live as an answer engine for institutional-style equity research. — “use perplexity to try and see how close we can get to what we would deem institutional quality outputs” (transcript)
- `2025-06-13` [@DavidTaggart, 2025-06-13](https://x.com/DavidTaggart/status/1933655565798187274): Master prompt plus uploaded documents in one space. — “now I'm going to start loading a bunch of information to this space” (transcript)
