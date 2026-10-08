---
id: fob-and-base-building
title: "FOBs, Hammers & Base Building"
version: 1.0.0
status: frozen
confidence: Medium
category: Vehicles & Outposts
topic: "FOB deployment, supply types, hammer tiers, structures, pallet logistics, costs"
market: Global
game_version: "Early Access Season 1, Update 0.1.2 (30 Sep 2026) plus hotfixes of 2 Oct 2026; pre-Season-02 baseline"
document_type: depth
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [vehicles-outposts-foundation, vehicle-roster-and-prices, air-and-counter-air, cash-rewards-and-costs, maps-environment-foundation]
tags: [fob, hammer, base-building, pallets, supplies, baseline, early-access]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | fob-and-base-building |
| Version | 1.0.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Vehicles & Outposts |
| Game version | Season 1, Update 0.1.2 plus 2 Oct 2026 hotfixes (pre-Season-02 baseline) |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

This document goes deeper than the parent foundation on forward operating bases (FOBs), the three hammer tiers, supply types, buildable structures and pallet logistics. It is a pre-Season-02 baseline: Season 02 is due 15 October 2026 and is expected to wipe progression, so every number is tabulated with its version and source class for mechanical diffing later.

The official Steam posts (saved locally and cited by Steam URL) settle the two conflicts the foundation left open. Large Hammer unlock moved from Support level 7 to level 8 in the Season 1 changelog, so level 8 is the current official value [1]. The Support-track Large Hammer unlock rose from $25,000 to $75,000 and the Medium Hammer unlock from $10,000 to $25,000 [1]. No source retrieved gives an $800 hammer price; see Open Questions. The FOB vendor price is $7,500 [1].

Confidence is Medium. Prices, levels and the 0.1.2 reward rules are official [1][2], but the build procedure, structure list, supply types and structure costs rest on player-reported guides [8][9][10], and no official text lists them.

# Key Takeaways

- Official, Season 1 (9 Sep 2026): FOB vendor price $2,500 to $7,500; Large Hammer vendor price $1,600 to $2,400 [1].
- Official, Season 1: Support-track unlocks are Medium Hammer $25,000 (was $10,000) and Large Hammer $75,000 (was $25,000), with Large Hammer level 7 to level 8 [1]. Level 8 is therefore the current value; level 7 is the pre-Season-1 value.
- Official, Update 0.1.2 (30 Sep 2026): rewards for destroying buildables scale with build progress, so destroying a placed schematic no longer pays in full; pallets deposited into a FOB outside the zone award reduced rewards [2].
- Official, 0.1.2: buildable "crit spots" were reworked to favour a spot reachable from where the attacker stands [2].
- Player-reported: four supply types (Build, Ammo, Fuel, Mechanical); hammer tiers Small, Medium, Large; Build Supplies $10 each or $500 per 50 [8][9].
- Official design intent: building and destruction are core Early Access features, and a FOB fortifies a chokepoint [3][4].

# Scope

Covers FOB price and deployment, supply types, hammer tiers and unlocks, buildable structures and their costs, pallet delivery and the 0.1.2 reward reduction, and the build and destroy interaction, at the game version above. Excludes the vehicle roster (see vehicle-roster-and-prices), air defence detail beyond cost (see air-and-counter-air), the wider cash model (see cash-rewards-and-costs), and map terrain (see maps-environment-foundation). It does not restate the foundation (vehicles-outposts-foundation); where numbers appear in both, this document adds source class and as-of version.

# Definitions

- **FOB**: player-deployed kit creating a build zone and supply storage; the official line is that players can build a forward operating base to fortify a chokepoint [4].
- **Hammer**: build tool in Small, Medium and Large tiers; the Support track sells the Medium and Large unlocks [1].
- **Pallet**: container used to deposit supplies into a FOB; 0.1.2 refers to depositing pallets into a FOB inside or outside the zone [2].
- **Schematic**: a placed, unbuilt structure; 0.1.2 refers to a "placed schematic" [2].
- **Build progress**: completion fraction of a buildable, which now scales destruction rewards [2].

# Current State

As of Update 0.1.2 and the 2 Oct 2026 hotfixes (neither hotfix changed hammers, FOBs or pallets) [2][5][6].

- The FOB costs $7,500 at the vendor [1].
- The Large Hammer costs $2,400 at the vendor, and unlocks on the Support track at level 8 for $75,000; the Medium Hammer unlock is $25,000 [1].
- Destroying a buildable pays a reward scaled by its build progress [2].
- Depositing pallets into a FOB outside the zone pays a reduced reward [2].
- Buildable crit spots no longer reappear in the same place, get pushed into corners or jump to the far side of a structure [2].
- A crash involving buildables was fixed at Season 1 launch [1].
- The 2 Oct IR Goggles and CIWS hotfix made the CIWS destroy the Havoc in about 6 seconds instead of 12 [5]; guides list the CIWS as a Large-tier structure [8][10].

# Detail

## Baseline values

Source class: Official = Steam announcement posts; Player = player-reported guide, not independently verified. "Season 1.0" is the 9 Sep 2026 changelog.

| Value | As-of version | Source |
|-------|---------------|--------|
| FOB vendor price $7,500 (was $2,500) | Season 1.0 | Official [1] |
| Large Hammer vendor price $2,400 (was $1,600) | Season 1.0 | Official [1] |
| Support: Medium Hammer unlock $25,000 (was $10,000) | Season 1.0 | Official [1] |
| Support: Large Hammer unlock $75,000 (was $25,000) | Season 1.0 | Official [1] |
| Support: Large Hammer unlock level 8 (was 7) | Season 1.0 | Official [1] |
| Medium Hammer unlock level 3 | Season 1 era | Player [8][9] |
| Small Hammer default, $100 | Season 1 era | Player [8][9] |
| Build Supplies $10 each, $500 per 50 | Season 1 era | Player [8] |
| Pilot: small armoured supply crate $10,000 (was $5,000) | Season 1.0 | Official [1] |
| Driver: Large Supply Crate unlock level 16 (was 20) | Season 1.0 | Official [1] |
| Driver: Kodiak Flatbed $35,000 (was $15,000), level 10 (was 2) | Season 1.0 | Official [1] |
| Supply crate purchase curve rescaled to 1-200 (was 25-250) | Season 1.0 | Official [1] |
| Supply crate item sold under $75: 1 XP (was 25 XP) | Season 1.0 | Official [1] |
| Buildable destruction reward scales with build progress (no figure published) | 0.1.2 | Official [2] |
| Pallet deposit outside FOB zone: reduced reward (no figure published) | 0.1.2 | Official [2] |
| Supply costs: Bunker 61, Mortar 91, Repair Station 121, Talon 601, CIWS 901, Drill Rig 1,351 | Season 1 era | Player [9] |
| CIWS kill time on Havoc about 6 seconds (was 12) | 2 Oct hotfix | Official [5] |

## FOB price and mechanics

The vendor price is the only officially published FOB number; the raise was made so the FOB and Large Hammer are "more of a choice" [1]. Official posts describe the FOB as a way to fortify a chokepoint and list building as an Early Access feature [3][4]. Player-reported procedure: deploy the kit on valid ground, not inside a building, a main base or another FOB's radius; deposit supplies into base storage through the FOB console; choose a structure from the build wheel; finish it with the hammer [8]. FOBs do not refill by themselves [9]. Enemies reaching the FOB console can reportedly hack the base, with a siren [8]. FOB count limits, radius and health are not published.

## The four supply types

All four are player-reported [8]; no official post names them.

| Supply type | Used by (player-reported) |
|-------------|--------------------------|
| Build | Structures; $10 each or $500 per 50 [8] |
| Ammo | Mortar, CIWS, SAM [8] |
| Fuel | Refuel Station, Drill Rig [8] |
| Mechanical | Repair Station [8] |

Official text confirms only supply crates as a purchasable item class (Pilot small armoured supply crate, Driver Large Supply Crate, Kodiak Flatbed) [1] and that helicopters can ferry supplies to teammates [4].

## Hammer tiers and unlocks

| Tier | Unlock | Structures needing the tier (player-reported) |
|------|--------|-----------------------------------------------|
| Small | Default; $100 (player-reported) [8][9] | Sandbags, barbed wire, hedgehogs, Recon Tent; no FOB needed [8] |
| Medium | Support track, $25,000 (official) [1]; level 3 (player-reported) [8][9] | HESCO, doors, gates [8] |
| Large | Support track, level 8, $75,000 (official) [1]; vendor $2,400 (official) [1] | Bunkers, Recon Towers, mortars, anti-air, Repair and Refuel Stations, Drill Rig [8] |

The required tier reportedly applies only to starting a blueprint; any hammer finishes it [8]. Hammers switch to Dismantle on finished objects and also repair [9].

Conflict resolution:

- **Level 7 versus 8.** The Season 1 changelog states "Large Hammer: level 7 to level 8" [1]. One guide still gave level 7 [9]; that is the pre-Season-1 value. Level 8 is the baseline.
- **$800 versus $25,000.** The official changelog gives $25,000 as the Medium Hammer Support unlock (previously $10,000) and as the former Large Hammer unlock, now $75,000 [1]. No retrieved official or press text gives an $800 hammer price. Any $800 figure is unsupported here; see Open Questions.
- **Vendor versus unlock.** The Support track gates the right to buy the hammer ($75,000, level 8), and the vendor charges $2,400 for a Large Hammer [1]. Whether the vendor price recurs per purchase is not stated.

## Buildable structures and costs

No official structure list or cost table exists in the posts retrieved. Player-reported supply costs [9]: Bunker 61, Mortar 91, Repair Station 121, Talon 601, CIWS 901, Drill Rig 1,351. Repair Stations repair and Refuel Stations refuel vehicles from stored supplies; the Drill Rig is reported to pull the Hot Zone toward a fuelled FOB [10]. Gates admit vehicles, doors are infantry-only, hedgehogs block vehicle routes [9]. Official: the CIWS was rebalanced on 2 Oct 2026 [5].

## Pallet delivery and the 0.1.2 reward reduction

Pallets are the logistics unit for moving supplies into a FOB; cargo vehicles carry small amounts and larger loads move on pallets (player-reported) [9]. Update 0.1.2 states: "Depositing pallets into a FOB outside the zone now awards reduced rewards" [2]. A press summary lists the same change among the cash and XP exploit fixes [7]. The size of the reduction and the zone boundary are not published. The post frames the change as anti-exploit and warns that players abusing repeatable exploits risk a permanent ban [2]. Supply crate sale XP was cut separately in Season 1 [1].

## Build-destroy interaction

Official: "Any rewards for destroying buildables now scale with their build progress - so destroying a placed schematic no longer gives a full reward" [2]. Rocket launchers can take down apartment blocks per the store page [4]. Player-reported: anything built can be destroyed, artillery can level fortifications from outside the zone, and unprotected pallets can be destroyed [8][9]. For diffing: reward scaling is by build progress, with no published curve.

# Early Access Changes & Known Issues

- 9 Sep 2026, Season 1: FOB $2,500 to $7,500; Large Hammer vendor $1,600 to $2,400; Medium Hammer unlock $10,000 to $25,000; Large Hammer unlock $25,000 to $75,000 and level 7 to 8; supply crate rescale; buildables crash fixed [1].
- 30 Sep 2026, Update 0.1.2: reduced pallet deposit rewards outside the FOB zone; destruction rewards scale with build progress; buildable crit spot fix [2].
- 2 Oct 2026: security hotfix without gameplay changes [6]; CIWS kill time on Havoc halved [5].
- Season 02, due 15 Oct 2026: expected progression wipe and rebalance; not yet in effect.

# Admin & Technical Notes

None found specific to FOBs or hammers. No official server setting for buildable limits appears in the posts retrieved.

# Risks & Caveats

- Supply types, hammer-to-structure mapping and structure supply costs are player-reported only and may be wrong or stale [8][9][10].
- Guides mix pre-Season-1 and Season 1 values; the official changelog overrides them where it speaks [1].
- Season 02 may reset unlocks or change prices; treat this as a dated baseline.

# Open Questions

- Source of the $800 hammer figure: not found in official or press text; resolve by an in-game vendor check.
- Official list of buildables and supply costs: not published.
- Size of the 0.1.2 pallet and destruction reward reductions: not published.
- The foundation lists Medium Hammer at Support level 3 from guides; no official level confirms it.
- Whether the hammer vendor price recurs per purchase after unlock: unstated.

# References

**Primary Sources**

- [1] **Bulkhead / Steam** — *Pre-Load Live and Season 1 Changelog*, 9 Sep 2026. https://store.steampowered.com/news/app/1867240/view/1843481262690549. Accessed 2026-10-08.
- [2] **Bulkhead / Steam** — *WARDOGS Update 0.1.2 (Minor Patch)*, 30 Sep 2026. https://store.steampowered.com/news/app/1867240/view/1845383656376490. Accessed 2026-10-08.
- [3] **Bulkhead / Steam** — *WARDOGS Top Questions*, 18 Feb 2026. https://store.steampowered.com/news/app/1867240/view/1825093633182385. Accessed 2026-10-08.
- [4] **Valve / Bulkhead** — *WARDOGS on Steam*. https://store.steampowered.com/app/1867240/WARDOGS/. Accessed 2026-10-08.
- [5] **Bulkhead / Steam** — *IR Goggles and CIWS Balance Hotfix*, 2 Oct 2026. https://store.steampowered.com/news/app/1867240/view/1845383656386801. Accessed 2026-10-08.
- [6] **Bulkhead / Steam** — *WARDOGS Security and Stability Hotfix*, 2 Oct 2026. https://store.steampowered.com/news/app/1867240/view/1845383656384445. Accessed 2026-10-08.

**Press & Secondary**

- [7] **BisectHosting** — *WARDOGS Update 0.1.2 patch notes*. https://www.bisecthosting.com/blog/wardogs-update-0-1-2-patch-notes-bug-fixes-improvements-flythrough-exploit-fob-pallet-delivery-xp. Accessed 2026-10-08.

**Player-Reported Evidence**

- [8] **KeenGamer** — *How to build a FOB in WARDOGS: supplies and costs*. https://www.keengamer.com/articles/guides/how-to-build-a-fob-in-wardogs-supplies-and-costs/. Accessed 2026-10-08.
- [9] **allthings.how** — *WARDOGS: how to build structures with hammers and FOBs*. https://allthings.how/wardogs-how-to-build-structures-with-hammers-and-fobs/. Accessed 2026-10-08.
- [10] **KeenGamer** — *WARDOGS best base building guide, FOB layout and build order*. https://www.keengamer.com/articles/guides/wardogs-best-base-building-guide-fob-layout-build-order/. Accessed 2026-10-08.

# Further Reading

The Steam news hub at https://store.steampowered.com/news/app/1867240 for Season 02 notes.

# Related Documents

- vehicles-outposts-foundation
- vehicle-roster-and-prices
- air-and-counter-air
- cash-rewards-and-costs
- maps-environment-foundation

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft; pre-Season-02 baseline. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after independent re-verification of validate, markdownlint, links (0 dead) and Steam post ids. Pre-Season-02 baseline. | Standing mandate (auto-approve on green QA) |
