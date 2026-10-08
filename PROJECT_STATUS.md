# Project Status

Updated 2026-10-08.

- **29 documents frozen** (7 foundations, 22 depth/reference docs) plus the dated baseline snapshot `snapshots/2026-10-08/` (official Steam posts, store data, review summary).
- All 13 pre-snapshot docs were revised to v1.1.0 (economy-foundation v1.2.0, air-and-counter-air v1.0.1) against the full official Steam text. Every Steam post id cited is verified against the snapshot index by `scripts/check_steam_gids.py` (also a CI gate).
- Confidence: see MASTER_INDEX. Low: weapons-catalogue, death-penalty-and-rebuy, season-2-announcements, rcon-and-server-admin, launch-maps-reference.
- **Not officially confirmed (stay labelled):** Season 02 wipe / rain / auto Gold Bar conversion; death penalty and re-buy rules; named maps; RCON/ini details; kernel-level anti-cheat wording and the "fighter jets" and "1-2 years" roadmap claims (not in the saved store JSON; need a live-page check); console 2028 and Linux/Proton statements (press-only, except the launch-trailer console line).
- **Season 02 lands 15 Oct 2026.** Procedure: `python scripts/snapshot_steam_news.py`, diff `snapshots/<new>` against `snapshots/2026-10-08`, then re-verify each doc whose Baseline values table changed (review_due 2026-10-22).
- Nothing published to GitHub.
