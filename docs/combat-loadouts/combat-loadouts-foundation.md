---
id: combat-loadouts-foundation
title: "Combat & Loadouts: Foundation"
version: 1.2.0
status: frozen
confidence: Medium
category: Combat & Loadouts
topic: "Weapons, gadgets, classes, damage and ballistics"
market: Global
game_version: "Early Access Season 02, Update 0.2.0 (15 Oct 2026); official posts through 2026-10-15 (snapshot 2026-10-30)"
document_type: foundation
created: 2026-10-08
updated: 2026-10-30
review_due: 2026-11-20
sources_verified: 2026-10-30
supersedes: null
related: [gameplay-modes-foundation, economy-foundation, vehicles-outposts-foundation, weapons-catalogue, gadgets-armor-and-equipment, damage-ballistics-and-balance, price-tables-season-1, progression-unlock-tables, patch-history]
tags: [combat, weapons, loadouts, roles, ballistics, early-access]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | combat-loadouts-foundation |
| Version | 1.2.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Combat & Loadouts |
| Game version | Early Access Season 02, Update 0.2.0 (15 Oct 2026); official posts through 2026-10-15 (snapshot 2026-10-30) |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-30 |
| Review due | 2026-11-20 |

# Executive Summary

WARDOGS has no fixed class selection at spawn. Each life, a player spends cash at a vendor to build a custom loadout of weapons, gear, utility and vehicles, starting from $10,000 [1]. Experience is earned on role tracks that gate which items can be bought. The Season 1 changelog named Career, Medic, Recon, Support, Driver and Pilot [2]; the Update 0.2.0 patch notes (posted 14 Oct 2026) instead list Assault, Medic, Recon, Support, Pilot and Driver tracks plus a "WARDOG Progression Track" [11]. The notes do not say what happened to the "Career" label (see Open Questions).

The developer's stance on realism is a middle line: the store page says "tactical gunplay" in About This Game and, under the Early Access current-state answer, "Realistic gunplay balanced for gameplay rather than simulation" (live capture 2026-10-08) [1], the February 2026 FAQ calls the game "a hardcore shooter that doesn't forget it's a game" with "Grounded Gunplay" as an Early Access feature [6], and a May 2026 post lists "real-world ballistics" among its pillars [7]. No official weapon list, damage value or ballistic parameter has been published. The official Steam text for the 9 Sep Season 1 changelog [2], the 30 Sep update 0.1.2 [3] and the 2 Oct balance hotfix [4] is the Season 1 baseline.

Update 0.2.0 (Season 02, released 15 Oct 2026 [12]; notes posted 14 Oct [11]) is the first official source to publish combat numbers: calibre base-damage reductions (.308 -25%, 7.62x54mmR -20%, 7.62x39mm -19%, .50 cal -16%), Level 3 armor and helmet damage reduction lowered 55% to 50%, Level 4 lowered 65% to 60%, suppression rebuilt with Level 3 and Level 4 helmets reducing it by 68% and 80%, a battery-powered Infrared Range Finder (about 80 s per battery), a new Molotov, four new weapons (TCX-SPR, PP-19 Bizon, Evo-3 Ultra, M14), parachute and Medical Bag changes [11]. Numbers are owned by damage-ballistics-and-balance, gadgets-armor-and-equipment, weapons-catalogue and price-tables-season-1. No official post after 2026-10-15 is in the 2026-10-30 snapshot, so nothing later is known here.

Document confidence is Medium: the structural model, role tracks, repricing and the 0.2.0 balance changes are official, but absolute per-weapon damage is still unpublished and pre-0.2.0 weapon details rest on beta-era press and player-reported guides (see weapons-catalogue).

# Key Takeaways

- Loadouts are bought with cash each life from a vendor; players start with $10,000 and cash persists between matches (Steam page, checked 2026-10-08) [1].
- There is no spawn-time class pick. Six role tracks (Career, Medic, Recon, Support, Driver, Pilot) were named in the official changelog of 9 Sep 2026 [2]; the 0.2.0 notes (14 Oct 2026) name Assault, Medic, Recon, Support, Pilot, Driver and a "WARDOG Progression Track" [11].
- Official gunplay wording on the store page: "tactical gunplay" (About This Game) and "Realistic gunplay balanced for gameplay rather than simulation" (Early Access current state) (live capture 2026-10-08) [1]; "a hardcore shooter that doesn't forget it's a game" and "Grounded Gunplay" (18 Feb 2026) [6]; "real-world ballistics" (21 May 2026) [7].
- Season 1 changelog (posted 9 Sep 2026, live for the 10 Sep launch) slowed role XP between levels 10 and 20, moved many unlocks and repriced hammers, scopes, the FOB and vehicles; the developer says each season gets a different XP curve and item order [2].
- Patch 0.1.2 (30 Sep 2026) made revive validity server authoritative, scaled buildable-destruction rewards by build progress, barred throwables from enclosed vehicle seats and fixed a Havoc bug that raised damage taken from 20mm and 30mm cannon fire [3].
- Balance hotfix (2 Oct 2026): IR Rangefinders were disabled in the vendor until Season 02, when they will need batteries, and the CIWS now destroys a Havoc in about 6 s instead of 12 s [4].
- Update 0.2.0 (notes 14 Oct 2026, live 15 Oct): Level 3 armor and helmets 55% to 50% damage reduction, Level 4 65% to 60%; Level 3 and Level 4 helmets reduce suppression by 68% and 80%; the Infrared Range Finder runs on batteries (about 80 s of active use); a Molotov is added; the Medical Bag durability rises 100 to 150 [11][12].
- Calibre base-damage cuts in 0.2.0: .308 Winchester -25%, 7.62x54mmR -20%, 7.62x39mm -19%, .50 Cal -16% (percentages only; absolute damage per weapon is still unpublished) [11].
- No official absolute damage, headshot or bullet-drop table exists; the beta-era claim that drop and travel time are modelled is press-reported only [9].

# Scope

Covers infantry combat, weapon categories, gadgets and equipment, the role/progression system as it relates to loadouts, the documented damage/ballistics model, and how loadout purchasing ties to the in-match economy. Game version: Early Access Season 02, Update 0.2.0 (15 Oct 2026), with Season 1 (0.1.2 and the 2 Oct 2026 hotfixes) kept as dated history. Official posts after 2026-10-15 are not in the 2026-10-30 snapshot.

Excluded: vehicle combat detail (see vehicles-outposts-foundation), mode rules (gameplay-modes-foundation), full economy mechanics (economy-foundation) and per-weapon, per-item and per-price tables, which live in the depth documents listed under Related Documents.

# Definitions

- **Loadout**: the set of weapons, gear, utility and vehicles bought for one life [1].
- **Role track**: a per-role XP progression that gates item purchases. Season 1 names: Career, Medic, Recon, Support, Driver and Pilot [2]. Update 0.2.0 notes headings: Assault, Medic, Recon, Support, Pilot, Driver [11].
- **WARDOG Progression Track**: an official 0.2.0 heading for general unlocks (for example Level 3 Helmet & Armor at level 70, Sport Parachute at level 34) [11]; the guide term "WARDOG Level" is player-reported [10].
- **Rebuy Last Loadout**: vendor button that, since 0.2.0, pre-populates the equipment vendor UI with the last loadout so items can be added or removed before purchase [11].

# Current State

- Each player starts with $10,000 and buys a custom loadout of weapons, gear, utility and vehicles each life; cash persists between matches (Steam page, 2026-10-08) [1].
- The store page's Early Access current-state answer lists "Realistic gunplay balanced for gameplay rather than simulation" (live capture 2026-10-08) [1].
- The store page's Mature Content Description says "Wardogs contains killing with weapons and melee combat", so melee combat exists; no melee weapon roster or stats are published (live capture 2026-10-08) [1].
- Teamwork earns cash, including reviving squadmates, transporting friendlies to the zone and controlling the objective [1].
- The store page describes "tactical gunplay and combined arms combat with building and destruction mechanics", sniping with a ghillie suit, rocket launchers that destroy apartment blocks and buildable forward operating bases [1].
- Role tracks named in the official Season 1 changelog (posted 9 Sep 2026): Career, Medic, Recon, Support, Driver, Pilot [2]. The changelog also shows items moving between tracks (Heavy Tank from Career 35 to Driver 35; Music Tape H from Pilot 28 to Driver 23) [2].
- Update 0.2.0 notes (14 Oct 2026) describe Assault as "the role for attacking enemy bases"; C4 and the Remote Detonator move into it and a Molotov Cocktail (level 13) joins it [11].
- Season 1 changelog (title "Pre-Load Live & Season 1 Changelog", posted 9 Sep 2026 UTC) states that "each season we will have a different XP curve with different item orders" [2].
- Update 0.1.2 is dated 30 Sep 2026 [3]. On 2 Oct 2026 two separate official posts appeared: a hotfix notice for 08:00 UTC about "minor security and stability issues" [5] and the balance hotfix on IR Rangefinders and the CIWS [4].
- Season 02 / Update 0.2.0 went live on 15 Oct 2026 ("We have now released Update 0.2.0. Servers are back online") [12]. The 0.1.2 post had said it would bring "new map conditions, equipment, balance reworks and additional features" [3][8]; the notes confirm new weapons, a Molotov, helmet and Range Finder changes, vehicles, buildables and a rain weather preset [11].
- Weapons added in 0.2.0: TCX-SPR (7.62x39mm assault rifle), PP-19 Bizon (9x19mm SMG), Evo-3 Ultra (.308 Win LMG), M14 (.308 Win marksman rifle) [11]. Prices and levels are in weapons-catalogue and price-tables-season-1.
- The 0.2.0 notes do not address death-cost rules or a progression wipe.

# Detail

## Loadout selection and economy

Loadouts are purchased at a vendor each life [1]. The Season 1 posts do not describe the death cost; those details are player-reported (see death-penalty-and-rebuy) [10]. The 0.2.0 notes confirm a "Rebuy Last Loadout" button and remove the old placeholder UI [11]; they do not state any death cost, and do not mention a progression wipe. A guide dated 17 Sep 2026 reports that a level requirement only unlocks the option to buy, after which a one-time unlock payment is needed and the item then has a normal per-life vendor price [10] (player-reported). The official changelog does list vendor prices separately from track prices, which is consistent with that two-price model: for example Large Hammer has a vendor price ($1,600 to $2,400) and a Support track price ($25,000 to $75,000) [2].

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

Update 0.2.0 (notes 14 Oct 2026) reversed the Season 1 slowdown: for example level 10 35,000 to 25,000, level 20 250,000 to 111,500, level 50 1,500,000 to 1,150,000 [11]. The "from" figures in the 0.2.0 notes differ from some Season 1 figures quoted above (for example level 15 110,000 matches, level 25 365,000 differs from 325,000, level 50 1,500,000 differs from 1,000,000); this document does not reconcile them (see progression-and-role-tracks). Reaching level 20 is stated to take less than half the Season 1 playtime [11]. Most attachments moved to earlier levels or new tracks [11].

Full ladders and price lists are in progression-unlock-tables and price-tables-season-1.

## Damage and ballistics

Official 0.2.0 combat-balance changes (notes 14 Oct 2026, live 15 Oct) [11]; full detail in damage-ballistics-and-balance:

- Calibre base damage: .308 Winchester -25%, 7.62x54mmR -20%, 7.62x39mm -19%, .50 Cal -16%, applying to infantry and vehicle weapons alike.
- Assault rifle body shots do slightly less damage; LMG body damage now matches assault rifles; sniper hit-location damage was increased to offset the base reduction; DMR headshots and upper-body hits are slightly weaker.
- Armor and helmets: Level 3 damage reduction 55% to 50%; Level 4 65% to 60%. Scout Rifle headshots one-shot a target with no helmet and need two on a Level 1 helmet.
- Suppression was rebuilt around per-weapon falloff curves; Level 3 helmets reduce suppression by 68% and Level 4 by 80%.
- 12 gauge slug and compound bow damage against armor now scale with armor tier.

The notes give percentages, not absolute damage per shot, so no per-weapon damage table exists officially. Before 0.2.0 no official values existed at all. The earlier official statements are positional: "tactical gunplay" and "Realistic gunplay balanced for gameplay rather than simulation" on the store page (live capture 2026-10-08) [1], "a hardcore shooter that doesn't forget it's a game" and "Grounded Gunplay" [6], and "real-world ballistics, audio and flight models" in a May 2026 post whose substance is in a video not captured as text [7]. Press from the closed beta reports that real bullet drop and travel time are modelled and that weapon weights differ (for example AMR 50 12.5 kg, LMGs 7.5 kg) [9]; this is not confirmed by the developer.

Official Season 1 combat-relevant fixes: update 0.1.2 fixed a Havoc bug causing increased damage from 20mm and 30mm cannon fire and fixed buildable "crit spots" reappearing in the same place or jumping to the far side of a structure, so they now favour a spot reachable from where the player stands [3]. The 2 Oct hotfix halved the CIWS kill time on a Havoc (about 12 s to about 6 s), which the developer calls correcting an overcorrection in the previous patch [4]. See damage-ballistics-and-balance for the full record.

## Gadgets and utility

Update 0.2.0 adds a Molotov (thrown incendiary; impact damage plus burn damage over time; throw overarm or underarm; burns destructible foliage; weaker in rain), makes the Infrared Range Finder battery-powered (about 80 s of active use per battery; drains faster if toggled on and off quickly), gives the Level 4 Helmet muffled audio, muffled proximity chat, restricted field of view and sprint fog-over, raises Medical Bag durability from 100 to 150, and changes parachute opening behaviour and prices (Basic $100 to $500, Sport $1,000 to $700) [11]. 30mm cannon ammo now takes a 2x2 slot and backpack stacks are capped at 50 [11]. Explosives and placeables can no longer be used from enclosed vehicle seats [11]. Details are in gadgets-armor-and-equipment.

Officially named in Season 1: ghillie suit, rocket launchers and forward operating bases [1]; grenades, smoke and C4 as throwables, parachutes, backpacks, flares, hammers and IR Rangefinders [2][3][4]. Player-reported: first aid kit, defibrillator, adrenaline pen and an Emergency Resuscitator [10]; see gadgets-armor-and-equipment. The 2 Oct post title says "IR Goggles" while its body says "IR Rangefinders"; whether these are one item is not stated [4]. The 0.2.0 notes use "Infrared Range Finder" [11].

# Early Access Changes & Known Issues

| Date | Change | Source |
|------|--------|--------|
| 2026-09-09 (live 10 Sep) | Season 1 changelog: unlock-level moves, repricing (hammers, FOB, scopes, vehicles), slower XP curve 10 to 20, deployables use more loadout space, crash fix when a weapon owner left | [2] |
| 2026-09-30 | Update 0.1.2: server-authoritative revives, reduced FOB pallet rewards outside the zone, rewards for destroying buildables scale with build progress, throwables barred from enclosed vehicle seats, adaptive crosshair hides when aiming down sights, buildable crit-spot fix, Havoc cannon-damage bug fixed | [3] |
| 2026-10-02 | Security and stability hotfix notice (08:00 UTC, about one hour downtime) | [5] |
| 2026-10-02 | Balance hotfix: IR Rangefinders disabled in the vendor until Season 02 (batteries required on return); CIWS kills a Havoc in about 6 s instead of 12 s; no client download or downtime | [4] |
| 2026-10-14 (live 2026-10-15) | Update 0.2.0 / Season 02: calibre damage cuts, Level 3/4 armor and helmet reductions lowered, suppression rework, battery Range Finder, Molotov, Level 4 Helmet drawbacks, Medical Bag durability 100 to 150, parachute rework, four new weapons, new attachments, rebuy UI, 30mm ammo 2x2 slot and 50-item backpack stack cap | [11][12] |

Season 02 shipped on 15 Oct 2026 with equipment and balance reworks [11][12]; no official post after that date is in the 2026-10-30 snapshot. The store page's Early Access roadmap, confirmed in the live capture 2026-10-08, plans "more maps, weapons, vehicles, and gameplay variety", "expanded weapon categories", deeper progression, a stronger seasonal meta game and fighter jets [1]. The earlier storefront-API JSON omitted this text. Season 1 numbers did not persist: the 0.2.0 notes change the XP curve, unlock levels and prices [11], consistent with the developer saying each season has its own curve and item order [2].

# Admin & Technical Notes

None specific to loadouts. The 0.2.0 notes add community-server ping-limit configuration and server-seeding changes (see server-hosting-and-browser) [11]. Patch 0.1.2 added admin features (scheduled daily restart, RCON AllowedHosts) unrelated to combat balance [3]. The live Steam page lists kernel-level anti-cheat (Elytra) (live capture 2026-10-08) [1].

# Risks & Caveats

- Season 1 weapon lists beyond the few official items come from a beta-era press table and from guides [9][10]; they predate 0.2.0.
- Item order and XP curves differ each season [2], and 0.2.0 changed many of them [11]; Season 1 values quoted here are history only.
- Official posts after 2026-10-15 are not in the 2026-10-30 snapshot; later hotfixes may exist.
- Melee combat is confirmed to exist by the store page's Mature Content Description, but no melee weapons, damage or roster are published (live capture 2026-10-08) [1].
- Guides use "Assault" and "WARDOG Level"; official text uses "Career" and no WARDOG Level [2][10].

# Open Questions

- Official full weapon roster, damage, headshot and armor values at the current build.
- Whether the Career track is the guide's "Assault" track, and the official weapon-to-track mapping.
- Exact death cost and rebuy pricing, and whether any insurance exists; no official post covers them (the 0.2.0 notes only describe the rebuy UI) [11].
- Which melee weapons exist and how melee damage works; the store page confirms melee only in its Mature Content Description.
- Whether the Season 1 "Career" label was replaced by "Assault" and the WARDOG track in 0.2.0; the notes do not say.
- IR Rangefinder battery price and whether the item is back in the vendor at launch (the notes list an Infrared Range Finder price of $3,200 but do not state availability) [11].
- Whether "IR Goggles" and "IR Rangefinders" are the same item.
- Whether Season 02 reset any progression: the 0.2.0 notes do not mention it.
- Patch numbering: the official post titles are "Patch 0.11" (14 Sep) and "Update 0.1.2" (30 Sep); no reading beyond that is supported.
- Anything after 2026-10-15: no later official post is in the 2026-10-30 snapshot.

# References

**Primary Sources**

- [1] **Valve / Bulkhead (Steam)** — *WARDOGS* store page, live browser capture 2026-10-08 (snapshots/2026-10-08/store-page-live.txt) and storefront data. https://store.steampowered.com/app/1867240/WARDOGS/. Accessed 2026-10-08.
- [2] **Valve / Bulkhead (Steam)** — *Pre-Load Live & Season 1 Changelog* (posted 9 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1843481262690549. Accessed 2026-10-08.
- [3] **Valve / Bulkhead (Steam)** — *WARDOGS | Update 0.1.2 (Minor Patch)* (30 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1845383656376490. Accessed 2026-10-08.
- [4] **Valve / Bulkhead (Steam)** — *IR Goggles & CIWS Balance Hotfix* (2 Oct 2026). https://store.steampowered.com/news/app/1867240/view/1845383656386801. Accessed 2026-10-08.
- [5] **Valve / Bulkhead (Steam)** — *WARDOGS | Security & Stability Hotfix* (2 Oct 2026). https://store.steampowered.com/news/app/1867240/view/1845383656384445. Accessed 2026-10-08.
- [6] **Valve / Bulkhead (Steam)** — *WARDOGS - TOP QUESTIONS* (18 Feb 2026, pre-release). https://store.steampowered.com/news/app/1867240/view/1825093633182385. Accessed 2026-10-08.
- [7] **Valve / Bulkhead (Steam)** — *WARDOGS - Tactical Depth & Teamplay* (21 May 2026, pre-release). https://store.steampowered.com/news/app/1867240/view/1833334318569240. Accessed 2026-10-08.
- [8] **Valve / Bulkhead (Steam)** — *WARDOGS / Season 02 Teaser* (22 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1844115010504839. Accessed 2026-10-08.

- [11] **Valve / Bulkhead (Steam)** — *WARDOGS | Season 02 Patch Notes* (14 Oct 2026; Update 0.2.0). https://store.steampowered.com/news/app/1867240/view/1846651706674560. Accessed 2026-10-30.
- [12] **Valve / Bulkhead (Steam)** — *WARDOGS | SEASON 02 IS NOW LIVE* (15 Oct 2026). https://store.steampowered.com/news/app/1867240/view/1846651706677015. Accessed 2026-10-30.

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
- season-2-announcements (Season 02 outcome)

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after independent re-verification of validate, markdownlint and links (0 dead). | Standing mandate (auto-approve on green QA) |
| 1.1.0 | 2026-10-08 | Research Pipeline (revision worker) | Revised against full official Steam text; corrected Season 1 changelog id (1843481262690549, 9 Sep); six official tracks (Career, Medic, Recon, Support, Driver, Pilot); official gunplay wording replaces "realistic but tuned for gameplay"; two 2 Oct hotfix posts and the official IR Rangefinder/CIWS balance change; corrected hammer unlock and vendor prices; unverifiable store claims (melee) moved to Open Questions | Standing mandate (auto-approve on green QA) |
| 1.1.1 | 2026-10-08 | Research Pipeline (revision worker) | Corrected against live store-page capture; restored Primary quote 'Realistic gunplay balanced for gameplay rather than simulation' alongside 'tactical gunplay'; melee confirmed by Mature Content Description and removed from Open Questions (no melee roster published); roadmap 'more maps, weapons, vehicles' and 'expanded weapon categories' now cited from the page; Elytra kernel anti-cheat noted | Standing mandate (auto-approve on green QA) |
| 1.2.0 | 2026-10-30 | Research Pipeline (virtual agent) | Revised for Update 0.2.0 (Season 02): calibre damage cuts, Level 3/4 armor and helmet reductions, suppression, Molotov, battery Range Finder, Medical Bag, new weapons, rebuy UI, track names (Assault/WARDOG); Season 1 values kept as history; no official posts after 2026-10-15 in snapshot. | — |
