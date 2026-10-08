---
id: technical-servers-foundation
title: "Technical & Servers: Foundation"
version: 1.0.0
status: frozen
confidence: Medium
category: Technical & Servers
topic: "System requirements, settings, netcode, dedicated and community servers, modding"
market: Global
game_version: "Season 1, patch 0.1.2 plus hotfixes to 2 Oct 2026"
document_type: foundation
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [gameplay-modes-foundation, maps-environment-foundation, meta-release-foundation]
tags: [technical, servers, community-servers, rcon, system-requirements, anti-cheat]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | technical-servers-foundation |
| Version | 1.0.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Technical & Servers |
| Game version | Season 1, patch 0.1.2 plus hotfixes to 2 Oct 2026 |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

This document covers what a player or server admin needs technically for WARDOGS (Bulkhead / Team17, Steam app 1867240) in Early Access: official system requirements, anti-cheat, platform support, the Community and Official server browsers, how community servers are hosted, the admin and RCON tooling, and modding status. It is verified against the Steam store page and press summaries of patch notes up to Season 1, patch 0.1.2 (30 September 2026) and the security hotfix of 2 October 2026 [1][6].

Headline facts: the Steam page lists a Windows 10/11 64-bit requirement, kernel-level anti-cheat, and no mention of dedicated servers or mods [1]. Patch 0.11 (14 September 2026) split the browser into Community and Official lists [3]. Community servers are reportedly rented from Bulkhead-approved hosts; the only statements on this are relayed through a fan site and a tracker guide, not read first-hand from Bulkhead [9][11]. No official RCON documentation was found; the detailed admin reference is an unofficial fan document [10].

Confidence is Medium. Steam page facts are primary, but patch contents rest on press summaries because Steam news bodies do not render to fetchers, and the whole hosting and admin layer rests on unofficial or provider material.

# Key Takeaways

- Minimum: Windows 10 64-bit, Core i5-8600 or Ryzen 5 3500, 16 GB RAM, GTX 1660 or RX 590, 50 GB storage, targeting 1080p Low at 60 fps (upscaled); recommended is an i7-12700K or Ryzen 7 5700X with an RTX 3070 or RX 6700 XT (Steam page, checked 2026-10-08) [1].
- The Steam page states "Uses Kernel Level Anti-Cheat"; the developers did not name the product in the sources found [1][8].
- Linux is not officially supported: the developers said on 5 Sep 2026 they cannot commit to it and are still working on Proton compatibility [8].
- Patch 0.11 (14 Sep 2026) split the server browser into Community and Official lists and made community server IDs persistent [3].
- Update 0.1.2 (30 Sep 2026) added scheduled daily restarts, an RCON AllowedHosts setting and capped RCON message lengths for community servers [5][6][7].
- A security and stability hotfix on 2 Oct 2026 caused about one hour of planned downtime with undisclosed fixes [6].
- Self-hosting is reportedly not offered: server code will not be released for everyone to host (fan-site relay of an official thread, checked 1 Sep 2026; player-reported) [9].
- No mod support is mentioned on the Steam page and no modding plan was found [1].

# Scope

Covered: system requirements, graphics and stability changes, anti-cheat, platform status, server browser, community server hosting and administration, RCON, and modding, at game version Season 1 / patch 0.1.2 with hotfixes to 2 Oct 2026. Excluded: game modes (see gameplay-modes-foundation), maps (maps-environment-foundation), and release and pricing history (meta-release-foundation). Season 2 (reported for 15 Oct 2026) is outside the verified version.

# Definitions

- **Community server:** a host-rented server listed in the Community browser [3].
- **Official server:** a Bulkhead-run server listed in the Official browser, with no modified game modes [3].
- **RCON:** the remote administration interface of a server. In WARDOGS it is reported to be an HTTP API on port 7776 by default [10][11].
- **Approved host:** a hosting company reported to have passed Bulkhead's launch standards [9].

# Current State

All statements below are at Season 1 / patch 0.1.2, checked 2026-10-08.

- **Platform and requirements.** Specifications are in the Detail section. Early Access started on 10 Sep 2026 and is expected to last about one to two years [1].
- **Languages and features.** 14 languages, a 100-player three-team match format, proximity voice chat, in-game chat and Steam Achievements [1].
- **Anti-cheat.** The Steam page says "Uses Kernel Level Anti-Cheat" [1]. A press report says the studio had used Easy Anti-Cheat and appeared to be testing something else; the developers did not name a system [8].
- **Linux.** Not officially supported. The developers said on 5 Sep 2026 that earlier Linux functionality in tests was accidental and that they are still working on official Proton compatibility; at launch they invited refunds from buyers who expected Linux support [8].
- **Server browser.** Two lists, Community and Official. The Official list lost its filters in 0.11, and 0.1.2 restored advanced filters to it [3][6].
- **Community server availability.** A fan site summarising an official thread (checked 2026-09-01) says only two hosting companies had passed launch standards and server code would not be released for everyone to host [9]. A server-tracking site (updated 2026-09-14) says three approved hosts exist [11]. The counts conflict (see Open Questions). Both are player-reported.
- **Modding.** The Steam page mentions neither dedicated servers nor mod support [1].

# Detail

## System requirements (Steam page, 2026-10-08)

| Item | Minimum | Recommended |
|------|---------|-------------|
| OS | Windows 10 (64-bit) | Windows 11 (64-bit) |
| CPU | Intel Core i5-8600 or AMD Ryzen 5 3500 | Intel Core i7-12700K or AMD Ryzen 7 5700X |
| RAM | 16 GB | 16 GB |
| GPU | Nvidia GTX 1660 or Radeon RX 590 | Nvidia RTX 3070 or Radeon RX 6700 XT |
| Storage | 50 GB | 50 GB |
| Target | 1080p Low, 60 fps (upscaled) | 1440p Medium 70+ fps native, or 4K Medium 60+ fps upscaled |

Source for the table: [1].

## Performance and settings changes at launch (Season 1 changelog, 10 Sep 2026) [4]

- DLSS Frame Generation can be turned off without a restart; the render target pool is configurable.
- Shadow cache refreshes were reduced (less hitching when taking control of a character); shadow quality is clamped to Low on high benchmark scores instead of being disabled.
- Dropped items no longer affect navigation.
- Startup reliability improved with clearer early-failure messages and a recovery path; a legacy graphics dependency was removed.
- Crash fixes covered two frame generation paths, network calls scheduled off the game thread, a chatbox tooltip, buildables, and firing a weapon whose owner had left. GPU crash reports include more detail.
- Voice chat recovery after a failed join and under load was improved.
- Netcode: none of the sources read describe tick rate, prediction or lag compensation. This is a gap, not a finding.

## Moderation and anti-cheat systems

- A report tracking system weights reports so repeat and bad-faith reporters have less influence; cheater bans are announced in the server when match termination is off; the "kicked from server" message appears only for real bans [4].
- Patch 0.11 states cash exploits get a timed ban plus a reset of cash and XP; exploit tutorials count as advertising cheats and risk permanent bans; the developer states "We track every server you enter" and joining known XP farming servers for more than a few minutes risks a permanent ban [3].

## Server browser timeline

| Date | Change |
|------|--------|
| 10 Sep 2026 | Filtering reworked; Host button links to the hosting page; community image scaling fixed [4] |
| 14 Sep 2026 (0.11) | Community and Official browsers; text search and Show Empty/Full toggle for Community; persistent longer server IDs; Asian capacity increased; 5% End of Match cash bonus on Community servers for one week [3] |
| 30 Sep 2026 (0.1.2) | New Deploy flow pointing to Infantry Mode and Low-Level community servers; advanced filters restored to the Official list [6] |

Planned but not shipped per the 0.11 post: favouriting, tiered priority queues, Message of the Day, improved warmup, no AFK kicks during seeding, team switching controls [3].

# Early Access Changes & Known Issues

- **14 Sep 2026, patch 0.11:** server browser overhaul, cash exploit fixes, more GPU crash fixes; servers down about one hour for maintenance [3].
- **30 Sep 2026, update 0.1.2:** fixed the WD-L020 crash tied to Windows 11 update KB5124010; added server-authoritative revive checks against XP and cash exploits; server stability hotfixes and unspecified security hardening [5][6][7]. Downtime began at 08:00 UTC for about one hour [7].
- **2 Oct 2026, security hotfix:** "minor security and stability issues", no gameplay, balance or UI changes, roughly one hour of planned maintenance; specifics undisclosed [6].
- **Known gaps:** Linux unsupported [8]; the planned community server features above remain unshipped in the sources read.
- **Next:** Season 02 is reported for 15 Oct 2026, with the first progression wipe [12]. This is outside the verified version.

# Admin & Technical Notes

Source warning: no official server-admin manual from Bulkhead was found. Everything in this section other than the 0.1.2 admin changes comes from unofficial or provider material and is labelled.

**Hosting model.**

- A fan site (self-described as unofficial, checked 2026-09-01) relays an official thread saying server code will not be released for everyone to host, citing performance and security, and that individuals rent from approved hosts [9]. Player-reported.
- A server-tracking site says there is no official developer documentation, that only three approved hosts run servers, and that RCON access depends on the host's panel [11]. Player-reported.
- Consequence for admins: you probably cannot run your own SteamCMD or Docker server; confirm with your host. Several commercial hosting pages advertised pre-launch capacity; treat these as marketing, not evidence of an available server download.

**Admin changes confirmed in 0.1.2 (30 Sep 2026)** [5][6][7]:

- Daily scheduled restart time, set in UTC.
- RCON AllowedHosts setting to restrict which hosts can reach RCON.
- RCON message and broadcast lengths capped; RCON responses default to Standard detail rather than Full; config responses no longer expose server internals.
- ServerImageURL is validated at config load.
- Since 0.11, community server IDs persist across map changes and restarts [3].

**Unofficial RCON and config reference** (fan site, self-described as not official docs and subject to change; player-reported) [10]:

- RCON is plain HTTP REST with JSON, base `http://<host>:<port>/v1/`, default port 7776 (`-RCONPort=`), no TLS, so the password crosses the network in clear text.
- Authentication is `Authorization: Bearer <rcon-password>`; one token has full read and write access; there is no read-only role. The listener is off by default (`bEnabled` in `[/Script/WDRCON.WDRCONSettings]`).
- Endpoint groups: status, players, bans, config, rotation, capabilities; writes include kick, kill, message, ban, broadcast and match map/end/restart. `PUT /v1/config` replaces the whole document and supports `If-Match` revision checks.
- Listed `ServerSettings.ini` keys include `ServerName`, `ServerPassword`, `ServerImageURL` (1024x256), cash and level min/max limits, `MaxReservedSlots` (default 20), `MaxPlayers` (listed default 128), `MinimumRequiredPlayers` (default 60), KOTH `ScorePeriod` (default 24 s) and map rotation (`Ordered` or `Random`).
- Several endpoints were reported removed in build ++Wardogs+Live-CL-501228 (2026-09-14) in favour of the config document [10].
- Assessment: because RCON uses one shared secret over unencrypted HTTP, restrict AllowedHosts and keep it on a private network or behind a TLS proxy. Confidence Medium, resting on [6] and [10].

**Third-party tools** (player-reported, not endorsed): Warcon, an open-source (MIT) self-hostable multi-server RCON panel with per-admin roles and audit log [13]; BattleMetrics has reportedly added WARDOGS RCON support [11]. The guide at [11] was written by Warcon's builders, so its recommendations are promotional.

**Hosting provider material** (secondary): BisectHosting summarises the 0.1.2 admin changes [5]; its support article on changing the automatic restart time returned HTTP 403 and is not cited. Host guides disagree on any built-in restart timer value (12 h versus 24 h of uptime); unverified.

**Modding.** The Steam page lists no mod support [1]. No official modding toolkit or plan was found.

**Client notes.** Kernel-level anti-cheat is listed [1]; Linux is unsupported [8]; Windows 11 update KB5124010 caused crash WD-L020, fixed 30 Sep 2026 [6].

# Risks & Caveats

- Patch contents rest on press summaries; Steam news bodies were not readable, so official notes were not read directly [2].
- Admin and RCON material is unofficial and may change per build; the endpoint removals on 14 Sep show churn [10].
- The Steam page was read through a fetch summariser; the store host is prone to age-gate and rate limits.
- Commercial host claims may predate any real server tool.
- Season 02 (reported 15 Oct 2026) will likely change versions and admin tooling.

# Open Questions

- Which hosts are approved? Reported counts of two and three conflict. An official Bulkhead post naming them would resolve it.
- Is there an official RCON or ServerSettings.ini document? Bulkhead or Steam announcements would resolve it.
- Which anti-cheat product is used? A developer statement would resolve it.
- Netcode characteristics (tick rate, lag compensation): no source found.
- Will modding or Linux/Proton support ship, and when?
- What was fixed in the 2 Oct security hotfix?

# References

**Primary Sources**

- [1] **Valve / Bulkhead** — *WARDOGS on Steam*. https://store.steampowered.com/app/1867240/WARDOGS/. Accessed 2026-10-08.
- [2] **Valve / Bulkhead** — *WARDOGS Steam News Hub*. https://store.steampowered.com/news/app/1867240. Accessed 2026-10-08.

**Press & Secondary**

- [3] **PlayDay** — *WARDOGS patch 0.11 focuses on server browsers (full notes)*. https://playday.one/2026/09/14/wardogs-patch-11-focuses-on-server-browsers-full-notes/. Accessed 2026-10-08.
- [4] **Gfinity Esports** — *WARDOGS Season 1 changelog*. https://www.gfinityesports.com/article/wardogs-season-1-changelog-early-access-patch-notes. Accessed 2026-10-08.
- [5] **BisectHosting (hosting provider, secondary)** — *WARDOGS Update 0.1.2 patch notes*. https://www.bisecthosting.com/blog/wardogs-update-0-1-2-patch-notes-bug-fixes-improvements-flythrough-exploit-fob-pallet-delivery-xp. Accessed 2026-10-08.
- [6] **In-Game News** — *WARDOGS update 0.1.2 and security hotfix*. https://ingamenews.com/gaming-news/wardogs-update-0-1-2-and-security-hotfix-a-comparative-overview/. Accessed 2026-10-08.
- [7] **MP1st** — *WARDOGS update 0.1.2 deployed on September 30*. https://mp1st.com/title-updates-and-patches/wardogs-update-0-1-2-deployed-on-september-30-as-servers-go-down. Accessed 2026-10-08.
- [8] **GamingOnLinux** — *WARDOGS developers clarify Linux support via Proton may come later*. http://www.gamingonlinux.com/2026/09/wardogs-developers-clarify-linux-support-via-proton-may-come-later. Accessed 2026-10-08.
- [12] **Gfinity Esports** — *WARDOGS Season 2: release date, content and what to expect* (date only, from a search result). https://www.gfinityesports.com/article/wardogs-season-2-everything-we-know. Accessed 2026-10-08.

**Player-Reported Evidence**

- [9] **WARDOGS-game.com (unofficial fan site)** — *WARDOGS Servers, Regions & Hosting*. https://wardogs-game.com/servers. Accessed 2026-10-08.
- [10] **wardogs.tech (unofficial)** — *Wardogs Server Reference*. https://wardogs.tech/rcon-reference. Accessed 2026-10-08.
- [11] **Wardog Servers (independent tracker)** — *WARDOGS RCON and admin tools*. https://wardogservers.com/guides/wardogs-rcon-and-admin-tools. Accessed 2026-10-08.
- [13] **Warcon project (GitHub)** — *warcon: self-hostable RCON panel for WARDOGS*. https://github.com/warcon-app/warcon. Accessed 2026-10-08.

# Further Reading

- Steam community announcements for app 1867240 (check for Season 02 notes and any official server documentation).

# Related Documents

- gameplay-modes-foundation
- maps-environment-foundation
- meta-release-foundation

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after independent re-verification of validate, markdownlint and links (0 dead). | Standing mandate (auto-approve on green QA) |
