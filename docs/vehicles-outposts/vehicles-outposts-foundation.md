---
id: vehicles-outposts-foundation
title: "Vehicles & Outposts: Foundation"
version: 1.1.0
status: frozen
confidence: Medium
category: Vehicles & Outposts
topic: "Vehicle roster, purchasing, outpost construction, destruction"
market: Global
game_version: "Early Access Update 0.1.2 (30 Sep 2026) plus hotfixes of 2 Oct 2026"
document_type: foundation
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-10-22
sources_verified: 2026-10-08
supersedes: null
related: [gameplay-modes-foundation, combat-loadouts-foundation, economy-foundation, maps-environment-foundation, vehicle-roster-and-prices, fob-and-base-building, air-and-counter-air, price-tables-season-1, progression-unlock-tables, destructibility-and-level-design, patch-history]
tags: [vehicles, fob, outposts, building, destruction, logistics, early-access]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | vehicles-outposts-foundation |
| Version | 1.1.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Vehicles & Outposts |
| Game version | Early Access Update 0.1.2 (30 Sep 2026) plus hotfixes of 2 Oct 2026 |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-10-22 |

# Executive Summary

WARDOGS pairs a combined-arms vehicle set (tanks, an artillery tank, helicopters, light ground vehicles) with player-built Forward Operating Bases (FOBs) and a destructible battlefield. Bulkhead's own posts confirm that Early Access includes "Grounded Gunplay & Vehicles" and "Destruction & Build Mechanics" [5], and the Steam page promotes tanks, an artillery tank, helicopters that ferry supplies, a buildable forward operating base and apartment blocks that rocket launchers can destroy [6].

This revision replaces the v1.0.0 reliance on press summaries with the full official Steam text. The Season 1 changelog (9 Sep 2026) is the only official source for vehicle and hammer prices and unlock levels, and it lists changes only, not a full table [1]. Official values now confirmed: FOB vendor $7,500, Large Hammer vendor $2,400, Medium Hammer unlock $25,000, Large Hammer unlock $75,000 at Support level 8, Kodiak Flatbed Driver 10 for $35,000, Heavy Tank Driver 35, Artillery Tank Career 90 for $500,000 [1]. Update 0.1.2 fixed the vehicle fly-through exploit, reduced pallet rewards outside the FOB zone and scaled buildable-destruction rewards by build progress [2]. The 2 Oct balance hotfix made the CIWS destroy a Havoc in about 6 seconds instead of 12 [3].

Still player-reported only: per-spawn vehicle prices, the build procedure, supply types, structure costs and which hammer tier builds what [7][8][9][10][11]. Document confidence is Medium: prices, levels and patch changes are official, but the roster is incomplete and the mechanics layer is guide-sourced. For depth see vehicle-roster-and-prices, fob-and-base-building and air-and-counter-air.

# Key Takeaways

- Early Access includes vehicles and destruction and build mechanics (official FAQ, 18 Feb 2026) [5]; the Steam page promotes a buildable FOB and destructible apartment blocks [6].
- The FOB vendor price is $7,500 (was $2,500) and the Large Hammer vendor price $2,400 (was $1,600), both raised at Season 1 "to make them more of a choice" (official, 9 Sep 2026) [1].
- Official Support-track unlocks: Medium Hammer $25,000 (was $10,000), Large Hammer $75,000 (was $25,000) at level 8 (was 7) [1].
- Official unlock tracks are Career, Medic, Recon, Support, Driver and Pilot; vehicles sit on Driver (ground), Pilot (air) and Career (Artillery Tank at level 90, $500,000) [1][5].
- Official ground levels: URAL 3, Kodiak Assault 6, Dune Buggy 8, Kodiak Flatbed 10 ($35,000, was level 2 and $15,000), URAL Covered 18, URAL Attack 25, Humvee with minigun 30, Heavy Tank 35 [1].
- Update 0.1.2 (30 Sep 2026): vehicle fly-through rewards capped; pallets deposited outside the FOB zone give reduced rewards; destroying buildables pays by build progress [2].
- 2 Oct 2026 balance hotfix: the CIWS now destroys the Havoc in around 6 seconds as opposed to 12 [3].
- Per-spawn vehicle prices, the build procedure and the "free armoured spawn vehicle" are player-reported only [7][10]. Sling-loading is unconfirmed in every source.

# Scope

Covers vehicle classes and named vehicles, how vehicles are bought, FOB construction and its supply logistics, and how destruction affects vehicles and outposts, as of Update 0.1.2 and the 2 Oct 2026 hotfixes. Excludes weapon stats (see combat-loadouts-foundation), cash rewards and death penalty (see economy-foundation), mode rules (see gameplay-modes-foundation) and map layout and terrain destruction detail (see maps-environment-foundation and destructibility-and-level-design). "Outpost" is used here for the player-built FOB; no official post uses a separate "outpost" feature. Full tables live in vehicle-roster-and-prices, fob-and-base-building, price-tables-season-1 and progression-unlock-tables; this document summarises and links.

# Definitions

- **FOB (Forward Operating Base)**: a deployable kit that creates a build zone and supply storage; the Steam page describes players building a forward operating base to fortify a chokepoint [6]. Update 0.1.2 refers to "depositing pallets into a FOB" inside or outside "the zone" [2].
- **Hammer**: build tool in Small, Medium and Large tiers. Official text names the Medium Hammer, Large Hammer and Support track [1]; the Small tier and tier-to-structure mapping are player-reported [8][9].
- **Pallet / crate**: containers used to haul supplies. Official text names supply crates (Pilot small armoured supply crate, Driver Large Supply Crate) and pallets deposited into a FOB [1][2].
- **Schematic**: a placed, unbuilt structure; 0.1.2 says destroying one no longer gives a full reward [2].
- **Vehicle Vendor**: a physical safe-zone stall selling vehicles in LAND and AIR tabs (player-reported) [10].
- **Tracks**: the six official progression tracks are Career, Medic, Recon, Support, Driver and Pilot [1][5]. Driver gates ground vehicles and Pilot gates helicopters [1].

# Current State

All facts as of 2026-10-08, Update 0.1.2 plus the 2 Oct hotfixes.

- Early Access includes "Grounded Gunplay & Vehicles" and "Destruction & Build Mechanics" [5]. Squads provide "vehicle locking" [5].
- The store page promotes tanks, an artillery tank to bombard enemy positions, helicopters that can ferry supplies to teammates, and a forward operating base to fortify a chokepoint [6].
- The FOB vendor price is $7,500 and the Large Hammer vendor price $2,400, both raised at Season 1 [1].
- Update 0.1.2 states: "Fixed vehicle fly through exploit, rewards are now capped", "Any rewards for destroying buildables now scale with their build progress - so destroying a placed schematic no longer gives a full reward" and "Depositing pallets into a FOB outside the zone now awards reduced rewards" [2]. It also fixed a Havoc bug that raised damage taken from 20mm and 30mm cannon fire and blocked throwables from enclosed vehicle seats [2].
- The 2 Oct 2026 security and stability hotfix announcement says a hotfix is planned for 08:00 UTC with about one hour of downtime; it lists no gameplay changes [4]. A separate 2 Oct balance hotfix disabled IR Rangefinders in the vendor until Season 02 and cut the CIWS time to destroy a Havoc from about 12 s to about 6 s [3].
- Players start with $10,000 and buy vehicles as part of a per-life loadout [5][6].

# Detail

## Vehicle roster

Only the Season 1 changelog gives official vehicle values, and only for what it changed [1]. Full tables, conflicts and labels are in vehicle-roster-and-prices. Spawn prices are the per-purchase cost and are player-reported only [7][10]; "unlock" is the one-time track price, a reading Inferred from the changelog's track headings [1].

| Class | Vehicle | Official track, level and unlock | Spawn price (player-reported) |
|-------|---------|----------------------------------|-------------------------------|
| Ground | Dune Buggy | Driver 8, $25,000 [1] | not published |
| Ground | URAL | Driver 3, $35,000 [1] | $6,000 [10] |
| Ground | URAL Covered / URAL Attack | Driver 18 / Driver 25 [1] | not published |
| Ground | Kodiak Assault | Driver 6 [1] | $3,750 [7][10] |
| Ground | Kodiak Flatbed | Driver 10, $35,000 (was level 2, $15,000) [1] | $2,500 [7]; $3,000 [10] |
| Ground | Humvee with minigun | Driver 30 [1] | $4,500 [7] |
| Ground | Heavy Tank | Driver 35 (was Career 35) [1] | about $14,000, "L2A6" unconfirmed [7] |
| Ground | Artillery Tank | Career 90, $500,000 (was Career 55, $400,000) [1] | about $8,000 [7] |
| Air | Little Bird with miniguns | Pilot, $50,000 (was $25,000); level not stated [1] | $7,000 [10] |
| Air | Z20 Lakota | Pilot, $35,000 (was $50,000); level not stated [1] | $7,400 [7]; $8,000 [10] |
| Air | Havoc | named in 0.1.2 and the CIWS hotfix; track, level and price not stated [2][3] | about $18,000, Pilot 35 [7] |

Guide-only rows with no official counterpart: Bobcat quad, base and M249 Humvee, Flakpanzer Gepard (a guide's "Wardog track" has no official counterpart; the six official tracks are listed under Definitions), AH-6M/AH-6R and the team armoured spawn vehicle [7][10]. Guide names such as "Kodiak (pickup)" match the official Kodiak Flatbed by level and price (Inferred). Season 1 also gave the Z20 Lakota a balance pass and pitch fix, capped vehicle turret operator rotation speed, applied helicopter input damping to every input device, fixed a DPI issue affecting tank aiming and reduced Lakota chase-camera rattle by 6 dB [1]. No naval vehicles appear in any source retrieved.

## Purchasing and delivery

Official: vehicles are bought with cash as part of the per-life loadout [5][6]. Player-reported flow [7][10]:

1. Stand at the Vehicle Vendor stall in the safe zone and choose a vehicle in the LAND or AIR tab.
2. Pay the one-time unlock if the vehicle is gated, then the spawn price on each purchase, with no confirmation prompt [10].
3. The vehicle appears for the buyer; armed variants cost more and die to the same anti-vehicle weapons [7].

Free options reported by one guide only: a team armoured spawn vehicle unlocked at 20 team points with a satellite dish that disables it if destroyed, plus free transport helicopters and SUVs a few minutes into a match [10]. Cargo vehicles carry small supply amounts and larger loads move on pallets (player-reported) [9]. The store page says helicopters can ferry supplies to teammates [6]. External sling-loading is unconfirmed in every source read; see air-and-counter-air.

## FOB construction

Official prices and levels [1], player-reported mechanics [8][9]. Full detail is in fob-and-base-building.

| Item | Detail |
|------|--------|
| FOB kit | $7,500 vendor price as of Season 1 (was $2,500) [1] |
| Small Hammer | default, $100 (player-reported) [8][9] |
| Medium Hammer | Support track, unlock $25,000 (was $10,000) [1]; level 3 is player-reported [8][9] |
| Large Hammer | Support level 8 (was 7), unlock $75,000 (was $25,000) [1]; vendor price $2,400 (was $1,600) [1] |
| Build Supplies | $10 each or $500 for a 50 stack (player-reported) [8] |

The "$800" hammer figure and the Large Hammer level 7 in earlier drafts are superseded or unsourced: level 7 was the pre-Season-1 value [1], and no official or press text gives $800. Procedure (player-reported): deploy the kit on valid ground (not inside a building, a main base or another FOB's radius), deposit supplies via the FOB console, pick a structure from the build wheel and hit the yellow X markers [8]. Small Hammer structures (sandbags, barbed wire, hedgehogs, Recon Tent) need no FOB; HESCO, doors and gates need Medium; bunkers, Recon Towers, mortars, anti-air, Repair and Refuel Stations and the Drill Rig need Large; the tier applies only to starting a blueprint [8]. Reported build costs include Bunker 61, Mortar 91, Repair Station 121, Talon 601, CIWS 901 and Drill Rig 1,351 supplies [9]. Supply types reported: Build, Ammo, Fuel and Mechanical [8]. The Drill Rig is reported to pull the Hot Zone toward a fuelled FOB [11]. No official post lists structures or supply costs.

## Destruction

Official: the store page says players can "Destroy apartment blocks with rocket launchers or tear your way through towns in heavily armoured tanks" [6], and the FAQ calls the battlefield "large-scale" and destructible [5]. Update 0.1.2 scales buildable-destruction rewards by build progress and reworked buildable crit spots so they favour a spot reachable from where the attacker stands [2]; a buildables crash was fixed at Season 1 [1]. Player-reported: anything built can be destroyed, artillery can level fortifications from outside the zone, hammers switch to Dismantle on finished objects and also repair, unprotected pallets can be destroyed, and enemies at the FOB console can hack the base with a siren [8][9]. Vehicles: a destroyed vehicle must be re-bought, and a damaged one can be repaired at a Repair Station using Mechanical Supplies (player-reported) [7][10]. No source gives structure health values. See destructibility-and-level-design for terrain and building destruction.

# Early Access Changes & Known Issues

- 9 Sep 2026, Season 1 changelog (live 10 Sep): FOB vendor $2,500 to $7,500; Large Hammer vendor $1,600 to $2,400; Medium Hammer unlock $10,000 to $25,000; Large Hammer unlock $25,000 to $75,000 and level 7 to 8; Kodiak Flatbed level 2 to 10 and $15,000 to $35,000; Artillery to Career 90 and $500,000; Heavy Tank to Driver 35; turret rotation cap; Lakota pass; a buildables crash fix; larger loadout space for 155mm, 122mm and flare deployables [1].
- 30 Sep 2026, Update 0.1.2: vehicle fly-through reward exploit capped; pallets deposited outside a FOB zone give reduced rewards; destroying buildables or a placed schematic scales with build progress; Havoc cannon-damage bug fixed; players caught abusing exploits risk a permanent ban [2].
- 2 Oct 2026: security and stability hotfix announced for 08:00 UTC with one hour of downtime and no listed gameplay changes [4]; balance hotfix halved the CIWS time to destroy a Havoc (about 12 s to about 6 s) and disabled IR Rangefinders in the vendor until Season 02 [3]. The developer says the CIWS had been "overcorrected" in the previous patch [3].
- Season 02 is planned as a larger update with new map conditions, equipment, balance reworks and features [2]. See patch-history.

# Admin & Technical Notes

None found specific to vehicles or FOBs. Update 0.1.2 added RCON and scheduled-restart server settings, but none concern vehicles or buildables [2].

# Risks & Caveats

- The changelog lists changed values only, so unchanged vehicle prices and levels are absent from official text [1].
- Guide figures mix beta and Season 1 values and conflict with each other and with the changelog; where they disagree, the official text wins [7][8][9][10].
- Reading the changelog's track prices as unlock prices, and matching guide vehicle names to official names, are Inferred.
- A fighter-jet and "more vehicles" roadmap line attributed to the Steam page in v1.0.0 is not in the saved store JSON snapshot, so it is not asserted here; see Open Questions.
- Season 02 is due 15 Oct 2026 and is expected to rebalance prices and unlocks; this document will go stale quickly.

# Open Questions

- Spawn price of every vehicle and the Lakota, Little Bird and Havoc Pilot levels: no official source.
- Whether the Havoc, Gepard and L2A6 are purchasable and at what values: no official text beyond the Havoc name [2][3].
- Whether fighter jets are planned for the full release: the claim is not in the saved store snapshot; re-verify from the live Steam page.
- Vehicle versus FOB cost on destruction, and any refund: no source found.
- Whether helicopters can sling-load pallets externally: unconfirmed in every source.
- Medium Hammer unlock level, structure list, supply costs, structure health, build radius and FOB count limits: not published officially.
- Size of the 0.1.2 pallet and destruction reward reductions: not published.

# References

**Primary Sources**

- [1] **Bulkhead / Steam News** — *Pre-Load Live & Season 1 Changelog*, 9 Sep 2026. https://store.steampowered.com/news/app/1867240/view/1843481262690549. Accessed 2026-10-08.
- [2] **Bulkhead / Steam News** — *WARDOGS | Update 0.1.2 (Minor Patch)*, 30 Sep 2026. https://store.steampowered.com/news/app/1867240/view/1845383656376490. Accessed 2026-10-08.
- [3] **Bulkhead / Steam News** — *IR Goggles & CIWS Balance Hotfix*, 2 Oct 2026. https://store.steampowered.com/news/app/1867240/view/1845383656386801. Accessed 2026-10-08.
- [4] **Bulkhead / Steam News** — *WARDOGS | Security & Stability Hotfix*, 2 Oct 2026. https://store.steampowered.com/news/app/1867240/view/1845383656384445. Accessed 2026-10-08.
- [5] **Bulkhead / Steam News** — *WARDOGS - TOP QUESTIONS*, 18 Feb 2026. https://store.steampowered.com/news/app/1867240/view/1825093633182385. Accessed 2026-10-08.
- [6] **Valve / Bulkhead** — *WARDOGS on Steam*. https://store.steampowered.com/app/1867240/WARDOGS/. Accessed 2026-10-08.

**Press & Secondary**

None cited directly; the v1.0.0 press reproductions of the changelog and 0.1.2 notes are superseded by [1] and [2].

**Player-Reported Evidence**

- [7] **GameBrief** — *WARDOGS vehicles guide 2026*. https://www.gamebrief.net/blog/wardogs-vehicles-guide-2026. Accessed 2026-10-08.
- [8] **KeenGamer** — *How to build a FOB in WARDOGS: supplies and costs*. https://www.keengamer.com/articles/guides/how-to-build-a-fob-in-wardogs-supplies-and-costs/. Accessed 2026-10-08.
- [9] **allthings.how** — *WARDOGS: how to build structures with hammers and FOBs*. https://allthings.how/wardogs-how-to-build-structures-with-hammers-and-fobs/. Accessed 2026-10-08.
- [10] **allthings.how** — *WARDOGS: how to get a vehicle, prices and unlock levels*. https://allthings.how/wardogs-how-to-get-a-vehicle-prices-and-unlock-levels/. Accessed 2026-10-08.
- [11] **KeenGamer** — *WARDOGS best base building guide, FOB layout and build order*. https://www.keengamer.com/articles/guides/wardogs-best-base-building-guide-fob-layout-build-order/. Accessed 2026-10-08.

# Further Reading

The official Steam news feed at https://store.steampowered.com/news/app/1867240 for Season 02 notes.

# Related Documents

- gameplay-modes-foundation
- combat-loadouts-foundation
- economy-foundation
- maps-environment-foundation
- vehicle-roster-and-prices
- fob-and-base-building
- air-and-counter-air
- price-tables-season-1
- progression-unlock-tables
- destructibility-and-level-design
- patch-history

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after independent re-verification of validate, markdownlint and links (0 dead). | Standing mandate (auto-approve on green QA) |
| 1.1.0 | 2026-10-08 | Research Pipeline (revision worker) | Revised against full official Steam text; Kodiak Flatbed to Driver 10 and $35,000; Large Hammer level 8; Medium and Large Hammer unlock prices $25,000 and $75,000 and Large vendor $2,400; $800 and "Wardog track" removed; official track list; FOB $7,500 confirmed; 0.1.2 and 2 Oct CIWS hotfix cited from primary text; 2 Oct security hotfix relabelled as announcement with no listed gameplay changes; fighter-jet claim moved to Open Questions; links to depth docs added. | Standing mandate (auto-approve on green QA) |
