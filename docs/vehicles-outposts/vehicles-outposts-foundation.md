---
id: vehicles-outposts-foundation
title: "Vehicles & Outposts: Foundation"
version: 1.0.0
status: frozen
confidence: Medium
category: Vehicles & Outposts
topic: "Vehicle roster, purchasing, outpost construction, destruction"
market: Global
game_version: "Early Access Update 0.1.2 (29-30 Sep 2026) plus security hotfix of 2 Oct 2026"
document_type: foundation
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [gameplay-modes-foundation, combat-loadouts-foundation, economy-foundation, maps-environment-foundation]
tags: [vehicles, fob, outposts, building, destruction, logistics, early-access]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | vehicles-outposts-foundation |
| Version | 1.0.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Vehicles & Outposts |
| Game version | Early Access Update 0.1.2 (29-30 Sep 2026) plus security hotfix of 2 Oct 2026 |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

WARDOGS pairs a combined-arms vehicle set (tanks, an artillery tank, helicopters, light ground vehicles) with player-built Forward Operating Bases (FOBs) and a destructible battlefield. The Steam page confirms that vehicles and logistics are part of Early Access, that players can build a forward operating base to fortify a chokepoint, that rocket launchers can take down apartment blocks, and that fighter jets are planned only for the full release [1].

Official sources give no vehicle table. Names, prices and unlock levels here come from the Season 1 launch changelog as reproduced by press [2] and from community guides, which are labelled player-reported and disagree in places. Build and logistics mechanics (hammer tiers, supply types, pallets) are likewise guide-sourced [5][6][7]. Update 0.1.2 changes to rewards for destroying buildables and delivering pallets are confirmed by two press summaries [3][4].

Document confidence is Medium: the headline mechanics are official, but nearly every number rests on press reproductions or player reports, and Early Access churns per patch.

# Key Takeaways

- Early Access includes vehicles and logistics; fighter jets are planned for the full release only (Steam page, 2026-10-08) [1].
- Players can build their own FOB; the Season 1 changelog raised the vendor FOB price from $2,500 to $7,500 (10 Sep 2026) [1][2].
- Vehicles are bought per life from a Vehicle Vendor in the safe zone, with higher tiers needing a one-time unlock fee and a track level (player-reported, 2026-10-08) [5][8].
- Unlock tracks are Driver (ground), Pilot (helicopters) and Career/Wardog (heavy armour, artillery); Artillery moved to Career level 90 and Heavy Tank to Driver level 35 in Season 1 [2][8].
- A FOB is not a respawn point; forward spawns come from a team armoured spawn vehicle unlocked at 20 team points (player-reported) [6][7].
- Update 0.1.2 capped vehicle fly-through rewards, reduced rewards for pallets deposited outside a FOB zone, and scaled rewards for destroying buildables by build progress [3][4].
- Anything built can be destroyed; hammers also dismantle and repair (player-reported) [7].

# Scope

Covers vehicle classes and named vehicles, how vehicles are bought and delivered, FOB construction and its supply logistics, and how destruction affects vehicles and outposts, as of Update 0.1.2 and the 2 Oct 2026 hotfix. Excludes weapon stats (see combat-loadouts-foundation), cash rewards and death penalty (see economy-foundation), mode rules (see gameplay-modes-foundation) and map layout and terrain destruction detail (see maps-environment-foundation). "Outpost" is used here for the player-built FOB; no source retrieved uses a separate "outpost" feature.

# Definitions

- **FOB (Forward Operating Base)**: a deployable kit that creates a build zone and supply storage; the Steam page describes players building a forward operating base [1].
- **Hammer**: build tool in Small, Medium and Large tiers (player-reported) [6].
- **Pallet / crate**: containers used to haul supplies to a FOB (player-reported) [6][7].
- **Vehicle Vendor**: a physical safe-zone stall that sells vehicles in LAND and AIR tabs (player-reported) [8].
- **Driver / Pilot / Career tracks**: progression tracks gating vehicle unlocks [2].

# Current State

All facts as of 2026-10-08, Update 0.1.2 plus the 2 Oct hotfix.

- Early Access includes vehicles and logistics; the full version is planned to add more vehicles and fighter jets [1].
- The store page promotes tanks, an artillery tank to bombard enemy positions, and helicopters that can ferry supplies to teammates [1].
- Players can build a forward operating base to fortify a chokepoint, and the battlefield is destructible [1].
- The FOB vendor price is $7,500 and the Large Hammer vendor price is $2,400, raised in the Season 1 launch changelog (10 Sep 2026) [2].
- Update 0.1.2 (posted 30 Sep 2026) states: "Fixed vehicle fly through exploit, rewards are now capped" and that destroying buildables now scales with build progress [3][4].
- The 2 Oct 2026 security and stability hotfix added no gameplay changes [4].

# Detail

## Vehicle roster

No official roster was retrievable. The table merges the Season 1 changelog [2] with two community guides [5][8], which are player-reported and partly conflict. Prices are per-spawn costs; "unlock" is a one-time fee.

| Class | Vehicle | Spawn price (player-reported) | Unlock gate |
|-------|---------|-------------------------------|-------------|
| Ground | Bobcat (quad) | about $500 [5] | none [5][8] |
| Ground | Dune Buggy | unlock price now $25,000 [2] | level 8 [2] |
| Ground | Kodiak (pickup) | $3,000 [8]; $2,500 [5] | Driver 10, $35,000 unlock [8] |
| Ground | Kodiak M249 / Assault | $3,750 [5][8] | level 6 [2]; Driver 6, $50,000 [8] |
| Ground | Humvee (base / M249 / minigun) | $3,000 / $3,750 / $4,500 [5] | minigun level 30 [2]; Driver 15 / 20 / 30 [8] |
| Ground | URAL / Ural Defender (M249) | $6,000 / $6,750 [8] | URAL level 3, $35,000 [2]; Defender Driver 18, M249 Driver 25 [8] |
| Ground | Heavy tank | about $14,000 (L2A6, unconfirmed) [5] | Driver 35 [2] |
| Ground | Flakpanzer Gepard (anti-air) | $10,000 [8]; about $8,000 [5] | Wardog track [8] |
| Ground | SPH-2 artillery tank | about $8,000 spawn [5] | $500,000, Career level 90 [2] |
| Air | AH-6M (miniguns) | $7,000 [8] | Pilot 4, $50,000 [8] |
| Air | AH-6R (rockets) | $12,500 [8] | Pilot 20, $250,000 [8] |
| Air | Z20 Lakota | $7,400 [5]; $8,000 with miniguns [8] | Pilot 10 [5]; Pilot 25 [8]; $35,000 [2] |
| Air | Havoc | about $18,000 [5] | Pilot 35 [5] |

Season 1 also gave the Z20 Lakota a balance pass and pitch fix, capped vehicle turret operator rotation speed, and applied helicopter input damping to all input devices [2]. No naval vehicles appear in any source retrieved. One guide counts roughly 20 vehicles and names about 16 [5].

## Purchasing and delivery

Player-reported flow [5][8]:

1. Stand at the Vehicle Vendor stall in the safe zone and choose a vehicle in the LAND or AIR tab.
2. Pay the one-time unlock fee if the vehicle is gated, then the spawn price, which is charged every purchase with no confirmation prompt [8].
3. The vehicle appears for the buyer; armed variants cost more and die to the same anti-vehicle weapons [5].

Free options reported: a team armoured spawn vehicle unlocked at 20 team points, with a satellite dish that disables it if destroyed and about a ten-minute per-player cooldown, plus free transport helicopters and SUVs a few minutes into a match [8]. Cargo vehicles carry small supply amounts; larger loads move on pallets bought at the Garage Vendor [7]. One guide claims helicopters can carry the crate or pallet loads; external sling-loading was not confirmed.

## FOB construction

Player-reported costs and rules [6][7]:

| Item | Detail |
|------|--------|
| FOB kit | $7,500, no unlock (Season 1) [2][6]; an older guide says about $2,500 [7] |
| Small Hammer | default, $100 [6][7] |
| Medium Hammer | Support level 3 [6][7]; unlock $25,000 [6] |
| Large Hammer | Support level 8, $75,000 unlock [6]; one guide says level 7 [7] |
| Build Supplies | $10 each or $500 for a 50 stack [6] |

Procedure: deploy the kit on valid ground (not inside a building, a main base or another FOB's radius), deposit supplies into base storage via the FOB console, pick a structure from the build wheel, and hit the yellow X markers to finish [6]. Small Hammer structures (sandbags, barbed wire, hedgehogs, Recon Tent) need no FOB; HESCO, doors and gates need Medium; bunkers, Recon Towers, mortars, anti-air, Repair and Refuel Stations and the Drill Rig need Large [6]. The required tier applies only to starting a blueprint; any hammer finishes it [6]. Reported build costs include Bunker 61, Mortar 91, Repair Station 121, Talon 601, CIWS 901 and Drill Rig 1,351 supplies [7].

Supply types: Build, Ammo (mortar, CIWS, SAM), Fuel (Refuel Station, Drill Rig) and Mechanical (Repair Station) [6]. FOBs do not refill by themselves [7]. The Drill Rig is reported to pull the Hot Zone toward the FOB when fuelled [9]. Gates admit vehicles, doors are infantry-only and hedgehogs block vehicle routes [7]. Repair Stations repair and Refuel Stations refuel vehicles from stored supplies [7].

## Destruction

The store page states rocket launchers can take down apartment blocks and tanks can tear through towns [1]. Guides report that anything built can be destroyed, with artillery used to level fortifications from outside the zone [7]. Hammers switch to "Dismantle" on finished objects and also repair [7]. Pallets left outside storage can be destroyed, and enemies reaching the FOB console can hack and take control of the base, with a siren (player-reported) [6]. Vehicles: a destroyed vehicle is gone and must be re-bought; a damaged one can be repaired at a Repair Station using Mechanical Supplies; a rolled vehicle can be flipped and repaired in the base repair area (player-reported) [5][8]. No source gives structure health values.

# Early Access Changes & Known Issues

- 10 Sep 2026, Season 1 launch: FOB vendor price $2,500 to $7,500, Large Hammer $1,600 to $2,400, vehicle price and unlock moves (Artillery to Career 90, Heavy Tank to Driver 35), turret rotation cap, Lakota pass, a buildables crash fix, and larger loadout space for 155mm, 122mm and flare deployables [2].
- 29-30 Sep 2026, Update 0.1.2: vehicle fly-through reward exploit capped; pallets deposited outside a FOB zone give reduced rewards; destroying buildables or a placed schematic no longer gives a full reward [3][4].
- 2 Oct 2026 (00:13 UTC): security and stability hotfix, no gameplay changes, one-hour maintenance [4].
- Planned: more vehicles and fighter jets by full release [1].

# Admin & Technical Notes

None found specific to vehicles or FOBs. No server setting for vehicle or buildable limits appears in the sources retrieved.

# Risks & Caveats

- Guide figures mix beta and Season 1 values (for example the $2,500 FOB) and conflict on unlock levels [6][7][8].
- Official Steam post bodies did not render to fetchers; patch contents rest on press summaries [2][3][4].
- Season 02 is expected to rebalance prices and unlocks; this document will go stale quickly.

# Open Questions

- Official vehicle roster, authoritative prices and unlock levels: resolve with in-game verification or official patch notes.
- Vehicle versus FOB cost on destruction, and any refund: no source found.
- Whether helicopters can sling-load pallets externally: unconfirmed.
- Hammer unlock levels (Large at 7 or 8) and prices: guides conflict [6][7].
- Structure health, build radius and FOB count limits: not published in sources retrieved.

# References

**Primary Sources**

- [1] **Valve / Bulkhead** — *WARDOGS on Steam*. https://store.steampowered.com/app/1867240/WARDOGS/. Accessed 2026-10-08.

**Press & Secondary**

- [2] **Gfinity Esports** — *WARDOGS Season 1 changelog, Early Access patch notes*. https://www.gfinityesports.com/article/wardogs-season-1-changelog-early-access-patch-notes. Accessed 2026-10-08.
- [3] **BisectHosting** — *WARDOGS Update 0.1.2 patch notes*. https://www.bisecthosting.com/blog/wardogs-update-0-1-2-patch-notes-bug-fixes-improvements-flythrough-exploit-fob-pallet-delivery-xp. Accessed 2026-10-08.
- [4] **Ingamenews** — *WARDOGS Update 0.1.2 and security hotfix, a comparative overview*. https://ingamenews.com/gaming-news/wardogs-update-0-1-2-and-security-hotfix-a-comparative-overview/. Accessed 2026-10-08.

**Player-Reported Evidence**

- [5] **GameBrief** — *WARDOGS vehicles guide 2026*. https://www.gamebrief.net/blog/wardogs-vehicles-guide-2026. Accessed 2026-10-08.
- [6] **KeenGamer** — *How to build a FOB in WARDOGS: supplies and costs*. https://www.keengamer.com/articles/guides/how-to-build-a-fob-in-wardogs-supplies-and-costs/. Accessed 2026-10-08.
- [7] **allthings.how** — *WARDOGS: how to build structures with hammers and FOBs*. https://allthings.how/wardogs-how-to-build-structures-with-hammers-and-fobs/. Accessed 2026-10-08.
- [8] **allthings.how** — *WARDOGS: how to get a vehicle, prices and unlock levels*. https://allthings.how/wardogs-how-to-get-a-vehicle-prices-and-unlock-levels/. Accessed 2026-10-08.
- [9] **KeenGamer** — *WARDOGS best base building guide, FOB layout and build order*. https://www.keengamer.com/articles/guides/wardogs-best-base-building-guide-fob-layout-build-order/. Accessed 2026-10-08.

# Further Reading

The official Steam news feed at https://steamcommunity.com/app/1867240/allnews/ for Season 02 notes.

# Related Documents

- gameplay-modes-foundation
- combat-loadouts-foundation
- economy-foundation
- maps-environment-foundation

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after independent re-verification of validate, markdownlint and links (0 dead). | Standing mandate (auto-approve on green QA) |
