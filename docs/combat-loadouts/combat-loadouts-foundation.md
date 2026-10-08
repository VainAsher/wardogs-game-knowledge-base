---
id: combat-loadouts-foundation
title: "Combat & Loadouts: Foundation"
version: 1.0.0
status: frozen
confidence: Medium
category: Combat & Loadouts
topic: "Weapons, gadgets, classes, damage and ballistics"
market: Global
game_version: "Early Access Season 1, patch 0.1.2 (30 Sep 2026, per secondary reproduction of official notes); Steam page checked 2026-10-08"
document_type: foundation
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [gameplay-modes-foundation, economy-foundation, vehicles-outposts-foundation]
tags: [combat, weapons, loadouts, roles, ballistics, early-access]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | combat-loadouts-foundation |
| Version | 1.0.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Combat & Loadouts |
| Game version | Early Access Season 1, patch 0.1.2 (30 Sep 2026) |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

WARDOGS has no fixed class selection at spawn. Each life, a player spends cash at a vendor to build a custom loadout of weapons, gear, utility and vehicles [1]. Experience is earned on role tracks (Assault, Medic, Recon, Support, Driver, Pilot) that gate which items can be bought [6]. Gunplay is described by the developer as realistic but tuned for gameplay rather than simulation [1].

The official Steam page confirms the loadout-per-life model, melee, sniping, destructible environments and buildable forward operating bases, but it publishes no weapon list, damage values or ballistic parameters [1]. Specific weapon names, prices and category-to-track mappings in this document come from press and player-reported coverage, much of it from the closed beta, and are labelled as such.

Document confidence is Medium: the structural model is official, but the weapon-level detail rests on secondary, partly pre-release sources, and the official Season 1 patch text could not be retrieved directly (see Open Questions).

# Key Takeaways

- Loadouts are bought with cash each life from a vendor; players start with $10,000 and cash persists between matches (Steam page, checked 2026-10-08) [1].
- There is no spawn-time class pick; six role tracks (Assault, Medic, Recon, Support, Driver, Pilot) gate unlocks, plus an account-wide WARDOG Level (player-reported, Sep 2026) [6].
- Gunplay is "realistic gunplay tuned for gameplay"; destructible buildings and melee exist [1].
- A beta-era press list recorded 33 weapons in the vendor, with 37 expected at Early Access launch; prices were explicitly not confirmed as final [5].
- Ballistics: press reports bullet drop and travel time are modelled; no damage numbers are officially published [5].
- Season 1 patch notes (10 Sep 2026) moved many unlock levels and prices and slowed role XP between levels 10 and 20 [3].
- Patch 0.1.2 (30 Sep 2026) validates revives server-side, bars throwables from enclosed vehicle seats and fixed a Havoc bug that raised 20mm/30mm cannon damage taken [4].

# Scope

Covers infantry combat, weapon categories and notable weapons, gadgets and equipment, the role/progression system as it relates to loadouts, the documented damage/ballistics model, and how loadout purchasing ties to the in-match economy. Game version: Early Access Season 1 through patch 0.1.2.

Excluded: vehicle combat detail (see vehicles-outposts-foundation), mode rules (gameplay-modes-foundation), full economy mechanics (economy-foundation), per-weapon stat tables (depth documents).

# Definitions

- **Loadout**: the set of weapons, gear, utility and vehicles bought for one life [1].
- **Role track**: per-role XP progression; the player-reported tracks are Assault, Medic, Recon, Support, Driver, Pilot [6].
- **WARDOG Level**: account-wide level that unlocks general items such as armor, backpacks, ammo types and sidearms (player-reported) [6].
- **Re-buy Loadout**: vendor option that rebuilds the previous kit after death (player-reported) [6].

# Current State

- Each player starts with $10,000 and buys a custom loadout of weapons, gear, utility and vehicles each life; cash persists between matches (Steam page, 2026-10-08) [1].
- Teamwork earns cash, including reviving squadmates, transporting friendlies to the zone and controlling the objective [1].
- The developer describes realistic gunplay tuned for gameplay, sniping with items such as a ghillie suit, melee combat, destructible environments (rocket launchers can destroy apartment blocks) and buildable forward operating bases [1].
- Planned additions include more weapons and weapon categories, deeper progression and a seasonal meta [1].
- Season 1 patch notes were posted on Steam news on the 10 Sep 2026 launch, titled "Pre-Load Live & Season 1 Changelog" [2]. Their contents as summarised by press are in Detail [3].
- Patch 0.1.2 is dated 30 Sep 2026 in a BisectHosting reproduction of the official notes [4]. It is the latest patch this document could verify; the Steam news feed itself was not machine-readable (see Open Questions).

# Detail

## Loadout selection and economy

Loadouts are purchased at a vendor each life. A guide dated 17 Sep 2026 reports that after death a player returns to the vendor and can use "Re-buy Loadout" to rebuild the prior kit, and that repeated deaths can drain cash; it gives no exact cost [6] (player-reported). A level requirement only unlocks the option to buy: a one-time unlock payment is required, after which the item has a normal per-life vendor price (player-reported, Sep 2026 guides) [6].

Example unlock costs reported by that guide, all player-reported [6]:

| Item | Unlock | One-time cost |
|------|--------|---------------|
| PP-19 Vityaz | Medic 4 | one-time payment (amount not stated) |
| Galil | Assault 10 | $35,000 |
| Individual First Aid Kit | Medic 9 | $25,000 |
| Defibrillator | Medic 11 | $50,000 ($1,600 per loadout purchase) |
| Adrenaline Pen | Medic 14 | $25,000 |
| Basic Parachute | n/a | $100 |

The Emergency Resuscitator is reported free and usable once per life for reviving teammates [6]. Small, medium and large tactical vests open additional quick slots [6]. Patch notes say 155mm, 122mm and flare deployables take up more loadout space [3].

## Weapon categories and notable weapons (beta list, not final)

A press table recorded vendor list prices during testing and states they are not confirmed as the shipping economy [5]. Entries below are examples only.

| Category | Examples (beta list price) |
|----------|----------------------------|
| Assault rifles | Bushmaster M17S ($0), AK74 ($1,600), M4 ($2,800), FAL ($6,500) |
| SMGs | AMP-9 ($900), MP5 ($1,500), PP-19 Vityaz ($1,200) |
| Shotguns | MP43 ($400), M500 ($1,200) |
| LMGs | M249 SAW ($3,200), PKM ($4,500) |
| Marksman rifles | SKS ($2,400), SVD ($4,800) |
| Sniper rifles | Mosin Nagant ($4,500), AMR 50 ($8,800) |
| Bow | Compound Bow ($800) |
| Sidearms | M1911 ($300), Deagle ($900) |
| Launchers | RPG-7 ($2,000), MAAWS ($2,600), 9K333 Verba (surface-to-air) |

The same source reports ammo billed separately by caliber (roughly $10 to $250 a box), a 50% vendor discount below WARDOG Level 9, and attachments (optics, foregrips, magazines) unlocked by level rather than purchase [5]. 33 weapons were recorded, with 37 expected at launch [5]. These beta values predate the Season 1 repricing [3], so treat them as stale.

## Roles and progression

Press-reported beta mapping of kills to tracks: Assault XP from assault rifles and sidearms, Medic from SMGs, Support from shotguns, LMGs and launchers, Recon from marksman rifles, sniper rifles and the bow [5]. A later guide lists six tracks including Driver and Pilot, and says each track unlocks weapons, equipment, attachments and vehicles [6]. These disagree on track count (four in the beta list versus six), consistent with changes between beta and launch; the official breakdown was not found.

Season 1 changes (10 Sep 2026, via press) [3]:

- Role-track XP requirements rose sharply in the middle band: level 10 from 25,000 to 35,000, level 15 from 54,750 to 110,000, level 20 from 111,500 to 250,000; levels below 6 unchanged.
- Unlock shifts included Deagle from level 90 to 85, PP-19 50-round drum from level 29 (was 33), and Large Hammer from level 7 to 8.
- Recon scopes repriced: 6-10x MRAD $25,000 to $40,000; 6-10x MOA $30,000 to $45,000.
- Support: Medium Hammer $10,000 to $25,000; Large Hammer $25,000 to $75,000; vendor Forward Operating Base $2,500 to $7,500.
- Air vehicle player-kill XP lowered from 300 to 250.

## Damage and ballistics

No official damage values, armor ratings or ballistic tables were found. The developer states gunplay is tuned for gameplay rather than simulation [1]. Press reports that real bullet drop and travel time are modelled and that weapon weights differ (for example AMR 50 12.5 kg, LMGs 7.5 kg) [5]. Patch 0.1.2 notes that buildable "crit spots" were reworked and a Havoc bug that increased damage from 20mm and 30mm cannon fire was fixed [4]; this indicates locational critical spots exist on buildables, but no further model is documented.

## Gadgets and utility

Officially named: ghillie suit, rocket launchers, forward operating bases [1]. Via patch notes: throwables (grenades, smoke, C4), parachutes, backpacks, flares and hammers [3][4]. Player-reported: smoke grenades, first aid kit, defibrillator, adrenaline pen [6].

# Early Access Changes & Known Issues

| Date | Change | Source |
|------|--------|--------|
| 2026-09-10 | Season 1 changelog: unlock-level moves, repricing, slower XP curve, deployables use more loadout space, fixes (weapon-fire crash when owner left) | [2][3] |
| 2026-09-30 | Patch 0.1.2: server-validated revives, reduced FOB pallet and buildable-destruction rewards, throwables barred from enclosed vehicle seats, adaptive crosshair hides when aiming down sights, Havoc cannon-damage bug fixed | [4] |

Planned: more weapons and categories, deeper progression, seasonal meta; fighter jets [1]. Season 1 numbers may not persist across seasons; this is unverified (see Open Questions).

# Admin & Technical Notes

None specific to loadouts. Patch 0.1.2 added admin features (scheduled restart, RCON restrictions) unrelated to combat balance [4]. Kernel-level anti-cheat is listed on the Steam page [1].

# Risks & Caveats

- Weapon lists and prices come from a beta-era press table and predate Season 1 repricing [3][5].
- The official Steam news text was not retrievable; patch content is taken from press reproduction [3][4].
- Guides disagree on role track structure and unlock details [5][6].
- Early Access balance changes per patch; prices are expected to change.

# Open Questions

- Official full weapon roster, damage, headshot and armor values at the current build.
- Official role-track list and the weapon-to-track mapping at launch.
- Exact death cost and re-buy pricing, and whether any insurance exists.
- Whether patch numbering differs between 0.1.2 and a "0.11" mentioned in community-wiki search snippets (not cited; unverified), and whether each season uses a different experience curve.
- Newer patches after 30 Sep 2026.

# References

**Primary Sources**

- [1] **Valve / Bulkhead (Steam)** — *WARDOGS* store page. https://store.steampowered.com/app/1867240/WARDOGS/. Accessed 2026-10-08.
- [2] **Valve / Bulkhead (Steam)** — *Pre-Load Live & Season 1 Changelog* (Steam news post; only the title was machine-readable). https://store.steampowered.com/news/app/1867240/view/701027323413004455?l=english. Accessed 2026-10-08.

**Press & Secondary**

- [3] **Gfinity Esports** — *WARDOGS Season 1 changelog, Early Access patch notes*. https://www.gfinityesports.com/article/wardogs-season-1-changelog-early-access-patch-notes. Accessed 2026-10-08.
- [4] **BisectHosting** — *WARDOGS Update 0.1.2 patch notes* (reproduces official Steam notes). https://www.bisecthosting.com/blog/wardogs-update-0-1-2-patch-notes-bug-fixes-improvements-flythrough-exploit-fob-pallet-delivery-xp. Accessed 2026-10-08.
- [5] **allthings.how** — *Wardogs beta: weapons, prices and progression* (beta data, not final). https://allthings.how/?p=121341. Accessed 2026-10-08.

**Player-Reported Evidence**

- [6] **KeenGamer** — *WARDOGS progression guide* (dated 17 Sep 2026). https://www.keengamer.com/articles/guides/wardogs-progression-guide/. Accessed 2026-10-08.

# Further Reading

- Team17 press release: https://www.gamedeveloper.com/press-release/wardogs-is-coming-to-steam-early-access-on-10-september

# Related Documents

- gameplay-modes-foundation
- economy-foundation
- vehicles-outposts-foundation

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after independent re-verification of validate, markdownlint and links (0 dead). | Standing mandate (auto-approve on green QA) |
