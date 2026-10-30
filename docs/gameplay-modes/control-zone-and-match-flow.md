---
id: control-zone-and-match-flow
title: "Control Zone & Match Flow"
version: 1.1.0
status: frozen
confidence: Medium
category: Gameplay & Modes
topic: "Match lifecycle, Control Zone and Hot Zone scoring, win conditions, spawning, team balance"
market: Global
game_version: "Early Access Season 02, Update 0.2.0 (15 Oct 2026); official posts through 2026-10-15 (snapshot 2026-10-30)"
document_type: depth
created: 2026-10-08
updated: 2026-10-30
review_due: 2026-11-20
sources_verified: 2026-10-30
supersedes: null
related:
  - gameplay-modes-foundation
  - progression-and-role-tracks
  - maps-environment-foundation
  - launch-maps-reference
  - cash-rewards-and-costs
  - server-hosting-and-browser
  - price-tables-season-1
tags:
  - gameplay
  - control-zone
  - hot-zone
  - scoring
  - spawning
  - team-switching
  - season-02
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | control-zone-and-match-flow |
| Version | 1.1.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Gameplay & Modes |
| Game version | Early Access Season 02, Update 0.2.0 (15 Oct 2026); official posts through 2026-10-15 (snapshot 2026-10-30) |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-30 |
| Review due | 2026-11-20 |

# Executive Summary

The official sources describe the match loop in a few sentences: three teams contest a randomised 2x2 km Control Zone inside a 256 km2 map, the team with the most players inside earns points, and the first to 100 points wins [1][2]. A Hot Zone is a shifting sub-zone inside the Control Zone where each player counts double towards the player count and cash is doubled [2]. That remains the whole of the officially published scoring rule; Update 0.2.0 (15 Oct 2026) did not change it [14].

Everything finer-grained is player-reported: the 30-second scoring tick, one point per tick, the tower and code mechanic that drags the Hot Zone, the deployment board, the APC spawn and its cooldown [12][13]. No official source published at 2026-10-08 states respawn timers, spawn placement rules, team-balance rules or match length. Update 0.2.0 added official match-flow rules around the loop: team-switch restrictions once a team is more than 10 points ahead, a victim-driven Forgive/Punish vote on team kills, a Squad Intent UI, server seeding rewards with pre-match entertainment, a 20% vendor discount for a team at least 40 points behind second place, and a Lonestar faction experiment [14]. The Season 01 baseline is kept below as dated history.

Confidence is Medium. The core rule and the 0.2.0 rules rest on the Steam page, the Top Questions post and the Season 02 patch notes; spawn, tick and tower detail still rests on player-reported guides, which may not raise a claim above Medium. No official post after 2026-10-15 is in the 2026-10-30 snapshot.

# Key Takeaways

- Win condition: first team to 100 points wins; the team with the most players inside the Control Zone earns points (official, stated 18 Feb 2026 and on the store page, unchanged through 2 Oct 2026) [1][2].
- Hot Zone: officially a shifting sub-zone; players count as double towards the player count and it yields double cash [2].
- Map scale: the Control Zone is 2x2 km inside a 256 km2 map, so it is a fraction of the map [2].
- Tick rate and points per tick are not official; one player-reported guide says one point per 30 seconds [12][13].
- Official posts still do not publish respawn timers, spawn rules or team-balance logic; the Deploy flow added in 0.1.2 is a server-browser screen, not an in-match spawn screen [7].
- Team switching (0.2.0, notes of 14 Oct 2026): once a team is more than 10 points ahead, a player cannot switch teams again for 15 minutes after joining one, their map stays obscured until they first reach the Control Zone, and they cannot use the spawn vehicle until then [14].
- Team kills (0.2.0): the victim chooses Forgive or Punish; Punish marks accumulate towards kicks and escalating bans; leaving the safe zone after respawning without voting forgives automatically [14].
- Squads have no size limit and give extra UI, communication tools and vehicle locking [2].
- The "Tactical Depth & Teamplay" post is a video wrapper; its text states only that decisions affect account balance [4].

# Scope

Covers the match lifecycle from server join to match end, Control Zone and Hot Zone mechanics, scoring and the first-to-100 rule, three-team dynamics, spawn, respawn and deploy flow, developer statements on intended tactical play, and changes by patch. Game version: Season 02, Update 0.2.0, with Season 01 (patch 0.1.2 plus the 2 Oct 2026 hotfixes) as dated history. This document owns team switching, Forgive/Punish, Squad Intent, seeding and pre-match entertainment. Excluded: vendor prices (see price-tables-season-1), ping limits and the server browser (see server-hosting-and-browser), cash amounts (see cash-rewards-and-costs), role tracks and XP (see progression-and-role-tracks), map detail (see maps-environment-foundation and launch-maps-reference), and the parent summary (see gameplay-modes-foundation).

# Definitions

- **Control Zone**: randomised 2x2 km objective area per match [1][2].
- **Hot Zone**: shifting sub-zone inside the Control Zone; presence counts double and cash is doubled [2].
- **Deploy (server browser flow)**: the 0.1.2 screen to choose Official, Community, Infantry Mode or Low-Level servers [7].
- **Deployment board / deployment computer**: the in-game spawn interface, player-reported [12][13].
- **Safe Zone**: the area with the Equipment Vendor, player-reported [12].

- **Forgive / Punish**: the victim's choice after a team kill (0.2.0) [14].
- **Squad Intent**: a pre-defined squad-leader entry visible on the squad list before joining (0.2.0) [14].
- **Server seeding**: joining and populating an empty server, rewarded once the match begins (0.2.0) [14].

See also `GLOSSARY.md`.

# Current State

Season 01 statements verified 2026-10-08; Update 0.2.0 statements verified 2026-10-30 against the 14 Oct patch notes [14] and the 15 Oct release post [16].

- Up to 100 players in three teams fight over one Control Zone [1][2]. Official team names are Lonestar, Valkyra and Manticore (18 Feb 2026) [2].
- The Control Zone is a randomised 2x2 km area within a 256 km2 map; zone location varies per match [2].
- The team with the most players in the zone earns points; the first team to 100 points wins [1][2].
- The Hot Zone is a shifting sub-zone; players count double towards player count and it pays double cash [2].
- Players start with $10,000 and buy a loadout each life; cash persists between matches [1][2].
- Squad size is unlimited; squads get extra UI, communication tools and vehicle locking [2].
- The live store page uses both phrases: "proximity voice chat" in the Early Access state list and "local voice chat" in About This Game; the 18 Feb 2026 post says proximity chat [1][2].
- Patch 0.1.2 (30 Sep 2026): revive validity checks are now fully server authoritative, vehicle fly-through rewards are capped, buildable-destruction rewards scale with build progress, and depositing pallets into a FOB outside the zone pays reduced rewards [7].
- 2 Oct 2026 balance hotfix: IR Rangefinders disabled in the vendor until Season 02 (where they will require batteries); the CIWS destroys the Havoc in about 6 seconds instead of 12 [8].
- Season 02 was dated 15 Oct 2026 by the 22 Sep teaser and released as Update 0.2.0 on 15 Oct 2026; servers were back online per the release post [7][9][16].
- 0.2.0 team switching: once a team is more than 10 points ahead, a player cannot switch teams again for 15 minutes after joining one; if they switch or join a match in progress their map stays obscured until they first reach the Control Zone, and they cannot use the spawn vehicle until then. The notes say this adds friction for team-switch abusers while still letting players join friends [14].
- 0.2.0 team kills: when a teammate kills you, you are asked to Forgive or Punish; Punish results accumulate against the teamkiller, leading to kicks and escalating bans for repeat offenders; Forgive removes a potential mark; respawning and then leaving the safe zone without voting forgives automatically [14]. Thresholds for kicks and bans are not stated.
- 0.2.0 Squad Intent UI: squad leaders can set a team-visible intent from a pre-defined list, shown on the squad list before a player chooses to join; squad invites and other timed prompts now queue [14].
- 0.2.0 server seeding and pre-match entertainment: players who join and populate empty servers earn rewards and a vendor discount once the match begins; before the match, each spawn has guns with targets, a football and a hidden radio [14]. Reward and discount sizes are not stated.
- 0.2.0 Lonestar faction experiment (Season 2 only): Lonestar cash and XP win bonus and Lonestar teamplay-action cash and XP multipliers, with sizes not stated; all faction spawns on Bakurani were moved and rebuilt with purpose-built routes to the zone; community-server hosts seen exploiting the faction bonus will be punished [14]. The developer calls it a social experiment prompted by Lonestar's lower win rate and uniform visibility [14]. The preview adds that Lonestar uniforms are more desaturated [15].
- 0.2.0 losing-team discount: any team at least 40 points behind second place gets 20% off vendor purchases; this applies to all teams, not just Lonestar [14].
- 0.2.0 assistance request ping timer: 20 s to 60 s [14].
- 0.2.0 parachutes: longer to open, no opening below about 10 m, fall damage if opened below roughly 50 m while falling fast; prices are in price-tables-season-1 [14].
- 0.2.0 controller changes (summary): Aim Assist strength slider in Settings > Controller > Advanced (default 1, 0 is off), Aim Assist on Firing Range target dummies, adjusted sensitivity and Aim Acceleration, and rebinds including Cycle Minimap Zoom and Reject Tip on View, Deploy Crate on D-Pad Up (hold), and squad invite accept/reject moved to View/Menu [14].
- 0.2.0 Wager Vendor: not available at launch, opens later in Season 2, not permanent [14][15].

# Detail

## Baseline values

All values are as of Season 01, 0.1.2 plus 2 Oct 2026 hotfixes, unless a different date is shown. The 0.2.0 notes change none of the scoring or zone values, and the Season 02 rows are at the end. "Official" means developer-published; "PR" means player-reported.

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
| Season 02 date: 15 Oct 2026 | Teaser 22 Sep 2026; released 15 Oct | Official [9][16] |
| Team-switch lock: 15 min, when a team is more than 10 points ahead | 0.2.0, 14 Oct 2026 | Official [14] |
| Losing-team vendor discount: 20% at 40+ points behind second | 0.2.0, 14 Oct 2026 | Official [14] |
| Assistance ping timer: 60 s (was 20 s) | 0.2.0, 14 Oct 2026 | Official [14] |

## Match lifecycle

| Stage | What is known | Class |
|-------|---------------|-------|
| 0. Seeding (0.2.0) | Players who populate an empty server earn rewards and a vendor discount once the match begins; pre-match entertainment is available before the match [14] | Official |
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

The developer designed three teams so that the zone is a three-way contest, with a lore split: Lonestar (Western paramilitary), Valkyra (Soviet-revival) and Manticore (Persian shadow army) [2]. Because points go to the team with the most players, a team can lead while outnumbered by the other two combined; this follows from the rule as stated and is an inference (Assessment: confidence Medium; basis: the scoring rule at [2]). No official source states how players are assigned to teams or whether teams are balanced to equal size. The 0.11 post listed "Team Switching Controls" and "AFK kicking during seeding disabling" as upcoming features on 12 Sep 2026 [6]; team switching restrictions shipped in 0.2.0 (next section), while the notes do not mention AFK-kick changes [14]. A player-reported guide gives about 33 players per team [13].

## Team switching restrictions (0.2.0)

Aim stated in the notes: stop late switching from deciding matches. Trigger: a team more than 10 points ahead. Effects: no switching teams again for 15 minutes after joining one; the map stays obscured until the first arrival at the Control Zone after a switch or a mid-match join; the spawn vehicle is unusable until then [14]. Whether it is a server setting is not stated.

## Team-kill Forgive / Punish (0.2.0)

Victim-driven vote after a teammate kills you. Punish accumulates marks leading to kicks and escalating bans; Forgive removes a potential mark; respawning and leaving the safe zone without voting forgives automatically [14]. Mark counts, ban lengths and any difference between Official and Community servers are not stated.

## Squads, Squad Intent and prompts (0.2.0)

Squad leaders choose a team-visible intent from a pre-defined list (the entries are not listed in the notes); it shows on the squad list before joining. Squad invites and other timed prompts now queue [14]. Squad size remains unlimited per the 18 Feb 2026 post [2]; the notes do not change it.

## Server seeding, pre-match entertainment and the losing-team discount (0.2.0)

Seeding: rewards and a vendor discount for players who join and populate empty servers, granted once the match begins. Pre-match entertainment: guns with targets, a football and a hidden radio in each spawn [14]. Separately, the Lonestar experiment adds a Season 2 win bonus and teamplay multipliers for Lonestar, and a 20% vendor discount for any team at least 40 points behind second place [14]. The notes give no sizes for the bonuses, seeding rewards or seeding discount; cash and XP figures are owned by cash-rewards-and-costs and vendor prices by price-tables-season-1.

## Ping limits and Wager Vendor (pointers)

Region-based ping limits and server-browser ping filters arrived in 0.2.0; see server-hosting-and-browser [14]. The Wager Vendor is not available at launch and opens later in Season 2 [14]; see gameplay-modes-foundation.

## Spawn, respawn and deploy

- Official: the 0.1.2 Deploy flow is a pre-match server selection screen aimed at steering players to Infantry Mode and Low-Level servers [7].
- Official: revive validity checks are server authoritative from 0.1.2 [7].
- Player-reported: loadout purchase at the Equipment Vendor, then spawn via the deployment board [12].
- Player-reported: there is no squad spawning; an M113 APC unlocks once any faction reaches 20 points, the deployment computer can teleport you to an allied APC with a 10-minute personal cooldown, and destroying an APC's satellite dish disables its spawn function [13].
- Player-reported: reviving is cheaper than respawning [13]. Revive duration is not given [12].
- Official (0.2.0): all three Bakurani team spawns were moved and rebuilt with purpose-built routes to the zone [14]. Map detail is owned by maps-environment-foundation.
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
| 2026-10-14 | Season 02 patch notes: team-switch restrictions, Forgive/Punish, Squad Intent UI and prompt queueing, server seeding and pre-match entertainment, Lonestar experiment, 20% losing-team discount, ping timer 20 s to 60 s, parachute and controller changes, Bakurani spawns moved, Wager Vendor announced for later | Official [14] |
| 2026-10-15 | Update 0.2.0 released, servers back online | Official [16] |
| after 2026-10-15 | No official post in the 2026-10-30 snapshot; later hotfixes neither confirmed nor excluded | Official [16] |

No official post read changed the 100-point threshold, the Hot Zone multipliers or zone size during Season 01. Team-switching controls shipped in 0.2.0 [14]; tiered priority queues and improved warmup were pipeline features on 14 Sep 2026 and the 0.2.0 notes do not mention them [6][14]. The notes also do not mention a change to the 100-point threshold, Hot Zone multipliers or zone size.

# Admin & Technical Notes

Community servers can run modifiers; Official servers had no modified modes at 14 Sep 2026 [6]. Infantry Mode and Low-Level servers are named in the 0.1.2 Deploy flow, but the rules they change are not defined in the official post [7]. Whether the 100-point threshold or tick is a server setting is not documented in sources read here.

# Risks & Caveats

- The 0.2.0 rules rest on one official post (the patch notes); later hotfixes would not appear until the snapshot is refreshed [14].
- Bonus sizes (Lonestar, seeding) are unstated, so the experiment's effect cannot be quantified from official text.
- The 30-second tick, tower codes and APC spawn rules come from player-reported guides and the developer has not confirmed them [12][13].
- The scoring text says "most players", which leaves ties and margin undefined.
- The Tactical Depth post is largely a video wrapper; its substance is not recoverable from text.

# Open Questions

- Scoring tick and points per tick: not official; resolve from an official post or a timed in-game test.
- Respawn timer, spawn distribution, spawn protection: unpublished.
- Forgive/Punish mark thresholds and ban lengths, Squad Intent entries, Lonestar bonus sizes, seeding reward and discount sizes: not stated in the 0.2.0 notes.
- Whether the player-reported tick, tower codes and APC spawn rules changed in 0.2.0: the notes do not mention them.
- Team assignment and balancing rules: unpublished (restrictions on switching are official from 0.2.0).
- Official confirmation of the tower and master-code mechanic, the drill rig, and the M113 APC spawn.
- Conflict with gameplay-modes-foundation: it says Official servers have no filters, while the 0.1.2 post says Advanced Filters were added back to the Official list [7]. Voice chat wording is no longer a conflict: the live store page (capture 2026-10-08) uses both "proximity voice chat" and "local voice chat" [1][2].
- gameplay-modes-foundation treats the 2 Oct hotfix content as inconsistent in press; the official posts show two separate hotfixes, a security and stability one and a balance one [8][11].
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
- [14] **Bulkhead Studios** — *WARDOGS | Season 02 Patch Notes* (Steam announcement, posted 14 Oct 2026; includes an in-post update to logistics values). https://store.steampowered.com/news/app/1867240/view/1846651706674560. Accessed 2026-10-30.
- [15] **Bulkhead Studios** — *WARDOGS Season 02 Preview* (Steam announcement, 9 Oct 2026). https://store.steampowered.com/news/app/1867240/view/1846018067933823. Accessed 2026-10-30.
- [16] **Bulkhead Studios** — *WARDOGS | SEASON 02 IS NOW LIVE* (Steam announcement, 15 Oct 2026). https://store.steampowered.com/news/app/1867240/view/1846651706677015. Accessed 2026-10-30.

**Press & Secondary**

None cited; official posts were preferred.

**Player-Reported Evidence**

- [12] **allthings.how** — *WARDOGS Hot Zone: how double presence and double cash work* (player guide). https://allthings.how/wardogs-hot-zone-how-double-presence-and-double-cash-work/. Accessed 2026-10-08.
- [13] **allthings.how** — *WARDOGS beginner's guide: how the zone and cash systems work* (player guide). https://allthings.how/wardogs-beginner-s-guide-how-the-zone-and-cash-systems-work/. Accessed 2026-10-08.

# Further Reading

Snapshots of official posts are under `snapshots/2026-10-08/steam-news/` and, for Season 02, `snapshots/2026-10-30/steam-news/`.

# Related Documents

- gameplay-modes-foundation
- progression-and-role-tracks
- maps-environment-foundation
- launch-maps-reference
- cash-rewards-and-costs
- server-hosting-and-browser (ping limits)
- price-tables-season-1 (vendor prices)

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft: pre-Season-02 baseline. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after independent re-verification of validate, markdownlint, links (0 dead) and Steam post ids. Pre-Season-02 baseline. | Standing mandate (auto-approve on green QA) |
| 1.0.1 | 2026-10-08 | Orchestrator | Voice-chat wording reconciled with the live store-page capture (page uses both phrases). | Standing mandate (auto-approve on green QA) |
| 1.1.0 | 2026-10-30 | Research Pipeline (virtual agent) | Revised for Update 0.2.0 (Season 02, live 15 Oct 2026) from the 14 Oct patch notes, 9 Oct preview and 15 Oct release post: team-switch restrictions, Forgive/Punish, Squad Intent UI and prompt queueing, server seeding and pre-match entertainment, Lonestar experiment and 20% losing-team discount, ping timer 60 s, parachute and controller summaries, Bakurani spawns, Wager Vendor pointer; Season 01 baseline kept as dated history; no official posts after 2026-10-15 in snapshot | — |
