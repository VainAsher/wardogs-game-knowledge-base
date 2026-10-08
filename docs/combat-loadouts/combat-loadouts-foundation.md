---
id: combat-loadouts-foundation
title: "Combat & Loadouts: Foundation"
version: 1.1.0
status: frozen
confidence: Medium
category: Combat & Loadouts
topic: "Weapons, gadgets, classes, damage and ballistics"
market: Global
game_version: "Early Access Season 1, patch 0.1.2 (30 Sep 2026) plus the 2 Oct 2026 hotfixes; Steam store data and news snapshot 2026-10-08"
document_type: foundation
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-10-22
sources_verified: 2026-10-08
supersedes: null
related: [gameplay-modes-foundation, economy-foundation, vehicles-outposts-foundation, weapons-catalogue, gadgets-armor-and-equipment, damage-ballistics-and-balance, price-tables-season-1, progression-unlock-tables, patch-history]
tags: [combat, weapons, loadouts, roles, ballistics, early-access]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | combat-loadouts-foundation |
| Version | 1.1.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Combat & Loadouts |
| Game version | Early Access Season 1, patch 0.1.2 (30 Sep 2026) plus 2 Oct 2026 hotfixes |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-10-22 |

# Executive Summary

WARDOGS has no fixed class selection at spawn. Each life, a player spends cash at a vendor to build a custom loadout of weapons, gear, utility and vehicles, starting from $10,000 [1]. Experience is earned on six role tracks, named in the official Season 1 changelog as Career, Medic, Recon, Support, Driver and Pilot, which gate which items can be bought [2]. "Assault" is a guide name, not an official one [10].

The developer's stance on realism is a middle line: the store page says "tactical gunplay" [1], the February 2026 FAQ calls the game "a hardcore shooter that doesn't forget it's a game" with "Grounded Gunplay" as an Early Access feature [6], and a May 2026 post lists "real-world ballistics" among its pillars [7]. No official weapon list, damage value or ballistic parameter has been published. This revision replaces press summaries with the full official Steam text for the 9 Sep Season 1 changelog [2], the 30 Sep update 0.1.2 [3] and the 2 Oct balance hotfix [4].

Document confidence is Medium: the structural model, role tracks, repricing and balance changes are official, but weapon-level names, prices and stats remain beta-era press or player-reported guides (see weapons-catalogue).

# Key Takeaways

- Loadouts are bought with cash each life from a vendor; players start with $10,000 and cash persists between matches (Steam page, checked 2026-10-08) [1].
- There is no spawn-time class pick. Six role tracks (Career, Medic, Recon, Support, Driver, Pilot) are named in the official changelog of 9 Sep 2026 [2]; an account-wide WARDOG Level is player-reported only [10].
- Official gunplay wording: "tactical gunplay" on the store page [1]; "a hardcore shooter that doesn't forget it's a game" and "Grounded Gunplay" (18 Feb 2026) [6]; "real-world ballistics" (21 May 2026) [7].
- Season 1 changelog (posted 9 Sep 2026, live for the 10 Sep launch) slowed role XP between levels 10 and 20, moved many unlocks and repriced hammers, scopes, the FOB and vehicles; the developer says each season gets a different XP curve and item order [2].
- Patch 0.1.2 (30 Sep 2026) made revive validity server authoritative, scaled buildable-destruction rewards by build progress, barred throwables from enclosed vehicle seats and fixed a Havoc bug that raised damage taken from 20mm and 30mm cannon fire [3].
- Balance hotfix (2 Oct 2026): IR Rangefinders were disabled in the vendor until Season 02, when they will need batteries, and the CIWS now destroys a Havoc in about 6 s instead of 12 s [4].
- No official damage, headshot, armor or bullet-drop figures exist; the beta-era claim that drop and travel time are modelled is press-reported only [9].

# Scope

Covers infantry combat, weapon categories, gadgets and equipment, the role/progression system as it relates to loadouts, the documented damage/ballistics model, and how loadout purchasing ties to the in-match economy. Game version: Early Access Season 1 through patch 0.1.2 and the 2 Oct 2026 hotfixes.

Excluded: vehicle combat detail (see vehicles-outposts-foundation), mode rules (gameplay-modes-foundation), full economy mechanics (economy-foundation) and per-weapon, per-item and per-price tables, which live in the depth documents listed under Related Documents.

# Definitions

- **Loadout**: the set of weapons, gear, utility and vehicles bought for one life [1].
- **Role track**: a per-role XP progression that gates item purchases. The official track names are Career, Medic, Recon, Support, Driver and Pilot [2].
- **WARDOG Level**: account-wide level that unlocks general items such as armor, backpacks, ammo types and sidearms (player-reported; not defined in any official post read) [10].
- **Re-buy Loadout**: vendor option that rebuilds the previous kit after death (player-reported; no official post mentions it) [10].

# Current State

- Each player starts with $10,000 and buys a custom loadout of weapons, gear, utility and vehicles each life; cash persists between matches (Steam page, 2026-10-08) [1].
- Teamwork earns cash, including reviving squadmates, transporting friendlies to the zone and controlling the objective [1].
- The store page describes "tactical gunplay and combined arms combat with building and destruction mechanics", sniping with a ghillie suit, rocket launchers that destroy apartment blocks and buildable forward operating bases [1].
- Role tracks named in the official Season 1 changelog (posted 9 Sep 2026): Career, Medic, Recon, Support, Driver, Pilot [2]. The changelog also shows items moving between tracks (Heavy Tank from Career 35 to Driver 35; Music Tape H from Pilot 28 to Driver 23) [2].
- Season 1 changelog (title "Pre-Load Live & Season 1 Changelog", posted 9 Sep 2026 UTC) states that "each season we will have a different XP curve with different item orders" [2].
- Update 0.1.2 is dated 30 Sep 2026 [3]. On 2 Oct 2026 two separate official posts appeared: a hotfix notice for 08:00 UTC about "minor security and stability issues" [5] and the balance hotfix on IR Rangefinders and the CIWS [4].
- Season 02 is announced for 15 Oct 2026; the 0.1.2 post says it will bring "new map conditions, equipment, balance reworks and additional features" [3][8].

# Detail

## Loadout selection and economy

Loadouts are purchased at a vendor each life [1]. The official posts do not describe the death cost or any re-buy feature; those details are player-reported (see death-penalty-and-rebuy) [10]. A guide dated 17 Sep 2026 reports that a level requirement only unlocks the option to buy, after which a one-time unlock payment is needed and the item then has a normal per-life vendor price [10] (player-reported). The official changelog does list vendor prices separately from track prices, which is consistent with that two-price model: for example Large Hammer has a vendor price ($1,600 to $2,400) and a Support track price ($25,000 to $75,000) [2].

Official equipment-space change: 155mm, 122mm and flare deployables take up more loadout space since the Season 1 changelog [2]. Per-item unlock costs from guides (medical gear, sidearms, parachute) are in gadgets-armor-and-equipment and weapons-catalogue rather than repeated here.

## Weapon categories and notable weapons

Official text names very few weapons: the Deagle (Career 90 to 85), the PP-19 50-round drum magazine (Medic 33 to 29), 762x54mm AP and 556mm AP ammo, and Recon 6-10x MRAD and MOA scopes [2]. Rocket launchers appear on the store page [1]. Everything else is beta-era press or player-reported [9][10].

A beta press table grouped the vendor into assault rifles, SMGs, shotguns, LMGs, marksman rifles, sniper rifles, a compound bow, sidearms and launchers (RPG-7, MAAWS, 9K333 Verba surface-to-air), recorded 33 weapons with 37 expected at launch, and said prices were not confirmed as final [9]. Those values predate the Season 1 repricing [2] and are stale; the full roster with prices and levels is in weapons-catalogue (confidence Low there).

## Roles and progression

Official: the Season 1 changelog names six tracks, Career, Medic, Recon, Support, Driver and Pilot, and lists unlock moves under Career, Medic, Support and Driver [2]. The beta press mapping of kills to four tracks (assault rifles and sidearms, SMGs, shotguns/LMGs/launchers, marksman/sniper/bow) used the guide name "Assault" and predates launch [9]; whether Career is a rename of that track is not stated officially (see progression-and-role-tracks). Guides add that Driver and Pilot are levelled by vehicles [10] (player-reported).

Season 1 changes (changelog posted 9 Sep 2026) [2]:

- Role-track XP requirements rose sharply in the middle band: level 6 from 8,750 to 9,250, level 10 from 25,000 to 35,000, level 15 from 54,750 to 110,000, level 20 from 111,500 to 250,000, level 25 from 192,000 to 325,000; levels below 6 unchanged, and the curve flattens from level 35 onward (level 50 is 1,000,000). The developer says median players at 20 to 25 hours will be around level 20.
- Career unlock moves: Deagle 90 to 85, Artillery Tank 55 to 90, Sports Parachute 36 to 35, Large Backpack 56 to 55, 762x54mm AP 83 to 82, 556mm AP 85 to 83. Medic: PP-19 50-round drum 33 to 29. Support: Large Hammer 7 to 8. Driver: Heavy Tank now Driver 35, plus nine other vehicle level moves.
- Recon scopes repriced: 6-10x MRAD $25,000 to $40,000; 6-10x MOA $30,000 to $45,000.
- Support track prices: Medium Hammer unlock $10,000 to $25,000; Large Hammer unlock $25,000 to $75,000. Vendor prices: Large Hammer $1,600 to $2,400; Forward Operating Base $2,500 to $7,500.
- Air vehicle player-kill XP lowered from 300 to 250.

Full ladders and price lists are in progression-unlock-tables and price-tables-season-1.

## Damage and ballistics

No official damage values, armor ratings or ballistic tables exist. The official statements are positional: "tactical gunplay" [1], "a hardcore shooter that doesn't forget it's a game" and "Grounded Gunplay" [6], and "real-world ballistics, audio and flight models" in a May 2026 post whose substance is in a video not captured as text [7]. Press from the closed beta reports that real bullet drop and travel time are modelled and that weapon weights differ (for example AMR 50 12.5 kg, LMGs 7.5 kg) [9]; this is not confirmed by the developer.

Official combat-relevant fixes: update 0.1.2 fixed a Havoc bug causing increased damage from 20mm and 30mm cannon fire and fixed buildable "crit spots" reappearing in the same place or jumping to the far side of a structure, so they now favour a spot reachable from where the player stands [3]. The 2 Oct hotfix halved the CIWS kill time on a Havoc (about 12 s to about 6 s), which the developer calls correcting an overcorrection in the previous patch [4]. See damage-ballistics-and-balance for the full record.

## Gadgets and utility

Officially named: ghillie suit, rocket launchers and forward operating bases [1]; grenades, smoke and C4 as throwables, parachutes, backpacks, flares, hammers and IR Rangefinders [2][3][4]. Player-reported: first aid kit, defibrillator, adrenaline pen and an Emergency Resuscitator [10]; see gadgets-armor-and-equipment. The 2 Oct post title says "IR Goggles" while its body says "IR Rangefinders"; whether these are one item is not stated [4].

# Early Access Changes & Known Issues

| Date | Change | Source |
|------|--------|--------|
| 2026-09-09 (live 10 Sep) | Season 1 changelog: unlock-level moves, repricing (hammers, FOB, scopes, vehicles), slower XP curve 10 to 20, deployables use more loadout space, crash fix when a weapon owner left | [2] |
| 2026-09-30 | Update 0.1.2: server-authoritative revives, reduced FOB pallet rewards outside the zone, rewards for destroying buildables scale with build progress, throwables barred from enclosed vehicle seats, adaptive crosshair hides when aiming down sights, buildable crit-spot fix, Havoc cannon-damage bug fixed | [3] |
| 2026-10-02 | Security and stability hotfix notice (08:00 UTC, about one hour downtime) | [5] |
| 2026-10-02 | Balance hotfix: IR Rangefinders disabled in the vendor until Season 02 (batteries required on return); CIWS kills a Havoc in about 6 s instead of 12 s; no client download or downtime | [4] |

Planned: Season 02 on 15 Oct 2026 with equipment and balance reworks [3][8]. The store page's Early Access roadmap (more weapons and categories, deeper progression, seasonal meta, fighter jets) is cited by sibling documents from the live page; it is not present in the saved store JSON [1]. Season 1 numbers may not persist across seasons because the developer says each season has its own curve and item order [2].

# Admin & Technical Notes

None specific to loadouts. Patch 0.1.2 added admin features (scheduled daily restart, RCON AllowedHosts) unrelated to combat balance [3]. The live Steam page lists kernel-level anti-cheat (not in the saved store JSON) [1].

# Risks & Caveats

- Weapon lists, prices and unlock levels beyond the few official items come from a beta-era press table and from guides [9][10].
- The developer says item order and XP curves differ each season, so every Season 1 level and price is expected to change on 15 Oct 2026 [2][8].
- Melee combat, mentioned in the previous version of this document as an official store-page claim, could not be confirmed in the saved store data and is moved to Open Questions.
- Guides use "Assault" and "WARDOG Level"; official text uses "Career" and no WARDOG Level [2][10].

# Open Questions

- Official full weapon roster, damage, headshot and armor values at the current build.
- Whether the Career track is the guide's "Assault" track, and the official weapon-to-track mapping.
- Exact death cost and re-buy pricing, and whether any insurance exists; no official post covers them.
- Whether melee combat is a store-page feature (the saved store JSON does not mention it) and what the live Early Access roadmap text says.
- What the 6-10x scope prices and other Season 1 values become at Season 02, and what IR Rangefinder batteries will cost.
- Whether "IR Goggles" and "IR Rangefinders" are the same item.
- Patch numbering: the official post titles are "Patch 0.11" (14 Sep) and "Update 0.1.2" (30 Sep); no reading beyond that is supported.
- Anything after the 2 Oct 2026 hotfixes.

# References

**Primary Sources**

- [1] **Valve / Bulkhead (Steam)** — *WARDOGS* store page and storefront data (snapshot 2026-10-08). https://store.steampowered.com/app/1867240/WARDOGS/. Accessed 2026-10-08.
- [2] **Valve / Bulkhead (Steam)** — *Pre-Load Live & Season 1 Changelog* (posted 9 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1843481262690549. Accessed 2026-10-08.
- [3] **Valve / Bulkhead (Steam)** — *WARDOGS | Update 0.1.2 (Minor Patch)* (30 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1845383656376490. Accessed 2026-10-08.
- [4] **Valve / Bulkhead (Steam)** — *IR Goggles & CIWS Balance Hotfix* (2 Oct 2026). https://store.steampowered.com/news/app/1867240/view/1845383656386801. Accessed 2026-10-08.
- [5] **Valve / Bulkhead (Steam)** — *WARDOGS | Security & Stability Hotfix* (2 Oct 2026). https://store.steampowered.com/news/app/1867240/view/1845383656384445. Accessed 2026-10-08.
- [6] **Valve / Bulkhead (Steam)** — *WARDOGS - TOP QUESTIONS* (18 Feb 2026, pre-release). https://store.steampowered.com/news/app/1867240/view/1825093633182385. Accessed 2026-10-08.
- [7] **Valve / Bulkhead (Steam)** — *WARDOGS - Tactical Depth & Teamplay* (21 May 2026, pre-release). https://store.steampowered.com/news/app/1867240/view/1833334318569240. Accessed 2026-10-08.
- [8] **Valve / Bulkhead (Steam)** — *WARDOGS / Season 02 Teaser* (22 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1844115010504839. Accessed 2026-10-08.

**Press & Secondary**

- [9] **allthings.how** — *Wardogs beta: weapons, prices and progression* (beta data, not final). https://allthings.how/?p=121341. Accessed 2026-10-08.

**Player-Reported Evidence**

- [10] **KeenGamer** — *WARDOGS progression guide* (dated 17 Sep 2026). https://www.keengamer.com/articles/guides/wardogs-progression-guide/. Accessed 2026-10-08.

# Further Reading

- Team17 press release: https://www.gamedeveloper.com/press-release/wardogs-is-coming-to-steam-early-access-on-10-september

# Related Documents

- gameplay-modes-foundation
- economy-foundation
- vehicles-outposts-foundation
- weapons-catalogue (roster, prices and levels)
- gadgets-armor-and-equipment (non-weapon items, IR gear)
- damage-ballistics-and-balance (realism statements, balance record)
- price-tables-season-1 (Season 1 prices)
- progression-unlock-tables (unlock ladders)
- patch-history (release timeline)

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after independent re-verification of validate, markdownlint and links (0 dead). | Standing mandate (auto-approve on green QA) |
| 1.1.0 | 2026-10-08 | Research Pipeline (revision worker) | Revised against full official Steam text; corrected Season 1 changelog id (1843481262690549, 9 Sep); six official tracks (Career, Medic, Recon, Support, Driver, Pilot); official gunplay wording replaces "realistic but tuned for gameplay"; two 2 Oct hotfix posts and the official IR Rangefinder/CIWS balance change; corrected hammer unlock and vendor prices; unverifiable store claims (melee) moved to Open Questions | Standing mandate (auto-approve on green QA) |
