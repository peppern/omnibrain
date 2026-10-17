# X bookmarks pipeline (external)

This content tree is the published knowledge. The ingestion pipeline lives outside this repo so Omnibrain stays text-only.

## Where it lives

- Repository: [peppern/omniscience](https://github.com/peppern/omniscience), package `omniscience/grok_x`, CLI `omni grok-x`
- Proposed in [peppern/omniscience#5](https://github.com/peppern/omniscience/pull/5) (branch `grok-x-bookmarks`, commit [`9a6bd0a`](https://github.com/peppern/omniscience/commit/9a6bd0a)). Not merged yet.
- Operator docs: `omniscience/grok_x/README.md`
- Run data (bookmarks, fetched content, media, transcripts, state) lives in the gitignored `.omni/grok-x/` (or `$GROK_X_DATA_DIR`) and is never committed to either repo.
- The original prototype (`/workspace/second-brain`, local commit `16632b9`) was migrated with `omni grok-x import-legacy`. Exporting the migrated 74 bookmarks over this branch at `31c90c3` produced zero diffs.

## How a run works

1. Fetch all bookmark pages for X user `20219699` (`@noahmp`) via the X connector (`get_users_bookmarks`, `max_results=100`, page until exhausted) and combine them into one JSON file.
2. `omni grok-x merge all_pages.json --complete` merges only unseen IDs and removes IDs no longer bookmarked (only when the merge file has no `next_token`). Optionally run `omni grok-x merge posts_by_ids.json` for full text, media and quoted posts.
3. Optional: `omni grok-x threads search_*.json` adds recovered author threads (`from:H to:H` searches).
4. `omni grok-x process` fetches links (ArticleGrabber), quoted posts, transcription (omniscience Whisper) and visuals. `omni grok-x process --retry` retries partial items.
5. `omni grok-x status` lists IDs needing a summary. The agent writes source-grounded summaries into `summaries.json` (no LLM calls in the pipeline).
6. `omni grok-x export --omnibrain /path/to/omnibrain` refreshes `research/x-bookmarks/{README.md,digest.md,notes/,transcripts/}`.
7. Commit on a feature branch and open or update a PR. Never push to `main`, never force-push.

## State contract (`state.json`)

| Key | Meaning |
| --- | --- |
| `processed` | post ID → ISO time when content was first processed. Reruns skip these unless the ID is deleted from this map. |
| `transcribed` | post ID → video transcription status/time |
| `visual` | post ID → `{inspected: bool, ...}` for image/frame review |
| `retry` | post ID → `{reason, retryable}` for partial/blocked items. Daily runs should retry these; failure here must not advance past unfinished work. |
| `removed` | post ID → ISO time when an un-bookmark deletion was applied |

Notes also store:

- `date` / Posted: publication time from X
- `First observed by pipeline`: when the pipeline first saw the ID (not the bookmark time; X does not expose bookmark times)

Manual edits in `content/`, `extra/`, `summaries.json`, and `digest_notes.md` are preserved across merges. Export prunes files only for IDs that left the bookmark set.

## Recent fix

`--complete` removals are driven only by the bookmarks payload, never by xposts loading (covered by a test in `tests/grok_x`).

## Scheduler

Configured on Grok Bot (agent Waffle):

- Routine name: `Process new X bookmarks`
- Schedule: weekdays at 07:49 (local agent schedule; cron `49 7 * * 1-5`)
- Companion: `Watch Omnibrain PR #1` watches review/CI/merge events on this PR

Evidence of a successful incremental run is filed under `runs/`.

## Acceptance checklist (from PR review)

- [x] Inline content findings addressed (visual/thread recovery, ambiguous source label, digest links + partial flags, first_observed chronology)
- [x] Incremental no-op: full live bookmark fetch + `--complete` merge processed 0 new IDs and left state/content hashes unchanged (see `runs/2026-10-16-incremental.md`)
- [x] Publish pipeline repo and link commit SHA here: peppern/omniscience#5 @ `9a6bd0a` (open PR, not merged)
- [ ] Demo: newly bookmarked older post discovered and noted regardless of publication date
- [ ] Demo: image or silent-video bookmark inspected
- [ ] Demo: thread / linked article recovered
- [ ] Demo: temporarily inaccessible source kept partial + retryable, then recovered on retry
- [x] Focused tests: `tests/grok_x` in omniscience (13 passing, fixtures + CliRunner: dedup, old-post discovery, un-bookmark removal, next_token safety, threads, retry, export). omniscience has no CI yet (tracked as beads issue `omni-5hm`).
- [ ] Second incremental rerun after the demo shows no duplicate notes
