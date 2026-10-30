---
id: vehicle-roster-and-prices
title: "Vehicle Roster & Prices"
version: 1.1.0
status: frozen
confidence: Medium
category: Vehicles & Outposts
topic: "Land and air vehicles: roster, price, unlock level, crew, role"
market: Global
game_version: "Early Access Season 02, Update 0.2.0 (15 Oct 2026); official posts through 2026-10-15 (snapshot 2026-10-30)"
document_type: reference-data
created: 2026-10-08
updated: 2026-10-30
review_due: 2026-11-20
sources_verified: 2026-10-30
supersedes: null
related: [vehicles-outposts-foundation, air-and-counter-air, fob-and-base-building, price-tables-season-1, progression-unlock-tables, cash-rewards-and-costs]
tags: [vehicles, prices, unlock-levels, season-2, update-0-2-0, season-1-history]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | vehicle-roster-and-prices |
| Version | 1.1.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Vehicles & Outposts |
| Game version | Early Access Season 02, Update 0.2.0 (15 Oct 2026); official posts through 2026-10-15 (snapshot 2026-10-30) |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-30 |
| Review due | 2026-11-20 |

# Executive Summary

Update 0.2.0 (Season 02, released 15 Oct 2026) is the first official source that states vehicle spawn prices, and it states both the old and new value for most of them [1][2]. The Season 02 patch notes (posted 14 Oct 2026) add four vehicles (Wolf-110, Wolf-110 [M2 Browning], T-72B3 and Flakpanzer Gepard), raise the vendor price of 10 listed existing vehicles (Kodiak [M249], two armed Humvees, two Ural Defenders, the L2A6 and four helicopters; plain and unarmed variants are not listed), move several Driver and Pilot unlock levels and costs, make purchased-vehicle inventories private by default, and fix a list of vehicle bugs [1]. Season 1 (0.1.2) values are kept below as dated history.

The notes use the vehicle names "Ural Defender", "Ural Defender [M249]", "Humvee [Minigun]", "L2A6" and "SPH-2", while the Season 1 changelog used "URAL Covered", "URAL Attack", "Heavy Tank" and "Artillery Tank" [3]. Matching the two name sets is Inferred from identical levels and prices (see the reconciliation table). The notes still publish no crew or seat counts.

Document confidence is Medium: every number below comes from official posts, but the name mapping is inferred, several unlock levels are not stated, and crew sizes are unpublished. The 2026-10-30 snapshot contains no official post after 2026-10-15 [2], so later hotfixes are neither assumed nor excluded.

# Key Takeaways

- Four vehicles are new in 0.2.0: Wolf-110 (Driver 8, $50,000 unlock, $2,200 spawn), Wolf-110 [M2 Browning] (Driver 16, $125,000, $7,800), T-72B3 (Driver 20, $250,000, $16,000) and Flakpanzer Gepard (Driver 25, $300,000, $14,000) [1].
- Spawn-price rises in 0.2.0 include L2A6 $14,000 to $22,000, Havoc $18,000 to $28,000, Humvee [Minigun] $4,500 to $10,000 and Little Bird AH-6M [Miniguns] $7,000 to $12,000 [1].
- Little Bird AH-6M [Miniguns] now unlocks at Pilot 8 for $125,000 (was Pilot 4, $50,000); the Havoc unlock is $650,000 (was $500,000) [1].
- Inventories of purchased vehicles are private to the driver and their squad by default; free team-spawn vehicles stay open to everyone [1].
- The notes do not state crew or seat counts, and do not state every unlock level (for example the L2A6, Lakota and Havoc levels) [1].
- Full unlock-level detail belongs to progression-unlock-tables; the vendor price list belongs to price-tables-season-1.

# Scope

Covers land and air vehicles: names, track, unlock level, unlock price, spawn price, role and crew where known, as of Update 0.2.0 (15 Oct 2026), with Season 1 values kept as history. Excludes FOB and hammer costs (see fob-and-base-building), air combat and anti-air mechanics (see air-and-counter-air), the full price list (see price-tables-season-1), reward values (see cash-rewards-and-costs) and the full unlock tables and XP curve (see progression-unlock-tables). No naval vehicles appear in any retrieved source. Fighter jets are planned for the full release only [4].

# Definitions

- **Unlock price**: the one-time cost on a progression track, listed in the patch notes as "to unlock" (for example "Humvee $25k → $75k to unlock") [1].
- **Spawn price**: the per-purchase cost at the Vehicle Vendor, listed under "Vendor Price Changes" in the notes [1].
- **Track**: Driver (ground), Pilot (air), WARDOG, Assault, Medic, Recon and Support [1].
- **Official / guide-only / Inferred**: row labels used below. Inferred means the identity or value is deduced, not stated.

# Current State

As of Update 0.2.0 (15 Oct 2026):

- Season 02 went live on 15 Oct 2026 after a maintenance window of 08:00 to 09:30 UTC [1][2].
- Four new vehicles were added: Wolf-110 ("a fast, light wheeled transport"), Wolf-110 [M2 Browning] ("with a ring-mounted M2 Browning"), T-72B3 ("a main battle tank. Slower than the L2A6, but cheaper and slightly more fuel-efficient") and Flakpanzer Gepard ("Anti Air Vehicle") [1].
- The Driver track gives armed-vehicle players more options before the L2A6: Wolf-110 [M2 Browning] at level 16, T-72B3 at level 20 and Flakpanzer Gepard at level 25. The SPH-2 moved into the Driver track at level 31 from WARDOG level 90 [1].
- Purchased-vehicle inventories are private to the driver and their squad by default. A new setting opens them to everyone once the vehicle is fully unlocked. Inventories of vehicles that spawn free for each team stay open to everyone regardless of the setting [1].
- 30mm cannon ammo takes a 2x2 inventory slot (was 1x1); backpack stacks are capped at 50 and vehicle storage stacks stay at 200 [1].
- The calibre base-damage cuts (.308 -25%, 7.62x54mmR -20%, 7.62x39mm -19%, .50 Cal -16%) apply to vehicle weapons, named as the Little Bird AH-6M Minigun, Z20 Lakota Minigun and Humvee Minigun [1].
- Each player starts with $10,000 per the Steam page (verified 2026-10-08; the 2026-10-30 store snapshot is not re-read here for this value) [4].

# Detail

## Season 02 (0.2.0) roster

Names follow the 0.2.0 patch notes [1]. "Season 1 name" is the Inferred match to the Season 1 changelog [3]. Crew and seat counts are not published for any row. Where the notes give no value the cell says "not stated".

| Vehicle (0.2.0 name) | Season 1 name (Inferred) | Track and level | Unlock price | Spawn price | Source |
|----------------------|--------------------------|-----------------|--------------|-------------|--------|
| Wolf-110 (new) | none | Driver 8 | $50,000 | $2,200 | Official [1] |
| Wolf-110 [M2 Browning] (new) | none | Driver 16 | $125,000 | $7,800 | Official [1] |
| T-72B3 (new) | none | Driver 20 | $250,000 | $16,000 | Official [1] |
| Flakpanzer Gepard (new) | none | Driver 25 | $300,000 | $14,000 | Official [1] |
| Dune Buggy | Dune Buggy | Driver 9 | not stated (S1: $25,000 [3]) | not stated | Official [1] |
| Humvee | Humvee (guide-only in S1) | Driver 14 | $75,000 | not stated | Official [1] |
| Humvee [M249] | Humvee M249 (guide-only in S1) | Driver 24 | not stated | $8,500 | Official [1] |
| Humvee [Minigun] | Humvee with minigun | Driver level not stated (S1: 30 [3]) | not stated | $10,000 | Official [1] |
| Ural Defender | URAL Covered | Driver 15 | not stated | $7,200 | Official [1]; match Inferred |
| Ural Defender [M249] | URAL Attack | Driver 22 | $100,000 | $9,500 | Official [1]; match Inferred |
| Kodiak [M249] | Kodiak Assault | not stated (S1: Driver 6 [3]) | not stated | $6,750 | Official [1]; match Inferred |
| L2A6 | Heavy Tank | not stated (S1: Driver 35 [3]) | not stated | $22,000 | Official [1]; match Inferred |
| SPH-2 | Artillery Tank | Driver 31 | $350,000 | not stated | Official [1]; match Inferred |
| Little Bird AH-6M [Miniguns] | Little Bird with miniguns | Pilot 8 | $125,000 | $12,000 | Official [1] |
| Little Bird AH-6R [Rockets] | AH-6R (guide-only in S1) | not stated | not stated | $18,800 | Official [1] |
| Z20 Lakota [Miniguns] | Z20 Lakota | Pilot level not stated | $85,000 | $15,000 | Official [1] |
| Havoc | Havoc | Pilot level not stated | $650,000 | $28,000 | Official [1] |

The notes also name the plain Kodiak, Ural, Bobcat, MH-6 and Z20 Lakota (unarmed) in the vehicle-destroyed reward list but give no price, level or unlock for them [1]. Armed-variant reward values and the spotting changes belong to cash-rewards-and-costs.

## Season 1 to Season 02 value changes

"Season 1 (0.1.2)" values are the "old" figure quoted by the 0.2.0 notes; Season 1 launch changelog values are in the next section [1][3].

| Vehicle | Spawn price, S1 to 0.2.0 | Unlock level, S1 to 0.2.0 | Unlock price, S1 to 0.2.0 |
|---------|--------------------------|---------------------------|---------------------------|
| Dune Buggy | not stated | 8 to 9 | not stated |
| Humvee | not stated | 15 to 14 | $25,000 to $75,000 |
| Humvee [M249] | $3,750 to $8,500 | 20 to 24 | not stated |
| Humvee [Minigun] | $4,500 to $10,000 | not stated | not stated |
| Ural Defender | $6,000 to $7,200 | 18 to 15 | not stated |
| Ural Defender [M249] | $6,750 to $9,500 | 25 to 22 | $125,000 to $100,000 |
| Kodiak [M249] | $3,750 to $6,750 | not stated | not stated |
| L2A6 | $14,000 to $22,000 | not stated | not stated |
| SPH-2 | not stated | WARDOG 90 to Driver 31 | $500,000 to $350,000 |
| Little Bird AH-6M [Miniguns] | $7,000 to $12,000 | 4 to 8 | $50,000 to $125,000 |
| Little Bird AH-6R [Rockets] | $12,500 to $18,800 | not stated | not stated |
| Z20 Lakota [Miniguns] | $8,000 to $15,000 | not stated | $75,000 to $85,000 |
| Havoc | $18,000 to $28,000 | not stated | $500,000 to $650,000 |
| Large Crate | not stated | 16 to 17 | not stated |

Source for every row: Season 02 patch notes, 14 Oct 2026 (Update 0.2.0) [1]. The two music-tape lines in the Driver and Pilot tracks ("reshuffled between the Driver and Pilot tracks") are not vehicles and are left out [1]. Progression-unlock-tables owns the complete track lists.

## Season 1 baseline values (history)

Values from the Season 1 launch changelog (9 Sep 2026, effective 10 Sep 2026) and updates through 2 Oct 2026. Where 0.2.0 changed a value, the current figure is in the tables above [1][3].

| Value | As-of version | Source |
|-------|---------------|--------|
| Dune Buggy: Driver level 8, unlock $25,000 (was level 10, $35,000) | S1 changelog, 10 Sep 2026 | [3] |
| URAL: Driver level 3, unlock $35,000 (was level 4, $50,000) | S1 changelog | [3] |
| URAL Covered: Driver level 18 (was 30) | S1 changelog | [3] |
| URAL Attack: Driver level 25 (was 40) | S1 changelog | [3] |
| Kodiak Assault: Driver level 6 (was 8) | S1 changelog | [3] |
| Kodiak Flatbed: Driver level 10, unlock $35,000 (was level 2, $15,000) | S1 changelog | [3] |
| Humvee with minigun: Driver level 30 (was 35) | S1 changelog | [3] |
| Heavy Tank: Driver level 35 (was Career level 35) | S1 changelog | [3] |
| Artillery Tank: Career level 90, unlock $500,000 (was level 55, $400,000) | S1 changelog | [3] |
| Little Bird with miniguns: Pilot, unlock $50,000 (was $25,000); level not stated | S1 changelog | [3] |
| Z20 Lakota: Pilot, unlock $35,000 (was $50,000); level not stated | S1 changelog | [3] |
| Large Supply Crate: Driver level 16 (was 20) | S1 changelog | [3] |
| CIWS time to destroy a Havoc: about 6 s (was about 12 s) | Hotfix 2 Oct 2026 | [5] |

Season 1 spawn prices came only from two player guides before 0.2.0 [8][9]. The "old" prices quoted in the 0.2.0 notes (for example Kodiak [M249] $3,750, Humvee [Minigun] $4,500, Havoc $18,000, Z20 Lakota [Miniguns] $8,000) match those guides, so the guides' Season 1 spawn prices are now corroborated by an official source for those rows [1][8][9].

Two Season 1 unlock figures conflict with the 0.2.0 "old" values and are left as recorded: the Season 1 changelog gave Z20 Lakota unlock "$35,000" [3], while the 0.2.0 notes say "$75k → $85k" [1]; and the Little Bird unlock was $50,000 in both [1][3]. The changelog's $35,000 may have been a different item or a later change; no source says which (see Open Questions).

## Reconciliation of names and guide-only rows

| Item | Evidence | Resolution |
|------|----------|------------|
| URAL Covered = Ural Defender | Both Driver 18 in S1; notes say "Ural Defender LVL 18 → LVL 15" [1][3] | Inferred match by level |
| URAL Attack = Ural Defender [M249] | Both Driver 25 in S1; notes "LVL 25 → LVL 22" [1][3] | Inferred match by level |
| Heavy Tank = L2A6 | Notes say T-72B3 is "slower than the L2A6" and name the L2A6 at $14,000 to $22,000 [1]; S1 guide linked L2A6 to about $14,000 [8] | Inferred; no post equates them |
| Artillery Tank = SPH-2 | S1 Career 90, $500,000 [3]; notes "SPH-2 ... moved from WARDOG LVL 90", "$500k → $350k" [1] | Inferred by level and price |
| Kodiak Assault = Kodiak [M249] | S1 spawn guide $3,750 [8][9]; notes Kodiak [M249] $3,750 to $6,750 [1] | Inferred |
| Kodiak Flatbed = Kodiak (Pickup) | Notes list "Pickup" as a Kodiak variant in destroyed rewards [1] | Inferred |
| Flakpanzer Gepard | S1: guide-only, "Wardog track" [9] | Now official: Driver 25 [1]; the guide's "Wardog" track was wrong |
| AH-6M, AH-6R | S1: guide-only [9] | Now official names with prices [1] |
| Bobcat (quad) | S1 guide: about $500 [8][9] | Named in the notes (destroyed reward $250 to $100) but no price stated [1] |
| Team armoured spawn vehicle | S1 guide only [9] | Notes refer to a "Spawn Vehicle" (SV) and a "spawn vehicle" restriction, no price [1] |

## Role notes (official, 0.2.0)

- Tracked vehicles feel weightier, "less floaty when in the air, less bouncy on landing" [1].
- Humvee handling is reworked: less stiff over terrain, slower build to top speed, better at climbing terrain [1].
- Dune Buggy brakes are less effective, slightly increasing skid and drift [1].
- Explosives and placeables can no longer be used from enclosed vehicle seats [1].
- Heavy and Artillery top machine turrets now use the assault rifle and LMG hit-location values on infantry, instead of the helicopter-cannon values [1].
- Reduced Vanguard CIWS damage to the Spawn Vehicle: it takes 2.25x longer to kill it [1].
- Team switching: after a team is more than 10 points ahead, a player who switches or joins in progress cannot use the spawn vehicle until reaching the control zone for the first time [1].
- Season 1 history: turret operator rotation speed cap, helicopter input damping, Lakota balance pass (10 Sep 2026) [3].

## Vehicle bug fixes in 0.2.0

All from the Season 02 patch notes, 14 Oct 2026 [1].

- Humvee gunner no longer faces the wrong direction after entering.
- Gunner fire desync and inconsistent firing audio fixed.
- Helicopter cockpit glass now works both ways: shooting out through it damages the vehicle the same as incoming fire.
- Tanks no longer launch themselves from their own turret collision.
- Vehicles no longer sink into the ground when ramming at speed.
- Wheeled vehicles no longer get stuck driving forward out of a backward roll.
- Gamepad: vehicle spinning after closing the tac map, inconsistent ADS on vehicle weapons, and crouching and seat swapping in mounted turrets fixed.
- A vehicle's smoke screen and flares now appear for late joiners.
- Exiting a vehicle places the player on the ground rather than pushing through it.

# Early Access Changes & Known Issues

- 10 Sep 2026, Season 1 launch changelog: the price and level moves in the Season 1 baseline table; air-vehicle kill XP cut from 300 to 250 [3].
- 30 Sep 2026, Update 0.1.2: fly-through exploit rewards capped; Havoc damage-intake bug from 20mm and 30mm cannons fixed; throwables blocked from enclosed vehicle seats [6].
- 2 Oct 2026, hotfix: CIWS time to destroy a Havoc halved from about 12 to about 6 seconds [5].
- 14 Oct 2026 (patch notes) and 15 Oct 2026 (live): Update 0.2.0 adds four vehicles, changes vehicle prices and unlock levels as tabled above, makes purchased-vehicle inventories private by default, reworks Humvee, tracked-vehicle and Dune Buggy handling, applies the calibre damage cuts to vehicle weapons, and fixes the bugs listed above [1][2].
- Preview versus final naming: the 9 Oct preview called the new vehicles "T-72", "Leopard" and "Wolf-110 (Assault)"; the final notes use T-72B3, L2A6 and Wolf-110 [M2 Browning]. This document follows the final notes [1][7].
- None seen in the 2026-10-30 snapshot: no official post after 2026-10-15 is saved, so hotfixes after that date are unknown.
- Planned: fighter jets and more vehicles by full release [4].

# Admin & Technical Notes

None found. No server setting for vehicle availability or prices appears in the official posts retrieved. The inventory-sharing option is a player setting available once a vehicle is fully unlocked [1].

# Risks & Caveats

- The notes list changed values only, so vehicles whose price or level did not change are absent from official text.
- Name mapping between the Season 1 changelog and the 0.2.0 notes is Inferred.
- Season 1 spawn prices came from player guides [8][9]; only rows that the 0.2.0 notes restate as "old" values are corroborated.
- The notes' Pilot track text says the Little Bird "now unlocks later and costs more", which matches the table; the Season 1 changelog's separate Lakota $35,000 figure conflicts with the 0.2.0 "$75k" old value.
- Official patches can change any value here at any time; the review date is 2026-11-20.

# Open Questions

- Unlock levels not stated in the 0.2.0 notes: L2A6, Humvee [Minigun], Kodiak variants, Ural, Z20 Lakota [Miniguns], Havoc, AH-6R. Resolve in game or from a later full table.
- Crew and seat counts for every vehicle: unpublished.
- Spawn prices of the plain Kodiak, Ural, Humvee, Dune Buggy, Bobcat, MH-6, plain Z20 Lakota and SPH-2: not stated in the notes.
- Why the Season 1 changelog gave Z20 Lakota an unlock of $35,000 while the 0.2.0 old value is $75,000.
- Whether a team armoured spawn vehicle has a purchase price: the notes mention a Spawn Vehicle only in rules text.
- Whether any hotfix after 2026-10-15 changed these values: none seen in the 2026-10-30 snapshot.

# References

**Primary Sources**

- [1] **BULKHEAD** — *WARDOGS | Season 02 Patch Notes*, Steam announcement, 14 Oct 2026. https://store.steampowered.com/news/app/1867240/view/1846651706674560. Accessed 2026-10-30.
- [2] **BULKHEAD** — *WARDOGS | Season 02 is now live*, Steam announcement, 15 Oct 2026. https://store.steampowered.com/news/app/1867240/view/1846651706677015. Accessed 2026-10-30.
- [3] **Bulkhead / Valve Steam News** — *Pre-Load Live & Season 1 Changelog*, 9 Sep 2026. https://store.steampowered.com/news/app/1867240/view/1843481262690549. Accessed 2026-10-08.
- [4] **Valve / Bulkhead** — *WARDOGS on Steam*. https://store.steampowered.com/app/1867240/WARDOGS/. Accessed 2026-10-08.
- [5] **Bulkhead / Valve Steam News** — *IR Goggles & CIWS Balance Hotfix*, 2 Oct 2026. https://store.steampowered.com/news/app/1867240/view/1845383656386801. Accessed 2026-10-08.
- [6] **Bulkhead / Valve Steam News** — *WARDOGS Update 0.1.2 (Minor Patch)*, 30 Sep 2026. https://store.steampowered.com/news/app/1867240/view/1845383656376490. Accessed 2026-10-08.
- [7] **BULKHEAD** — *WARDOGS | Season 02 Preview*, Steam announcement, 9 Oct 2026. https://store.steampowered.com/news/app/1867240/view/1846018067933823. Accessed 2026-10-30.

**Press & Secondary**

None cited directly.

**Player-Reported Evidence**

- [8] **GameBrief** — *WARDOGS vehicles guide 2026*. https://www.gamebrief.net/blog/wardogs-vehicles-guide-2026. Accessed 2026-10-08.
- [9] **allthings.how** — *WARDOGS: how to get a vehicle, prices and unlock levels*. https://allthings.how/wardogs-how-to-get-a-vehicle-prices-and-unlock-levels/. Accessed 2026-10-08.

# Further Reading

The official Steam news feed at https://steamcommunity.com/app/1867240/allnews/ for later notes.

# Related Documents

- vehicles-outposts-foundation
- air-and-counter-air
- fob-and-base-building
- price-tables-season-1
- progression-unlock-tables
- cash-rewards-and-costs

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. Pre-Season-02 baseline. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after independent re-verification of validate, markdownlint, links (0 dead) and Steam post ids. Pre-Season-02 baseline. | Standing mandate (auto-approve on green QA) |
| 1.1.0 | 2026-10-30 | Research Pipeline (virtual agent) | Revised for Update 0.2.0: added Wolf-110, Wolf-110 [M2 Browning], T-72B3, Flakpanzer Gepard; Season 02 spawn prices and unlock changes; private vehicle inventories; handling changes; vehicle bug fixes; kept Season 1 values as history; replaced forward-looking Season 02 statements with the outcome. | — |
