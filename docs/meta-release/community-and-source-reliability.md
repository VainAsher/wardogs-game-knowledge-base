---
id: community-and-source-reliability
title: "Community Channels & Source Reliability Register"
version: 1.0.1
status: frozen
confidence: Medium
category: Meta & Release
topic: "Official channels, community hubs, and a reliability rating for every source class and outlet used"
market: Global
game_version: "Early Access Update 0.1.2 (30 Sep 2026) plus hotfixes to 2 Oct 2026; pre-Season-02 baseline (Season 02 due 15 Oct 2026)"
document_type: depth
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-10-22
sources_verified: 2026-10-08
supersedes: null
related: [meta-release-foundation, patch-history, editions-pricing-platforms]
tags: [community, sources, reliability, reviews, baseline, official-channels]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | community-and-source-reliability |
| Version | 1.0.1 |
| Status | frozen |
| Confidence | Medium |
| Category | Meta & Release |
| Game version | Early Access Update 0.1.2 (30 Sep 2026) plus hotfixes to 2 Oct 2026; pre-Season-02 baseline |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-10-22 |
| Sources verified | 2026-10-08 |

# Executive Summary

This document does two jobs. First, it lists the channels BULKHEAD and Team17 are confirmed to use for WARDOGS, based on the official Steam posts saved locally on 2026-10-08. Second, it rates every outlet and site cited anywhere in this knowledge base for reliability, commercial conflict of interest and track record against the official text. It is the basis for future staleness and trust decisions.

The Steam store page (browser-rendered live capture of 2026-10-08) and the Steam News hub are the only channels whose address and content are fully verified. Official posts confirm that a community Discord and "socials" exist [6][11], and that a Twitch show and a contest site were used [9][22], and the live store page links Discord, X, TikTok, Facebook, Instagram and QQ [1], but neither the snapshots nor the capture contain a Discord invite or X handle. On 2026-10-08 the live page showed English "Mostly Positive" (63,179) and "Total reviews in all languages: 95,146" [1], while the storefront review API showed 109,396 reviews (81,290 positive, 74.3% computed) [3]; the two all-language totals disagree and the cause is unexplained.

Confidence is Medium. The channel and review facts rest on official or first-party data (High on their own). The outlet ratings are judgements. I did not re-open every outlet page this session, so track-record notes compare claims already recorded in other KB documents against the official posts, and each rating states that basis.

# Key Takeaways

- Steam is the authoritative channel: 32 of the 65 items in the saved news feed are official posts from BULKHEAD (Steam news snapshot, 2026-10-08) [1][2].
- Official posts confirm a community Discord of "10k+ members" on 9 Feb 2026 and refer to "socials" and Discord announcements, but give no invite link or X handle. The live store page links Discord, X, TikTok, Facebook, Instagram and QQ and says developers engage via Discord, X and YouTube; the link targets (handles, invites) were not captured, so they stay unconfirmed [1][6][7].
- Review figures at 2026-10-08 have two scopes that disagree. Live store page: English Mostly Positive (63,179) and "Total reviews in all languages: 95,146" [1]. Storefront review API (same day): 81,290 positive, 28,106 negative, 109,396 total [3]. The 95,146 versus 109,396 gap is unexplained.
- Methodology lesson: the storefront-API JSON omits page-only fields (anti-cheat product, Steam Deck status, the Early Access developer Q&A), so absence from the API JSON is not evidence of absence from the page; the live page capture is the Primary store source [1].
- The live page names the anti-cheat as Elytra (kernel level) and shows Steam Deck compatibility as Unsupported [1].
- Steam post bodies are now readable from the local snapshot, so patch facts can rest on official text. The earlier "bodies do not render" caveat in other documents is resolved for the 32 official posts.
- Official text confirms, against earlier uncertainty: the 2 Oct balance hotfix (IR Rangefinders disabled until Season 02, CIWS about 6 s instead of 12 s) [21], the 30 Sep date for 0.1.2 [19], and three approved hosts named on 8 Sep [22].
- Official text does not support any Season 02 "progression wipe" claim. The teaser gives only a date (15 Oct 2026) and a trailer [17].
- Commercial sellers (boosting, hosting) and single-source outlets are rated lowest; their claims are leads, never facts (see the register).

# Scope

Covers confirmed official channels, the Steam review snapshot, and a reliability register for every host cited in `docs/` as of 2026-10-08 plus outlets seen in the Steam news feed. Excludes in-game mechanics (see the category foundation documents), patch contents (see patch-history) and prices (see editions-pricing-platforms). Not covered: I did not verify accounts on X, YouTube, Twitch or Discord directly; they are named only where an official post names them.

# Definitions

- **Official**: authored by BULKHEAD or Team17 (Steam announcements, official sites, press release). Source rank 1-3 in `SOURCE_REGISTRY.md`.
- **Press**: independent news outlet reporting on the game (rank 5).
- **Player-reported**: fan sites, guides, wikis, hosts, sellers (ranks 4 and 6). Never establishes a fact alone.
- **COI**: commercial conflict of interest, meaning the publisher sells something the article promotes (boosting, hosting, cash).
- **Reliability grade**: R1 matches official text and is usable as a secondary confirmation; R2 usable with corroboration; R3 lead only, label player-reported; R4 do not cite for facts. Grades are Assessment, not fact.
- **Baseline**: values recorded before the Season 02 wipe window so later diffs are mechanical.

# Current State

## Confirmed official channels (as of 2026-10-08)

| Channel | Status | Evidence |
|---------|--------|----------|
| Steam store page, app 1867240 | Confirmed (live capture 2026-10-08). Developer BULKHEAD, publisher Team17, released 10 Sep 2026, Early Access; names anti-cheat Elytra; Steam Deck: Unsupported | [1][2] |
| Steam News hub / community announcements | Confirmed. The feed carries 65 items; 32 are from the official announcement feed, the rest are outside outlets (PCGamesN, SteamDB, PlayGround.ru, GamingOnLinux, Rock, Paper, Shotgun) | [2] |
| Team17 WARDOGS page and Team17 support | Confirmed. The store record lists Team17 support at team17.com/support; the Team17 game page lists WARDOGS | [4][5] |
| Press release distribution | Team17 press release (via Game Developer) | [23] |
| Community Discord | Existence confirmed: linked from the store page, which also says developers engage there; "10k+ members" (9 Feb 2026) and used for playtest announcements; invite URL not captured | [1][6][7] |
| Social media | Store page links X, TikTok, Facebook, Instagram and QQ, and says developers engage via X; account handles and URLs were not captured | [1][6][15] |
| Twitch (The FPS Games Show, Twitch Drops) | Used for 3 Sep 2026 announcement show; show is a third-party Twitch channel | [9][10] |
| Contest site wardogs100k.com | Named in an official post; not fetched by me | [22] |
| Golden Joystick Awards vote page | Named in an official post (Best Early Access Game 2026 nomination); third-party vote page | [18] |
| YouTube | Store page says developers engage via YouTube (no YouTube link in its links list); trailers and devlogs embedded in official posts; channel address not given | [1][6][7][17] |

Assessment: the Steam page and hub are the only channels this KB should treat as authoritative and link-checkable; confidence High. The store page links Discord and X but the live capture records link labels only, so the official Discord invite and X handle remain unconfirmed; confidence that they exist is High, confidence in any specific handle is none until an official source prints it.

## Approved hosting partners (official channel for server rental)

BULKHEAD's 8 Sep 2026 post names three Approved Hosting Partners: QONZER, BisectHosting and xREALM [22]. BisectHosting is therefore both an approved partner and a seller of hosting; its blog is rated with that COI in the register.

## Steam review snapshot (2026-10-08)

| Field | Value |
|-------|-------|
| Live page: English reviews | Mostly Positive (63,179) [1] |
| Live page: "Total reviews in all languages" | 95,146 (Mostly Positive) [1] |
| Live page: curators who reviewed | 132 [1] |
| API: review score label | Mostly Positive (review_score 6) [3] |
| API: total reviews (all languages, all purchase types) | 109,396 [3] |
| API: positive | 81,290 [3] |
| API: negative | 28,106 [3] |
| API: positive share (computed, not Steam-stated) | 74.3% [3] |

Sources: the browser-rendered live capture of the Steam store page, 2026-10-08 [1], and the storefront review API summary snapshot taken the same day [3]. The earlier figure in meta-release-foundation (79% of 63,152 English reviews) is a different scope (English only), not a contradiction; both fall in the Mostly Positive band. The live page's "Total reviews in all languages: 95,146" [1] differs from the API total of 109,396 [3]; both are described as all-language totals, and the cause of the gap is unexplained (it is not stated on the page). An earlier version of this document called 95,146 a store-record "recommendations total"; the live capture shows it is the page's all-language review total.

# Detail

## Baseline values (pre-Season-02 wipe)

Every row is a value a later snapshot can diff mechanically.

| Value | As-of version / date | Source |
|-------|----------------------|--------|
| Steam review label: Mostly Positive | Update 0.1.2 + hotfixes, 2026-10-08 | [3] |
| Reviews total 109,396 (all languages) | 2026-10-08 | [3] |
| Reviews positive 81,290 | 2026-10-08 | [3] |
| Reviews negative 28,106 | 2026-10-08 | [3] |
| Positive share 74.3% (computed from the two counts) | 2026-10-08 | [3] |
| Live page English reviews: Mostly Positive (63,179) | 2026-10-08 | [1] |
| Live page "Total reviews in all languages" 95,146 (disagrees with API 109,396; unexplained) | 2026-10-08 | [1] |
| Anti-cheat: Elytra (kernel level), named on the store page | 2026-10-08 | [1] |
| Steam Deck compatibility: Unsupported (store page) | 2026-10-08 | [1] |
| Price GBP 36.99 (Standard), GBP 45.99 (Supporter Edition, includes Supporter Pack), Supporter Pack DLC GBP 11.99 | 2026-10-08 | [1][2] |
| Price USD 39.99 (Standard), USD 49.99 (Supporter Edition), Supporter Pack DLC USD 12.99 (USD from the API record; not shown in the GBP page capture) | 2026-10-08 | [2] |
| Release date 10 Sep 2026 | 2026-10-08 | [1][2] |
| Steam news feed items 65, of which 32 official | 2026-10-08 snapshot | [2] |
| Official wishlist milestones: 100,000 (10 Feb), 500,000 (26 May), 1,000,000 (14 Aug 2026) | post titles, 2026 | [2] |
| Official sales milestones: 1.25 million (11 Sep), 2 million (15 Sep), 3 million (26 Sep 2026) | official posts | [14][16][18] |
| Official peak concurrent users: "400,000" (12 Sep post) | 12 Sep 2026 | [15] |
| Community Discord size: "10k+" | 9 Feb 2026 | [6] |
| Approved hosting partners: 3 (QONZER, BisectHosting, xREALM) | 8 Sep 2026 | [22] |
| Season 02 start: 15 Oct 2026 (no time given) | 22 Sep 2026 | [17] |
| Latest patch: Update 0.1.2, 30 Sep 2026, maintenance 08:00 UTC for about 1 hour | 30 Sep 2026 | [19] |
| Latest hotfixes: 2 Oct 2026 security/stability at 08:00 UTC (1 hour); balance hotfix posted 15:39 UTC | 2 Oct 2026 | [20][21] |

Note the 1.25 million, 2 million and 3 million sales figures are the studio's own claims in its own posts; no independent audit is available.

## Methodology lessons (register)

| Lesson | Evidence | Rule going forward |
|--------|----------|--------------------|
| The storefront-API JSON omits page-only fields. Absence from the API JSON is not evidence of absence from the page. | The live capture shows the anti-cheat product (Elytra), Steam Deck status (Unsupported) and the Early Access developer Q&A (1 to 2 years in Early Access; plans for fighter jets; "proximity voice chat"; "Realistic gunplay balanced for gameplay rather than simulation"), none of which the saved API JSON carried [1] | Treat the browser-rendered live store-page capture as the Primary store source; use the API JSON for prices and counts only, and never conclude a feature is absent because the JSON lacks it |
| Two review totals can disagree on the same day | 95,146 on the page versus 109,396 from the review API [1][3] | Record both with scope and field source; do not reconcile by guessing |

## Source-class reliability scale

| Class | Typical sources | How the KB may use it |
|-------|-----------------|------------------------|
| Official (rank 1-3) | Steam page, Steam announcements, Team17 site and press release | Establishes facts, with date and version |
| Press, wire-style | Push Square, Pure Xbox, GamingOnLinux, Vice, MP1st | Confirms release and business facts; label as press |
| Press, aggregating | Gfinity, InGameNews, PlayDay, CoGConnected, GosuGamers, SteamDeckHQ | Cross-check only; re-verify against official text |
| Provider / seller | BisectHosting, XGamingServer, Boostroom, Supercraft, Timesaver | Player-reported with COI; never establishes a fact |
| Fan sites and guides | allthings.how, KeenGamer, Gamebrief, Neonsect, wardogs-game.com, wardogs.tech, Wardog Servers, wardogswiki.com, Dexerto wiki | Player-reported; use only where nothing official exists, labelled |
| Single-source or anonymous | MMOEXP, Gaming with Daopa, XGamingServer roadmap | Leads only |

## Outlet register

Grades: R1 reliable against official text, R2 usable with corroboration, R3 lead only, R4 do not cite alone. "Track record" is stated against the official Steam posts read for this document [2]. Where a row says "not tested", the outlet's claims in this KB have no official counterpart yet.

| Outlet / site | Class | COI | Track record against official text | Grade |
|---------------|-------|-----|-------------------------------------|-------|
| Steam store page (live capture) and API | Official | None | Prices, date, developer, publisher and review counts are first-party [1][2][3]. The page carries fields the API JSON omits (anti-cheat, Deck status, developer Q&A), so the page is the Primary store source [1]. The page and API all-language review totals disagree (95,146 versus 109,396), unexplained [1][3] | Authority |
| Steam News (BULKHEAD posts) | Official | Self-reporting | Authority for patches, dates and studio claims. Studio sales figures are its own claims [2] | Authority |
| Team17 game page / support | Official | Publisher | Lists game and support; no contradiction found [4][5] | Authority |
| Team17 press release (gamedeveloper.com) | Official, republished | Publisher marketing | Dates and price claims agree with the Steam page; 21-23 Aug beta matches the official post [7][23] | R1 |
| Gfinity Esports | Press | None found | Season 1 changelog matches the official 9 Sep pre-load post on XP bands and prices, but labels it 10 Sep (the official post is dated 9 Sep) [12][24]. 0.1.2 notes match the official 30 Sep text [19][25]. Its 3-6 Sep beta dating is consistent with the official Closed Beta 02 and open-beta posts [10][11] | R1 |
| MP1st | Press | None found | 0.1.2 date (30 Sep) and 08:00 UTC window match [19][26] | R1 |
| Vice | Press | None found | 0.1.2 notes: 30 Sep, same window [19][27]. The Season 2 "rain" article cites a BULKHEAD statement that is not in the saved official posts [28] | R2 |
| InGameNews | Press | None found | Timestamps accurate: 0.1.2 at 06:57 UTC and the hotfix post at 00:13 UTC match the official posts to the minute [19][20][29]. Its ambiguity over whether the hotfix was scheduled is resolved by the official post: scheduled for 08:00 UTC, one hour [20] | R1 |
| PlayDay | Press | None found | 0.11 notes match the official 12 Sep post on browser split, persistent IDs and the 5% bonus [15][30] | R1 |
| Push Square, Pure Xbox | Press | None found | 1.25 million sold by 11 Sep matches the official post [14][31][32]; Xbox/PS5 2028 is not testable on Steam | R1 |
| GamingOnLinux, SteamDeckHQ | Press | None found | Linux/Proton statements come from developers; the studio's Steam feed itself carries GamingOnLinux items [2][33][34] | R2 |
| CoGConnected, GosuGamers | Press | None found | "Over 1 million" and "3 million in just over two weeks" agree with the official posts [14][18][35][36] | R1 |
| Gameluster | Press | None found | 1 million wishlists agrees with the official 14 Aug post [2][37] | R1 |
| PCGamesN, Rock Paper Shotgun, PlayGround.ru, SteamDB | Press / stats, seen in the feed only | None found | Bodies were not saved, so no track record could be tested; not cited as facts in this KB [2] | Not rated |
| KeenGamer | Press and guides | None found | Season 2 "confirmed features, rumors" mixes both labels in the title; progression guide is player-reported [38][39] | R3 |
| Dexerto wiki | Community wiki on a press brand | None found | Its Season 2 wiki asserts a wipe and Black Market that the official teaser does not state [17][40] | R3 |
| allthings.how | Guide site | None found | Maps/Control Zone figures conflict with the official 2x2 km Control Zone; "four playable battlegrounds" intro contradicts its own list [41][42] | R3 |
| Gamebrief | Guide site | None found | Maps/vehicle guides agree with the three-launch-maps count; no official counterpart for numbers [43] | R3 |
| Timesaver.gg | Seller blog | Yes (boosting/cash seller) | 2 Oct hotfix: IR rangefinder disabled and CIWS 12 s to 6 s agree with the official post [21][44]. Season 2 article: wipe, Gold Bar conversion and 16:00 UTC time are not in the teaser [17][45] | R3 for hotfix (verified), R4 for Season 2 |
| MMOEXP | Seller blog, single podcast | Yes (currency seller) | Dates the 0.1.2 patch to 29 Sep; the official post says 30 Sep [19][46]. Season 2 wipe claim not supported [17] | R4 |
| BisectHosting blog | Provider | Yes (approved host partner) | 0.1.2 admin notes (restart time, RCON) match the official text [19][22][47] | R2 |
| XGamingServer, Boostroom, Supercraft | Hosting / boosting sellers | Yes | Map guides and prices uncorroborated; hosting prices are pre-approval and not official [48][49][50] | R4 |
| wardogs-game.com, wardogs.tech, wardogservers.com, warcon (GitHub) | Unofficial fan and tool sites | Mixed (tracker/tool publishers) | Host count (two to three) is dated, not wrong, and the official 8 Sep post confirms three [22][51][52][53][54] | R3 |
| Neonsect | Fan guide | None found | Its three named hosts match the official 8 Sep post exactly [22][55] | R2 |
| wardogswiki.com | Unofficial wiki | Unknown | Season 2 page not corroborated by the teaser [17][56] | R3 |
| Gaming with Daopa | Community repost | Unknown | Closed-beta notes dated 14 Aug are not in the saved official feed; unverified [2][57] | R4 |

Assessment: ranking the outlets by agreement with official text, wire and aggregator press (Gfinity, MP1st, InGameNews, PlayDay, Push Square) is dependable on dates and patch contents; sellers and wikis are dependable only when an official post confirms the specific claim. Confidence High for the agreement findings (compared line by line to official text), Medium for the COI judgements (inferred from what each site sells).

## Where earlier KB documents are corrected or sharpened by official text

| Topic | Earlier KB wording | Official text | Effect |
|-------|--------------------|---------------|--------|
| IR Rangefinders and CIWS (2 Oct) | CWIS 12 s to 6 s "reported by a conflicted source"; battery rule "player-reported" | Official: Rangefinders disabled in the vendor until Season 02 where they "will require batteries"; CIWS now about 6 s versus 12 s [21] | Can be treated as official; supersedes the conflict note |
| Security hotfix (2 Oct) | Ambiguous whether scheduled or completed | Post at 00:13 UTC announces a planned 08:00 UTC fix on "Friday 2nd", one hour [20] | Resolved: scheduled |
| Closed beta dates | Open question whether 21-23 Aug and 3-6 Sep were one beta | Two betas: 21-23 Aug closed beta [7][8][9]; Closed Beta 02 announced 1 Sep, opened to all on 5 Sep until Sunday 08:00 UTC [10][11] | Resolved: two betas |
| Season 1 changelog date | 10 Sep | Official "Pre-Load Live & Season 1 Changelog" is dated 9 Sep [12] | Date should read 9 Sep for the notes, 10 Sep for launch |
| Season 02 wipe | Reported by Dexerto and Timesaver | Teaser contains only the date and a trailer; the 0.1.2 post says Season 02 has "new map conditions, equipment, balance reworks and additional features" [17][19] | Wipe remains unconfirmed |
| Hosting partners | Fan guide says QONZER, BisectHosting, xREALM | Official post names the same three on 8 Sep [22] | Confirmed |

# Early Access Changes & Known Issues

- 10 Sep 2026: launch stability hotfix #1 forced a client restart and batch re-entry after join, kick and queue problems [13].
- 12 Sep 2026: the studio publicly said community servers had been "underserved" and shipped 0.11 [15].
- 2 Oct 2026: two hotfixes in one day (security/stability at 08:00 UTC; balance hotfix at 15:39 UTC) [20][21].
- Season 02 on 15 Oct 2026 will change many baseline values; re-run this register after it, including review counts and the 65/32 feed counts [17].

# Admin & Technical Notes

The official admin-facing channels are the Steam announcements for the Approved Hosting Partners and 0.1.2 admin notes (daily restart, RCON AllowedHosts) [19][22]. Third-party RCON references are rated in the register (R3). Server docs themselves are covered in technical-servers-foundation.

# Risks & Caveats

- Grades are judgements frozen at 2026-10-08 and the outlets will change; a single wrong article lowers a grade only if repeated.
- I did not re-open each outlet's page this session; outlet notes rely on claims already recorded in other KB documents and the official posts. The grade for an outlet I compared only on one fact (for example Vice) is correspondingly weak.
- Steam feed items from non-official feeds (PCGamesN and others) were not saved, so they could not be tested.
- Review counts and positive share change daily; the baseline is a snapshot, not a trend. The page and API figures may differ partly through timing or method; that is a guess, not a finding.
- The live capture records link labels (Discord, X and others), not their target URLs, and omits account-specific lines by design.
- Studio sales and concurrency numbers are self-reported and unaudited.
- The review summary URL used in the reference list is the Steam reviews endpoint shape matched by the saved file; the checker may not follow it.

# Open Questions

- Official WARDOGS Discord invite URL, X handle and the TikTok, Facebook, Instagram and QQ addresses: the live store page links them [1] but the capture did not record targets. Capturing the link hrefs would resolve this.
- Why the store page's "Total reviews in all languages" (95,146) differs from the review API total (109,396) [1][3].
- Whether the Vice "rain will not change mid-match" statement exists in an official post (it is not in the saved Steam feed; it may come from X or Discord).
- Whether Dexerto, Timesaver and wardogswiki.com describe a Season 02 wipe from a real developer statement or from speculation; the 15 Oct notes will decide.
- Whether the Gaming with Daopa 14 Aug closed-beta notes are genuine developer notes; no matching official post is saved.

# References

**Primary Sources**

- [1] **Valve / BULKHEAD** — *WARDOGS on Steam* (browser-rendered live capture 2026-10-08, saved as snapshots/2026-10-08/store-page-live.txt). https://store.steampowered.com/app/1867240/WARDOGS/. Accessed 2026-10-08.
- [2] **Valve / BULKHEAD** — *Steam storefront API record and saved Steam news feed index* (local snapshot 2026-10-08; omits page-only fields). https://store.steampowered.com/news/app/1867240. Accessed 2026-10-08.
- [3] **Valve** — *Steam reviews summary for app 1867240* (local snapshot 2026-10-08). https://store.steampowered.com/appreviews/1867240?json=1&language=all&purchase_type=all&num_per_page=0. Accessed 2026-10-08.
- [4] **Team17** — *WARDOGS game page*. https://www.team17.com/games/wardogs/. Accessed 2026-10-08.
- [5] **Team17** — *Team17 support*. https://www.team17.com/support/. Accessed 2026-10-08.
- [6] **BULKHEAD** — *WARDOGS Official Announcement Trailer* (Steam post, 9 Feb 2026). https://store.steampowered.com/news/app/1867240/view/1823825466504264. Accessed 2026-10-08.
- [7] **BULKHEAD** — *PRE-ORDER NOW!* (Steam post, 11 Aug 2026). https://store.steampowered.com/news/app/1867240/view/1840310314354505. Accessed 2026-10-08.
- [8] **BULKHEAD** — *WARDOGS Closed Beta Schedule* (Steam post, 20 Aug 2026). https://store.steampowered.com/news/app/1867240/view/1841579228666871. Accessed 2026-10-08.
- [9] **BULKHEAD** — *WARDOGS Beta Recap & Next Steps* (Steam post, 24 Aug 2026). https://store.steampowered.com/news/app/1867240/view/1841579228676589. Accessed 2026-10-08.
- [10] **BULKHEAD** — *WARDOGS Closed Beta 02 Announcement* (Steam post, 1 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1842212951313938. Accessed 2026-10-08.
- [11] **BULKHEAD** — *The Closed Beta Is Now An Open Beta* (Steam post, 5 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1842846814449809. Accessed 2026-10-08.
- [12] **BULKHEAD** — *Pre-Load Live & Season 1 Changelog* (Steam post, 9 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1843481262690549. Accessed 2026-10-08.
- [13] **BULKHEAD** — *Launch Stability Hotfix #1* (Steam post, 10 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1843481262693332. Accessed 2026-10-08.
- [14] **BULKHEAD** — *1.25 Million Copies Sold!* (Steam post, 11 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1843481262693807. Accessed 2026-10-08.
- [15] **BULKHEAD** — *Scheduled Maintenance & Patch 0.11* (Steam post, 12 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1843481262698449. Accessed 2026-10-08.
- [16] **BULKHEAD** — *2 Million Copies Sold* (Steam post, 15 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1843481262705755. Accessed 2026-10-08.
- [17] **BULKHEAD** — *WARDOGS Season 02 Teaser* (Steam post, 22 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1844115010504839. Accessed 2026-10-08.
- [18] **BULKHEAD** — *3 Million Sales + Golden Joystick Awards* (Steam post, 26 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1844751498227777. Accessed 2026-10-08.
- [19] **BULKHEAD** — *WARDOGS Update 0.1.2 (Minor Patch)* (Steam post, 30 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1845383656376490. Accessed 2026-10-08.
- [20] **BULKHEAD** — *WARDOGS Security & Stability Hotfix* (Steam post, 2 Oct 2026). https://store.steampowered.com/news/app/1867240/view/1845383656384445. Accessed 2026-10-08.
- [21] **BULKHEAD** — *IR Goggles & CIWS Balance Hotfix* (Steam post, 2 Oct 2026). https://store.steampowered.com/news/app/1867240/view/1845383656386801. Accessed 2026-10-08.
- [22] **BULKHEAD** — *The 11th Reason NOT To Buy WARDOGS* (Steam post, 8 Sep 2026; names wardogs100k.com and the three Approved Hosting Partners). https://store.steampowered.com/news/app/1867240/view/1842846814456311. Accessed 2026-10-08.
- [23] **Team17 / BULKHEAD** — *WARDOGS is coming to Steam Early Access on 10 September* (press release). https://www.gamedeveloper.com/press-release/wardogs-is-coming-to-steam-early-access-on-10-september. Accessed 2026-10-08.

**Press & Secondary**

- [24] **Gfinity Esports** — *WARDOGS Season 1 changelog*. https://www.gfinityesports.com/article/wardogs-season-1-changelog-early-access-patch-notes. Accessed 2026-10-08.
- [25] **Gfinity Esports** — *Wardogs Update 0.1.2 Patch Notes*. https://www.gfinityesports.com/article/wardogs-update-012-patch-notes-cash-and-xp-exploit-fixes-are-here. Accessed 2026-10-08.
- [26] **MP1st** — *Wardogs Update 0.1.2 Deployed on September 30*. https://mp1st.com/title-updates-and-patches/wardogs-update-0-1-2-deployed-on-september-30-as-servers-go-down. Accessed 2026-10-08.
- [27] **Vice** — *WARDOGS update 0.1.2 patch notes*. https://www.vice.com/en/article/wardogs-update-0-1-2-patch-notes/. Accessed 2026-10-08.
- [28] **Vice** — *WARDOGS developer confirms Season 2 rain will not change mid-match*. https://www.vice.com/en/article/wardogs-season-2-rain-progression-wipe/. Accessed 2026-10-08.
- [29] **InGameNews** — *WARDOGS update 0.1.2 and security hotfix*. https://ingamenews.com/gaming-news/wardogs-update-0-1-2-and-security-hotfix-a-comparative-overview/. Accessed 2026-10-08.
- [30] **PlayDay** — *WARDOGS patch 0.11 focuses on server browsers*. https://playday.one/2026/09/14/wardogs-patch-11-focuses-on-server-browsers-full-notes/. Accessed 2026-10-08.
- [31] **Push Square** — *Multiplayer shooter WARDOGS confirmed for PS5*. https://www.pushsquare.com/news/2026/09/multiplayer-shooter-wardogs-confirmed-for-ps5-as-early-access-launch-goes-nuclear. Accessed 2026-10-08.
- [32] **Pure Xbox** — *WARDOGS is coming to Xbox in 2028*. https://www.purexbox.com/news/2026/09/wardogs-is-coming-to-xbox-in-2028-and-is-available-today-with-steam-early-access. Accessed 2026-10-08.
- [33] **GamingOnLinux** — *WARDOGS developers clarify Linux support via Proton may come later*. http://www.gamingonlinux.com/2026/09/wardogs-developers-clarify-linux-support-via-proton-may-come-later. Accessed 2026-10-08.
- [34] **SteamDeckHQ** — *WARDOGS devs are working on Proton support*. https://steamdeckhq.com/news/wardogs-devs-are-working-on-proton-support/. Accessed 2026-10-08.
- [35] **CoGConnected** — *WARDOGS has officially sold over 1 million copies*. https://cogconnected.com/2026/09/wardogs-has-officially-sold-over-over-1-million-copies/. Accessed 2026-10-08.
- [36] **GosuGamers** — *WARDOGS sells 3 million copies in just over two weeks*. https://www.gosugamers.net/entertainment/news/79260-wardogs-sells-3-million-copies-in-just-over-two-weeks-after-early-access-launch. Accessed 2026-10-08.
- [37] **Gameluster** — *Wardogs hits one million wishlists*. https://gameluster.com/wardogs-million-wishlists/. Accessed 2026-10-08.
- [38] **KeenGamer** — *WARDOGS Season 2: confirmed features, rumors, changes*. https://www.keengamer.com/articles/guides/wardogs-season-2-confirmed-features-rumors-changes/. Accessed 2026-10-08.

**Player-Reported Evidence** — labelled as such in the text.

- [39] **KeenGamer** — *WARDOGS progression guide*. https://www.keengamer.com/articles/guides/wardogs-progression-guide/. Accessed 2026-10-08.
- [40] **Dexerto** — *WARDOGS Season 2 update* (community wiki). https://www.dexerto.com/wikis/wardogs/season-2-update/. Accessed 2026-10-08.
- [41] **allthings.how** — *WARDOGS maps: every location*. https://allthings.how/wardogs-maps-every-location-and-what-each-one-fights-over/. Accessed 2026-10-08.
- [42] **allthings.how** — *WARDOGS Hot Zone*. https://allthings.how/wardogs-hot-zone-how-double-presence-and-double-cash-work/. Accessed 2026-10-08.
- [43] **Gamebrief** — *WARDOGS maps guide*. https://www.gamebrief.net/blog/wardogs-maps-guide-2026. Accessed 2026-10-08.
- [44] **Timesaver.gg** — *WARDOGS IR goggles and CWIS hotfix* (boosting seller). https://timesaver.gg/blog/wardogs-ir-goggles-cwis-hotfix. Accessed 2026-10-08.
- [45] **Timesaver.gg** — *WARDOGS Season 2: everything we know* (boosting seller). https://timesaver.gg/blog/wardogs-season-2-everything-we-know. Accessed 2026-10-08.
- [46] **MMOEXP** — *WARDOGS October 2 update, Season 2 wipe* (single podcast). https://www.mmoexp.com/News/wardogs-october-2-update-season-2-wipe-ir-rangefinder-nerf-and-new-weapons.html. Accessed 2026-10-08.
- [47] **BisectHosting** — *WARDOGS Update 0.1.2 patch notes* (approved host). https://www.bisecthosting.com/blog/wardogs-update-0-1-2-patch-notes-bug-fixes-improvements-flythrough-exploit-fob-pallet-delivery-xp. Accessed 2026-10-08.
- [48] **XGamingServer** — *WARDOGS map guide* (hosting seller). https://xgamingserver.com/blog/wardogs-map-guide/. Accessed 2026-10-08.
- [49] **Boostroom** — *WARDOGS map guide* (boosting seller). https://boostroom.com/blog/wardogs-map-guide-control-zones-hot-zones-and-battlefield-strategy. Accessed 2026-10-08.
- [50] **Supercraft.host** — *WARDOGS hosting reservation page* (host, not confirmed approved). https://supercraft.host/?p=49132. Accessed 2026-10-08.
- [51] **WARDOGS-game.com (unofficial fan site)** — *Servers, Regions & Hosting*. https://wardogs-game.com/servers. Accessed 2026-10-08.
- [52] **wardogs.tech (unofficial)** — *Wardogs Server Reference*. https://wardogs.tech/rcon-reference. Accessed 2026-10-08.
- [53] **Wardog Servers (independent tracker)** — *WARDOGS RCON and admin tools*. https://wardogservers.com/guides/wardogs-rcon-and-admin-tools. Accessed 2026-10-08.
- [54] **Warcon project (GitHub)** — *warcon: self-hostable RCON panel*. https://github.com/warcon-app/warcon. Accessed 2026-10-08.
- [55] **Neonsect** — *WARDOGS community servers guide*. https://neonsect.com/wardogs/wardogs-community-servers-guide/. Accessed 2026-10-08.
- [56] **wardogswiki.com (unofficial)** — *WARDOGS Season 2*. https://www.wardogswiki.com/en/guides/wardogs-season-2. Accessed 2026-10-08.
- [57] **Gaming with Daopa** — *Wardogs Closed Beta Patch Notes, August 14th*. https://gamingwithdaopa.ellatha.com/wardogs/closed-beta-patch-notes-august-14th/. Accessed 2026-10-08.

# Further Reading

- The saved official posts in `snapshots/2026-10-08/steam-news/` (index.json lists every gid).
- SOURCE_REGISTRY.md for the ranked source order and the bot-block host list.

# Related Documents

- meta-release-foundation
- patch-history
- editions-pricing-platforms

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft: official channels, review baseline, outlet reliability register. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after independent re-verification of validate, markdownlint, links (0 dead) and Steam post ids. Pre-Season-02 baseline. | Standing mandate (auto-approve on green QA) |
| 1.0.1 | 2026-10-08 | Research Pipeline (revision worker) | Corrected against live store-page capture; review figures recorded with scope (page 63,179 English and 95,146 all-language versus API 109,396), 95,146 no longer called "recommendations"; methodology lesson added; official channels updated (Discord, X, TikTok, Facebook, Instagram, QQ, YouTube engagement); Steam Deck Unsupported; anti-cheat Elytra; second package named Supporter Edition | Standing mandate (auto-approve on green QA) |
