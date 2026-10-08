---
id: patch-history
title: "Patch & Update History"
version: 1.0.0
status: frozen
confidence: Medium
category: Meta & Release
topic: "Dated per-patch changelog from closed beta through 0.1.2 and hotfixes"
market: Global
game_version: "Early Access Update 0.1.2 plus hotfixes to 2 Oct 2026"
document_type: reference-data
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [meta-release-foundation, technical-servers-foundation, economy-foundation, editions-pricing-platforms]
tags: [patch-history, changelog, early-access]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | patch-history |
| Version | 1.0.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Meta & Release |
| Game version | Early Access Update 0.1.2 plus hotfixes to 2 Oct 2026 |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

This reference lists every dated WARDOGS build change found between the August 2026 closed betas and 8 October 2026, with changes grouped by gameplay, economy, servers and bugs. It goes deeper than the one-line patch table in meta-release-foundation and does not restate the release timeline.

Every entry rests on press or community summaries: the Steam News post bodies do not render to automated fetchers, so no official patch note was read directly [1]. The 0.1.2 date resolves to 30 September 2026 (maintenance from 08:00 UTC); one secondary source says "September 29" and is treated as an error [2][3][4][5][6][8]. Season 02 is announced, not live [11].

Confidence is Medium: the change lists agree across independent outlets, but all are secondary, and the hotfix and Season 02 entries are thinner or conflicted.

# Key Takeaways

- Version labels in press are "Season 1.0" (10 Sep), "0.11" (14 Sep) and "0.1.2" (30 Sep); the 14 Sep notes call the patch 0.11, not 0.1.1 [7][10].
- 0.1.2 went live on 30 Sep 2026 with one hour of maintenance starting 08:00 UTC [3][5]. A "September 29" reference appears only in one secondary article [8].
- 0.1.2 is mostly an economy-integrity and server-tooling patch: server-side revive checks, a fly-through reward cap, scaled buildable rewards, a new DEPLOY flow and RCON restrictions [3][4].
- The 2 Oct entry is probably two items: a no-gameplay security hotfix (00:13 UTC per one outlet) and a later balance hotfix covering the IR rangefinder and anti-air [6][8].
- Season 1.0 changed the economy sharply: XP for levels 10-20 became roughly 40-124% slower and many vendor prices changed (10 Sep 2026) [10].
- Season 02 is scheduled for 15 Oct 2026 and is not live at 8 Oct 2026 [11].

# Scope

Covers the closed beta notes, the Early Access launch changelog, 0.11, 0.1.2 and the October hotfixes, as of 8 Oct 2026. Excludes full unlock tables beyond what is summarised, and Season 02 content. Release dates, prices and platforms are in meta-release-foundation and editions-pricing-platforms; in-game economy rules are in economy-foundation; server administration is in technical-servers-foundation.

# Definitions

- **Official vs press**: "Official" means published by BULKHEAD or Team17. Every source cited for change contents here is press or player-reported, though most reproduce official notes.
- **Season 1.0**: label in the launch-day changelog for the unlock-level changes [10].
- **0.11**: version label of the 14 Sep 2026 patch [7].
- **WD-L020**: crash code BULKHEAD linked to Windows 11 update KB5124010 [3].
- **RCON**: remote console used by community server admins.

# Current State

At 8 Oct 2026 the live build is Update 0.1.2 as modified by the 2 Oct hotfix or hotfixes. The balance hotfix is reported to apply as regional servers restart, with no client download [8]. Season 02 has been announced for 15 Oct 2026 but is not live [11].

# Detail

## Version label conflict

| Label | Date | Used by | Note |
|-------|------|---------|------|
| Season 1.0 | 10 Sep 2026 | Gfinity changelog [10] | Only label given; no build number |
| 0.11 | 14 Sep 2026 | PlayDay [7] | Article states 0.11, not 0.1.1 |
| 0.1.2 | 30 Sep 2026 | Gfinity, MP1st, Bisect, Vice, InGameNews [2][3][4][5][6] | Vice calls it a minor patch, InGameNews substantial [5][6] |

Assessment: 0.11 and 0.1.2 are inconsistent as a numbering scheme (0.11 reads as 0.1.1 in dotted form), so the press probably follows the studio's own inconsistent labels. Confidence Low; no developer explanation was found and no build ID was found.

## 0.1.2 date: 29 vs 30 September

| Claim | Evidence |
|-------|----------|
| 30 Sep 2026, maintenance from 08:00 UTC (01:00 PT), about one hour | MP1st article stamped 30 Sep [3]; Vice, published 30 Sep, same window [5] |
| Deployed 30 Sep | Gfinity, published 30 Sep, "deployed today" [2]; BisectHosting post dated 30 Sep [4]; InGameNews table 30 Sep 06:57 UTC [6] |
| "September 29 patch" | One MMOEXP article, which says its details come from a single podcast [8] |

Assessment: 30 September is correct; 29 September is a secondary-source slip. Confidence High, because five outlets and the maintenance window agree and none of them mentions the 29th.

## Entry index

| Date | Build or label | Official or press | Source |
|------|----------------|-------------------|--------|
| 14 Aug 2026 | Closed beta notes (partial) | Community repost of developer notes, published 21 Aug | [12] |
| 21-23 Aug 2026 | Closed Beta Weekend | Official press release | [13] |
| 3-6 Sep 2026 | Second closed beta | Press | [10] |
| 10 Sep 2026 | Season 1.0 (Early Access launch) | Press | [10] |
| 14 Sep 2026 | 0.11 | Press, full notes | [7] |
| 30 Sep 2026 | 0.1.2 | Press, multiple | [2][3][4][6] |
| 2 Oct 2026 | Security and stability hotfix | Press | [6] |
| 2 Oct 2026 | Balance hotfix | Press, single source | [8][9] |
| 15 Oct 2026 | Season 02 | Announced, not live | [11] |

## Closed beta, notes dated 14 Aug 2026 (partial)

- Gameplay: pistol damage up; AK74, Galil, M4 and FAL handling improved; 122mm damage against air vehicles reduced; Gepard removed from unlock tracks and vendor [12].
- Economy: level-up costs raised above level 15; vehicle and weapon unlock costs raised across classes; sniper kill-streak bonuses removed in No Man's Land; a rebuy bug fixed [12].
- Bugs and UI: held vehicle inputs lost on menu open fixed; Havoc spawning in the shooting range fixed; Hot Zone magnet shrink fixed; HOTAS bindings persist; new Background FPS Limit setting [12].
- The source says the full list was still being compiled [12]. The 21-23 Aug beta weekend is attested by a press release and the 3-6 Sep beta by Gfinity; whether the 14 Aug notes belong to the former is not stated [10][12][13].

## 10 Sep 2026, Early Access launch ("Season 1.0")

- Gameplay: church roof exploit fixed; Z20 Lakota balance pass; helicopter input damping on all devices; vehicle turret rotation cap; 155mm, 122mm and flare deployables take more loadout space; tank aiming DPI fix [10].
- Progression: levels 10-20 slower, curve flattens from level 35; Artillery to Career 90, Heavy Tank to Driver 35. Example bands: level 10 from 25,000 to 35,000 XP; level 20 from 111,500 to 250,000; level 50 from 838,000 to 1,000,000. Air vehicle kill XP 300 to 250 [10].
- Economy: Forward Operating Base vendor price $2,500 to $7,500; Artillery Tank $400,000 to $500,000; Z20 Lakota $50,000 to $35,000; URAL $50,000 to $35,000; supply-crate pricing rescaled to a 1-200 range [10].
- Servers: reworked server browser filtering, community server image scaling fixed, Host button goes to the hosting page, report tracking with weighted reports, ban announcements, voice chat recovery [10].
- Bugs and stability: DLSS Frame Generation toggle without restart, several crash paths fixed, more detailed GPU crash reports [10].

## 14 Sep 2026, Patch 0.11

- Maintenance about one hour from 08:00 UTC [7].
- Servers: browser split into Official and Community; Official lost filters; Community gained text search; Community Server IDs persist across matches and restarts; Show Empty/Full option; more Asia capacity [7].
- Economy: 5% end-of-match cash bonus on Community servers for one week, as an apology; exploit sanctions defined (timed ban plus cash and XP reset; permanent ban for XP-farming servers and for publishing unreported exploit content) [7].
- Bugs: various cash exploits and more GPU crashes fixed [7].
- Gameplay: none completed; community favouriting, priority queues, message of the day, warmup activities, seeding AFK kick disable and team switching were listed as not yet ready [7].

## 30 Sep 2026, Update 0.1.2

- Bugs: WD-L020 crash (Windows 11 KB5124010) fixed; throwables blocked from enclosed vehicle seats; adaptive crosshair hides when aiming; buildable crit spots favour reachable spots; Havoc 20mm and 30mm damage bug fixed; localisation improved [3][4].
- Economy: revive validity checks fully server-side; vehicle fly-through exploit fixed and capped; buildable destruction rewards scale with build progress; FOB pallet deposits outside the zone give reduced reward; cash and progression resets and bans for exploits and real-money trading, with first-time leniency ended [2][3][4].
- Servers: DEPLOY flow (Official, Community, Infantry Mode, Low-Level); Advanced Filters back on Official; full names on hover; queue position; Anonymous mode; gamepad support on DEPLOY [3][4].
- Admin: daily restart time in UTC, RCON AllowedHosts, RCON length caps, Standard response detail default, ServerImageURL checked on load [3][4].

## 2 Oct 2026 hotfixes

- Security and stability hotfix: minor undisclosed issues, no gameplay, balance, economy or UI changes, one-hour maintenance; InGameNews timestamp 00:13 UTC. The same article is ambiguous on whether the maintenance was scheduled or completed [6].
- Balance hotfix: IR rangefinder removed from the vendor until Season 02 and reported to need batteries on return; the anti-air Sea Whiz time to kill a Havoc cut from about 12 s to about 6 s; no download, rolling out as regional servers restart over about 12 hours [8]. This is player-reported podcast material; a search summary of further coverage places this item at 15:39 UTC and one outlet's title links it to a CWIS change [8][9].

## Season 02 (announced, not live)

Announced for 15 Oct 2026 in BULKHEAD's teaser; contents and launch time are not confirmed [11]. Listed only so the sequence is complete; nothing under Season 02 has happened yet.

# Early Access Changes & Known Issues

- This whole document is the change record; see Detail. The main known discrepancies are 29 vs 30 September, the 0.11 vs 0.1.2 labels, and the two 2 Oct hotfixes.
- No hotfixes were found between 14 Sep and 30 Sep, but absence of evidence is not proof; the Steam News feed is the authority [1].

# Admin & Technical Notes

Admin-relevant entries: Community Server IDs persist (0.11, 14 Sep 2026), daily restart time and RCON restrictions (0.1.2, 30 Sep 2026) [7][3]. Config detail belongs in technical-servers-foundation.

# Risks & Caveats

- No official patch text was read; each outlet may paraphrase or lag, and Steam News post bodies do not render to fetchers [1].
- Dates use article timestamps and maintenance windows, not Steam post times.
- MMOEXP relies on one podcast, and Timesaver.gg sells boosting services [8][11].
- Season 02 will supersede the Current State on 15 Oct 2026.

# Open Questions

- Official Steam post titles and exact post times for each patch: resolve by reading the Steam News posts in a browser.
- Whether the 2 Oct entries are one hotfix or two: resolve from the Steam News feed.
- Why the studio labels 0.11 and 0.1.2 inconsistently.
- Whether the 14 Aug notes belong to the 21-23 Aug beta or an earlier one.
- Whether any hotfix shipped between 14 and 30 Sep.

# References

**Primary Sources**

- [1] **Valve / BULKHEAD** — *WARDOGS Steam News Hub*. https://store.steampowered.com/news/app/1867240. Accessed 2026-10-08.
- [13] **Team17 / BULKHEAD** — *WARDOGS is coming to Steam Early Access on 10 September* (press release). https://www.gamedeveloper.com/press-release/wardogs-is-coming-to-steam-early-access-on-10-september. Accessed 2026-10-08.

**Press & Secondary**

- [2] **Gfinity Esports** — *Wardogs Update 0.1.2 Patch Notes: Cash and XP Exploit Fixes Are Here*. https://www.gfinityesports.com/article/wardogs-update-012-patch-notes-cash-and-xp-exploit-fixes-are-here. Accessed 2026-10-08.
- [3] **MP1st** — *Wardogs Update 0.1.2 Deployed on September 30 as Servers Go Down*. https://mp1st.com/title-updates-and-patches/wardogs-update-0-1-2-deployed-on-september-30-as-servers-go-down. Accessed 2026-10-08.
- [4] **BisectHosting** — *WARDOGS Update 0.1.2 patch notes*. https://www.bisecthosting.com/blog/wardogs-update-0-1-2-patch-notes-bug-fixes-improvements-flythrough-exploit-fob-pallet-delivery-xp. Accessed 2026-10-08.
- [5] **Vice** — *WARDOGS update 0.1.2 patch notes*. https://www.vice.com/en/article/wardogs-update-0-1-2-patch-notes/. Accessed 2026-10-08.
- [6] **InGameNews** — *WARDOGS update 0.1.2 and security hotfix: a comparative overview*. https://ingamenews.com/gaming-news/wardogs-update-0-1-2-and-security-hotfix-a-comparative-overview/. Accessed 2026-10-08.
- [7] **PlayDay** — *WARDOGS patch 0.11 focuses on server browsers (full notes)*. https://playday.one/2026/09/14/wardogs-patch-11-focuses-on-server-browsers-full-notes/. Accessed 2026-10-08.
- [10] **Gfinity Esports** — *WARDOGS Season 1 changelog*. https://www.gfinityesports.com/article/wardogs-season-1-changelog-early-access-patch-notes. Accessed 2026-10-08.

**Player-Reported Evidence**

- [8] **MMOEXP** — *WARDOGS October 2 update, Season 2 wipe, IR rangefinder nerf and new weapons* (single podcast source). https://www.mmoexp.com/News/wardogs-october-2-update-season-2-wipe-ir-rangefinder-nerf-and-new-weapons.html. Accessed 2026-10-08.
- [9] **Timesaver.gg** — *WARDOGS IR goggles and CWIS hotfix* (sells boosting services). https://timesaver.gg/blog/wardogs-ir-goggles-cwis-hotfix. Accessed 2026-10-08.
- [11] **Timesaver.gg** — *WARDOGS Season 2: everything we know* (sells boosting services). https://timesaver.gg/blog/wardogs-season-2-everything-we-know. Accessed 2026-10-08.
- [12] **Gaming with Daopa** — *Wardogs Closed Beta Patch Notes, August 14th* (community repost, published 21 Aug 2026). https://gamingwithdaopa.ellatha.com/wardogs/closed-beta-patch-notes-august-14th/. Accessed 2026-10-08.

# Further Reading

- meta-release-foundation for the release timeline and Steam reception.
- Dexerto WARDOGS patch notes wiki: https://www.dexerto.com/wikis/wardogs/patch-notes/

# Related Documents

- meta-release-foundation
- technical-servers-foundation
- economy-foundation
- editions-pricing-platforms

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | - |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after independent re-verification of validate, markdownlint and links (0 dead). | Standing mandate (auto-approve on green QA) |
