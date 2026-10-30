---
id: server-hosting-and-browser
title: "Server Hosting & Server Browser"
version: 1.2.0
status: frozen
confidence: Medium
category: Technical & Servers
topic: "Official vs community servers, approved hosts, regions, browser behaviour, restarts"
market: Global
game_version: "Early Access Season 02, Update 0.2.0 (15 Oct 2026); official posts through 2026-10-15 (snapshot 2026-10-30)"
document_type: depth
created: 2026-10-08
updated: 2026-10-30
review_due: 2026-11-20
sources_verified: 2026-10-30
supersedes: null
related: [technical-servers-foundation, rcon-and-server-admin, meta-release-foundation]
tags: [servers, hosting, server-browser, community-servers, approved-hosts]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | server-hosting-and-browser |
| Version | 1.2.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Technical & Servers |
| Game version | Early Access Season 02, Update 0.2.0 (15 Oct 2026); official posts through 2026-10-15 (snapshot 2026-10-30) |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-30 |
| Review due | 2026-11-20 |

# Executive Summary

This depth document extends the technical-servers-foundation with how WARDOGS servers are obtained and found: the hosts-only model, the approved hosts, the Official and Community split introduced in patch 0.11, regions, browser behaviour, slot counts, restart handling and prices. Version 1.2.0 adds Season 02, Update 0.2.0 (patch notes 14 Oct 2026, released 15 Oct 2026) [7][8]. Version 1.1.0 had been revised against the full official Steam posts (snapshot of 8 Oct 2026), which were unreadable when version 1.0.0 was written from fan relays; its Season 1 / 0.1.2 content is kept as dated history. Update 0.2.0 added region-based ping limits with automatic kicks on Official servers, admin-configurable limits on community servers, ping tags and filters in the browser, server seeding rewards and a penalty for community hosts exploiting the faction bonus [7].

Headline findings: the studio's own 8 September 2026 post names three Approved Hosting Partners, QONZER, BisectHosting and xREALM, and says Community Hosted Servers could be pre-ordered through them ahead of the 10 September launch [1]. That settles the two-versus-three conflict: the two-host figure was a fan-site statement dated 1 September [12]. The patch 0.11 browser changes and the 0.1.2 Deploy flow, restored Official filters and daily restart time are now confirmed from the official posts [2][3]. What remains unofficial is the self-hosting and server-code position, prices, slot tiers, regions and any default restart interval. The 12-hour versus 24-hour restart conflict is still unresolved: the official post states only that admins can set a daily restart time in UTC [3].

Confidence is Medium. The hosting model, host names, browser split and restart mechanism rest on official posts; prices, slot sizes, regions and the server-code claim rest on fan sites and commercial pages and are labelled player-reported throughout.

# Key Takeaways

- Official (8 Sep 2026): there are three Approved Hosting Partners, QONZER, BisectHosting and xREALM, and Community Hosted Servers could be pre-ordered through them ahead of Early Access on 10 Sep [1].
- Official: community-hosted servers are where "admins can instantly ban bad actors"; the studio's advice on official servers is to use the in-game report function [1].
- Official (Update 0.2.0, notes 14 Oct 2026): Official servers enforce region-based maximum ping limits; players who consistently exceed the limit over a sustained period are kicked and cannot rejoin that server until the next map transition; community admins can set their own limits; the browser has maximum-ping tags and filters. The notes call the initial values "quite lenient" and give none [7].
- Official (0.2.0): players who join and populate empty servers earn rewards and a vendor discount once the match begins; community hosts "seen to exploit the faction bonus will be punished" (penalty not stated) [7].
- Press only: PCGamesN (27 Oct 2026) reports two new server hosts, GG Host and 1of1 Servers; no official post in the 2026-10-30 snapshot confirms it, so the approved list stays at three officially [11].
- Self-hosting is reportedly not offered: the developer is said not to release server code (fan-site relay; player-reported). No official post read states this [12][13].
- Official (patch 0.11, 14 Sep 2026): the browser split into Community and Official; Official lost its filters because there are no Official modified game modes; Community gained text search and filter reliability fixes; Show Empty/Full was added to the quick bar [2].
- Official: Community Server IDs persist across matches and restarts, are unique, and are longer for security [2].
- Official (0.1.2, 30 Sep 2026): admins can set a daily restart time in UTC; advanced filters returned to the Official list; the Deploy flow offers Official, Community, Infantry Mode and Low-Level [3]. No official post gives a built-in 12 h or 24 h interval.
- Listed monthly prices on provider pages (checked 13 Sep 2026): QONZER GBP 49.95 to 69.95, BisectHosting from USD 71.99, xREALM from EUR 59.99; smallest size sold is 60 slots. Player-reported compilation; no official price [13].
- No official region list exists; fan and tracker sources disagree on labels [14][15]. The only official regional statement is increased capacity in Asia [2].

# Scope

Covers the hosting model, approved hosts, Official versus Community servers, regions, browser behaviour, slots, restart cycles, how a prospective admin gets a server, and documented costs, at Season 02 / Update 0.2.0 (15 Oct 2026), with Season 1 / 0.1.2 and hotfixes to 2 Oct 2026 as history. Excludes RCON and config detail (see rcon-and-server-admin and the foundation), system requirements, and release and pricing history of the game itself (meta-release-foundation). Official, provider and fan reporting are labelled throughout. No Bulkhead server manual exists in the sources read; the official layer here is the Steam news posts only.

# Definitions

- **Community server:** a server rented from an approved host and listed in the Community browser [1][2].
- **Official server:** a Bulkhead-run server in the Official browser; no Official modified game modes at 12 Sep 2026 [2].
- **Approved Hosting Partner:** the studio's own term for the three named hosts, QONZER, BisectHosting and xREALM [1]. Reportedly the only parties with access to server code (player-reported) [12][13].
- **Deploy screen:** the in-game flow that leads to the server lists; reworked in 0.1.2 [3].

# Current State

Statements at Season 02 / Update 0.2.0 unless dated otherwise (official posts through 2026-10-15; none seen in the 2026-10-30 snapshot after that). Items from earlier checks keep their dates.

- **Ping limits (0.2.0).** Official servers enforce region-dependent maximum pings; sustained excess causes an automatic kick (short spikes and server-side lag spikes are excluded) and a rejoin block on that server until the next map transition [7]. Community admins configure their own limits, allowing cross-regional play or stricter rules [7]. The browser shows maximum-ping tags and filters [7]. Values are not published.
- **Seeding (0.2.0).** Rewards and a vendor discount for players who populate empty servers, paid once the match begins; amounts not stated [7]. See control-zone-and-match-flow.
- **Release.** Maintenance 08:00 to 09:30 UTC on 15 Oct 2026 (about 90 minutes estimated), then Update 0.2.0 released and servers back online [7][8].

- **Approved hosts.** Three Approved Hosting Partners: QONZER, BisectHosting and xREALM (official, 8 Sep 2026) [1]. A tracker (updated 14 Sep 2026) also says three exist and agrees [14].
- **Hosting model.** Community servers are bought through those partners [1]. That self-hosting is unavailable and that the developer withholds server code is player-reported only (fan site, evidence dated 1 Sep 2026) [12]; a second guide says no other host has access to the server code [13].
- **Browser.** Community and Official lists since 14 Sep 2026 [2]. The 0.1.2 Deploy flow offers Official, Community, Infantry Mode and Low-Level, and advanced filters are back on the Official list [3].
- **Restart.** Admins can set a daily restart time in UTC (official, 0.1.2) [3]; BisectHosting repeats this [9].
- **Regions.** The region selector exists and shows how many regions are selected [3]. No official region list was found; a tracker lists seven regions it tracks (see Detail) [14].

# Detail

## Resolving the host count (2 versus 3)

| Date of evidence | Claim | Source | Class |
|------------------|-------|--------|-------|
| 1 Sep 2026 | Two hosts passed launch standards, names unpublished, more in the pipeline | [12] | Fan site |
| 7 Sep 2026 | Studio names QONZER and BisectHosting (relayed) | [13] | Fan guide, unconfirmed |
| 8 Sep 2026 | Three Approved Hosting Partners named: QONZER, BisectHosting, xREALM | [1] | Official |
| 14 Sep 2026 | "Only the three approved hosts run WARDOGS servers" | [14] | Tracker |

Assessment: confirmed. The conflict was stale evidence, not disagreement, and the official post names the same three the fan guide listed. Confidence High on the three names, resting on [1]. The fan guide's claim that the first two were named on 7 Sep and xREALM added on 8 Sep is not supported by the official post, which names all three together; no 7 Sep post is in the snapshot, so the stepwise dating stays unconfirmed [13]. Other sellers (XGamingServer, Survival Servers, LOW.MS, Supercraft) advertise WARDOGS hosting but are not on the official list; XGamingServer itself says it is "onboarding" through partners and does not claim approval [16][17]. Treat such pages as pre-approval marketing.

## Official versus Community (patch 0.11, 14 Sep 2026) [2]

| Aspect | Official | Community |
|--------|----------|-----------|
| Operator | Bulkhead | Approved host customer |
| Filters | Removed in 0.11 (no Official modified modes); advanced filters added back in 0.1.2 [3] | Reliability improved, text search added |
| Quick bar | Show Empty/Full added to the browser quick bar (post does not split by list) | Same |
| Server ID | Not stated | Persistent, longer, unique, joinable by ID |
| Naming | Names sorted alphabetically regardless of special characters and numbers; no repeated spaces | Same |

The post frames the change as favouring community servers: it admits Community Servers "have been underserved" and that the studio rushed its Community Server strategy [2]. The studio notes that matchmaking would suit a game of this size but that it does not want community admins and hosts to suffer, hence the two browsers [2]. The Host button was updated to direct to the correct location [2]. PlayDay's press summary matches the official text [10].

Planned and not shipped per the 0.11 post: community server favouriting, tiered priority queues for Community servers, Message of the Day prompt, improved warmup activities, disabling AFK kicking during seeding, and team switching controls [2]. A one-week 5 percent End of Match cash bonus on Community servers ran from 14 Sep and has ended [2].

## Browser behaviour

- Official: 0.1.2 shows your place in the queue after clicking Join, no longer truncates long server names (hover shows the full name), and adds gamepad support on the Deploy screen [3].
- Region is picked via Deploy, Server Browser, Region, tick regions, Confirm (player-reported guide) [15]. The official 0.1.2 note says only that region select now shows how many regions are selected [3].
- Ticking several regions has been reported to return an empty list; guides advise selecting one and clearing persisted search text (player-reported) [13][15]. A fan site calls the one-region rule a temporary August Beta workaround, not a confirmed Early Access rule [12].
- Official: Asian capacity was increased in 0.11; no slot or per-region figures were published [2].

## Regions

| Source | Regions named | Class |
|--------|---------------|-------|
| Official 12 Sep post | "The Asian region" capacity increase only; no list | Primary [2] |
| Tracker, 14 Sep 2026 | Europe, North America East, North America Central, North America West, Oceania, Asia, South America | Player-reported [14] |
| Guide screenshot caption | Europe, North America, South America, Asia, with ping values | Player-reported [15] |
| Hosting vendor | Datacentres in East/West USA, Europe (Germany), Oceania, Singapore | Commercial [16] |

No official region list was found; labels disagree. Oceania as a browser region is unconfirmed [12][15]. The time-zone table in the 12 Sep post is a maintenance schedule, not a region list [2].

## Slots and capacity

No official post read states slot counts for community servers. Matches are 100 players across three teams per the foundation. Hosts sell by different units: xREALM 60, 80 or 100 player packages; QONZER sells by CPU threads (8, 10 or 12) and says it does not limit slots; the smallest size sold anywhere is 60 slots (player-reported compilation, 13 Sep 2026) [13]. The unofficial config reference lists `MaxPlayers` default 128, "clamped by a developer-set min/max" [18].

## Costs (provider pages as compiled 13 Sep 2026; verify before buying; no official price) [13]

| Host | Price shown | Notes |
|------|-------------|-------|
| QONZER | GBP 49.95, 59.95, 69.95 per month | 5% quarterly, 10% semi-annual, 15% annual prepay discounts |
| BisectHosting | from USD 71.99 per month | per-tier prices not visible |
| xREALM | from EUR 59.99 per month | 60/80/100 slots |

Roundups conflict with these figures [13]. Pre-approval pages quote far lower numbers (for example XGamingServer USD 24.50 to 42.00 and a Supercraft reservation page USD 17.99 to 39.99), marked "coming soon" or reservation-only [16][17]; they are not approved-host prices.

## Restart cycles (12 h versus 24 h)

- Official: "Scheduled restarts: you can now set a daily restart time (UTC)" for community server admins, in 0.1.2 [3]. This is a once-per-day schedule, which fits "24 h", but the post states no default or minimum interval.
- Not documented: the unofficial config reference lists no scheduled-restart key, only on-demand `POST /v1/match/restart`; some session keys apply only at next restart [18].
- The 12 h figure was not found in any official post or any source I could open. The foundation's statement that host guides disagree remains unverified. Persistent IDs mean a restart no longer changes a server's identity [2].
- Whole-service maintenance is a separate matter: official one-hour windows at 08:00 UTC on 14 Sep, 30 Sep and 2 Oct [2][3][4].

## How a prospective admin gets a server

1. Choose one of the three Approved Hosting Partners (QONZER, BisectHosting, xREALM) [1]. 2. The in-game Host button links to the hosting page [2][6]. 3. Check slots, region, billing term and refund terms on the host's own page (player-reported advice) [12]. 4. RCON was described in August as in development, with day-one controls limited to maps and modes [12]; RCON additions including AllowedHosts arrived in 0.1.2 [3] (see rcon-and-server-admin).

# Early Access Changes & Known Issues

- 5 Sep 2026: the closed beta became an open beta until Sunday 08:00 UTC; the post makes no hosting statement [5].
- 8 Sep 2026: Approved Hosting Partners named; Community Hosted Servers open for pre-order ahead of 10 Sep [1].
- 9 Sep 2026: Season 1 changelog (pre-load) reworked server browser filtering, fixed community server images scaling, and linked the Host a server button to the hosting page [6].
- 14 Sep 2026 (0.11): Community/Official split, persistent IDs, Asian capacity up, about one hour downtime from 08:00 UTC [2].
- 30 Sep 2026 (0.1.2): Deploy flow, Official filters restored, daily restart time, region count display, RCON AllowedHosts [3].
- 2 Oct 2026: security and stability hotfix at 08:00 UTC, expected downtime one hour; no hosting or browser change stated [4].
- 15 Oct 2026 (0.2.0): region-based ping limits and high-ping kicks on Official servers, admin-configurable limits on community servers, ping tags and filters in the browser, seeding rewards, faction-bonus exploitation penalty for community hosts, "Server stability & security improvements" (no detail); maintenance 08:00 to 09:30 UTC [7][8]. Season 1 (0.1.2) stated no ping limits in the posts read.
- 27 Oct 2026: PCGamesN reports two additional hosts (press only, unconfirmed) [11].
- Known: multi-region selection can show an empty list (player-reported) [13]. Favourites and priority queues are unshipped [2].

# Admin & Technical Notes

Update 0.2.0 adds per-server ping limits that community admins "will be able to configure" [7]; the setting name, ini key, units and RCON exposure are not stated and stay unconfirmed. Official admin-facing changes in 0.1.2 are the daily restart time (UTC), RCON AllowedHosts, capped RCON message and broadcast lengths, Standard RCON response detail by default and ServerImageURL checks on config load [3]. Provider material (labelled): BisectHosting's blog, from an Approved Hosting Partner with a commercial interest, repeats the restart wording [9]; host-specific panels differ and RCON access depends on the host. Hosts are the only route to server files (player-reported); do not buy from unlisted sellers. Persistence of bans and rotation across restarts and reinstalls is a question to put to the host [14].

# Risks & Caveats

- Prices and slot sizes are third-party compilations from 13 to 14 Sep and will have moved; Season 02 (15 Oct 2026) did not change the approved-host list in any official post read, but the model may still move.
- The server-code and self-hosting position is fan-relayed; no official post read states it.
- Provider pages are marketing and some predate the approval announcement.
- The studio's X posts were not read; the snapshot covers Steam news only, and posts outside the snapshot index are not cited.
- WebFetch summaries of dynamic pages may omit content.

# Open Questions

- Are GG Host and 1of1 Servers (PCGamesN, 27 Oct) approved partners? Only an official post would settle it.
- What are the per-region ping limits and the admin setting for them, and what is the faction-bonus exploitation penalty?
- Any approved partner added after 8 Sep 2026, and whether the 7 Sep stepwise naming relayed by a fan guide happened.
- Is there any default restart interval (12 h or 24 h), and who stated it? The official post gives only a settable daily time.
- Official region list and whether Oceania and South America are separate in the picker.
- Real current prices; official slot counts; whether Official servers have fixed slot counts.
- Official statement on self-hosting and server code.
- Favourites, priority queues and MOTD: the 0.2.0 notes do not mention them (not a statement that they are absent).

# References

**Primary Sources**

- [1] **BULKHEAD** — *The 11th Reason NOT To Buy WARDOGS* (Steam post, 8 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1842846814456311. Accessed 2026-10-08.
- [2] **BULKHEAD** — *SCHEDULED MAINTENANCE & PATCH 0.11* (Steam post, 12 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1843481262698449. Accessed 2026-10-08.
- [3] **BULKHEAD** — *WARDOGS | Update 0.1.2 (Minor Patch)* (Steam post, 30 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1845383656376490. Accessed 2026-10-08.
- [4] **BULKHEAD** — *WARDOGS | Security & Stability Hotfix* (Steam post, 2 Oct 2026). https://store.steampowered.com/news/app/1867240/view/1845383656384445. Accessed 2026-10-08.
- [5] **BULKHEAD** — *THE CLOSED BETA IS NOW AN OPEN BETA!* (Steam post, 5 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1842846814449809. Accessed 2026-10-08.
- [6] **BULKHEAD** — *Pre-Load Live & Season 1 Changelog* (Steam post, 9 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1843481262690549. Accessed 2026-10-08.
- [7] **Bulkhead** — *WARDOGS Season 2 Patch Notes* (Steam post, 14 Oct 2026 14:59 UTC; Update 0.2.0 notes and maintenance-window notice). https://store.steampowered.com/news/app/1867240/view/1846651706674560. Accessed 2026-10-30.
- [8] **Bulkhead** — *WARDOGS Season 02 is now LIVE* (Steam post, 15 Oct 2026 09:59 UTC; Update 0.2.0 released, servers back online). https://store.steampowered.com/news/app/1867240/view/1846651706677015. Accessed 2026-10-30.

**Press & Secondary**

- [9] **BisectHosting (hosting provider, secondary; Approved Hosting Partner)** — *WARDOGS Update 0.1.2 patch notes*. https://www.bisecthosting.com/blog/wardogs-update-0-1-2-patch-notes-bug-fixes-improvements-flythrough-exploit-fob-pallet-delivery-xp. Accessed 2026-10-08.
- [10] **PlayDay** — *WARDOGS patch 0.11 focuses on server browsers (full notes)*. https://playday.one/2026/09/14/wardogs-patch-11-focuses-on-server-browsers-full-notes/. Accessed 2026-10-08.
- [11] **PCGamesN** — *Wardogs adds two new server hosts, but community servers are still a work in progress* (27 Oct 2026; press report, not an official post; the Steam news-feed item redirects to this page). https://www.pcgamesn.com/wardogs/community-servers. Accessed 2026-10-30.

**Player-Reported Evidence**

- [12] **WARDOGS-game.com (unofficial fan site)** — *WARDOGS Servers, Regions & Hosting*. https://wardogs-game.com/servers. Accessed 2026-10-08.
- [13] **Neonsect (fan guide)** — *WARDOGS community servers guide*. https://neonsect.com/wardogs/wardogs-community-servers-guide/. Accessed 2026-10-08.
- [14] **Wardog Servers (independent tracker)** — *WARDOGS RCON and admin tools*. https://wardogservers.com/guides/wardogs-rcon-and-admin-tools. Accessed 2026-10-08.
- [15] **allthings.how (fan guide)** — *WARDOGS how to change server region*. https://allthings.how/wardogs-how-to-change-server-region/. Accessed 2026-10-08.
- [16] **XGamingServer (commercial host, not confirmed approved)** — *WARDOGS server hosting*. https://xgamingserver.com/wardogs-server-hosting. Accessed 2026-10-08.
- [17] **Supercraft.host (commercial host, not confirmed approved)** — *WARDOGS hosting reservation page*. https://supercraft.host/?p=49132. Accessed 2026-10-08.
- [18] **wardogs.tech (unofficial)** — *Wardogs Server Reference*. https://wardogs.tech/rcon-reference. Accessed 2026-10-08.

# Further Reading

- technical-servers-foundation, for requirements, anti-cheat and the admin overview.
- community-and-source-reliability, for the register of official channels and the Approved Hosting Partners entry.
- patch-history, for the full patch timeline.
- Steam community announcements for app 1867240 (Season 02 and any official host or region list).

# Related Documents

- technical-servers-foundation
- rcon-and-server-admin
- meta-release-foundation

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after independent re-verification of validate, markdownlint and links (0 dead). | Standing mandate (auto-approve on green QA) |
| 1.1.0 | 2026-10-08 | Research Pipeline (revision worker) | Revised against full official Steam text; host list, browser split, 0.1.2 Deploy flow, restored Official filters and daily restart time relabelled Primary; six official posts added as references; 7 Sep stepwise host dating marked unconfirmed; confidence Low to Medium; 12 h vs 24 h, prices, slots and regions left unofficial. | Standing mandate (auto-approve on green QA) |
| 1.2.0 | 2026-10-30 | Research Pipeline (virtual agent) | Revised for Update 0.2.0 (14-15 Oct 2026): region-based ping limits and kicks, admin-configurable limits, browser ping tags and filters, seeding rewards, faction-bonus exploitation penalty, server stability and security improvements, 08:00-09:30 UTC 15 Oct maintenance; PCGamesN two-new-hosts report added as unconfirmed press; Season 02 forward-looking text replaced | — |
