# Context management

> Practices and tools are what the cited sources say (verbatim evidence). **Proposals are the agent's inferences** for Noah's agents/repos, each grounded in at least one quoted source claim.

Theme: `context-management` · Sources: 4 · Published 2024-08-03 → 2026-10-19 · First seen by pipeline: 2026-10-16

What context agents get, and how sessions are scoped.

## Practices and patterns

- Give the AI a standing brief of the codebase: dependencies, deployment and file structure. — “add a basic explanation of your code base there: the dependencies, deployment, and file structure” (main) [@alexanderisorax, 2024-08-03](https://x.com/alexanderisorax/status/1819671375759487270)
- Keep one task per session so earlier generations don't pollute the context. — “One task per session. Do not pollute the context with previous code generations and discussions.” (main) [@alexanderisorax, 2024-08-03](https://x.com/alexanderisorax/status/1819671375759487270)
- Paste current framework docs when the model doesn't know the latest version. — “simply copy-paste the entire doc file into it and ask to generate code according to the latest spec” (main) [@alexanderisorax, 2024-08-03](https://x.com/alexanderisorax/status/1819671375759487270)
- Break complex tasks into smaller components. — “Break complex tasks into smaller components.” (main) [@alexanderisorax, 2024-08-03](https://x.com/alexanderisorax/status/1819671375759487270)
- Ask the AI to review its own output after generating code. — “After generating code, ask the AI to review it for potential improvements.” (main) [@alexanderisorax, 2024-08-03](https://x.com/alexanderisorax/status/1819671375759487270)
- Databases deserve documentation and tests as much as code; schema docs let others query the DB without engineering help. — “dbs are more important than the code that uses them” (main) / “the docs enable data science and product to query the DB without help from Eng” (main) [@sebasbensu, 2024-08-09](https://x.com/sebasbensu/status/1821972759658066429)
- Route general (not item-specific) review feedback into one shared standards markdown file that every related skill references, so the skills improve as feedback accumulates. — “if I give feedback that is generally applicable across the board” (transcript) / “make sure you log it into that MD file and that MD file feeds all the skills” (transcript) [@alexgoughcooper, 2026-10-15](https://x.com/alexgoughcooper/status/2110853666739556518)
- Seed a skill's rules by having the agent compile past reviewer feedback (30 days of comments in the review tool) into a document. — “I want you to look into frame for the last 30 days and compile all of the feedback that all of my team have given” (transcript) [@alexgoughcooper, 2026-10-15](https://x.com/alexgoughcooper/status/2110853666739556518)
- Split a general skill into style-specific skills, each built from three or four examples of that style. — “have a look at these four ads and I want you to make a skill based on this edit style” (transcript) [@alexgoughcooper, 2026-10-15](https://x.com/alexgoughcooper/status/2110853666739556518)
- Build feedback loops into whatever the agent produces and make them accessible to the whole team. — “build feedback loops in and make it accessible for your team” (transcript) [@alexgoughcooper, 2026-10-15](https://x.com/alexgoughcooper/status/2110853666739556518)
- Start each task from a short handoff file (goal, decisions, paths, open questions, next action) in a fresh conversation instead of carrying a long chat forward. — “Create or update HANDOFF.md for this workflow” (main) / “Keep it under 400 words” (main) [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640)
- Extract only the passages a question needs before analysis, while keeping the full originals and the details (units, dates, billing terms) that change the meaning. — “Extract the passages or fields needed to answer those questions” (main) / “Do not silently truncate required evidence” (main) [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640)
- Run a cheap change check against the last snapshot before a full analysis, and never count a failed check as unchanged. — “A lightweight change check before a full analysis” (main) / “A failed check must never count as unchanged” (main) [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640)
- Store a refresh rule with each saved result so later runs reuse still-valid facts (keeping their original check date) and redo only expired parts. — “Give Completed Work an Expiration Rule” (main) / “Do not relabel old information as newly checked” (main) [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640)
- Give each task one owner, cap a failing operation at two attempts, save progress first, and on resume retry only the unfinished step. — “Allow at most two attempts at the same failing operation” (main) / “Do not restart completed assignments” (main) [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640)
- Define done as a checklist evaluated PASS/FAIL/UNKNOWN against evidence, with one focused correction pass; otherwise return NEEDS REVIEW. — “Mark PASS, FAIL, or UNKNOWN” (main) / “A bot saying “verified” is not evidence” (main) [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640)

## Tools

- **LiteLLM**: Tracks spend and sets budgets on API calls. — “track spending and set budgets for connected API calls” (main) [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640)
- **RouteLLM**: Sends simpler requests to a cheaper model. — “route simpler API requests to a cheaper model” (main) [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640)
- **LLMLingua**: Compresses long inputs before the model reads them. — “compress lengthy inputs before the model reads them” (main) [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640)
- **RTK**: Compresses common command outputs before they enter the conversation. — “compress common command outputs before they enter the conversation” (main) [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640)
- **changedetection.io**: Monitors web pages and sends change notifications. — “changedetection.io can monitor web pages and issue change notifications” (main) [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640)
- **PyBreaker**: Pauses calls to a repeatedly failing service. — “pause calls to a repeatedly failing service” (main) [@Greshamtrade, 2026-10-19; content retrieved 2026-10-21](https://x.com/Greshamtrade/status/2112270735116812640)

## Proposed improvements (agent inference)

Also in [`improvement-backlog.jsonl`](improvement-backlog.jsonl).

### One fresh agent session per beads issue (`f8babee948b1`)

- Target: `agent-workflow` · Effort: S
- Hypothesis: Scoping each session to one bd issue (seeded with `bd prime` and `bd show`) reduces cross-task context pollution.
- Experiment: Run the next 10 bd issues as one session each, starting from `bd prime` + `bd show <id>`; compare with mixed sessions.
- Success metric: Fewer reverted or redone changes and review findings per issue.
- Basis: One task per session keeps context clean. — “One task per session.”

### Codebase brief in AGENTS.md (dependencies, deployment, file map) (`3e296de2b630`)

- Target: `omniscience` · Effort: S
- Hypothesis: A short, current map of entry points and structure in AGENTS.md makes agent replies more precise and saves re-explanation.
- Experiment: Add a 'Codebase map' section (packages, entry points, data dirs, deployment) to omniscience AGENTS.md and keep it current in PRs.
- Success metric: Agents stop asking or grepping for entry points; less time-to-first-change on new tasks.
- Basis: A standing explanation of dependencies, deployment and file structure saves time and improves precision. — “It will save you much time explaining the same thing and make AI's replies more precise.”

### Generated schema docs for omniscience's Postgres tables (`ce7c29dad3dd`)

- Target: `omniscience` · Effort: M
- Hypothesis: Documented tables/columns (generated from SQLAlchemy models plus hand-written meaning) let agents write correct queries without reading model code.
- Experiment: Generate docs/schema.md from omniscience/models with a short purpose line per table and column; check it in CI for drift.
- Success metric: An agent answers 5 library/DB questions correctly using only docs/schema.md.
- Basis: Quality schema docs are a high-value investment for a team. — “Quality schema docs are a great investment for an engineering team”


## Evidence log

- `2024-08-03` [@alexanderisorax, 2024-08-03](https://x.com/alexanderisorax/status/1819671375759487270): Give the AI a standing brief of the codebase: dependencies, deployment and file structure. — “add a basic explanation of your code base there: the dependencies, deployment, and file structure” (main)
- `2024-08-03` [@alexanderisorax, 2024-08-03](https://x.com/alexanderisorax/status/1819671375759487270): Keep one task per session so earlier generations don't pollute the context. — “One task per session. Do not pollute the context with previous code generations and discussions.” (main)
- `2024-08-03` [@alexanderisorax, 2024-08-03](https://x.com/alexanderisorax/status/1819671375759487270): Paste current framework docs when the model doesn't know the latest version. — “simply copy-paste the entire doc file into it and ask to generate code according to the latest spec” (main)
- `2024-08-03` [@alexanderisorax, 2024-08-03](https://x.com/alexanderisorax/status/1819671375759487270): Break complex tasks into smaller components. — “Break complex tasks into smaller components.” (main)
- `2024-08-03` [@alexanderisorax, 2024-08-03](https://x.com/alexanderisorax/status/1819671375759487270): Ask the AI to review its own output after generating code. — “After generating code, ask the AI to review it for potential improvements.” (main)
- `2024-08-03` [@alexanderisorax, 2024-08-03](https://x.com/alexanderisorax/status/1819671375759487270): One task per session keeps context clean. — “One task per session.” (main)
- `2024-08-03` [@alexanderisorax, 2024-08-03](https://x.com/alexanderisorax/status/1819671375759487270): A standing explanation of dependencies, deployment and file structure saves time and improves precision. — “It will save you much time explaining the same thing and make AI's replies more precise.” (main)
- `2024-08-09` [@sebasbensu, 2024-08-09](https://x.com/sebasbensu/status/1821972759658066429): Databases deserve documentation and tests as much as code; schema docs let others query the DB without engineering help. — “dbs are more important than the code that uses them” (main) / “the docs enable data science and product to query the DB without help from Eng” (main)
- `2024-08-09` [@sebasbensu, 2024-08-09](https://x.com/sebasbensu/status/1821972759658066429): Quality schema docs are a high-value investment for a team. — “Quality schema docs are a great investment for an engineering team” (main)
- `2026-10-15` [@alexgoughcooper, 2026-10-15](https://x.com/alexgoughcooper/status/2110853666739556518): Route general (not item-specific) review feedback into one shared standards markdown file that every related skill references, so the skills improve as feedback accumulates. — “if I give feedback that is generally applicable across the board” (transcript) / “make sure you log it into that MD file and that MD file feeds all the skills” (transcript)
- `2026-10-15` [@alexgoughcooper, 2026-10-15](https://x.com/alexgoughcooper/status/2110853666739556518): Seed a skill's rules by having the agent compile past reviewer feedback (30 days of comments in the review tool) into a document. — “I want you to look into frame for the last 30 days and compile all of the feedback that all of my team have given” (transcript)
- `2026-10-15` [@alexgoughcooper, 2026-10-15](https://x.com/alexgoughcooper/status/2110853666739556518): Split a general skill into style-specific skills, each built from three or four examples of that style. — “have a look at these four ads and I want you to make a skill based on this edit style” (transcript)
- `2026-10-15` [@alexgoughcooper, 2026-10-15](https://x.com/alexgoughcooper/status/2110853666739556518): Build feedback loops into whatever the agent produces and make them accessible to the whole team. — “build feedback loops in and make it accessible for your team” (transcript)
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
