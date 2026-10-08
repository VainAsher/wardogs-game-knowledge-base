---
id: technical-servers-foundation
title: "Technical & Servers: Foundation"
version: 1.1.0
status: frozen
confidence: Medium
category: Technical & Servers
topic: "System requirements, settings, netcode, dedicated and community servers, modding"
market: Global
game_version: "Season 1, patch 0.1.2 plus hotfixes to 2 Oct 2026"
document_type: foundation
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-10-22
sources_verified: 2026-10-08
supersedes: null
related: [gameplay-modes-foundation, maps-environment-foundation, meta-release-foundation, server-hosting-and-browser, rcon-and-server-admin, system-requirements-and-performance, patch-history, community-and-source-reliability]
tags: [technical, servers, community-servers, rcon, system-requirements, anti-cheat]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | technical-servers-foundation |
| Version | 1.1.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Technical & Servers |
| Game version | Season 1, patch 0.1.2 plus hotfixes to 2 Oct 2026 |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-10-22 |

# Executive Summary

This document covers what a player or server admin needs technically for WARDOGS (Bulkhead / Team17, Steam app 1867240) in Early Access: official system requirements, anti-cheat, platform support, the Community and Official server browsers, how community servers are hosted, the admin and RCON tooling, and modding status. Version 1.1.0 is revised against the full text of the official Steam posts and the store data snapshot of 2026-10-08, up to Season 1, patch 0.1.2 (30 September 2026) and the hotfixes of 2 October 2026 [1][7][8][9].

Headline facts. The store data lists Windows only, with Windows 10 64-bit minimum and a 1080p Low 60 fps (upscaled) target [1]. Patch 0.11 (deployed 14 September 2026) split the browser into Community and Official lists [6]. Bulkhead itself names three Approved Hosting Partners (QONZER, BisectHosting, xREALM) in its 8 September post, which resolves the earlier two-versus-three count conflict by dating [3]. Update 0.1.2 added a Deploy flow, restored Advanced Filters to the Official list and added scheduled restarts and RCON hardening for community servers [7]. The detailed RCON and ServerSettings.ini reference remains unofficial only, and predates 0.1.2 [14].

Confidence is Medium. System requirements, patch contents and the approved-host list are now Primary. The kernel-level anti-cheat wording is not present in the store API snapshot and so is no longer rated Primary, and RCON and config detail, self-hosting status and netcode rest on unofficial material or are undocumented.

# Key Takeaways

- Minimum: Windows 10 64-bit, Core i5-8600 or Ryzen 5 3500, 16 GB RAM, GTX 1660 or RX 590, 50 GB storage, broadband, targeting 1080p Low at 60 fps (upscaled); recommended is Windows 11, an i7-12700K or Ryzen 7 5700X with an RTX 3070 or RX 6700 XT (store data, 2026-10-08) [1].
- Platform flags in the store data are Windows true, Mac false, Linux false [1]. Linux is not officially supported: the developers said on 5 Sep 2026 they cannot commit to it and are still working on Proton compatibility (press report) [11].
- Anti-cheat: Bulkhead's 8 Sep post deliberately says nothing about the technology ("you don't talk about anti-cheat") and points players to the in-game report function and community-hosted servers [3]. The "Kernel Level Anti-Cheat" line seen on the live store page in earlier reading is not in the 2026-10-08 store API snapshot; treat it as unconfirmed here [1].
- Three Approved Hosting Partners (QONZER, BisectHosting, xREALM), named officially on 8 Sep 2026, sell community servers [3].
- Patch 0.11 (announced 12 Sep, deployed 14 Sep 2026) split the browser into Community and Official, removed filters from Official, added text search for Community and made community server IDs persistent [6].
- Update 0.1.2 (30 Sep 2026, maintenance 08:00 UTC for about one hour) added the Deploy flow (Official, Community, Infantry Mode, Low-Level), restored Advanced Filters to the Official list, and added scheduled daily restarts and an RCON AllowedHosts setting [7].
- A security and stability hotfix on 2 Oct 2026 (08:00 UTC, about one hour) had undisclosed specifics; a separate no-downtime balance hotfix followed the same day [8][9].
- No official RCON or ServerSettings.ini documentation was found; the detailed reference is unofficial and Low confidence [14]. No mod support is mentioned in the store data, and no modding plan was found in the official posts read [1].

# Scope

Covered: system requirements, graphics and stability changes, anti-cheat, platform status, server browser, community server hosting and administration, RCON, and modding, at game version Season 1 / patch 0.1.2 with hotfixes to 2 Oct 2026. Excluded: game modes (see gameplay-modes-foundation), maps (maps-environment-foundation), and release and pricing history (meta-release-foundation). Depth is in server-hosting-and-browser, rcon-and-server-admin and system-requirements-and-performance; patch chronology is in patch-history and source trust in community-and-source-reliability. Season 2 (officially announced for 15 Oct 2026) is outside the verified version [10]. Official posts are read from the Steam news feed [2].

# Definitions

- **Community server:** a host-rented server listed in the Community browser [6].
- **Official server:** a Bulkhead-run server listed in the Official browser; Bulkhead states it has no officially modified game modes [6].
- **Approved Hosting Partner:** one of the three hosting companies Bulkhead names as selling community servers: QONZER, BisectHosting and xREALM [3].
- **Infantry Mode / Low-Level servers:** community-server modifiers that the 0.1.2 Deploy flow signposts [7].
- **RCON:** the remote administration interface of a server. Official posts confirm it exists and has an AllowedHosts setting [7]; the protocol detail (HTTP API, port 7776) is unofficial [14].

# Current State

All statements below are at Season 1 / patch 0.1.2 plus hotfixes, checked 2026-10-08.

- **Platform and requirements.** Windows only per the store platform flags; full specification is in Detail [1]. Early Access began on 10 Sep 2026 [1]. The expected Early Access duration previously stated in this document is not in the store API snapshot and is not asserted here.
- **Languages and features.** Fourteen languages (English, French, Italian, German, Spanish - Spain, Japanese, Korean, Portuguese - Brazil, Russian, Simplified and Traditional Chinese, Polish, Turkish, Ukrainian; an asterisk marks the languages with full audio support) and Steam categories Multi-player, PvP, Online PvP and Steam Achievements [1].
- **Anti-cheat.** Bulkhead's 8 Sep post says the most important thing players can do is use the in-game report function on official servers, and that community-hosted servers give "the ultimate protection" because admins can instantly ban bad actors [3]. The 9 Sep changelog added a report tracking system with weighted reports [4]. The product name and kernel-level nature are not stated in any official text read; see Open Questions.
- **Linux.** Not supported. Store flags show Linux false [1]. Press reported the developers' 5 Sep clarification [11].
- **Server browser.** Two lists, Community and Official, since 0.11 [6]. 0.1.2 added Advanced Filters back to the Official list and a Deploy flow offering Official, Community, Infantry Mode or Low-Level servers [7]. Detail in server-hosting-and-browser.
- **Community server availability.** Bulkhead's 8 Sep post says community hosted servers were available to pre-order through "our 3 Approved Hosting Partners; QONZER, BisectHosting and xREALM" ahead of the 10 Sep launch [3]. The hosts-only model itself (no self-hosting, server code withheld) is still known only from a fan site and a tracker, not from an official statement read [13][15].
- **Modding.** The store data mentions neither dedicated servers nor mod support [1].

# Detail

## System requirements (store data, 2026-10-08)

| Item | Minimum | Recommended |
|------|---------|-------------|
| OS | Windows 10 (64-bit) | Windows 11 (64-bit) |
| CPU | Intel Core i5-8600 or AMD Ryzen 5 3500 | Intel Core i7-12700K or AMD Ryzen 7 5700X |
| RAM | 16 GB | 16 GB |
| GPU | Nvidia GTX 1660 or Radeon RX 590 | Nvidia RTX 3070 or Radeon RX 6700 XT |
| Network | Broadband Internet connection | Broadband Internet connection |
| Storage | 50 GB | 50 GB |
| Target | 1080p Low, 60 fps (upscaled) | 1440p Medium 70+ fps native, or 4K Medium 60+ fps upscaled |

Source for the table: [1]. Both columns state a 64-bit processor and operating system requirement. The Linux requirement fields are empty [1]. See system-requirements-and-performance for depth.

## Performance and settings changes at launch (Season 1 changelog, 9 Sep 2026) [4]

- DLSS Frame Generation can be turned off without a restart; the render target pool is configurable.
- Shadow cache refreshes were reduced (less hitching when taking control of a character); shadow quality is clamped to Low on high benchmark scores rather than switched off.
- Dropped items no longer affect navigation.
- Startup reliability improved with clearer early-failure messages and a recovery route; a legacy graphics dependency was removed.
- Crash fixes covered two frame generation paths, network calls scheduled off the game thread, a chatbox tooltip, buildables, and firing a weapon whose owner had left. GPU crash reports carry more detail.
- Voice chat recovery after a failed join and under load was improved, with a visible communication status.
- Launch day: a client hotfix on 10 Sep forced a restart and staged re-entry through the login queue to address players unable to join, unexpected kicks and long queues [5].
- Netcode: none of the official text read describes tick rate, prediction or lag compensation. This is a gap, not a finding.

## Moderation and anti-cheat systems

- Report tracking: reports are weighted so repeat and bad-faith reporters carry less influence; cheater bans are announced in server when match termination is off; the "kicked from server" message appears only for real bans [4].
- Economy abuse (patch 0.11 post): cash exploits get a timed ban plus a reset of cash and XP to 0; content that tutorialises exploits is treated as advertising cheats and risks a permanent ban; the developer states "We track every server you enter" and joining known XP farming servers for more than a few minutes risks a permanent ban [6].
- 0.1.2 (30 Sep): leniency for first-time offenders is declared over; players caught abusing repeatable exploits or Real Money Trading risk permanent bans without warning [7].

## Server browser timeline

| Date | Change |
|------|--------|
| 10 Sep 2026 (Season 1 changelog, 9 Sep) | Filtering reworked; Host a server button links to the hosting page; community image scaling fixed [4] |
| 14 Sep 2026 (0.11) | Community and Official browsers; filters removed from Official; text search and Show Empty/Full on the quick bar for Community; persistent, longer unique server IDs; server names ordered alphabetically with single spaces only; Asian capacity increased; 5% End of Match cash bonus on Community servers for one week [6] |
| 30 Sep 2026 (0.1.2) | Deploy flow (Official, Community, Infantry Mode, Low-Level); Advanced Filters restored to Official; long names no longer truncated; queue position shown after Join; gamepad support on the Deploy screen [7] |

Planned but not shipped per the 0.11 post and not announced as shipped in 0.1.2: community server favouriting, tiered priority queues, Message of the Day prompt, improved warmup activities, disabling AFK kicking during seeding, team switching controls [6][7].

# Early Access Changes & Known Issues

- **8 Sep 2026:** Bulkhead names QONZER, BisectHosting and xREALM as its three Approved Hosting Partners [3].
- **14 Sep 2026, patch 0.11:** server browser overhaul, cash exploit fixes, more GPU crash fixes, Asia capacity; servers down about one hour from 08:00 UTC [6].
- **30 Sep 2026, update 0.1.2:** fixed the WD-L020 crash tied by Bulkhead to Windows 11 update KB5124010; server-authoritative revive checks and other cash and XP exploit fixes; Deploy flow; scheduled restarts and RCON hardening; "various server stability hotfixes" and increased server security. Maintenance began 08:00 UTC for about one hour [7].
- **2 Oct 2026, security and stability hotfix:** announced as fixing "minor security and stability issues affecting some players", 08:00 UTC, one hour expected downtime; specifics undisclosed [8].
- **2 Oct 2026, balance hotfix:** IR Rangefinders disabled in the vendor until Season 02 and CIWS now destroys the Havoc in about 6 seconds instead of 12; no client download or server downtime needed [9].
- **Known gaps:** Linux unsupported [1][11]; the planned community server features above remain unannounced as shipped.
- **Next:** Season 02 is officially announced for 15 Oct 2026 [10]. A first progression wipe is press-reported only [12]; see season-2-announcements. This is outside the verified version.

# Admin & Technical Notes

Source warning: Bulkhead has published no server-admin manual that was found. Only the 0.1.2 admin changes below are official; the RCON and config reference is unofficial, predates 0.1.2 and is labelled Low confidence.

**Hosting model.**

- Official: community hosted servers are sold through three Approved Hosting Partners, QONZER, BisectHosting and xREALM, per the 8 Sep 2026 post [3]. The in-game Host button links to the hosting page [4][6].
- The 2-versus-3 conflict is resolved by dating: a fan site relaying evidence checked on 1 Sep 2026 said two unnamed hosts had passed launch standards [13]; a tracker updated 14 Sep 2026 says three [15]; the official post of 8 Sep confirms three and names them [3].
- Player-reported only: the fan site says server code will not be released for everyone to host (citing performance and security) and the tracker says RCON access depends on the host's panel [13][15]. No official statement of a hosts-only model, or of the absence of a downloadable dedicated server, was read in the snapshot. Consequence for admins: you probably cannot run your own SteamCMD or Docker server; confirm with your host. Detail in server-hosting-and-browser.

**Admin changes confirmed in 0.1.2 (30 Sep 2026, official)** [7]:

- Scheduled restarts: a daily restart time can be set (UTC).
- RCON AllowedHosts setting to restrict who can access RCON.
- RCON message and broadcast lengths are capped.
- RCON now defaults to Standard response detail instead of Full, and config responses no longer expose server internals.
- ServerImageURL is checked when the config loads.
- Since 0.11, community server IDs persist across map changes and restarts and are longer for security reasons [6].

**Unofficial RCON and config reference** (wardogs.tech, self-described as not official docs, version 0.39, written before 0.1.2; player-reported, Low confidence) [14]:

- RCON is plain HTTP REST with JSON, base `http://<host>:<port>/v1/`, default port 7776 (`-RCONPort=`), no TLS, so the password crosses the network in clear text.
- Authentication is `Authorization: Bearer <rcon-password>`; one token has full read and write access with no read-only role. The listener is off by default (`bEnabled` in `[/Script/WDRCON.WDRCONSettings]`).
- Endpoint groups: status, players, bans, config, rotation, capabilities; writes include kick, kill, message, ban, broadcast and match map/end/restart. `PUT /v1/config` replaces the whole document and supports `If-Match` revision checks.
- Listed `ServerSettings.ini` keys include `ServerName`, `ServerPassword`, `ServerImageURL` (1024x256), cash and level min/max limits, `MaxReservedSlots` (default 20), `MaxPlayers` (listed default 128), `MinimumRequiredPlayers` (default 60), KOTH `ScorePeriod` (default 24 s) and map rotation (`Ordered` or `Random`).
- Several endpoints were reported removed in build ++Wardogs+Live-CL-501228 (2026-09-14) in favour of the config document [14]. Because the reference predates 0.1.2, response detail defaults and config output may now differ (the official 0.1.2 notes say Standard detail is now the default and config no longer exposes internals) [7].
- Assessment: because RCON as documented uses one shared secret over unencrypted HTTP, the official AllowedHosts setting [7] should be used and RCON kept on a private network or behind a TLS proxy. Confidence Low to Medium: the AllowedHosts fact is official, the transport detail is unofficial [14].

**Third-party tools** (player-reported, not endorsed): Warcon, an open-source (MIT) self-hostable multi-server RCON panel with per-admin roles and audit log [16]; BattleMetrics has reportedly added WARDOGS RCON support [15]. The guide at [15] was written by Warcon's builders, so its recommendations are promotional. See rcon-and-server-admin.

**Restart timers.** Host guides disagreed on any built-in restart timer (12 h versus 24 h of uptime); this is unverified. The only official restart statement is the configurable daily UTC restart time in 0.1.2 [7].

**Modding.** The store data lists no mod support [1]. No official modding toolkit or plan was found in the official posts read.

**Client notes.** Windows only [1]; Linux unsupported [11]; Windows 11 update KB5124010 caused crash WD-L020, fixed 30 Sep 2026 [7].

# Risks & Caveats

- Admin and RCON material is unofficial, predates 0.1.2 and may change per build; the endpoint removals on 14 Sep show churn [14].
- The hosts-only and no-self-hosting claims are not confirmed by an official text read; only the three-host list is [3].
- The kernel-level anti-cheat wording was observed on the live store page in the earlier reading but is absent from the 2026-10-08 store API snapshot, which carries only structured fields; a reader should recheck the live page [1].
- The 2 Oct security hotfix content is undisclosed [8].
- Commercial host and fan-site claims may predate current server tooling; see community-and-source-reliability.
- Season 02 (15 Oct 2026) will likely change versions and admin tooling [10].

# Open Questions

- Which anti-cheat product is used, and is it kernel level? No official text read names it; a developer statement or a recheck of the live store page would resolve it.
- Is there an official statement that self-hosting or a downloadable server is unavailable? Only unofficial relays were found.
- Is there an official RCON or ServerSettings.ini document, and how did 0.1.2 change the unofficial reference?
- Netcode characteristics (tick rate, lag compensation): no source found.
- Will modding or Linux/Proton support ship, and when?
- What was fixed in the 2 Oct security hotfix?
- What is the officially stated Early Access duration? Not in the store API snapshot.

# References

**Primary Sources**

- [1] **Valve / Bulkhead** — *WARDOGS on Steam (store data snapshot 2026-10-08)*. https://store.steampowered.com/app/1867240/WARDOGS/. Accessed 2026-10-08.
- [2] **Valve / Bulkhead** — *WARDOGS Steam News Hub*. https://store.steampowered.com/news/app/1867240. Accessed 2026-10-08.
- [3] **Bulkhead** — *The 11th Reason NOT To Buy WARDOGS* (8 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1842846814456311. Accessed 2026-10-08.
- [4] **Bulkhead** — *Pre-Load Live & Season 1 Changelog* (9 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1843481262690549. Accessed 2026-10-08.
- [5] **Bulkhead** — *Launch Stability Hotfix 1* (10 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1843481262693332. Accessed 2026-10-08.
- [6] **Bulkhead** — *Scheduled Maintenance & Patch 0.11* (12 Sep 2026, deployed 14 Sep). https://store.steampowered.com/news/app/1867240/view/1843481262698449. Accessed 2026-10-08.
- [7] **Bulkhead** — *WARDOGS Update 0.1.2 (Minor Patch)* (30 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1845383656376490. Accessed 2026-10-08.
- [8] **Bulkhead** — *WARDOGS Security & Stability Hotfix* (2 Oct 2026). https://store.steampowered.com/news/app/1867240/view/1845383656384445. Accessed 2026-10-08.
- [9] **Bulkhead** — *IR Goggles & CIWS Balance Hotfix* (2 Oct 2026). https://store.steampowered.com/news/app/1867240/view/1845383656386801. Accessed 2026-10-08.
- [10] **Bulkhead** — *WARDOGS Season 02 Teaser* (22 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1844115010504839. Accessed 2026-10-08.

**Press & Secondary**

- [11] **GamingOnLinux** — *WARDOGS developers clarify Linux support via Proton may come later*. http://www.gamingonlinux.com/2026/09/wardogs-developers-clarify-linux-support-via-proton-may-come-later. Accessed 2026-10-08.
- [12] **Gfinity Esports** — *WARDOGS Season 2: release date, content and what to expect* (progression wipe claim only; press). https://www.gfinityesports.com/article/wardogs-season-2-everything-we-know. Accessed 2026-10-08.

**Player-Reported Evidence**

- [13] **WARDOGS-game.com (unofficial fan site)** — *WARDOGS Servers, Regions & Hosting*. https://wardogs-game.com/servers. Accessed 2026-10-08.
- [14] **wardogs.tech (unofficial)** — *Wardogs Server Reference*. https://wardogs.tech/rcon-reference. Accessed 2026-10-08.
- [15] **Wardog Servers (independent tracker)** — *WARDOGS RCON and admin tools*. https://wardogservers.com/guides/wardogs-rcon-and-admin-tools. Accessed 2026-10-08.
- [16] **Warcon project (GitHub)** — *warcon: self-hostable RCON panel for WARDOGS*. https://github.com/warcon-app/warcon. Accessed 2026-10-08.

# Further Reading

- Steam community announcements for app 1867240 (check for Season 02 notes and any official server documentation).
- server-hosting-and-browser, rcon-and-server-admin, system-requirements-and-performance, patch-history.

# Related Documents

- gameplay-modes-foundation
- maps-environment-foundation
- meta-release-foundation
- server-hosting-and-browser
- rcon-and-server-admin
- system-requirements-and-performance
- patch-history
- community-and-source-reliability

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after independent re-verification of validate, markdownlint and links (0 dead). | Standing mandate (auto-approve on green QA) |
| 1.1.0 | 2026-10-08 | Research Pipeline (revision worker) | Revised against full official Steam text; three Approved Hosting Partners confirmed officially (8 Sep), host-count conflict resolved by dating; patch 0.11, 0.1.2 and 2 Oct hotfixes now cited to official posts; system requirements from store data; anti-cheat wording downgraded to unconfirmed; RCON detail kept unofficial and Low | Standing mandate (auto-approve on green QA) |
