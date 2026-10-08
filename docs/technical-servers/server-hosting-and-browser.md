---
id: server-hosting-and-browser
title: "Server Hosting & Server Browser"
version: 1.0.0
status: frozen
confidence: Low
category: Technical & Servers
topic: "Official vs community servers, approved hosts, regions, browser behaviour, restarts"
market: Global
game_version: "Season 1, patch 0.1.2 plus hotfixes to 2 Oct 2026"
document_type: depth
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [technical-servers-foundation, rcon-and-server-admin, meta-release-foundation]
tags: [servers, hosting, server-browser, community-servers, approved-hosts]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | server-hosting-and-browser |
| Version | 1.0.0 |
| Status | frozen |
| Confidence | Low |
| Category | Technical & Servers |
| Game version | Season 1, patch 0.1.2 plus hotfixes to 2 Oct 2026 |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

This depth document extends the technical-servers-foundation with how WARDOGS servers are obtained and found: the hosts-only model, the approved hosts, the Official and Community split introduced in patch 0.11, regions, browser behaviour, slot counts, restart handling and prices. It is verified as far as the sources allow against Season 1, patch 0.1.2 and hotfixes to 2 October 2026. Season 02 is reported for 15 October 2026 and is outside this version [3].

Headline findings: the hosting-count conflict (two versus three) is a dating problem rather than a contradiction. A fan site reporting evidence checked on 1 September 2026 says two unnamed hosts had passed [1]; a guide checked on 13 September says the studio named QONZER and BisectHosting on 7 September and xREALM on 8 September, giving three [3]. Prices, slot sizes and regions are known only from provider pages and fan guides. The 12-hour versus 24-hour restart conflict could not be resolved: no source read states either interval, and the only documented mechanism is a once-daily restart time in UTC [2][3].

Confidence is Low. The patch 0.11 browser facts rest on a press summary of official notes [4], but the approved-host names, prices, slot tiers and regions rest on fan sites and commercial pages, and key claims conflict or are undated.

# Key Takeaways

- Self-hosting is reportedly not offered: the developer is said not to release server code, so community servers are rented from approved hosts (fan-site relay; player-reported) [1][3].
- Host count is dated, not contradictory: two unnamed hosts as of 1 Sep 2026 [1]; QONZER and BisectHosting named 7 Sep and xREALM added 8 Sep, per a fan guide relaying the studio's X posts, checked 13 Sep 2026 [3]. The studio's own posts were not read first-hand.
- Patch 0.11 (14 Sep 2026) split the browser into Community and Official; Official lost its filters because Official servers did not run modified modes, and Community gained text search and a Show Empty/Full option [4].
- Community server IDs persist across matches and restarts since 0.11, and are longer for security [4].
- Update 0.1.2 (30 Sep 2026) added a daily restart time for community admins, set in UTC; no source gives a built-in 12 h or 24 h interval [2][3].
- Listed monthly prices on provider pages (checked 13 Sep 2026): QONZER GBP 49.95 to 69.95, BisectHosting from USD 71.99, xREALM from EUR 59.99; smallest size sold is 60 slots (player-reported compilation) [3].
- No authoritative region list exists; fan and tracker sources disagree on labels [5][6].

# Scope

Covers the hosting model, approved hosts, Official versus Community servers, regions, browser behaviour, slots, restart cycles, how a prospective admin gets a server, and documented costs, at Season 1 / 0.1.2 with hotfixes to 2 Oct 2026. Excludes RCON and config detail (see rcon-and-server-admin and the foundation), system requirements, and release and pricing history of the game itself (meta-release-foundation). Official versus provider or fan reporting is labelled throughout; nothing here is read directly from a Bulkhead server document.

# Definitions

- **Community server:** a server rented from an approved host and listed in the Community browser [4].
- **Official server:** a Bulkhead-run server in the Official browser; no modified game modes at 14 Sep 2026 [4].
- **Approved host:** a provider the studio permits to run community servers; reportedly the only parties with access to server code [1][3].
- **Deploy screen:** the in-game flow that leads to the server browsers; updated in 0.1.2 [3].

# Current State

Statements at Season 1 / patch 0.1.2, checked 2026-10-08.

- **Hosts-only model.** Self-hosting is not supported; the developer is reported to withhold server code, citing security and performance (fan site, evidence dated to 1 Sep 2026; player-reported) [1]. A second guide says no other host has access to the server code [3].
- **Approved hosts.** Three: QONZER, BisectHosting and xREALM, named by the studio on 7 and 8 September 2026 according to a fan guide (player-reported, checked 13 Sep 2026) [3]. A tracker (updated 14 Sep 2026) says three approved hosts exist but does not name them [5].
- **Browser.** Community and Official lists since 14 Sep 2026 [4]; the Deploy screen offers Official, Community, Infantry Mode and Low-Level options as of 0.1.2 (player-reported summary) [3].
- **Restart.** Community admins can set a daily restart time in UTC (BisectHosting blog, a provider) [2].
- **Regions.** A tracker lists seven regions it tracks (see Detail) [5]; no official list was found.

# Detail

## Resolving the host count (2 versus 3)

| Date of evidence | Claim | Source | Class |
|------------------|-------|--------|-------|
| 1 Sep 2026 | Two hosts passed launch standards, names unpublished, more in the pipeline | [1] | Fan site |
| 7 Sep 2026 | Studio names QONZER and BisectHosting (relayed) | [3] | Fan guide |
| 8 Sep 2026 | Studio adds xREALM (relayed) | [3] | Fan guide |
| 14 Sep 2026 | "Only the three approved hosts run WARDOGS servers" | [5] | Tracker |

Assessment: the sequence is consistent with two hosts growing to three in early September; the conflict is stale evidence, not disagreement. Confidence Medium, resting on [1][3][5], all unofficial; the studio posts themselves were not read. Other sellers (XGamingServer, Survival Servers, LOW.MS, Supercraft) advertise WARDOGS hosting but were not on the named list; XGamingServer itself says it is "onboarding" through partners and does not claim approval [7][8]. Treat such pages as pre-approval marketing.

## Official versus Community (patch 0.11, 14 Sep 2026) [4]

| Aspect | Official | Community |
|--------|----------|-----------|
| Operator | Bulkhead | Approved host customer |
| Filters | Removed in 0.11 (no modified modes); advanced filters restored in 0.1.2 per foundation | Reliability improved, text search added |
| Quick bar | Show Empty/Full added | Show Empty/Full added |
| Server ID | n/a | Persistent, longer, unique, joinable by ID |
| Naming | Names sorted alphabetically ignoring special characters and numbers; no repeated spaces | Same |

Planned and not shipped per the 0.11 post: favouriting, tiered priority queues, Message of the Day, improved warmup, AFK-kick suspension during seeding, team-switching controls [4]. A one-week 5 percent End of Match cash bonus on Community servers ran from 14 Sep and has ended [3][4].

## Browser behaviour

- Region is picked via Deploy, Server Browser, Region, tick regions, Confirm (player-reported guide) [6]. The 0.1.2 region selector shows how many regions are selected [2].
- Ticking several regions has been reported to return an empty list; guides advise selecting one, and clearing persisted search text (player-reported) [3][6]. A fan site calls the one-region rule a temporary August Beta workaround, not a confirmed Early Access rule [1].
- Asian capacity was increased in 0.11; no slot or per-region figures were published [4].

## Regions

| Source | Regions named | Class |
|--------|---------------|-------|
| Tracker, 14 Sep 2026 | Europe, North America East, North America Central, North America West, Oceania, Asia, South America | Player-reported [5] |
| Guide screenshot caption | Europe, North America, South America, Asia, with ping values | Player-reported [6] |
| Hosting vendor | Datacentres in East/West USA, Europe (Germany), Oceania, Singapore | Commercial [7] |

No official list was found; labels disagree. Oceania as a browser region is unconfirmed [1][6].

## Slots and capacity

Matches are 100 players across three teams per the foundation. Hosts sell by different units: xREALM 60, 80 or 100 player packages; QONZER sells by CPU threads (8, 10 or 12) and says it does not limit slots; the smallest size sold anywhere is 60 slots (player-reported compilation, 13 Sep 2026) [3]. The unofficial config reference lists `MaxPlayers` default 128, "clamped by a developer-set min/max" [9].

## Costs (provider pages as compiled 13 Sep 2026; verify before buying) [3]

| Host | Price shown | Notes |
|------|-------------|-------|
| QONZER | GBP 49.95, 59.95, 69.95 per month | 5% quarterly, 10% semi-annual, 15% annual prepay discounts |
| BisectHosting | from USD 71.99 per month | per-tier prices not visible |
| xREALM | from EUR 59.99 per month | 60/80/100 slots |

Roundups conflict with these figures [3]. Pre-approval pages quote far lower numbers (for example XGamingServer USD 24.50 to 42.00 and a Supercraft reservation page USD 17.99 to 39.99), marked "coming soon" or reservation-only [7][8]; they are not approved-host prices.

## Restart cycles (12 h versus 24 h)

- Documented: a daily restart time, in UTC, settable by community admins since 0.1.2 [2]. This is a once-per-day schedule, which fits "24 h", but no source states a default interval.
- Not documented: the unofficial config reference lists no scheduled-restart key, only on-demand `POST /v1/match/restart`; some session keys apply only at next restart [9].
- The 12 h figure was not found in any source I could open; searches returned only unrelated client memory-leak advice. The foundation's statement that host guides disagree remains unverified. Persistent IDs mean a restart no longer changes a server's identity [4].

## How a prospective admin gets a server

1. Choose one of the three named hosts (QONZER, BisectHosting, xREALM) [3]. 2. The in-game Host button links to the hosting page [3][4]. 3. Check slots, region, billing term and refund terms on the host's own page [1]. 4. RCON was described in August as in development, with day-one controls limited to maps and modes [1]; RCON additions arrived in 0.1.2 [2] (see rcon-and-server-admin).

# Early Access Changes & Known Issues

- 10 Sep 2026: Host button links to hosting page (foundation, citing the Season 1 changelog).
- 14 Sep 2026 (0.11): Community/Official split, persistent IDs, Asian capacity up, one hour downtime from 08:00 UTC [4].
- 30 Sep 2026 (0.1.2): daily restart time, region count display, RCON AllowedHosts [2]; Deploy flow per [3].
- Known: multi-region selection can show an empty list (player-reported) [3]. Favourites and priority queues are unshipped [4].

# Admin & Technical Notes

Provider material (labelled): BisectHosting's blog, a host, is the only source for the daily restart wording [2]; the host-specific panels differ and RCON access depends on the host. Hosts are the only route to server files; do not buy from unlisted sellers. Persistence of bans and rotation across restarts and reinstalls is a question to put to the host [5].

# Risks & Caveats

- Host names, prices and slot sizes are third-party compilations from 13 to 14 Sep and will have moved; Season 02 (15 Oct 2026) may change the model.
- The studio's X posts naming hosts were not read first-hand; fan relay only.
- Provider pages are marketing and some predate the approval announcements.
- WebFetch summaries of dynamic pages may omit content.

# Open Questions

- Official Bulkhead statement of the approved host list and any further additions after 8 Sep 2026.
- Is there any default restart interval (12 h or 24 h), and who stated it?
- Official region list and whether Oceania and South America are separate in the picker.
- Real current prices; whether Official servers have fixed slot counts.
- Do favourites, priority queues and MOTD ship in Season 02?

# References

**Primary Sources**

None read first-hand for this document; the Steam news bodies and the studio's X posts were not readable. See the foundation for the Steam page.

**Press & Secondary**

- [2] **BisectHosting (hosting provider, secondary)** — *WARDOGS Update 0.1.2 patch notes*. https://www.bisecthosting.com/blog/wardogs-update-0-1-2-patch-notes-bug-fixes-improvements-flythrough-exploit-fob-pallet-delivery-xp. Accessed 2026-10-08.
- [4] **PlayDay** — *WARDOGS patch 0.11 focuses on server browsers (full notes)*. https://playday.one/2026/09/14/wardogs-patch-11-focuses-on-server-browsers-full-notes/. Accessed 2026-10-08.

**Player-Reported Evidence**

- [1] **WARDOGS-game.com (unofficial fan site)** — *WARDOGS Servers, Regions & Hosting*. https://wardogs-game.com/servers. Accessed 2026-10-08.
- [3] **Neonsect (fan guide)** — *WARDOGS community servers guide*. https://neonsect.com/wardogs/wardogs-community-servers-guide/. Accessed 2026-10-08.
- [5] **Wardog Servers (independent tracker)** — *WARDOGS RCON and admin tools*. https://wardogservers.com/guides/wardogs-rcon-and-admin-tools. Accessed 2026-10-08.
- [6] **allthings.how (fan guide)** — *WARDOGS how to change server region*. https://allthings.how/wardogs-how-to-change-server-region/. Accessed 2026-10-08.
- [7] **XGamingServer (commercial host, not confirmed approved)** — *WARDOGS server hosting*. https://xgamingserver.com/wardogs-server-hosting. Accessed 2026-10-08.
- [8] **Supercraft.host (commercial host, not confirmed approved)** — *WARDOGS hosting reservation page*. https://supercraft.host/?p=49132. Accessed 2026-10-08.
- [9] **wardogs.tech (unofficial)** — *Wardogs Server Reference*. https://wardogs.tech/rcon-reference. Accessed 2026-10-08.

# Further Reading

- technical-servers-foundation, for requirements, anti-cheat and the admin overview.
- Steam community announcements for app 1867240 (Season 02 and any official host list).

# Related Documents

- technical-servers-foundation
- rcon-and-server-admin
- meta-release-foundation

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after independent re-verification of validate, markdownlint and links (0 dead). | Standing mandate (auto-approve on green QA) |
