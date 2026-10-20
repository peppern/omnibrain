# Agent tools and APIs

> Practices and tools are what the cited sources say (verbatim evidence). **Proposals are the agent's inferences** for Noah's agents/repos, each grounded in at least one quoted source claim.

Theme: `agent-tools-and-apis` · Sources: 5 · Published 2026-02-05 → 2026-10-18 · First seen by pipeline: 2026-10-16

Tools, models and APIs agents can call; packaging capabilities for agents.

## Practices and patterns

- A key lesson attributed to @steipete: package capabilities as a CLI plus an agent skill. — “make everything a cli + skill” (main) [@aniketapanjwani, 2026-02-05](https://x.com/aniketapanjwani/status/2019401717364748767)
- Practitioners disagree about 'ralph loops' (long autonomous agent loops): Matt Pocock is bullish, Peter Steinberger bearish. — “Matt is really bullish on ralph whereas Peter is really bearish” (main) [@aniketapanjwani, 2026-02-05](https://x.com/aniketapanjwani/status/2019401717364748767)
- In a post quoted by @champagnekofi, Peter Czepiga pitches wrapping a platform's raw MCP in a tool that applies your saved preferences (copy, settings, URLs) on every call instead of specifying them by hand. — “we launch your ads with every nuanced preference already applied” (main) / “raw-dogging Meta's MCP to launch ads” (main) [@champagnekofi, 2026-10-16](https://x.com/champagnekofi/status/2111086010222477440)
- Have an agent generate a formal verification suite for the properties you care about, e.g. TLA+ models of state machines and concurrency, or Kani checks for undefined behavior in Rust. — “this is a meta-skill that creates a new skill and formal verification suite based on the characteristics you want to verify” (main) / “model state machines and systems with concurrency using TLA+, or use kani in rust to check for undefined behavior” (main) [@poteto, 2026-10-18](https://x.com/poteto/status/2111926622278521253)
- The author reports that modeling their team's code in TLA+ with a generated skill has already found several bugs. — “i've been experimenting with modeling our code with TLA+ and have already found several bugs” (main) [@poteto, 2026-10-18](https://x.com/poteto/status/2111926622278521253)

## Tools

- **Indra OCR (Datalab)**: A 1M-parameter OCR model claimed at 49 pages/s on CPU, 11x faster than PaddleOCR and 17x faster than Tesseract, with layout and line boxes. — “49 pages/s on CPU, 11x faster than PaddleOCR and 17x Tesseract” (main) / “Full layout and line bounding boxes” (main) [@VikParuchuri, 2026-10-13](https://x.com/VikParuchuri/status/2110058905875460393)
- **Openverse API** (<https://api.openverse.org/v1/>): Free, keyless API to search 5.2M+ openly licensed sound effects, ambience and music clips, usable by an agent editing videos. — “you can give it a library of 5.2M+ audio files for $0” (main) / “openverse has a free api. no key needed.” (main) [@ElliotPadfield, 2026-10-15](https://x.com/ElliotPadfield/status/2110764303087288788)
- **Ad launch MCP (Peter Czepiga)**: Peter Czepiga's ad-launch MCP (from his quoted post) launches Meta ads with saved preferences such as copy, Advantage+ settings and URL already applied; @champagnekofi endorses it. — “the right copy, Adv+ preferences, URL, and more” (main) [@champagnekofi, 2026-10-16](https://x.com/champagnekofi/status/2111086010222477440)
- **pstack /create-formal-verification-skill**: A beta meta-skill shipped in pstack v0.15.27 that creates a new skill and formal verification suite for chosen properties, alongside the existing /create-verification-skill. — “pstack v0.15.27 ships with a new skill /create-formal-verification-skill” (main) [@poteto, 2026-10-18](https://x.com/poteto/status/2111926622278521253)

## Proposed improvements (agent inference)

Also in [`improvement-backlog.jsonl`](improvement-backlog.jsonl).

### Package omni grok-x / tracks routines as agent skills over the CLI (`6ac1ba5d94bf`)

- Target: `agent-workflow` · Effort: S
- Hypothesis: Thin skill files that call the `omni` CLI make the daily bookmark and tracks routines reproducible across agents and machines.
- Experiment: Write one skill for the daily routine (merge → process → classify → export → PR) that only calls `omni` commands; run it on two agents.
- Success metric: Both agents complete the routine with no ad-hoc scripts.
- Basis: Make everything a CLI plus a skill. — “make everything a cli + skill”

### Evaluate Indra as grok-x's OCR backend (`0e8572626f99`)

- Target: `grok-x` · Effort: S
- Hypothesis: A fast CPU OCR model would let grok-x OCR every bookmarked image and frame sheet (tesseract isn't installed on the agent box).
- Experiment: Run Indra and Tesseract on the 18 uninspected visual bookmarks; compare text quality and time.
- Success metric: Usable text for most images at under 1s per image on CPU.
- Basis: Indra beats PaddleOCR and Tesseract on a text benchmark. — “Beats them on OmniParseBench text”

### Openverse sound search for omniscience episode/clip builds (`9c04a71b11c9`)

- Target: `omniscience` · Effort: S
- Hypothesis: Giving episode-building agents an Openverse search step yields properly sourced sound design without manual downloads.
- Experiment: Add a small Openverse client to the clip/episode pipeline that records each clip's license and attribution; try it on one episode.
- Success metric: One episode built with Openverse audio, all licenses and attributions recorded.
- Basis: Agents can search Openverse whenever sound effects are needed. — “whenever you need sound effects search Openverse to find the best options”

### Model-check the tracks intake journal and rollback (`da705511a960`)

- Target: `omniscience` · Effort: M
- Hypothesis: The tracks intake commit (locks, journaled transaction, byte-for-byte rollback, crash recovery) is a concurrent state machine of the kind TLA+ modeling is said to catch bugs in.
- Experiment: Generate or hand-write a small TLA+ spec of intake apply, rollback and crash restore, and model-check interleavings with a concurrent writer.
- Success metric: Spec model-checks clean, or at least one real bug is found and filed in beads.
- Basis: TLA+ is suggested for modeling state machines and concurrent systems, and the author found bugs this way. — “model state machines and systems with concurrency using TLA+”

### Open questions

- [P3] What exactly are 'ralph loops', and would one suit the daily bookmark routine? — A practitioner-debated pattern that could replace the scheduled routine. (`7e3e480817c6`)
- [P2] Is Indra open-weights and licensed for local use, and how do you install it? — Decides whether it can replace Tesseract in grok-x. (`31f930392688`)
- [P2] Which Openverse audio licenses (CC0/CC BY/BY-SA/NC) are acceptable for Noah's published episodes? — Licensing decides whether the tool is usable for published work. (`5ebec1a2631c`)


## Evidence log

- `2026-02-05` [@aniketapanjwani, 2026-02-05](https://x.com/aniketapanjwani/status/2019401717364748767): A key lesson attributed to @steipete: package capabilities as a CLI plus an agent skill. — “make everything a cli + skill” (main)
- `2026-02-05` [@aniketapanjwani, 2026-02-05](https://x.com/aniketapanjwani/status/2019401717364748767): Practitioners disagree about 'ralph loops' (long autonomous agent loops): Matt Pocock is bullish, Peter Steinberger bearish. — “Matt is really bullish on ralph whereas Peter is really bearish” (main)
- `2026-02-05` [@aniketapanjwani, 2026-02-05](https://x.com/aniketapanjwani/status/2019401717364748767): Make everything a CLI plus a skill. — “make everything a cli + skill” (main)
- `2026-10-13` [@VikParuchuri, 2026-10-13](https://x.com/VikParuchuri/status/2110058905875460393): A 1M-parameter OCR model claimed at 49 pages/s on CPU, 11x faster than PaddleOCR and 17x faster than Tesseract, with layout and line boxes. — “49 pages/s on CPU, 11x faster than PaddleOCR and 17x Tesseract” (main) / “Full layout and line bounding boxes” (main)
- `2026-10-13` [@VikParuchuri, 2026-10-13](https://x.com/VikParuchuri/status/2110058905875460393): Indra beats PaddleOCR and Tesseract on a text benchmark. — “Beats them on OmniParseBench text” (main)
- `2026-10-15` [@ElliotPadfield, 2026-10-15](https://x.com/ElliotPadfield/status/2110764303087288788): Free, keyless API to search 5.2M+ openly licensed sound effects, ambience and music clips, usable by an agent editing videos. — “you can give it a library of 5.2M+ audio files for $0” (main) / “openverse has a free api. no key needed.” (main)
- `2026-10-15` [@ElliotPadfield, 2026-10-15](https://x.com/ElliotPadfield/status/2110764303087288788): Agents can search Openverse whenever sound effects are needed. — “whenever you need sound effects search Openverse to find the best options” (main)
- `2026-10-16` [@champagnekofi, 2026-10-16](https://x.com/champagnekofi/status/2111086010222477440): In a post quoted by @champagnekofi, Peter Czepiga pitches wrapping a platform's raw MCP in a tool that applies your saved preferences (copy, settings, URLs) on every call instead of specifying them by hand. — “we launch your ads with every nuanced preference already applied” (main) / “raw-dogging Meta's MCP to launch ads” (main)
- `2026-10-16` [@champagnekofi, 2026-10-16](https://x.com/champagnekofi/status/2111086010222477440): Peter Czepiga's ad-launch MCP (from his quoted post) launches Meta ads with saved preferences such as copy, Advantage+ settings and URL already applied; @champagnekofi endorses it. — “the right copy, Adv+ preferences, URL, and more” (main)
- `2026-10-18` [@poteto, 2026-10-18](https://x.com/poteto/status/2111926622278521253): Have an agent generate a formal verification suite for the properties you care about, e.g. TLA+ models of state machines and concurrency, or Kani checks for undefined behavior in Rust. — “this is a meta-skill that creates a new skill and formal verification suite based on the characteristics you want to verify” (main) / “model state machines and systems with concurrency using TLA+, or use kani in rust to check for undefined behavior” (main)
- `2026-10-18` [@poteto, 2026-10-18](https://x.com/poteto/status/2111926622278521253): The author reports that modeling their team's code in TLA+ with a generated skill has already found several bugs. — “i've been experimenting with modeling our code with TLA+ and have already found several bugs” (main)
- `2026-10-18` [@poteto, 2026-10-18](https://x.com/poteto/status/2111926622278521253): A beta meta-skill shipped in pstack v0.15.27 that creates a new skill and formal verification suite for chosen properties, alongside the existing /create-verification-skill. — “pstack v0.15.27 ships with a new skill /create-formal-verification-skill” (main)
- `2026-10-18` [@poteto, 2026-10-18](https://x.com/poteto/status/2111926622278521253): TLA+ is suggested for modeling state machines and concurrent systems, and the author found bugs this way. — “model state machines and systems with concurrency using TLA+” (main) / “have already found several bugs” (main)
