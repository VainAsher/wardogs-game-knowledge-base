---
id: air-and-counter-air
title: "Air Vehicles & Counter-Air"
version: 1.1.0
status: frozen
confidence: Medium
category: Vehicles & Outposts
topic: "Helicopters, aircraft, anti-air systems (Vanguard CIWS, Talon 9K-SAM, Flakpanzer Gepard, Havoc), pilots, IR countermeasures"
market: Global
game_version: "Early Access Season 02, Update 0.2.0 (15 Oct 2026); official posts through 2026-10-15 (snapshot 2026-10-30)"
document_type: depth
created: 2026-10-08
updated: 2026-10-30
review_due: 2026-11-20
sources_verified: 2026-10-30
supersedes: null
related: [vehicles-outposts-foundation, vehicle-roster-and-prices, fob-and-base-building, gadgets-armor-and-equipment, damage-ballistics-and-balance, progression-unlock-tables, cash-rewards-and-costs]
tags: [helicopters, pilot-track, anti-air, ciws, talon, gepard, havoc, ir-rangefinder, season-2, update-0-2-0, season-1-history, early-access]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | air-and-counter-air |
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

This document goes deeper than the parent foundation on WARDOGS aircraft (all helicopters in Early Access) and the systems that counter them. Update 0.2.0 (Season 02, patch notes 14 Oct 2026, live 15 Oct 2026) is the first official source with numbers for most of this topic [9][10]. It adds the Flakpanzer Gepard as a vehicle-mounted anti-air option (Driver level 25, $300,000 unlock, $14,000 spawn), cuts the build cost of the Talon 9K-SAM (1,000 to 650 supplies) while slowing its reload (2 s to 5 s), cuts the Vanguard CIWS build cost (1,500 to 1,200), makes the Little Bird AH-6M [Miniguns] unlock later and cost more, raises the vendor price of every listed armed helicopter, and makes helicopter cockpit glass work both ways [9].

The Season 1 position (Update 0.1.2 plus the 2 Oct 2026 hotfix) is kept as dated history: the CIWS time to destroy a Havoc was halved from about 12 s to about 6 s, and IR Rangefinders were pulled from the vendor until Season 02 [3][4]. The notes also describe the Infrared Range Finder as battery-powered (about 80 s of active use) [9].

Confidence is Medium. Every Season 02 number is Primary, but the Season 1 roster, levels and anti-air costs came only from conflicting player guides, several levels are still not stated by any official post (Lakota, Havoc, AH-6R, MH-6), and sling-loading remains unconfirmed. The 2026-10-30 snapshot has no official post after 2026-10-15 [10].

# Key Takeaways

- 0.2.0 (15 Oct 2026): Flakpanzer Gepard is official, "Anti Air Vehicle", Driver level 25, $300,000 to unlock, $14,000 at the vendor [9]. The Season 1 guide claims of a "Wardog track" unlock and an $8,000-$10,000 price were wrong or outdated [12][13].
- 0.2.0: Talon 9K-SAM build cost 1,000 to 650 supplies, reload 2 s to 5 s, restock from munition supplies 50 to 200; Vanguard CIWS build cost 1,500 to 1,200; CIWS cannon damage to structures retuned; CIWS now takes 2.25x longer to kill the Spawn Vehicle [9].
- 0.2.0: Little Bird AH-6M [Miniguns] Pilot 4 to 8, unlock $50,000 to $125,000, spawn $7,000 to $12,000; Z20 Lakota [Miniguns] unlock $75,000 to $85,000, spawn $8,000 to $15,000; Havoc unlock $500,000 to $650,000, spawn $18,000 to $28,000; AH-6R spawn $12,500 to $18,800 [9].
- 0.2.0: helicopter cockpit glass works both ways, so shooting out through it damages the vehicle as much as incoming fire [9].
- 0.2.0: the calibre base-damage cuts apply to the Little Bird AH-6M Minigun and Z20 Lakota Minigun; the notes do not name the calibre [9].
- Season 1 history (2 Oct 2026): CIWS time to destroy a Havoc about 12 s to about 6 s [4].
- Fighter jets are named only by the 2026-10-08 store capture; no Season 02 post mentions them [1][9]. Sling-loading is unconfirmed in every source read.

# Scope

Covers helicopter and air roster, Pilot-track gating, anti-air (vehicle and base-built), countermeasures and cockpit-glass behaviour, the Season 02 (0.2.0) changes and the Season 1 history, and sling-loading status. Excludes general ground vehicles and the full price list (vehicle-roster-and-prices, price-tables-season-1), FOB mechanics and build-cost tables (fob-and-base-building), handheld gadgets (gadgets-armor-and-equipment), damage models (damage-ballistics-and-balance), full unlock tables (progression-unlock-tables) and reward values (cash-rewards-and-costs). Version: Update 0.2.0 (15 Oct 2026).

# Definitions

- **Pilot track**: progression track unlocking helicopters; Season 1 player reports said only helicopter time advances it [13].
- **Havoc**: the top attack helicopter; official posts name it [3][4][9].
- **Vanguard CIWS**: the base-built close-in weapon system, called "CIWS" in the 2 Oct 2026 post and "Vanguard CIWS" in the 0.2.0 notes; the community calls it "Sea Whiz" [4][9][11].
- **Talon 9K-SAM**: the base-built surface-to-air missile emplacement named in the 0.2.0 notes [9].
- **Flakpanzer Gepard**: the anti-air vehicle added in 0.2.0 [9].
- **IR Rangefinder / Infrared Range Finder**: vendor item; the 2 Oct 2026 post title says "IR Goggles" [4][9].
- **Countermeasures**: a vendor-tile field and key `V` in one Season 1 guide; the 0.2.0 notes mention a vehicle's smoke screen and flares [9][13].

# Current State

As of Update 0.2.0 (15 Oct 2026).

- Season 02 went live on 15 Oct 2026 after a maintenance window of 08:00 to 09:30 UTC [9][10].
- The Flakpanzer Gepard is a new Driver-track vehicle (level 25, $300,000 unlock) with a $14,000 vendor price [9].
- Base-built anti-air changed: Talon 9K-SAM 1,000 to 650 supplies and Vanguard CIWS 1,500 to 1,200, all build supply costs [9]. The wider build-cost and Talon rebalance is owned by fob-and-base-building.
- The Little Bird AH-6M [Miniguns] moved to Pilot level 8 for $125,000. The notes say it "was too strong for how early it unlocked" [9].
- Purchased-vehicle inventories are private to the driver and their squad by default, which includes purchased helicopters; free team-spawn vehicles stay open to everyone [9].
- A vehicle's smoke screen and flares now appear for players who joined late [9].
- The Infrared Range Finder now runs on batteries: about 80 s of active use per battery, draining faster if toggled quickly on and off [9]. It is priced at $3,200 (was $1,200) [9]. Whether it is back on sale in the vendor is not stated in the notes; the 2 Oct 2026 post said it was disabled "until Season 02" [4].
- The Steam store page (live capture 2026-10-08) promotes ferrying supplies to teammates by helicopter and lists "new vehicle types including fighter jets" among planned additions, with no date or roster [1]. The 2026-10-30 store data still carries the helicopter line [2]; the fighter-jet wording is not present in that data, and no official post says it was dropped or kept [2].

# Detail

## Season 02 (0.2.0) air roster and prices

All rows from the Season 02 patch notes (14 Oct 2026) [9]. "Not stated" means the notes give no value.

| Aircraft | Pilot level | Unlock (S1 to 0.2.0) | Spawn price (S1 to 0.2.0) | Destroyed reward (S1 to 0.2.0) |
|----------|-------------|----------------------|----------------------------|--------------------------------|
| Little Bird AH-6M [Miniguns] | 8 (was 4) | $50,000 to $125,000 | $7,000 to $12,000 | $6,000 (new per-variant value) |
| Little Bird AH-6R [Rockets] | not stated | not stated | $12,500 to $18,800 | $9,400 (new) |
| Z20 Lakota [Miniguns] | not stated | $75,000 to $85,000 | $8,000 to $15,000 | $7,500 (new) |
| Z20 Lakota (unarmed) | not stated | not stated | not stated | $3,700 to $1,500 |
| MH-6 | not stated | not stated | not stated | $3,125 to $1,250 |
| Havoc | not stated | $500,000 to $650,000 | $18,000 to $28,000 | $18,000 to $14,000 |

Reward values are owned by cash-rewards-and-costs; they are shown for the air-combat trade-off only. Armed variants give 1.5x the XP of the default variant, and repair XP now goes into the pilot or driver track depending on the vehicle repaired [9]. The Gold Market gains a "Black & Gold" Little Bird camo and a "Two-Tone Desert" Havoc camo [9].

## Counter-air options (0.2.0)

| Option | How it is obtained | 0.2.0 facts | Source |
|--------|--------------------|-------------|--------|
| Flakpanzer Gepard | Driver track, level 25, $300,000; $14,000 at vendor | New in 0.2.0; destroyed reward $7,000 | [9] |
| Talon 9K-SAM | Base-built; build cost 650 supplies (was 1,000) | Reload 2 s to 5 s; restock from munition supplies 50 to 200; destroyed reward $2,000 to $650 | [9] |
| Vanguard CIWS | Base-built; build cost 1,200 supplies (was 1,500) | Cannon damage against structures retuned ("shreds light cover and struggles against heavy fortifications"); 2.25x longer to kill the Spawn Vehicle; destroyed reward $3,000 to $1,200 | [9] |
| Smoke screen and flares | Vehicle equipment | Now appear for late joiners; flare deployables took more loadout room since 10 Sep 2026 | [9][5] |

The notes give no damage, range, ammunition or seat figures for the Gepard, Talon or CIWS against aircraft, and do not say which hammer builds the Talon or CIWS. The Season 1 foundation placed anti-air among Large Hammer builds and Ammo as the supply for CIWS and SAM (player-reported) [15]. One Season 1 guide gave the CIWS build cost as 901 supplies [14]; the 0.2.0 notes give the old value as 1,500, which conflicts, so the 901 figure is not used (the notes may be counting a different supply type, no source says).

## Helicopter combat and handling changes (0.2.0)

- Cockpit glass: "now works both ways", shooting out through it damages the vehicle the same as incoming fire [9].
- Calibre base-damage cuts (.308 -25%, 7.62x54mmR -20%, 7.62x39mm -19%, .50 Cal -16%) apply to vehicle weapons, and the notes name the Little Bird AH-6M Minigun and the Z20 Lakota Minigun. The notes do not say which round those miniguns fire, so which cut applies is not stated [9].
- MGL-40 on the Little Bird bench seat: much more inaccuracy and sway, slower ADS and a reload penalty "to reduce reliability" [9].
- Parachutes: slower to open and will not open below about 10 m; opening below roughly 50 m while falling fast means fall damage. The notes add "Make sure you trust a pilot before getting into their aircraft" [9]. Basic Parachute $100 to $500, Sport Parachute $1,000 to $700 [9].
- Exiting a vehicle now places the player on the ground rather than pushing through it [9].
- Handling changes in the notes are for tracked vehicles, the Humvee and the Dune Buggy; no helicopter flight-model change is listed [9].

## Season 1 history (0.1.2 and earlier)

| Value | As-of version | Source |
|-------|---------------|--------|
| CIWS time to destroy Havoc: about 6 s (was about 12 s) | Hotfix 2 Oct 2026 | official [4] |
| IR Rangefinder: removed from vendor until Season 02; batteries required on return | 2 Oct 2026 | official [4] |
| Fly-through reward: capped (no figure published) | 0.1.2, 30 Sep 2026 | official [3] |
| Havoc 20mm/30mm damage-taken bug: fixed | 0.1.2 | official [3] |
| Flare deployable loadout space: increased (no figure) | Season 1, 10 Sep 2026 | official [5] |
| Lakota balance and pitch fix, helicopter input damping | Season 1, 10 Sep 2026 | official [5] |
| AH-6M $7,000, Pilot 4, unlock $50,000 | Season 1 | player-reported [13]; now corroborated by 0.2.0 "old" values [9] |
| AH-6R $12,500, Pilot 20, unlock $250,000 | Season 1 | player-reported [13]; spawn price corroborated by [9] |
| Z20 Lakota [Miniguns] $8,000, unlock $75,000 | Season 1 | player-reported [13]; corroborated by [9] |
| Z20 Lakota $7,400 / Pilot 10 [12] or Pilot 25 [13] | Season 1 | player-reported, conflict, still unresolved |
| MH-6 about $6,250 | Season 1 | player-reported [12]; no price in [9] |
| Havoc $18,000, Pilot 35 | Season 1 | player-reported [12][13]; price corroborated by [9] |
| Gepard about $8,000 [12] / $10,000 [13], "Wardog track" | Season 1 | player-reported, conflicting; superseded by [9] |
| CIWS build cost 901 supplies | Season 1 | player-reported [14]; conflicts with [9] |

The Season 1 guides say transport helicopters carry no offensive armament and that a free large transport helicopter and an SUV appear at team spawn a few minutes into a match (player-reported) [12][13].

## Press conflict of 2 Oct 2026 (history)

The official post "IR Goggles & CIWS Balance Hotfix" (15:39 UTC) is separate from the "Security & Stability Hotfix" announced for 08:00 UTC that day [4][6]. InGameNews reported that the 2 Oct hotfix had no gameplay changes, which is true only of the security hotfix [6][11]. Timesaver.gg and MMOEXP (player-reported) reported the IR nerf and the CIWS 12 s to 6 s change, which match the official post [4][16][17].

## Sling-loading

Unconfirmed. The official posts including the 0.2.0 notes, the Steam page and both vehicle guides never mention it; guides describe supply drops from the seat (`G` drops a crate) [12][13][9]. The store page's helicopter supply ferrying is not described as sling-loading [1].

# Early Access Changes & Known Issues

- 10 Sep 2026, Season 1 changelog: Lakota balance and pitch fix, helicopter input damping, flare deployables take more room [5].
- 30 Sep 2026, 0.1.2: fly-through exploit fix with capped rewards; Havoc cannon-damage bug fix [3].
- 2 Oct 2026 00:13 UTC: security hotfix announced, one hour of downtime [6].
- 2 Oct 2026 15:39 UTC: IR Rangefinder removal and CIWS 12 s to 6 s [4].
- 22 Sep 2026, Season 02 Teaser: announced the 15 Oct 2026 Season 02 date; the outcome is the 0.2.0 entry below [7].
- 9 Oct 2026, Season 02 Preview: named the Flakpanzer Gepard as an "Anti Air Vehicle" with other new vehicles; the final notes renamed the tank and wheeled vehicles but kept the Gepard name [8][9].
- 14 Oct 2026 (patch notes) and 15 Oct 2026 (live), Update 0.2.0: Gepard added; Talon and CIWS rebalanced; Little Bird, Lakota and Havoc prices and unlocks raised; cockpit glass two-way; calibre cuts applied to vehicle miniguns; private vehicle inventories; late-joiner smoke and flares fixed [9][10].
- None seen in the 2026-10-30 snapshot: no official post after 2026-10-15 is saved, so later hotfixes are unknown.
- Planned: fighter jets "for the fuller game" per the 2026-10-08 store capture, with no date [1].

# Admin & Technical Notes

None found. No server setting for air vehicles or anti-air was seen in the official posts retrieved.

# Risks & Caveats

- Any value can change at any time; the review date is 2026-11-20.
- Season 1 levels and anti-air costs are player-reported and conflict; only rows restated as "old" values in the 0.2.0 notes are corroborated [9].
- The 0.2.0 notes list changed values only, so unchanged values (for example Havoc, Lakota and AH-6R Pilot levels) are absent from official text.
- The 2 Oct post title and body differ (Goggles vs Rangefinders); this document follows the body [4].
- Whether the Talon, CIWS and Gepard are effective against particular aircraft is not covered by any source; no combat claim is made.

# Open Questions

- Which calibre the Little Bird and Lakota miniguns use, and so which 0.2.0 cut applies.
- Whether the Infrared Range Finder is back in the vendor in 0.2.0 (the notes give a price and battery behaviour but no availability statement).
- Pilot levels for Lakota, Havoc and AH-6R in Season 02; Season 1 guides conflict and the notes do not state them.
- Whether the Gepard has a fixed seat count or a gunner seat; unpublished.
- The 901-supply CIWS figure versus the notes' 1,500 supplies: which supply type or version differs.
- Is external sling-loading present? Unconfirmed.
- Fighter jets: planned per the 2026-10-08 store capture, absent from the 2026-10-30 store data; no timing or roster stated.
- Whether any hotfix after 2026-10-15 changed these values: none seen in the 2026-10-30 snapshot.

# References

**Primary Sources**

- [1] **Valve / Bulkhead** — *WARDOGS on Steam* (store page, browser-rendered live capture 2026-10-08, snapshots/2026-10-08/store-page-live.txt). https://store.steampowered.com/app/1867240/WARDOGS/. Accessed 2026-10-08.
- [2] **Valve / Bulkhead** — *WARDOGS on Steam* (store data, snapshots/2026-10-30/store-app-us.json). https://store.steampowered.com/app/1867240/WARDOGS/. Accessed 2026-10-30.
- [3] **BULKHEAD** — *WARDOGS | Update 0.1.2 (Minor Patch)*, Steam announcement, 30 Sep 2026. https://store.steampowered.com/news/app/1867240/view/1845383656376490. Accessed 2026-10-08.
- [4] **BULKHEAD** — *IR Goggles & CIWS Balance Hotfix*, Steam announcement, 2 Oct 2026. https://store.steampowered.com/news/app/1867240/view/1845383656386801. Accessed 2026-10-08.
- [5] **BULKHEAD** — *Season 1 changelog (pre-load live)*, Steam announcement, 9 Sep 2026. https://store.steampowered.com/news/app/1867240/view/1843481262690549. Accessed 2026-10-08.
- [6] **BULKHEAD** — *WARDOGS | Security & Stability Hotfix*, Steam announcement, 2 Oct 2026. https://store.steampowered.com/news/app/1867240/view/1845383656384445. Accessed 2026-10-08.
- [7] **BULKHEAD** — *WARDOGS | Season 02 Teaser*, Steam announcement, 22 Sep 2026. https://store.steampowered.com/news/app/1867240/view/1844115010504839. Accessed 2026-10-08.
- [8] **BULKHEAD** — *WARDOGS | Season 02 Preview*, Steam announcement, 9 Oct 2026. https://store.steampowered.com/news/app/1867240/view/1846018067933823. Accessed 2026-10-30.
- [9] **BULKHEAD** — *WARDOGS | Season 02 Patch Notes*, Steam announcement, 14 Oct 2026. https://store.steampowered.com/news/app/1867240/view/1846651706674560. Accessed 2026-10-30.
- [10] **BULKHEAD** — *WARDOGS | Season 02 is now live*, Steam announcement, 15 Oct 2026. https://store.steampowered.com/news/app/1867240/view/1846651706677015. Accessed 2026-10-30.

**Press & Secondary**

- [11] **InGameNews** — *WARDOGS update 0.1.2 and security hotfix, a comparative overview*. https://ingamenews.com/gaming-news/wardogs-update-0-1-2-and-security-hotfix-a-comparative-overview/. Accessed 2026-10-08.

**Player-Reported Evidence**

- [12] **GameBrief** — *WARDOGS vehicles guide 2026*. https://www.gamebrief.net/blog/wardogs-vehicles-guide-2026. Accessed 2026-10-08.
- [13] **allthings.how** — *WARDOGS: how to get a vehicle, prices and unlock levels*. https://allthings.how/wardogs-how-to-get-a-vehicle-prices-and-unlock-levels/. Accessed 2026-10-08.
- [14] **allthings.how** — *WARDOGS: how to build structures with hammers and FOBs*. https://allthings.how/wardogs-how-to-build-structures-with-hammers-and-fobs/. Accessed 2026-10-08.
- [15] **KeenGamer** — *How to build a FOB in WARDOGS: supplies and costs*. https://www.keengamer.com/articles/guides/how-to-build-a-fob-in-wardogs-supplies-and-costs/. Accessed 2026-10-08.
- [16] **Timesaver.gg** — *WARDOGS IR goggles and CWIS hotfix* (sells boosting services). https://timesaver.gg/blog/wardogs-ir-goggles-cwis-hotfix. Accessed 2026-10-08.
- [17] **MMOEXP** — *WARDOGS October 2 update, Season 2 wipe, IR rangefinder nerf and new weapons* (single podcast source). https://www.mmoexp.com/News/wardogs-october-2-update-season-2-wipe-ir-rangefinder-nerf-and-new-weapons.html. Accessed 2026-10-08.

# Further Reading

Steam News hub: https://store.steampowered.com/news/app/1867240 for later notes.

# Related Documents

- vehicles-outposts-foundation
- vehicle-roster-and-prices
- fob-and-base-building
- gadgets-armor-and-equipment
- damage-ballistics-and-balance
- progression-unlock-tables
- cash-rewards-and-costs

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft; pre-Season-02 baseline. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after independent re-verification of validate, markdownlint, links (0 dead) and Steam post ids. Pre-Season-02 baseline. | Standing mandate (auto-approve on green QA) |
| 1.0.1 | 2026-10-08 | Orchestrator | Relabelled the fighter-jets claim as unverified (absent from the saved store data and all official posts). | Standing mandate (auto-approve on green QA) |
| 1.0.2 | 2026-10-08 | Research Pipeline (revision worker) | Corrected against live store-page capture; restored fighter jets as Primary (store page, live capture 2026-10-08), added helicopter supply-ferrying wording, updated Key Takeaways, Current State, Executive Summary, Open Questions and reference [1]. | Standing mandate (auto-approve on green QA) |
| 1.1.0 | 2026-10-30 | Research Pipeline (virtual agent) | Revised for Update 0.2.0: added Flakpanzer Gepard, Talon 9K-SAM and Vanguard CIWS changes, Little Bird, Lakota and Havoc price and unlock changes, cockpit glass, calibre cuts on vehicle miniguns, IR Range Finder batteries, private vehicle inventories; kept Season 1 and 2 Oct values as history; replaced the forward-looking Season 02 wipe statements with the known outcome. | — |
