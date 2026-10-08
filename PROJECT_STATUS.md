# Project Status

Updated 2026-10-08.

- **29 documents frozen** (7 foundations, 22 depth/reference docs) plus the dated baseline snapshot `snapshots/2026-10-08/` (official Steam posts, store data, review summary).
- All 13 pre-snapshot docs were revised to v1.1.0 (economy-foundation v1.2.0, air-and-counter-air v1.0.1) against the full official Steam text. Every Steam post id cited is verified against the snapshot index by `scripts/check_steam_gids.py` (also a CI gate).
- Confidence: see MASTER_INDEX. Low: weapons-catalogue, death-penalty-and-rebuy, season-2-announcements, rcon-and-server-admin, launch-maps-reference.
- **Live store page checked in Chrome (2026-10-08, `snapshots/2026-10-08/store-page-live.txt`):** kernel anti-cheat is named (Elytra); Steam Deck is Unsupported; fighter jets, 'around 1 to 2 years' Early Access, lower EA price, 'Realistic gunplay balanced for gameplay rather than simulation', 'proximity' and 'local' voice chat, melee, and 'large-scale maps with dynamic objective zones' are all Primary store-page claims. The storefront API JSON omits these page-only fields: absence from it is not evidence of absence from the page. Review totals disagree and are unexplained (page 95,146 all-language vs API 109,396).
- **Not officially confirmed (stay labelled):** Season 02 wipe / rain / auto Gold Bar conversion; death penalty and re-buy rules; named maps; RCON/ini details; console 2028 and Linux/Proton statements (press-only, except the launch-trailer console line).
- **Season 02 lands 15 Oct 2026.** Procedure: `python scripts/snapshot_steam_news.py`, diff `snapshots/<new>` against `snapshots/2026-10-08`, then re-verify each doc whose Baseline values table changed (review_due 2026-10-22).
- Nothing published to GitHub.
