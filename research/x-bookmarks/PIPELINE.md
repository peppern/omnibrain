# X bookmarks pipeline (external)

This content tree is the published knowledge. The ingestion pipeline lives outside this repo so Omnibrain stays text-only.

## Where it lives today

- Working tree on the Grok Bot agent box: `/workspace/second-brain` (local git commit `16632b9`)
- Not yet published as its own GitHub repository (decision pending). When published, replace this bullet with the repo URL and the commit SHA used for the run.
- Entry points: `process.py`, `transcribe.py`, `visual.py`, `threads.py`, `render.py`, `export_omnibrain.py`
- Operator notes: `/workspace/second-brain/README.md`

## How a run works

1. Fetch all bookmark pages for X user `20219699` (`@noahmp`) via the X connector (`get_users_bookmarks`, `max_results=100`, page until exhausted).
2. `python3 process.py --merge all_pages.json --complete` merges only unseen IDs, and removes notes for IDs no longer bookmarked (only when the merge file has no `next_token`).
3. Optional: `transcribe.py` for video audio, `visual.py` for images/frame sheets, `threads.py` for recovered author threads.
4. Agent writes source-grounded summaries into `summaries.json` for IDs listed in `needs_summary.txt`, then `render.py`.
5. `python3 export_omnibrain.py /path/to/omnibrain` refreshes `research/x-bookmarks/{README.md,digest.md,notes/,transcripts/}`.
6. Commit on a feature branch and open or update a PR. Never push to `main`, never force-push.

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

`--complete` now uses a dedicated `merge_payload` so xposts loading cannot drive removals.

## Scheduler

Configured on Grok Bot (agent Waffle):

- Routine name: `Process new X bookmarks`
- Schedule: weekdays at 07:49 (local agent schedule; cron `49 7 * * 1-5`)
- Companion: `Watch Omnibrain PR #1` watches review/CI/merge events on this PR

Evidence of a successful incremental run is filed under `runs/`.

## Acceptance checklist (from PR review)

- [x] Inline content findings addressed (visual/thread recovery, ambiguous source label, digest links + partial flags, first_observed chronology)
- [x] Incremental no-op: full live bookmark fetch + `--complete` merge processed 0 new IDs and left state/content hashes unchanged (see `runs/2026-10-16-incremental.md`)
- [ ] Publish pipeline repo (or attach versioned tarball) and link commit SHA here
- [ ] Demo: newly bookmarked older post discovered and noted regardless of publication date
- [ ] Demo: image or silent-video bookmark inspected
- [ ] Demo: thread / linked article recovered
- [ ] Demo: temporarily inaccessible source kept partial + retryable, then recovered on retry
- [x] Focused tests exist locally (`tests/test_merge_state.py`, 4 passing: dedup, new old-post discovery, un-bookmark removal, next_token safety). Still need the owning repo published so CI can run them.
- [ ] Second incremental rerun after the demo shows no duplicate notes
