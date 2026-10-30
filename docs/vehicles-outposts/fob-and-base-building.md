---
id: fob-and-base-building
title: "FOBs, Hammers & Base Building"
version: 1.1.0
status: frozen
confidence: Medium
category: Vehicles & Outposts
topic: "FOB deployment, supply types, hammer tiers, structures, pallet logistics, costs"
market: Global
game_version: "Early Access Season 02, Update 0.2.0 (15 Oct 2026); official posts through 2026-10-15 (snapshot 2026-10-30)"
document_type: depth
created: 2026-10-08
updated: 2026-10-30
review_due: 2026-11-20
sources_verified: 2026-10-30
supersedes: null
related: [vehicles-outposts-foundation, vehicle-roster-and-prices, air-and-counter-air, cash-rewards-and-costs, maps-environment-foundation]
tags: [fob, hammer, base-building, pallets, supplies, season-02, early-access]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | fob-and-base-building |
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

This document goes deeper than the parent foundation on forward operating bases (FOBs), the three hammer tiers, supply types, buildable structures and pallet logistics. Update 0.2.0 (Season 02, notes posted 14 Oct 2026, live 15 Oct 2026) gave the first official structure costs, so the document now tabulates the 0.2.0 values with their Season 1 predecessors where the notes state them [11][12]. Season 1 (0.1.2) values remain as dated history.

The official Building Balance section is "a full pass on build costs, build speed and durability" [11]. It adds three buildables (MG Nest, Large Shelter, Wooden Step), raises most supply costs, makes the Medium Hammer contribute less per swing, severely cuts Drill Rig uptime, slows the Talon and Mortar, and lets the Halligan bar breach doors and gates while hammers no longer can [11]. FOB hacking now also pays teammates in the radius, and destroying a FOB pays a bonus based on the supplies it held; cash and XP amounts are owned by cash-rewards-and-costs [11].

Not stated in the 0.2.0 notes: hammer unlock levels and prices, the FOB vendor price, structure health, build radius and FOB count limits, and whether Season 1 hammer values were changed. The notes do not mention a progression wipe. Confidence is Medium: costs and changes are official and Primary [11], but the build procedure, hammer-to-structure mapping for older structures and supply types still rest on player-reported guides [8][9][10].

# Key Takeaways

- Official, Update 0.2.0 (14 to 15 Oct 2026): new buildables MG Nest (Large Hammer), Large Shelter (Medium Hammer and above) and Wooden Step (Small Hammer and above) [11].
- Official, 0.2.0 build supply costs (old to new): Door 22 to 80, Gate 85 to 200, L81 Mortar 150 to 600, Stingray 150 to 650, Talon 9K-SAM 1,000 to 650, Vanguard CIWS 1,500 to 1,200, Hot Zone Magnet 2,250 to 2,750; MG Nest 650, Large Shelter 250, Wood Base 15 [11].
- Official, 0.2.0: Medium Hammer contributes less per swing, critical spots give a smaller bonus, Large Hammer build rate per swing unchanged [11].
- Official, 0.2.0: the Halligan bar can breach doors and gates; hammers no longer can [11]. Destroying structures, FOB hacking and FOB destruction rewards: see cash-rewards-and-costs [11].
- Official, 0.2.0 Drill Rig: minimum activation fuel 1,500 to 2,000; duration per fuel 0.05 to 0.03 (max uptime 375 s to 300 s); max fuel 7,500 to 10,000; longer post-spawn cooldown [11].
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

Update 0.2.0 (15 Oct 2026) changes are in the new "Update 0.2.0 Building Balance" section below [11][12]. The bullets here are the Season 1 / 0.1.2 state (2026-10-08, neither 2 Oct hotfix changed hammers, FOBs or pallets) [2][5][6]; the 0.2.0 notes do not restate these hammer, FOB-price or unlock values, so they are neither confirmed nor shown changed [11].

- The FOB costs $7,500 at the vendor [1].
- The Large Hammer costs $2,400 at the vendor, and unlocks on the Support track at level 8 for $75,000; the Medium Hammer unlock is $25,000 [1].
- Destroying a buildable pays a reward scaled by its build progress [2].
- Depositing pallets into a FOB outside the zone pays a reduced reward [2].
- Buildable crit spots no longer reappear in the same place, get pushed into corners or jump to the far side of a structure [2].
- A crash involving buildables was fixed at Season 1 launch [1].
- The 2 Oct IR Goggles and CIWS hotfix made the CIWS destroy the Havoc in about 6 seconds instead of 12 [5]; guides list the CIWS as a Large-tier structure [8][10].

# Detail

## Update 0.2.0 Building Balance

Source: Season 02 patch notes, posted 14 Oct 2026, live 15 Oct 2026 [11][12]. All figures below are build supply costs unless stated; "old" is the Season 1 (0.1.2) value the notes give. Where the notes show only a new value, old is "not stated".

| Buildable | Old (0.1.2) | New (0.2.0) |
|-----------|-------------|-------------|
| Wood Base | not stated | 15 |
| Bremmer wall | 15 | 32 |
| Door | 22 | 80 |
| Gate | 85 | 200 |
| Large Shelter | not stated | 250 |
| Air raid shelter, bunker, crow's nest | 100 | 200 |
| L81 Mortar | 150 | 600 |
| Stingray | 150 | 650 |
| MG Nest | not stated | 650 |
| Talon 9K-SAM | 1,000 | 650 |
| Vanguard CIWS | 1,500 | 1,200 |
| Hot Zone Magnet | 2,250 | 2,750 |

New buildables and the hammer that builds them [11]:

| Buildable | Description (notes) | Built with |
|-----------|---------------------|------------|
| Wooden Step | "A step. Made of wood." | Small Hammer and above |
| Large Shelter | large metal shelter for covering key assets or keeping the rain off | Medium Hammer and above |
| MG Nest | manned M2 Browning emplacement | Large Hammer |

Build speed [11]: the Medium Hammer now contributes less per swing; critical spots give a smaller bonus than before; the Large Hammer build rate per swing is unchanged. Numeric rates are not stated. The stated aim is to make structures "a considered investment rather than something you spam" without hard limits on player freedom [11].

Drill Rig (severe cut to active time, to stop multi-rig builds dominating) [11]:

| Setting | Season 1 (0.1.2) | Season 02 (0.2.0) |
|---------|------------------|-------------------|
| Minimum fuel to activate | 1,500 | 2,000 |
| Duration per fuel | 0.05 (max uptime 375 s) | 0.03 (max uptime 300 s, "matches capturable towers") |
| Max fuel | 7,500 | 10,000 |
| Post-spawn cooldown | not stated | "substantially increased"; a destroyed rig cannot immediately be replaced |

Buildable weapons [11]: Talon reload 2 s to 5 s and restock from munition supplies 50 to 200; Mortar restock from munition supplies 75 to 150 ("to reduce the amount of shots that can be fired per pallet drop-off") and a new firing animation where the player drops the shell in as it fires, slowing fire rate.

Misc building changes [11]:

- Barbed wire and sandbags can be placed on top of Bremmer walls; barbed wire no longer gives cash or XP on kills.
- Foundations fit against slopes, stairs and walls; unfinished buildables collapse as soon as they lose a support instead of floating; tank traps can only be placed on a defined set of surfaces.
- Doors and gates can no longer be breached with a hammer; the Halligan bar can now breach both (Halligan breaching rewards, uses and vendor price: see cash-rewards-and-costs [11]).
- CIWS cannon damage against structures was "properly tuned": it shreds light cover and struggles against heavy fortifications, with no numbers stated [11]. Separately the Vanguard CIWS now takes 2.25x longer to kill the team Spawn Vehicle [11].

FOB hacking and destruction (amounts in cash-rewards-and-costs) [11]: hacking a FOB now also rewards teammates in the FOB radius (the hacker's own reward is unchanged); destroying a FOB pays a bonus based on the supplies it held, maxed at 25,000 supplies. Destroying a buildable now pays cash equal to its build supply cost, with XP about 25% of the cash, scaled by how built it is, and its XP is now assault XP rather than support [11]. FOB Supplied Assist is split between assisting players [11]. The notes state cash and XP pay amounts for these rewards; see cash-rewards-and-costs for the table rather than a copy here.

Logistics note [11]: base logistics rewards are lower, with new delivery streaks; the notes were edited after posting to give values including the Control Zone multiplier. Values: cash-rewards-and-costs.

## Baseline values

Source class: Official = Steam announcement posts; Player = player-reported guide, not independently verified. "Season 1.0" is the 9 Sep 2026 changelog. Rows are Season 1 / 0.1.2 history; where Update 0.2.0 changed a row it is flagged in the previous section.

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
| Supply costs: Bunker 61, Mortar 91, Repair Station 121, Talon 601, CIWS 901, Drill Rig 1,351 | Season 1 era | Player [9]; contradicted by the official old values in the notes (Mortar 150, Talon 1,000, CIWS 1,500, bunker 100) [11], so treat as unreliable |
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

Official 0.2.0 costs for named buildables are in the Building Balance section above [11]; there is still no complete official structure list (Repair and Refuel Stations, Drill Rig, sandbags and hedgehogs have no stated build cost). The earlier player-reported figures (Bunker 61, Mortar 91, Repair Station 121, Talon 601, CIWS 901, Drill Rig 1,351) [9] disagree with the official old values and are retained only as history. Repair Stations repair and Refuel Stations refuel vehicles from stored supplies; the Drill Rig is reported to pull the Hot Zone toward a fuelled FOB [10]. Gates admit vehicles, doors are infantry-only, hedgehogs block vehicle routes [9]. Official: the CIWS was rebalanced on 2 Oct 2026 [5].

## Pallet delivery and the 0.1.2 reward reduction

Pallets are the logistics unit for moving supplies into a FOB; cargo vehicles carry small amounts and larger loads move on pallets (player-reported) [9]. Update 0.1.2 states: "Depositing pallets into a FOB outside the zone now awards reduced rewards" [2]. A press summary lists the same change among the cash and XP exploit fixes [7]. The size of the reduction and the zone boundary are not published. The post frames the change as anti-exploit and warns that players abusing repeatable exploits risk a permanent ban [2]. Supply crate sale XP was cut separately in Season 1 [1].

## Build-destroy interaction

Official: "Any rewards for destroying buildables now scale with their build progress - so destroying a placed schematic no longer gives a full reward" [2]. Rocket launchers can take down apartment blocks per the store page [4]. Player-reported: anything built can be destroyed, artillery can level fortifications from outside the zone, and unprotected pallets can be destroyed [8][9]. For diffing: reward scaling is by build progress, with no published curve.

# Early Access Changes & Known Issues

- 9 Sep 2026, Season 1: FOB $2,500 to $7,500; Large Hammer vendor $1,600 to $2,400; Medium Hammer unlock $10,000 to $25,000; Large Hammer unlock $25,000 to $75,000 and level 7 to 8; supply crate rescale; buildables crash fixed [1].
- 30 Sep 2026, Update 0.1.2: reduced pallet deposit rewards outside the FOB zone; destruction rewards scale with build progress; buildable crit spot fix [2].
- 2 Oct 2026: security hotfix without gameplay changes [6]; CIWS kill time on Havoc halved [5].
- 14 to 15 Oct 2026, Update 0.2.0 / Season 02: Building Balance pass (costs, build speed, Drill Rig, Talon, Mortar, misc), three new buildables, Halligan breaching, CIWS structure damage tuning, FOB hacking and FOB destroy rewards [11][12]. No progression wipe is mentioned in the notes. No official post after 2026-10-15 appears in the 2026-10-30 snapshot.

# Admin & Technical Notes

None found specific to FOBs or hammers. No official server setting for buildable limits appears in the posts retrieved.

# Risks & Caveats

- Supply types, hammer-to-structure mapping and structure supply costs are player-reported only and may be wrong or stale [8][9][10].
- Guides mix pre-Season-1 and Season 1 values; the official changelog overrides them where it speaks [1].
- Later hotfixes may have changed 0.2.0 values; none seen in the 2026-10-30 snapshot, which is not proof none exist.
- Hammer unlock levels and prices in this document are Season 1 values; the 0.2.0 notes neither restate nor change them.

# Open Questions

- Source of the $800 hammer figure: not found in official or press text; resolve by an in-game vendor check.
- Complete official list of buildables and supply costs: partial only (0.2.0 notes name 12 cost rows); Repair/Refuel Station, Drill Rig and Small Hammer structures not costed.
- Numeric Medium Hammer swing contribution, critical-spot bonus and CIWS-versus-structure damage: not stated.
- Whether Season 1 hammer unlocks and the $7,500 FOB price still hold in Season 02: the notes do not say.
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
- [11] **Bulkhead / Steam News** — *WARDOGS | Season 02 Patch Notes*, 14 Oct 2026 (includes in-post logistics update). https://store.steampowered.com/news/app/1867240/view/1846651706674560. Accessed 2026-10-30.
- [12] **Bulkhead / Steam News** — *WARDOGS Season 02 is now live*, 15 Oct 2026. https://store.steampowered.com/news/app/1867240/view/1846651706677015. Accessed 2026-10-30.

**Press & Secondary**

- [7] **BisectHosting** — *WARDOGS Update 0.1.2 patch notes*. https://www.bisecthosting.com/blog/wardogs-update-0-1-2-patch-notes-bug-fixes-improvements-flythrough-exploit-fob-pallet-delivery-xp. Accessed 2026-10-08.

**Player-Reported Evidence**

- [8] **KeenGamer** — *How to build a FOB in WARDOGS: supplies and costs*. https://www.keengamer.com/articles/guides/how-to-build-a-fob-in-wardogs-supplies-and-costs/. Accessed 2026-10-08.
- [9] **allthings.how** — *WARDOGS: how to build structures with hammers and FOBs*. https://allthings.how/wardogs-how-to-build-structures-with-hammers-and-fobs/. Accessed 2026-10-08.
- [10] **KeenGamer** — *WARDOGS best base building guide, FOB layout and build order*. https://www.keengamer.com/articles/guides/wardogs-best-base-building-guide-fob-layout-build-order/. Accessed 2026-10-08.

# Further Reading

The Steam news hub at https://store.steampowered.com/news/app/1867240 for any posts after 2026-10-15.

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
| 1.1.0 | 2026-10-30 | Research Pipeline (virtual agent) | Revised for Season 02 / Update 0.2.0 from the official patch notes (14 Oct) and release post (15 Oct): Building Balance (new buildables and hammers, supply cost table, build speed, Drill Rig, Talon, Mortar, misc, Halligan breaching, CIWS vs structures), FOB hacking and destroy rewards (linked), Season 1 values kept as dated history; guide supply costs flagged as contradicted; Open Questions and Risks updated. | — |
