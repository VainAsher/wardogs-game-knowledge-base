# CLAUDE.md — WARDOGS Knowledge Base rules

Subject: WARDOGS (Bulkhead / Team17), a 100-player, 3-team tactical FPS in Steam Early Access since 10 Sept 2026 (Steam app 1867240).
Audience: players and server admins. Genre: **reference**. Region: Global.

## Rules (never relax)
1. Evidence over model confidence. Every fact cites an authoritative source with a working link and states the game version/date it applies to.
2. Early Access: facts churn per patch. Each doc carries `game_version` and `review_due`; a fact change cuts a new version with a revision note, never a silent edit.
3. Community material (Reddit, wikis, videos) is labelled player-reported and never establishes a fact alone.
4. One writer per file. Workers write only their own doc and never edit shared files or run git. Only the orchestrator edits shared files, runs git and releases.
5. Gates, all green before freezing: `validate.py`, `markdownlint`, `check_links.py` (0 dead; orchestrator re-runs independently).
6. Flow: worker clusters -> merge -> gate -> freeze at v1.0.0 + git tag per cluster. Standing mandate (granted 2026-10-08): auto-approve on green QA; pause on gate failures or unverifiable core claims.
7. Publishing to GitHub only on explicit per-repo authorization.
8. Unofficial fan reference. Not affiliated with Bulkhead or Team17.
