# WARDOGS Game Knowledge Base

Evidence-based, source-cited reference for WARDOGS (Bulkhead / Team17): gameplay, combat, vehicles, economy, maps and server administration. Unofficial; not affiliated with Bulkhead or Team17. Every fact cites a source and the game version it applies to.

See `MASTER_INDEX.md` for the catalogue.

## Baselines and staleness checks

`snapshots/<date>/` holds dated captures taken with `python scripts/snapshot_steam_news.py`. The published repo tracks only `steam-news/index.json` (post ids, dates, titles, hashes) and `reviews-summary.json`; the verbatim post bodies and store-page text are third-party content and stay local (gitignored). `scripts/check_steam_gids.py` checks every cited Steam post id against the index. Re-run the script after each patch and diff against the previous folder to find stale claims.
