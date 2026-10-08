---
id: control-zone-and-match-flow
title: "Control Zone & Match Flow"
version: 1.0.0
status: frozen
confidence: Medium
category: Gameplay & Modes
topic: "Match lifecycle, Control Zone and Hot Zone scoring, win conditions, spawning, team balance"
market: Global
game_version: "Early Access Season 01, patch 0.1.2 (30 Sep 2026) plus 2 Oct 2026 hotfixes; pre-Season-02 baseline (Season 02 due 15 Oct 2026)"
document_type: depth
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related:
  - gameplay-modes-foundation
  - progression-and-role-tracks
  - maps-environment-foundation
  - launch-maps-reference
  - cash-rewards-and-costs
tags:
  - gameplay
  - control-zone
  - hot-zone
  - scoring
  - spawning
  - baseline
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | control-zone-and-match-flow |
| Version | 1.0.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Gameplay & Modes |
| Game version | Season 01, patch 0.1.2 (30 Sep 2026) plus 2 Oct 2026 hotfixes (pre-Season-02 baseline) |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

The official sources describe the match loop in a few sentences: three teams contest a randomised 2x2 km Control Zone inside a 256 km2 map, the team with the most players inside earns points, and the first to 100 points wins [1][2]. A Hot Zone is a shifting sub-zone inside the Control Zone where each player counts double towards the player count and cash is doubled [2]. That is the whole of the officially published scoring rule at Season 01.

Everything finer-grained is player-reported: the 30-second scoring tick, one point per tick, the tower and code mechanic that drags the Hot Zone, the deployment board, the APC spawn and its cooldown [12][13]. No official source published at 2026-10-08 states respawn timers, spawn placement rules, team-balance rules or match length. This document records those gaps explicitly as a baseline so Season 02 changes can be diffed.

Confidence is Medium. The core rule rests on the Steam page and the developer's Top Questions post; spawn, tick and tower detail rests on player-reported guides, which may not raise a claim above Medium.

# Key Takeaways

- Win condition: first team to 100 points wins; the team with the most players inside the Control Zone earns points (official, stated 18 Feb 2026 and on the store page, unchanged through 2 Oct 2026) [1][2].
- Hot Zone: officially a shifting sub-zone; players count as double towards the player count and it yields double cash [2].
- Map scale: the Control Zone is 2x2 km inside a 256 km2 map, so it is a fraction of the map [2].
- Tick rate and points per tick are not official; one player-reported guide says one point per 30 seconds [12][13].
- Official posts do not publish respawn timers, spawn rules or team-balance logic; the Deploy flow added in 0.1.2 is a server-browser screen, not an in-match spawn screen [7].
- Squads have no size limit and give extra UI, communication tools and vehicle locking [2].
- The "Tactical Depth & Teamplay" post is a video wrapper; its text states only that decisions affect account balance [4].

# Scope

Covers the match lifecycle from server join to match end, Control Zone and Hot Zone mechanics, scoring and the first-to-100 rule, three-team dynamics, spawn, respawn and deploy flow, developer statements on intended tactical play, and changes by patch. Game version: Season 01, patch 0.1.2 plus the 2 Oct 2026 hotfixes. Excluded: cash amounts (see cash-rewards-and-costs), role tracks and XP (see progression-and-role-tracks), map detail (see maps-environment-foundation and launch-maps-reference), and the parent summary (see gameplay-modes-foundation).

# Definitions

- **Control Zone**: randomised 2x2 km objective area per match [1][2].
- **Hot Zone**: shifting sub-zone inside the Control Zone; presence counts double and cash is doubled [2].
- **Deploy (server browser flow)**: the 0.1.2 screen to choose Official, Community, Infantry Mode or Low-Level servers [7].
- **Deployment board / deployment computer**: the in-game spawn interface, player-reported [12][13].
- **Safe Zone**: the area with the Equipment Vendor, player-reported [12].

See also `GLOSSARY.md`.

# Current State

Verified 2026-10-08 against the sources shown.

- Up to 100 players in three teams fight over one Control Zone [1][2]. Official team names are Lonestar, Valkyra and Manticore (18 Feb 2026) [2].
- The Control Zone is a randomised 2x2 km area within a 256 km2 map; zone location varies per match [2].
- The team with the most players in the zone earns points; the first team to 100 points wins [1][2].
- The Hot Zone is a shifting sub-zone; players count double towards player count and it pays double cash [2].
- Players start with $10,000 and buy a loadout each life; cash persists between matches [1][2].
- Squad size is unlimited; squads get extra UI, communication tools and vehicle locking [2].
- Proximity chat is confirmed by the developer; the store page calls it local voice chat [1][2].
- Patch 0.1.2 (30 Sep 2026): revive validity checks are now fully server authoritative, vehicle fly-through rewards are capped, buildable-destruction rewards scale with build progress, and depositing pallets into a FOB outside the zone pays reduced rewards [7].
- 2 Oct 2026 balance hotfix: IR Rangefinders disabled in the vendor until Season 02 (where they will require batteries); the CIWS destroys the Havoc in about 6 seconds instead of 12 [8].
- Season 02 is dated 15 Oct 2026 and is described as a larger update with new map conditions, equipment, balance reworks and additional features [7][9].

# Detail

## Baseline values

All values are as of Season 01, 0.1.2 plus 2 Oct 2026 hotfixes, unless a different date is shown. "Official" means developer-published; "PR" means player-reported.

| Value | As-of version | Source |
|-------|---------------|--------|
| Max players per match: 100 | Season 01 (store page, 18 Feb 2026 post) | Official [1][2] |
| Teams: 3 (Lonestar, Valkyra, Manticore) | Season 01 | Official [2] |
| Win threshold: 100 points | Season 01 | Official [1][2] |
| Control Zone size: 2x2 km, randomised | Season 01 | Official [1][2] |
| Map size: 256 km2 | 18 Feb 2026 post | Official [2] |
| Hot Zone presence weight: x2 per player | 18 Feb 2026 post | Official [2] |
| Hot Zone cash multiplier: x2 | 18 Feb 2026 post | Official [2] |
| Starting cash: $10,000 | Season 01 | Official [1] |
| Squad size: unlimited | 18 Feb 2026 post | Official [2] |
| Scoring tick: 30 s, 1 point to leader | Guide read Oct 2026 | PR [12][13] |
| Players per team: about 33 | Guide read Oct 2026 | PR [13] |
| Capture towers per Control Zone: 3 to 5 | Guide read Oct 2026 | PR [13] |
| Drill rig activation: 6,000 fuel | Guide read Oct 2026 | PR [13] |
| Zone occupation pay: $160 (Control Zone), $320 (Hot Zone) per cycle | Guide read Oct 2026 | PR [13] |
| M113 APC unlock: any faction at 20 points | Guide read Oct 2026 | PR [13] |
| APC spawn personal cooldown: 10 minutes | Guide read Oct 2026 | PR [13] |
| New Recruit discount: 50% until account level 9 | Guide read Oct 2026 | PR [13] |
| Match length: can exceed 1 hour | Guide read Oct 2026 | PR [13] |
| CIWS time to destroy Havoc: about 6 s (was 12 s) | 2 Oct 2026 hotfix | Official [8] |
| IR Rangefinder: disabled in vendor until Season 02 | 2 Oct 2026 hotfix | Official [8] |
| Community-server end-of-match cash bonus: 5% for one week | 0.11, 14 Sep 2026 (expired) | Official [6] |
| Season 02 date: 15 Oct 2026 | Teaser 22 Sep 2026 | Official [9] |

## Match lifecycle

| Stage | What is known | Class |
|-------|---------------|-------|
| 1. Find a server | From 0.1.2, Deploy offers Official, Community, Infantry Mode and Low-Level lists; the browsers were split into Official and Community in 0.11; a queue position is shown after Join [6][7] | Official |
| 2. Spawn and buy | Buy a loadout each life at the Equipment Vendor in the Safe Zone, then spawn through the deployment board; "Rebuy Last Loadout" restores the previous kit [1][12][13] | Store page official; interface detail PR |
| 3. Reach the zone | Transporting friendlies to the zone earns cash; ground vehicles and helicopters carry players [1][13] | Official / PR |
| 4. Contest | The team with most players in the zone earns points; Hot Zone doubles presence [1][2] | Official |
| 5. End | First team to 100 points wins [1][2] | Official |

Not published officially: what happens after a win (map rotation, scoreboard, lobby return), match-length targets and round time limits. Assessment: the lifecycle after step 5 cannot be described from sources; confidence Low.

## Control Zone and scoring

Officially, scoring is a comparison of player counts inside the zone, awarding points to the leader, to a threshold of 100 [1][2]. The official text does not say how often points are awarded, whether a tie awards points, or whether the margin matters. One player-reported guide gives a 30-second check with one point to the leading team, which implies a minimum of about 50 minutes (100 checks) if a team leads every check [13]. Assessment: that figure is arithmetic on a player-reported tick, not a measured match length; confidence Low. The same guide says matches can pass an hour [13].

## Hot Zone

Official: a shifting sub-zone within the Control Zone; players count as double towards player count, "leading to match-swinging potential", and it yields double cash [2]. The store page repeats "chase the Hot Zone to earn double the cash" [1].

Player-reported: it appears as a yellow sub-zone on the tactical map with a circular minimap outline; size and relocation interval are not published [12]. A second guide describes a drifting circle that can be pulled toward a tower by entering a master code, and toward a player FOB by a fuel-fed drill rig [13]. These tower and rig mechanics are not described in any official post read for this document.

## Three-team dynamics

The developer designed three teams so that the zone is a three-way contest, with a lore split: Lonestar (Western paramilitary), Valkyra (Soviet-revival) and Manticore (Persian shadow army) [2]. Because points go to the team with the most players, a team can lead while outnumbered by the other two combined; this follows from the rule as stated and is an inference (Assessment: confidence Medium; basis: the scoring rule at [2]). No official source states how players are assigned to teams, whether teams are balanced to equal size, or whether team switching is restricted. The 0.11 post lists "Team Switching Controls" and "AFK kicking during seeding disabling" as upcoming features, which implies team switching and seeding phases exist but were not yet adequately controlled on 12 Sep 2026 [6]. A player-reported guide gives about 33 players per team [13].

## Spawn, respawn and deploy

- Official: the 0.1.2 Deploy flow is a pre-match server selection screen aimed at steering players to Infantry Mode and Low-Level servers [7].
- Official: revive validity checks are server authoritative from 0.1.2 [7].
- Player-reported: loadout purchase at the Equipment Vendor, then spawn via the deployment board [12].
- Player-reported: there is no squad spawning; an M113 APC unlocks once any faction reaches 20 points, the deployment computer can teleport you to an allied APC with a 10-minute personal cooldown, and destroying an APC's satellite dish disables its spawn function [13].
- Player-reported: reviving is cheaper than respawning [13]. Revive duration is not given [12].
- Not published: respawn timer, spawn point distribution, spawn protection, spawn-camping rules.

## Developer statements on intended tactical play

The "Tactical Depth & Teamplay" post (21 May 2026) gives three bullets: real-world ballistics, audio and flight models; every decision affects your account balance; a 100% player-driven militaristic sandbox. It frames a Debrief video on three pillars of tactical depth [4]. The post text names no mechanic more specific than that; the video content is not transcribed in the snapshot. Related official statements elsewhere:

- "Teamplay isn't encouraged, it's rewarded": revives, transport, kills, spotting and more pay cash in the zone [2].
- Roles are player-defined by purchased gear, earning XP across six tracks [2].
- "There are no set rules of engagement"; examples include chasing the Hot Zone, sniping in a ghillie suit, helicopter supply runs, building a forward operating base at a chokepoint, and artillery tanks [1].
- The mode was developed with the original ARMA King of the Hill mod creators as a standalone KOTH-inspired shooter [3].
- A 16 Jun 2026 devlog says the line between arcade and realistic has been drawn by the developer, without stating mechanics [5].

# Early Access Changes & Known Issues

| Date | Change relevant to match flow | Source |
|------|-------------------------------|--------|
| 2026-09-09 | Season 1 changelog: report tracking, vehicle turret rotation caps, deployables take more loadout room; no zone or scoring change | Official [10] |
| 2026-09-14 | 0.11: Official/Community browser split, filters removed from Official, 5% community end-of-match cash bonus for one week; team-switching controls and warmup improvements listed as upcoming | Official [6] |
| 2026-09-30 | 0.1.2: Deploy flow, server-authoritative revives, reward caps (fly-through, buildables, pallets outside zone), Advanced Filters returned to Official list | Official [7] |
| 2026-10-02 | Hotfix: IR Rangefinders removed from vendor; CIWS kill time on Havoc 12 s to about 6 s | Official [8] |
| 2026-10-02 | Separate hotfix at 08:00 UTC for minor security and stability; no gameplay detail | Official [11] |
| 2026-10-15 | Season 02 due: new map conditions, equipment, balance reworks | Official [7][9] |

No official post read changed the 100-point threshold, the Hot Zone multipliers or zone size during Season 01. Team-switching controls, tiered priority queues and improved warmup were pipeline features on 14 Sep 2026 and are not confirmed shipped [6].

# Admin & Technical Notes

Community servers can run modifiers; Official servers had no modified modes at 14 Sep 2026 [6]. Infantry Mode and Low-Level servers are named in the 0.1.2 Deploy flow, but the rules they change are not defined in the official post [7]. Whether the 100-point threshold or tick is a server setting is not documented in sources read here.

# Risks & Caveats

- Season 02 is due 15 Oct 2026 and promises balance reworks and new map conditions; the baseline table may go stale within days [7][9].
- The 30-second tick, tower codes and APC spawn rules come from player-reported guides and the developer has not confirmed them [12][13].
- The scoring text says "most players", which leaves ties and margin undefined.
- The Tactical Depth post is largely a video wrapper; its substance is not recoverable from text.

# Open Questions

- Scoring tick and points per tick: not official; resolve from an official post or a timed in-game test.
- Respawn timer, spawn distribution, spawn protection: unpublished.
- Team assignment and balancing rules: unpublished.
- Official confirmation of the tower and master-code mechanic, the drill rig, and the M113 APC spawn.
- Conflict with gameplay-modes-foundation: it says Official servers have no filters, while the 0.1.2 post says Advanced Filters were added back to the Official list [7]. It also says the Steam page lists "proximity voice chat"; the store page says "local voice chat" and the 18 Feb 2026 post says proximity chat [1][2].
- gameplay-modes-foundation treats the 2 Oct hotfix content as inconsistent in press; the official posts show two separate hotfixes, a security and stability one and a balance one [8][11].
- The foundation's role-track names (Assault or Career) are not given in the official post, which says only six tracks "from Medic to Pilot" [2].
- Match end flow and map rotation after 100 points.

# References

**Primary Sources**

- [1] **Valve / Bulkhead Studios** — *WARDOGS on Steam* (store page, snapshot 2026-10-08). https://store.steampowered.com/app/1867240/WARDOGS/. Accessed 2026-10-08.
- [2] **Bulkhead Studios** — *WARDOGS - TOP QUESTIONS* (Steam announcement, 18 Feb 2026). https://store.steampowered.com/news/app/1867240/view/1825093633182385. Accessed 2026-10-08.
- [3] **Bulkhead Studios** — *Evolving the King of the Hill Mod!* (Steam announcement, 19 Feb 2026). https://store.steampowered.com/news/app/1867240/view/1825093633185779. Accessed 2026-10-08.
- [4] **Bulkhead Studios** — *WARDOGS - Tactical Depth & Teamplay* (Steam announcement, 21 May 2026). https://store.steampowered.com/news/app/1867240/view/1833334318569240. Accessed 2026-10-08.
- [5] **Bulkhead Studios** — *WARDOGS | Addressing Feedback* (Steam announcement, 16 Jun 2026). https://store.steampowered.com/news/app/1867240/view/1835236783575445. Accessed 2026-10-08.
- [6] **Bulkhead Studios** — *Scheduled Maintenance & Patch 0.11* (Steam announcement, 12 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1843481262698449. Accessed 2026-10-08.
- [7] **Bulkhead Studios** — *WARDOGS | Update 0.1.2 (Minor Patch)* (Steam announcement, 30 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1845383656376490. Accessed 2026-10-08.
- [8] **Bulkhead Studios** — *IR Goggles & CIWS Balance Hotfix* (Steam announcement, 2 Oct 2026). https://store.steampowered.com/news/app/1867240/view/1845383656386801. Accessed 2026-10-08.
- [9] **Bulkhead Studios** — *WARDOGS Season 02 Teaser* (Steam announcement, 22 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1844115010504839. Accessed 2026-10-08.
- [10] **Bulkhead Studios** — *Pre-load live / Season 1 changelog* (Steam announcement, 9 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1843481262690549. Accessed 2026-10-08.
- [11] **Bulkhead Studios** — *WARDOGS | Security & Stability Hotfix* (Steam announcement, 2 Oct 2026). https://store.steampowered.com/news/app/1867240/view/1845383656384445. Accessed 2026-10-08.

**Press & Secondary**

None cited; official posts were preferred.

**Player-Reported Evidence**

- [12] **allthings.how** — *WARDOGS Hot Zone: how double presence and double cash work* (player guide). https://allthings.how/wardogs-hot-zone-how-double-presence-and-double-cash-work/. Accessed 2026-10-08.
- [13] **allthings.how** — *WARDOGS beginner's guide: how the zone and cash systems work* (player guide). https://allthings.how/wardogs-beginner-s-guide-how-the-zone-and-cash-systems-work/. Accessed 2026-10-08.

# Further Reading

Snapshots of all official posts are under `snapshots/2026-10-08/steam-news/`.

# Related Documents

- gameplay-modes-foundation
- progression-and-role-tracks
- maps-environment-foundation
- launch-maps-reference
- cash-rewards-and-costs

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft: pre-Season-02 baseline. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after independent re-verification of validate, markdownlint, links (0 dead) and Steam post ids. Pre-Season-02 baseline. | Standing mandate (auto-approve on green QA) |
