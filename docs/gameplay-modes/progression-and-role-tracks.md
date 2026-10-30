---
id: progression-and-role-tracks
title: "Progression & Role Tracks"
version: 1.1.0
status: frozen
confidence: Medium
category: Gameplay & Modes
topic: "XP curves, role tracks, WARDOG level, season resets"
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
  - progression-unlock-tables
  - season-reset-and-currencies
  - combat-loadouts-foundation
  - economy-foundation
tags:
  - progression
  - xp
  - role-tracks
  - baseline
  - season-01
  - season-02
  - update-0-2-0
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | progression-and-role-tracks |
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

This document explains how WARDOGS progression works: role tracks, the role-track XP curve, XP events, level caps, the account-wide WARDOG level, the exploit policy and what the developer has said about seasons. It is revised for Season 02 (Update 0.2.0), using the full official patch notes (14 Oct 2026) [10] and the release post (15 Oct 2026) [11]. Full per-item unlock levels and costs are in progression-unlock-tables.

The 0.2.0 notes replace the Season 1 XP curve: reaching level 20 now takes 111,500 total XP instead of 250,000 (55 percent quicker) and level 50 takes 1,150,000 instead of 1,500,000 (23 percent quicker); the developer says level 20 now takes less than half the playtime it did in Season 1 [10]. The notes name seven track headings: WARDOG, Assault, Medic, Recon, Support, Pilot and Driver [10]. The Season 1 changelog (9 Sep 2026) used Career, Medic, Recon, Support, Driver and Pilot [1]. The notes also move some XP between roles: buildable destruction, IEDs and C4 now give Assault XP, artillery gives Driver XP, and repair XP goes to Driver or Pilot [10].

Confidence is Medium. The XP table, event values and reassignments rest on the official notes (High on their own). The level cap, the WARDOG level formula and the seasonal wipe rest on player-reported or press sources, or are not mentioned in the notes, which holds the document at Medium [8][9][10].

# Key Takeaways

- Season 02 (Update 0.2.0, notes 2026-10-14, live 2026-10-15) lowered the total XP needed at every published level from 10 to 50: level 10 35,000 to 25,000; level 20 250,000 to 111,500; level 50 1,500,000 to 1,150,000 [10][11].
- Season 1 history: the 9 Sep 2026 changelog had slowed the curve (level 20 from 111,500 to 250,000; level 50 from 838,000 to 1,000,000) [1]. The 0.2.0 notes print different "before" values for levels 25 to 50 (for example level 50: 1,500,000); the discrepancy is unexplained [1][10].
- Seven track headings appear in the 0.2.0 notes: WARDOG, Assault, Medic, Recon, Support, Pilot, Driver [10]. "Career" from the Season 1 changelog is not used in the notes; Assessment: WARDOG matches Career by level (Deagle 85, Sport Parachute 35), confidence Medium [1][10].
- 0.2.0 role-XP reassignment: destroying a buildable, IED and C4 now give Assault XP (was Support); artillery gives Driver XP (was Support); repair XP goes to Driver or Pilot by vehicle [10].
- Season 1 developer statement: "Each season we will have a different XP curve with different item orders" [1].
- The 0.2.0 notes do not mention a Season 02 progression wipe, automatic cash-to-Gold-Bar conversion or any level cap; the unconfirmed press claim of a wipe stays in Open Questions [8][10].
- Patch 0.1.2 (30 Sep 2026) fixed several cash and XP exploits and ended first-offence leniency; 0.2.0 adds more exploit fixes (spotting, supply crates, FOB assist) [2][10].
- Two Season 1 XP event values (air vehicle kill 250 XP; low-value crate sale 1 XP) are not mentioned in the 0.2.0 notes (not changed in the notes) [1][10].

# Scope

Covers role tracks and naming, XP sources and the Season 02 and Season 1 curves, level caps, the WARDOG level, the 0.1.2 and 0.11 XP-exploit policy and what is known about seasons and XP. Game version: Update 0.2.0 as of the 2026-10-30 snapshot; no official post after 2026-10-15 is in that snapshot. Excluded: full unlock tables (see progression-unlock-tables), currency conversion and Gold Bar rates (see season-reset-and-currencies), weapon detail (see combat-loadouts-foundation), cash and XP reward amounts (see cash-rewards-and-costs) and prices (see economy-foundation).

# Definitions

- **Role track**: a per-role XP and level track that gates which items can be bought. The 0.2.0 notes use the headings WARDOG, Assault, Medic, Recon, Support, Pilot and Driver [10]; the Season 1 changelog used Career, Medic, Recon, Support, Driver and Pilot [1].
- **Total XP required**: the 0.2.0 notes' name for the XP needed to reach a level [10]. The Season 1 changelog called these XP bands [1].
- **WARDOG level**: an account-wide level, described by a player-reported guide as the sum of the six track levels [9]. Not defined in any official post I read. The 0.2.0 notes also use "WARDOG" for a track heading [10].
- **Season**: a period after which, per press, cash and level progression reset; the developer says each season has its own XP curve [1][8]. Season 02 is the first season after Season 1.

# Current State

- Release: Update 0.2.0 went live on 2026-10-15 and servers were back online [11]; the patch notes were posted 2026-10-14 [10].
- XP curve: Season 02 total XP required is 25,000 (level 10), 54,750 (15), 111,500 (20), 206,600 (25), 318,200 (30), 525,000 (35), 712,500 (40), 920,850 (45) and 1,150,000 (50) [10]. Levels not listed have no published value.
- Developer intent: "Levels 10 to 20 were a slow grind, and many players stalled out before unlocking the gear that defines each role"; level 20 now takes less than half the Season 1 playtime [10].
- Role tracks: seven headings in the notes, with item unlocks, additions and moves between tracks listed in progression-unlock-tables [10].
- Role XP: destroying a buildable, IED and C4 give Assault XP; artillery gives Driver XP; repairs feed Driver or Pilot by vehicle [10].
- The developer has said it will never monetise in-game cash or Gold Bars, which "must be earned through play" (pre-order post, 11 Aug 2026) [5].
- Exploit policy: cash and XP reset to 0 and timed bans for cash exploits, permanent bans for XP farming (patch 0.11 post, 12 Sep 2026) [4]; reaffirmed and tightened in 0.1.2 (30 Sep 2026) [2]. The 0.2.0 notes add exploit fixes listed below [10].
- Season 02 wipe: not mentioned in the 0.2.0 notes or the release post [10][11].

# Detail

## Role tracks and the 4-versus-6 and naming conflicts

| Question | Official text | Other sources | Resolution |
|----------|---------------|---------------|------------|
| How many tracks? | Season 1 changelog (9 Sep 2026): six names, Career, Medic, Recon, Support, Driver, Pilot [1]. Update 0.2.0 notes (14 Oct 2026): seven headings, WARDOG, Assault, Medic, Recon, Support, Pilot, Driver [10] | Six tracks, four levelled by weapons and tools, Driver and Pilot levelled by vehicles (player-reported) [9] | The count depends on date and on whether Career and WARDOG are one track. As of 0.2.0 the notes show seven headings. Whether Assault is a new seventh track is not stated. |
| What is the first track called? | Season 1: "Career" [1]. 0.2.0: "WARDOG Progression Track" [10] | "Assault", levelled from assault rifles (player-reported) [9] | Assessment: WARDOG is Career renamed, because the levels match (Deagle 85, Sport Parachute 35, 556mm AP 83 before the 0.2.0 change), confidence Medium [1][10]. The notes never say so. |
| Is Assault an official track? | The 0.2.0 notes have an "Assault Progression Track" heading and say "Assault is now the role for attacking enemy bases" [10] | Guides use "Assault" for the rifle track [9] | Yes, as of 0.2.0. The Season 1 changelog did not list it [1]. |
| Does an official post call the tracks "roles"? | The Season 1 post says "role track"; the 0.2.0 notes say "Role Track XP" and "Role Track Unlocks" [1][10] | Guides say "roles" [9] | Use "role track". |

Evidence that WARDOG is a full track and not a catch-all: the 0.2.0 notes list unlocks such as pallets, pistols, ammo types, armour and the Gold Market under it [10]. Items keep moving between tracks: in Season 1, Music Tape H from Pilot to Driver and Heavy Tank from Career to Driver [1]; in 0.2.0, the SPH-2 from WARDOG level 90 to Driver level 31, the C4 charge from Support to Assault, and many scopes and foregrips between WARDOG, Assault, Medic and Support [10].

## XP sources named in official text

| Source | Value | Source of value |
|--------|-------|-----------------|
| Player kill using an air vehicle | 250 XP (was 300), Season 1; not mentioned in the 0.2.0 notes | [1][10] |
| Supply crate item sold under $75 | 1 XP (was 25), Season 1; not mentioned in the 0.2.0 notes | [1][10] |
| FOB hacking (teammates in radius) | $1,000 / 250 XP; the hacker still gets $2,500 / 250 XP (0.2.0) | [10] |
| Destroying a FOB | bonus up to +$7,500 / +250 XP by supplies held, maxed at 25,000 supplies (0.2.0) | [10] |
| Capturing a hostile drill tower | $750 to $1,500 and XP 250 to 300 (0.2.0) | [10] |
| Logistics delivery streaks | e.g. crates +$100 / +50 XP per crate in a row up to 10 (0.2.0; updated values include the zone multiplier) | [10] |
| Revives | Validity now server authoritative (value not published) | [2] |
| Destroying buildables | Reward scales with build progress (0.1.2); in 0.2.0 the XP goes to the Assault track and cash matches the build supply cost with XP about 25 percent of cash | [2][10] |
| Vehicle fly-through | Rewards capped (cap not published) | [2] |
| FOB pallet deposit outside the zone | Reduced reward (value not published) | [2] |

0.2.0 role-XP reassignment: destroying a buildable, IED and C4 now give Assault XP instead of Support; artillery gives Driver XP instead of Support; repair XP goes into Driver or Pilot depending on the vehicle repaired instead of a flat Support amount [10]. Amounts for all reward events are owned by cash-rewards-and-costs.

Other XP sources (kills, objectives) are described only in guides; the guide says Driver XP comes from "kills and objectives from a ground vehicle" and Pilot XP from flying helicopters (player-reported) [9].

## Season 02 role-track XP curve (Update 0.2.0)

The notes list "Total XP Required" per level, with the old value before the arrow [10].

| Level | Old (per 0.2.0 notes) | Season 02 | Change stated |
|-------|-----------------------|-----------|---------------|
| 10 | 35,000 | 25,000 | 29% quicker |
| 15 | 110,000 | 54,750 | 50% quicker |
| 20 | 250,000 | 111,500 | 55% quicker |
| 25 | 365,000 | 206,600 | 43% quicker |
| 30 | 500,000 | 318,200 | 36% quicker |
| 35 | 750,000 | 525,000 | 30% quicker |
| 40 | 975,000 | 712,500 | 27% quicker |
| 45 | 1,225,000 | 920,850 | 25% quicker |
| 50 | 1,500,000 | 1,150,000 | 23% quicker |

Source: [10]. Conflicts and limits:

- For levels 25 to 50 the "old" value in the 0.2.0 notes (365,000 to 1,500,000) is higher than the value in the Season 1 changelog (325,000 to 1,000,000) in the history table below [1][10]. The notes do not explain the difference. Season 02 values are taken from the notes only.
- The Season 02 totals at levels 10, 15 and 20 equal the pre-Season-1 ("beta") values printed in the Season 1 changelog (25,000 / 54,750 / 111,500) [1][10]. The notes do not comment.
- No values are published for levels below 10, between listed levels or above 50; the notes do not say whether a figure is cumulative, though "Total XP Required" reads as cumulative (Assessment: Medium confidence) [10].

## Season 1 curve versus beta (history, superseded by 0.2.0)

The changelog says the earlier balancing "was designed specifically for weekend long beta tests" and that the new values are "in-line with where we believe they should be" [1]. The "old" column below is therefore the beta-era curve, as stated by the developer.

| Level | Beta XP | Season 1 XP | Change as published | Derived: Season 1 XP added since previous band |
|-------|---------|-------------|---------------------|-----------------------------------------------|
| Below 6 | unchanged | unchanged | unchanged | n/a |
| 6 | 8,750 | 9,250 | 5.7% slower | n/a |
| 10 | 25,000 | 35,000 | 40.0% slower | 25,750 |
| 15 | 54,750 | 110,000 | 100.9% slower | 75,000 |
| 20 | 111,500 | 250,000 | 124.2% slower | 140,000 |
| 25 | 192,000 | 325,000 | 69.3% slower | 75,000 |
| 30 | 293,750 | 400,000 | 36.2% slower | 75,000 |
| 35 | 416,500 | 500,000 | 20.0% slower | 100,000 |
| 40 | 551,250 | 650,000 | 17.9% slower | 150,000 |
| 45 | 689,500 | 800,000 | 16.0% slower | 150,000 |
| 50 | 838,000 | 1,000,000 | 19.3% slower | 200,000 |

Source for the first four data columns: [1]. The last column is my subtraction of adjacent Season 1 values and is not in any source. Assessment: the headline says the slowdown is "around 10 to 20" with flattening from 35 onward, yet the published bands show every band to level 50 slower than beta by at least 16 percent; confidence High that this is what the table says, Low on what the developer meant by "flatten" (the post does not elaborate) [1]. The same section describes "a larger increase at level 10" than the 5.7 percent at level 6 [1].

Intermediate levels (for example 7 to 9, 11 to 14) have no published XP value; the post gives bands only [1]. Whether the figures are cumulative per track or per level is not spelled out; the XP-to-reach wording ("Level 10: 25,000 to 35,000") reads as cumulative requirement (Assessment: Medium confidence, based on the figures rising monotonically) [1].

## Level caps and WARDOG level

- Official: no level cap is stated. The highest levels named in the changelog are Career level 90 (Artillery Tank) and Career level 85 (Deagle), so a cap of at least 90 is implied (Assessment: High that the cap is 90 or more, from [1]).
- Player-reported: each track caps at level 100, and the account-wide WARDOG Level is "the sum of all six tracks" capped at 600 [9]. The arithmetic (6 x 100 = 600) is consistent with a cap of 100, but neither number is in an official post I read.
- Official XP stops at level 50 (Season 1: 1,000,000 XP [1]; Season 02: 1,150,000 XP [10]); XP needed for levels 51 to 100 is not published. The 0.2.0 notes do not state a cap, and the highest level named in them is WARDOG level 90 (the SPH-2, before its move to Driver) [10].

## How Season 1 changed progression versus beta

| Area | Beta | Season 1 | Source |
|------|------|----------|--------|
| XP design target | Tuned for weekend-long tests | Tuned for long-term play; per-season curves | [1] |
| XP curve | See table above | Slowed at every published band from level 6 | [1] |
| Air vehicle kill XP | 300 | 250 | [1] |
| Low-value supply crate sale XP | 25 | 1 | [1] |
| Supply crate purchase curve | 25 to 250 | 1 to 200 ("rescaled") | [1] |
| Items per track | Many items at earlier levels | Many moved (see below) | [1] |

Baseline of unlock-level moves in the Season 1 changelog (full tables belong to progression-unlock-tables) [1]:

| Track | Item | Old level | Season 1 level |
|-------|------|-----------|----------------|
| Career | Sports Parachute | 36 | 35 |
| Career | Large Backpack | 56 | 55 |
| Career | 762x54mm AP | 83 | 82 |
| Career | 556mm AP | 85 | 83 |
| Career | Deagle | 90 | 85 |
| Career | Artillery Tank | 55 | 90 |
| Medic | PP-19 50 round drum magazine | 33 | 29 |
| Support | Large Hammer | 7 | 8 |
| Driver | URAL | 4 | 3 |
| Driver | Kodiak Assault | 8 | 6 |
| Driver | Dune Buggy | 10 | 8 |
| Driver | Kodiak Flatbed | 2 | 10 |
| Driver | Large Supply Crate | 20 | 16 |
| Driver | URAL Covered | 30 | 18 |
| Driver | Music Tape H | Pilot 28 | Driver 23 |
| Driver | URAL Attack | 40 | 25 |
| Driver | Humvee with minigun | 35 | 30 |
| Driver | Heavy Tank | Career 35 | Driver 35 |

## 0.1.2 XP and cash exploit fixes (30 Sep 2026)

All from the official 0.1.2 post [2]:

1. Revive action validity checks are fully server authoritative.
2. Vehicle fly-through exploit fixed; rewards capped.
3. Rewards for destroying buildables scale with build progress.
4. Depositing pallets into a FOB outside the zone awards reduced rewards.
5. Policy: anyone caught abusing cash and XP exploits or Real Money Trading "has had their cash and progression reset and risks being permanently banned"; first-time leniency is over; repeatable unintended exploits can bring a permanent ban without warning [2].

The earlier patch 0.11 post (12 Sep 2026) set the tiers: cash exploits get a timed ban and a cash and XP reset to 0; tutorials on exploits count as advertising cheats and get a permanent ban; XP farming "will result in the most serious bans" and joining a known XP-farming server for more than a few minutes risks a permanent ban [4]. The post gives no figure for the reduced or capped rewards [2].

## What Season 02 says about XP and resets

The Season 02 teaser (22 Sep 2026) gave only the date 15 October 2026 [3]. The outcome, as published:

- Official: the 0.2.0 notes (14 Oct 2026) contain a "Progression Changes" section with the Role Track XP table and unlock changes [10]. The release post (15 Oct 2026) says only that Update 0.2.0 is released and servers are back online [11]. Neither mentions a progression wipe, a cash-to-Gold-Bar conversion or a change to the account level; the notes are silent, which is not a statement that none occurred.
- Official, indirect: "Each season we will have a different XP curve with different item orders" (Season 1 changelog) [1]; Season 02 was described as "a larger content update, with new map conditions, equipment, balance reworks and additional features" [2].
- Official, Season 02 only: Lonestar faction cash and XP win bonus and teamplay cash and XP multipliers, "Season 2 only", plus a 20 percent vendor discount for a team at least 40 points behind second place [10]. The bonus amounts are not stated.
- Press: Vice (23 Sep 2026) said players "should expect a progression wipe", that cash and level progression reset at the end of a season, that leftover cash converts to Gold Bars and that Gold Bars and cosmetics persist; the unlock order and conversion rate were not yet shared [8]. The official 0.2.0 posts neither confirm nor deny this.
- Player-reported: a guide says WARDOG Level and cash "drop to zero" when a major update cycle ends [9].

## Exploit fixes added in 0.2.0

Spotting added and removed rewards scale with build progress; destroying a buildable pays by how built it is; selling from a supply crate has diminishing returns per buyer until you break even with no profit or XP; selling to an enemy player gives no cash or XP; destroying an empty enemy crate pays half cash and half XP; supply crate rewards scale with the supplies inside; FOB Supplied Assist is split between assisting players [10]. Reward amounts: see cash-rewards-and-costs.

## Season 02 baseline values (Update 0.2.0, 2026-10-15)

| Value | As-of version | Source |
|-------|---------------|--------|
| XP to reach level 10 / 15 / 20 / 25 / 30: 25,000 / 54,750 / 111,500 / 206,600 / 318,200 | 0.2.0 | [10] |
| XP to reach level 35 / 40 / 45 / 50: 525,000 / 712,500 / 920,850 / 1,150,000 | 0.2.0 | [10] |
| Track headings: WARDOG, Assault, Medic, Recon, Support, Pilot, Driver (7) | 0.2.0 notes | [10] |
| Destroying buildable, IED, C4: Assault XP; artillery: Driver XP | 0.2.0 | [10] |
| Official level cap | not published | [10] |
| Season 02 release | 2026-10-15 | [11] |

## Baseline values (Season 1 / patch 0.1.2, 8 Oct 2026; history)

| Value | As-of version | Source |
|-------|---------------|--------|
| Role tracks: Career, Medic, Recon, Support, Driver, Pilot (6) | Season 1 changelog, 9 Sep 2026 | [1] |
| XP to reach level 6: 9,250 (beta 8,750) | Season 1 | [1] |
| XP to reach level 10: 35,000 (beta 25,000) | Season 1 | [1] |
| XP to reach level 15: 110,000 (beta 54,750) | Season 1 | [1] |
| XP to reach level 20: 250,000 (beta 111,500) | Season 1 | [1] |
| XP to reach level 25: 325,000 (beta 192,000) | Season 1 | [1] |
| XP to reach level 30: 400,000 (beta 293,750) | Season 1 | [1] |
| XP to reach level 35: 500,000 (beta 416,500) | Season 1 | [1] |
| XP to reach level 40: 650,000 (beta 551,250) | Season 1 | [1] |
| XP to reach level 45: 800,000 (beta 689,500) | Season 1 | [1] |
| XP to reach level 50: 1,000,000 (beta 838,000) | Season 1 | [1] |
| Levels below 6 | unchanged from beta | [1] |
| Median-player target: about level 20 at 20 to 25 hours (0.2.0 notes: level 20 now takes less than half the Season 1 playtime) | Season 1 | [1][10] |
| Air vehicle player kill: 250 XP | Season 1 | [1] |
| Supply crate item sold under $75: 1 XP | Season 1 | [1] |
| Supply crate purchase curve: 1 to 200 | Season 1 | [1] |
| Artillery Tank: Career level 90 | Season 1 | [1] |
| Heavy Tank: Driver level 35 | Season 1 | [1] |
| Official level cap | not published | [1][2] |
| Level cap per track: 100 (player-reported) | Sep 2026 | [9] |
| WARDOG level cap: 600, sum of six tracks (player-reported) | Sep 2026 | [9] |
| Season 02 date: 15 Oct 2026 | teaser 22 Sep 2026 | [3] |
| Community-server end-of-match cash bonus: 5% for one week (apology) | 0.11, 12 Sep 2026 | [4] |

# Early Access Changes & Known Issues

| Date | Change | Source |
|------|--------|--------|
| 2026-04-07 | Developer says a Metagame for "earning, progressing and adding value to your account" will be built throughout Early Access | [6] |
| 2026-08-11 | Never monetise cash or Gold Bars; no monetisation in Early Access except the Supporter Edition | [5] |
| 2026-09-09/10 | Season 1 changelog: XP bands slowed, event XP changed, unlocks moved | [1][7] |
| 2026-09-12 | Patch 0.11 post: cash and XP reset for exploiters; XP-farming permanent bans; cash exploits fixed | [4] |
| 2026-09-22 | Season 02 teaser: date only | [3] |
| 2026-09-30 | Update 0.1.2: XP and cash exploit fixes, zero tolerance | [2] |
| 2026-10-14 | Season 02 patch notes: new Role Track XP table (levels 10 to 50), unlock changes for seven track headings, role-XP reassignment, more exploit fixes | [10] |
| 2026-10-15 | Update 0.2.0 released; servers back online | [11] |

Known issues: the 0.1.2 post gives no reduced-reward or cap numbers, so exploit-fix effects cannot be measured from official text [2]. No official post after 2026-10-15 is in the 2026-10-30 snapshot (none seen).

# Admin & Technical Notes

None found. The progression curve is published as a game-wide Season 1 value; no server setting for XP rate appears in the official posts read. Community servers earned a temporary 5 percent cash bonus in the week after 12 Sep 2026 [4]. Whether community servers award progression XP is not stated in the posts read (see Open Questions).

# Risks & Caveats

- The Season 02 curve is the current value as of 0.2.0; the developer says curves and item orders differ per season, so it may be replaced [1][10].
- The 0.2.0 "old" XP values for levels 25 to 50 conflict with the Season 1 changelog; see the curve section [1][10].
- The cap, WARDOG level and wipe details are player-reported or press-reported only, or not mentioned in the notes [8][9][10].
- Percentages in the Season 02 table are the developer's own figures; the Season 1 derived column is my subtraction.
- The name mapping Career to WARDOG is an inference from matching levels [1][10].

# Open Questions

- Career vs WARDOG vs Assault: is WARDOG the former Career track, and is Assault a seventh track? Resolve in game [1][9][10].
- XP table conflict: why do the 0.2.0 "old" totals for levels 25 to 50 differ from the Season 1 changelog [1][10]?
- Level cap: not in any official post read, including the 0.2.0 notes. Resolve in game [9][10].
- WARDOG level: no official definition; the sum-of-tracks formula and 600 cap are from one player-reported guide [9].
- Season 02 wipe: the 0.2.0 notes and the release post do not mention a reset of levels or the Gold Bar conversion; Vice cites earlier developer statements [8][10][11]. Unconfirmed; resolve by locating the original developer post.
- XP values for kills and objectives, and the exploit reward caps, are unpublished [2][10].
- Lonestar cash and XP win bonus and multipliers: amounts not stated [10].
- Whether community-server play earns progression XP, and the per-level XP between bands, are not stated.
- Official-versus-foundation difference: the foundation says "Assault or Career" and level 100 and 600 caps; the official text supports Career (Season 1) and WARDOG and Assault (0.2.0), with no cap [1][10].

# References

**Primary Sources**

- [1] **Bulkhead / Steam** — *Pre-Load Live & Season 1 Changelog* (posted 2026-09-09). https://store.steampowered.com/news/app/1867240/view/1843481262690549. Accessed 2026-10-08.
- [2] **Bulkhead / Steam** — *WARDOGS | Update 0.1.2 (Minor Patch)* (posted 2026-09-30). https://store.steampowered.com/news/app/1867240/view/1845383656376490. Accessed 2026-10-08.
- [3] **Bulkhead / Steam** — *WARDOGS | Season 02 Teaser* (posted 2026-09-22). https://store.steampowered.com/news/app/1867240/view/1844115010504839. Accessed 2026-10-08.
- [4] **Bulkhead / Steam** — *Scheduled Maintenance & Patch 0.11* (posted 2026-09-12). https://store.steampowered.com/news/app/1867240/view/1843481262698449. Accessed 2026-10-08.
- [5] **Bulkhead / Steam** — *Pre-Order Now* (posted 2026-08-11). https://store.steampowered.com/news/app/1867240/view/1840310314354505. Accessed 2026-10-08.
- [6] **Bulkhead / Steam** — *WARDOGS Early Access & Beyond* (posted 2026-04-07). https://store.steampowered.com/news/app/1867240/view/1828894815567544. Accessed 2026-10-08.

- [10] **Bulkhead / Steam** — *WARDOGS | Season 02 Patch Notes* (posted 2026-10-14, with an in-post logistics update). https://store.steampowered.com/news/app/1867240/view/1846651706674560. Accessed 2026-10-30.
- [11] **Bulkhead / Steam** — *WARDOGS | SEASON 02 IS NOW LIVE* (posted 2026-10-15). https://store.steampowered.com/news/app/1867240/view/1846651706677015. Accessed 2026-10-30.

**Press & Secondary**

- [7] **Gfinity Esports** — *WARDOGS Season 1 changelog: Early Access patch notes*. https://www.gfinityesports.com/article/wardogs-season-1-changelog-early-access-patch-notes. Accessed 2026-10-08.
- [8] **Vice** — *WARDOGS developer confirms Season 2 rain won't change mid-match* (23 Sep 2026). https://www.vice.com/en/article/wardogs-season-2-rain-progression-wipe/. Accessed 2026-10-08.

**Player-Reported Evidence**

- [9] **allthings.how** — *WARDOGS roles: how to pick the best class for you*. https://allthings.how/wardogs-roles-how-to-pick-the-best-class-for-you/. Accessed 2026-10-08.

# Further Reading

The Steam store page and the other posts in the 2026-10-08 and 2026-10-30 snapshots give background but are not cited here.

# Related Documents

- gameplay-modes-foundation
- progression-unlock-tables
- season-reset-and-currencies
- combat-loadouts-foundation
- economy-foundation
- cash-rewards-and-costs

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft; pre-Season 02 baseline from official Steam posts. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after independent re-verification of validate, markdownlint, links (0 dead) and Steam post ids. Pre-Season-02 baseline. | Standing mandate (auto-approve on green QA) |
| 1.1.0 | 2026-10-30 | Research Pipeline (virtual agent) | Revised for Season 02 / Update 0.2.0 from the official patch notes (14 Oct) and release post (15 Oct): new Role Track XP table (levels 10 to 50) with the old/new conflict flagged, seven track headings and Career/WARDOG/Assault naming, role-XP reassignment, 0.2.0 exploit fixes, Season 02 outcome replacing the teaser-era wipe discussion; Season 1 curve and baseline kept as history. | — |
