---
id: damage-ballistics-and-balance
title: "Damage, Ballistics & Balance Changes"
version: 1.1.0
status: frozen
confidence: Medium
category: Combat & Loadouts
topic: "Damage model, ballistics, hit registration, and the balance-change history"
market: Global
game_version: "Early Access Season 02, Update 0.2.0 (15 Oct 2026); official posts through 2026-10-15 (snapshot 2026-10-30); Season 1 baseline kept as history"
document_type: depth
created: 2026-10-08
updated: 2026-10-30
review_due: 2026-11-20
sources_verified: 2026-10-30
supersedes: null
related: [combat-loadouts-foundation, weapons-catalogue, gadgets-armor-and-equipment, patch-history]
tags: [combat, damage, ballistics, balance, patch-notes, season-1, season-02, update-0-2-0, suppression, early-access]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | damage-ballistics-and-balance |
| Version | 1.1.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Combat & Loadouts |
| Game version | Early Access Season 02, Update 0.2.0 (15 Oct 2026); official posts through 2026-10-15 (snapshot 2026-10-30) |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-30 |
| Review due | 2026-11-20 |

# Executive Summary

The developer still has not published a damage table, ballistic table or hit-registration description for WARDOGS. What changed with Update 0.2.0 (patch notes 14 Oct 2026, release 15 Oct 2026) is that the "Combat Balance" section of the notes states relative damage changes and some armour and suppression percentages for the first time [15][17]. These are percentages and rules, not absolute per-shot damage.

The 0.2.0 damage rework cuts base damage by calibre (.308 Win -25%, 7.62x54mmR -20%, 7.62x39mm -19%, .50 Cal -16%, applied to every weapon using the round, including vehicle weapons), evens out and slightly lowers assault-rifle torso damage, aligns LMG body damage with assault rifles, adjusts DMR hit-location values, raises sniper-rifle hit-location damage, lowers Level 3 and Level 4 armour and helmet damage reduction (55% to 50%, 65% to 60%), and rebuilds suppression around shared falloff curves per weapon, with Level 3 and 4 helmets reducing suppression by 68% and 80% [15].

Season 1 material (the 10 Sep 2026 changelog through the 2 Oct 2026 hotfix) is kept as dated history. Document confidence is Medium: the Season 02 changes are Primary and itemised, but no absolute damage values exist, the realism and hit-registration sections rest on marketing-register text, and the ballistics claim rests on one beta-era press report. No official post after 15 Oct 2026 appears in the 2026-10-30 snapshot.

# Key Takeaways

- Official, Update 0.2.0 (14 Oct 2026): calibre base damage reductions of .308 Win -25%, 7.62x54mmR -20%, 7.62x39mm -19%, .50 Cal -16%, affecting infantry and vehicle weapons [15].
- Official, 0.2.0: Level 3 armour and helmets damage reduction 55% to 50%; Level 4 65% to 60%; Level 3 and 4 helmets reduce suppression by 68% and 80% [15].
- Official, 0.2.0: suppression rebuilt around shared falloff curves per weapon, stronger near-miss suppression from small and medium calibres, rate of fire accounted for, less screen shake [15].
- Official, 0.2.0: assault-rifle body shots slightly weaker, LMG body damage matches assault rifles, DMR headshots and upper-body hits slightly weaker, sniper hit-location damage increased, Scout Rifle headshots one-shot unhelmeted targets [15].
- Official stance: "WARDOGS is a hardcore shooter that doesn't forget it's a game" (Feb 2026, Jun 2026) [3][4]; store page: "Realistic gunplay balanced for gameplay rather than simulation" (live capture 2026-10-08) [1].
- Still no official absolute damage, headshot-multiplier, muzzle velocity or bullet-drop figure in any saved post [1][2][3][4][6][8][9][15].
- Season 1 combat balance (history): Havoc cannon-damage bug fix (30 Sep 2026) [8]; CIWS versus Havoc about 12 s to about 6 s (2 Oct 2026) [9].

# Scope

Covers what the developer has officially said about realism versus gameplay tuning, what is documented about bullet drop and travel, hit-registration and damage statements, and a chronological list of every balance-relevant change in each official Steam patch post up to the 0.2.0 notes of 14 Oct 2026. The Season 1 baseline tables are retained as history so that the diff to Season 02 is mechanical.

Covers the Update 0.2.0 combat-balance rules (damage, armour, suppression, bow, slugs, turrets, recoil and per-weapon changes) as the current state, with the Season 1 baseline kept for diffing. Excluded: per-weapon prices and unlocks (see weapons-catalogue), gadget and armour item detail such as the Molotov, rangefinder and medical bag (see gadgets-armor-and-equipment), the full release timeline (see patch-history), build and economy changes (see their owning documents), and server, anti-cheat and stability fixes except where they touch damage or balance. Sources are the saved official Steam posts and store snapshot dated 2026-10-08 and 2026-10-30; press is used only where it adds something the posts lack and is labelled.

# Definitions

- **Balance change**: a change the developer itself files under balance, XP bands, economy, unlocks, or a combat-affecting fix (see Detail for the exact filter).
- **Baseline values**: the Season 1 figures (through 2 Oct 2026), kept as history so Season 02 changes can be diffed.
- **Archetype**: the weapon class used in the 0.2.0 notes (assault rifle, DMR, LMG, sniper rifle, SMG) [15].
- **Suppression**: the screen and aim effect of near-miss fire; rebuilt in 0.2.0 [15].
- **Hit-location damage**: damage by body region (head, upper, middle and lower torso); adjusted per archetype in 0.2.0 [15].
- **CIWS**: close-in weapon system, named in the 2 Oct 2026 hotfix post as an anti-Havoc defence; its mechanics are not described officially [9].
- **Havoc**: an aircraft named in the 0.1.2 and 2 Oct 2026 posts; the posts do not describe it further [8][9].
- **Crit spot**: a damage-weak point on a buildable, referenced in the 0.1.2 bug-fix list [8].

# Current State

- Official, Update 0.2.0 (released 15 Oct 2026; notes posted 14 Oct 2026): the "Damage Update" reduces calibre base damage and rebalances archetypes; "Suppression Improvements" rebuilds suppression; detail in the Season 02 section below [15][17].
- Official, 0.2.0: the notes say the calibre reductions affect "every weapon that uses these rounds, including infantry & vehicle weapons" [15].
- Official: no post after 15 Oct 2026 is in the 2026-10-30 snapshot; later hotfixes are neither confirmed nor ruled out.
- The developer describes the game as "a hardcore shooter that doesn't forget it's a game", "balance gameplay depth and accessibility", with the line "Play YOUR way" (post of 18 Feb 2026) [4].
- A 16 Jun 2026 devlog titled "Addressing Feedback" states "Every player's line between arcade and realistic is different. We've drawn ours" and that "This isn't just about Killcam. This is our approach going forward throughout Early Access & Beyond" [3]. The post text is two sentences; the substance is in a video not captured here.
- A 21 May 2026 post, "Tactical Depth & Teamplay", lists "Real-world ballistics, audio and flight models" and "Every decision affects YOUR account balance" as the pillars of tactical depth, and says "every bullet fired, every loadout built" has consequences for the account balance [2].
- The 6 Jun 2026 gameplay-trailer post says "Play it slow, tactical and methodical, OR embrace the hardcore shooter that doesn't forget it's a game" [12].
- The Steam store page (live capture 2026-10-08) lists, as the Early Access current state, "Realistic gunplay balanced for gameplay rather than simulation", and describes "tactical gunplay and combined arms combat with building and destruction mechanics" and rockets that "destroy apartment blocks" [1]. Its Mature Content Description reads "Wardogs contains killing with weapons and melee combat", so melee combat exists; no melee damage detail is published [1]. The page's planned-features answer lists "expanded weapon categories" and new vehicle types including fighter jets for the full version [1].
- Before 0.2.0, the latest balance statement was the 2 Oct 2026 hotfix post: "we agree with player sentiment" that IR Rangefinders are too overpowered, and "we acknowledge we overcorrected" the CIWS in "the previous patch" [9]. In 0.2.0 the Infrared Range Finder runs on batteries, a battery lasting around 80 s of active use [15].
- The 30 Sep 2026 post said Season 02 "is planned to be a larger content update, with new map conditions, equipment, balance reworks and additional features" [8]; the 22 Sep 2026 Season 02 teaser had announced the season [11]; the 0.2.0 notes delivered the balance reworks [15], and the preview post of 9 Oct 2026 announced them in advance (it used pre-release names such as "Heavy and Super Heavy helmets") [16]. The notes' final names prevail.

# Detail

## Season 02 (Update 0.2.0) combat balance

All rows are official, from the Season 02 patch notes posted 2026-10-14 and live from 2026-10-15 [15][17]. The notes give relative changes; absolute damage is not stated. Where the notes give a Season 1 value it is shown as "Season 1 (0.1.2) -> Season 02 (0.2.0)".

The developer's stated reasoning: high-calibre rounds such as .308 and 7.62x54mmR were built for sniper rifles, where slow fire rate and small magazines balance big damage per shot, but in assault rifles, DMRs and LMGs they did "close to sniper damage at a much faster fire rate". The update "brings them closer to the other weapons in their archetype"; the FAL keeps the highest damage per shot among assault rifles but sits closer to the TCX-SPR and M4 [15].

### Calibre base damage reductions

The notes say these affect every weapon that uses the round, "including infantry & vehicle weapons" [15].

| Calibre | Base damage change |
|---------|--------------------|
| .308 Winchester | -25% |
| 7.62x54mmR | -20% |
| 7.62x39mm | -19% |
| .50 Cal | -16% |

Vehicle weapons named as affected: Little Bird AH-6M Minigun, Z20 Lakota Minigun, Humvee Minigun [15]. Which individual infantry weapons use each round is in weapons-catalogue.

### Archetype hit-location changes

| Archetype or item | Season 02 (0.2.0) change |
|-------------------|--------------------------|
| DMRs | Hit-location damage adjusted for the new calibre values; headshots and upper-body hits slightly weaker, so DMRs sit between assault rifles and snipers [15] |
| Assault rifles | Upper, middle and lower torso damage made more even; body shots do slightly less damage [15] |
| LMGs | Body damage now matches assault rifles; LMGs are meant to win through sustained fire and magazine size [15] |
| Sniper rifles | Hit-location damage increased to offset the base damage reduction [15] |
| Scout Rifle | Headshots now one-shot targets with no helmet; a Level 1 helmet takes two headshots [15] |
| Heavy and Artillery top machine turrets | Previously used the helicopter cannon's hit-location values; now use the assault-rifle and LMG values, so they do less damage to infantry depending on hit location [15] |

### Armour and helmets

| Item | Season 1 (0.1.2) | Season 02 (0.2.0) |
|------|------------------|-------------------|
| Level 3 armour and helmets, damage reduction | 55% | 50% [15] |
| Level 4 armour and helmets, damage reduction | 65% | 60% [15] |
| Level 3 helmet, suppression reduction | not stated | 68% [15] |
| Level 4 helmet, suppression reduction | not stated | 80% [15] |
| Level 4 helmet, other effects | none stated | Muffled audio, muffled proximity chat, restricted field of view, fogs over when sprinting [15] |

The preview post of 9 Oct 2026 used "Heavy and Super Heavy" helmet names; the final notes use Level 3 and Level 4 [15][16]. Vendor prices of these items are in price-tables-season-1; item detail is in gadgets-armor-and-equipment.

### Slugs and bow versus armour

- 12 gauge slugs: damage against armour now scales with armour tier instead of one flat reduction [15].
- Compound Bow: arrow trajectory has a shorter drop-off; slightly more effective against lower-tier armour than Season 1; bow damage against armour scales with armour tier [15].

### Suppression rebuild

The notes say suppression "was inconsistent and often unnoticeable" and has been rebuilt around shared falloff curves per weapon [15].

- Near-miss suppression from small and medium calibres is considerably stronger.
- Rate of fire is accounted for, so fast-firing small and medium weapons (such as SMGs and pistols) do not suppress disproportionately.
- Suppression screen shake is reduced to offset the stronger effects.
- Level 3 helmets reduce suppression by 68%; Level 4 helmets by 80%.

No numeric suppression strengths or falloff curves are published [15].

### Recoil and per-weapon adjustments

| Weapon | Change in 0.2.0 |
|--------|-----------------|
| MP5 | Recoil pattern updated to be more horizontal, "as it was too easy to use" [15] |
| Super-45 | Damage fall-off increased beyond 50 m (its effective range), pushing it into close quarters [15] |
| DMRs | New recoil pass across all DMRs to match their power curve [15] |
| MGL-40 | Muzzle velocity -25%; stronger damage fall-off at the 40mm outer radius; much more inaccuracy and sway, slower ADS speed and a reload penalty when used on the Little Bird bench [15] |
| Mosin | New PU 91/30 (3.5x) scope; no access to other optics until future customisation features [15] |

Prices and unlock levels for these weapons are in weapons-catalogue.

### Related 0.2.0 items touching combat

- Molotov: a thrown incendiary dealing impact damage plus damage over time to anyone standing in the flames; rain reduces molotov fire [15]. Detail in gadgets-armor-and-equipment.
- Infrared Range Finder: runs on batteries, about 80 s of active use, draining faster if toggled quickly [15].
- Medical Bag durability 100 -> 150 [15].
- Parachutes: take longer to open, do not open below about 10 m, and opening below roughly 50 m while falling fast means fall damage [15].
- Vanguard CIWS: reduced damage to the Spawn Vehicle (2.25x longer to kill it); CIWS cannon damage against structures retuned to shred light cover and struggle against heavy fortifications [15].
- Helicopter cockpit glass now works both ways, so shooting out through it damages the vehicle like incoming fire [15].
- Some weapon inspects are silent, which the developer says is known [15].

## What the developer has said about realism versus tuning

| Date (UTC) | Official post | Statement (quoted or closely paraphrased) | Source class |
|------------|---------------|-------------------------------------------|--------------|
| 2026-10-08 (capture) | Steam store page, "What is the current state of the Early Access version?" [1] | "Realistic gunplay balanced for gameplay rather than simulation"; About This Game: "tactical gunplay and combined arms combat" | Official (store page, Primary) |
| 2026-02-18 | "WARDOGS - Top Questions" [4] | "MILSIM? ARCADE? WARDOGS is a hardcore shooter that doesn't forget it's a game. Aiming to balance gameplay depth and accessibility. Every decision matters. From moment-to-moment gunfights to Progression Unlocks." Setting described as "grounded militaristic gameplay"; Early Access feature list includes "Grounded Gunplay & Vehicles". Custom "WAR DYNAMICS FRAMEWORK" on UE5; the post says the team is "heavily conscious of performance & input latency" | Official |
| 2026-03-03 | "Answering Your Questions" [5] | Video Q&A (100 players and 3 teams, monetisation, console release). The saved text has no combat content, so nothing on damage or ballistics can be cited from it | Official |
| 2026-05-21 | "Tactical Depth & Teamplay" [2] | "Real-world ballistics, audio and flight models"; "every bullet fired, every loadout built, and every second-to-second choice has real consequences for your account balance" | Official (marketing register) |
| 2026-06-06 | "Gameplay Trailer" [12] | "Play it slow, tactical and methodical, OR embrace the hardcore shooter that doesn't forget it's a game"; the game was shown in pre-alpha | Official |
| 2026-06-16 | "Addressing Feedback" [3] | "Every player's line between arcade and realistic is different. We've drawn ours. This isn't just about Killcam." Approach applies "throughout Early Access & Beyond" | Official |

Assessment: the developer's stated position is a deliberate middle between milsim and arcade, with the line left to the developer (High confidence that this is the stated position; evidence [1][3][4]). Where the line sits for any specific mechanic (damage falloff, recoil, time-to-kill) is not stated in text (Low confidence on any such inference; no evidence either way).

The 16 Jun 2026 post names "Killcam" explicitly, which implies a killcam feature was a feedback topic. The post text does not say whether a killcam exists in the Early Access build or how it was changed [3]. This is recorded in Open Questions.

## Bullet drop and bullet travel as documented

- Official sources: none. No saved Steam post and not the store page mention bullet drop, bullet velocity, travel time, gravity, zeroing or range tables [1][2][3][4][6][7][8][9]. The only official hook is the phrase "Real-world ballistics" [2].
- Press (beta era): the foundation document cites an allthings.how beta write-up reporting that real bullet drop and travel time are modelled and that carried weights differ (for example AMR 50 12.5 kg, LMGs 7.5 kg) [13]. This is press, drawn from closed-beta play, and is not confirmed by the developer. It is consistent with, but does not prove, the "real-world ballistics" claim [2].
- Related fix: the Season 1 changelog lists "Fixed a DPI issue affecting tank aiming"; that concerns input scaling on vehicle weapons, not ballistic behaviour [6].
- Related change: "Vehicle turrets now have a maximum operator rotation speed" (Season 1 changelog) [6].

## Damage model and hit registration as documented

| Topic | What is officially documented | Source |
|-------|-------------------------------|--------|
| Weapon damage values, headshot multipliers, falloff | Still no absolute values. 0.2.0 gives relative base-damage changes by calibre, qualitative hit-location changes by archetype, and the Super-45 falloff beyond 50 m and MGL-40 outer-radius falloff changes (Season 02 section) | [1][2][3][4][6][8][9][15] |
| Armor ratings, plate or vest damage reduction | From 0.2.0: Level 3 armour and helmets 55% to 50%, Level 4 65% to 60% damage reduction. Not published for other tiers (a Level 1 helmet exists; its reduction is not stated). Season 1 changelog gave no armour stats | [6][15] |
| Ammo types | AP ("762x54mm AP", "556mm AP") and, from 0.2.0, flesh-damage (HP) ammo (5.45x39mm, 9x19mm, 5.56mm, .308 Win) exist as unlocks; their damage effect is not described | [6][15] |
| Hit registration or netcode for hit validation | Revive validity checks are "fully server authoritative" (0.1.2). Hit validation itself is not described. The team states performance and input latency are priorities | [4][8] |
| Buildable damage | "Crit spots" on buildables were fixed to stop reappearing in the same place or jumping to the far side of a structure; they "now favour a spot you can reach from where you're standing". Destruction rewards "scale with their build progress" | [8] |
| Vehicle and air damage | Havoc bug "causing increased damage taken from 20mm and 30mm cannon fire" fixed (0.1.2); CIWS kill time on a Havoc about 12 s down to about 6 s (hotfix) | [8][9] |
| Melee | Melee combat exists (store-page Mature Content Description: "killing with weapons and melee combat"); no damage or balance detail is published | [1] |
| Killcam | Named in a devlog title context only | [3] |

## Chronological list of balance changes in each official patch post

Source posts: Season 1 changelog posted 2026-09-09 22:46 UTC (published as the launch-day pre-load) [6]; Launch Stability Hotfix #1 of 2026-09-10 [10]; Patch 0.11 post of 2026-09-12 (deployed 14 Sep) [7]; Update 0.1.2 of 2026-09-30 [8]; Security & Stability Hotfix notice of 2026-10-02 [14]; IR Goggles & CIWS Balance Hotfix of 2026-10-02 [9].

### 1. Season 1 changelog (9 to 10 Sep 2026) [6]

Developer-filed "Gameplay and vehicles":

- Z20 Lakota balance pass, plus a fix for sluggish pitch.
- Helicopter input damping now applies to every input device.
- Vehicle turrets now have a maximum operator rotation speed.
- 155mm, 122mm and flare deployables now take up more room in the loadout.
- Fixed a DPI issue affecting tank aiming.
- Z20 Lakota chase-camera rotation rattle reduced by 6 dB.

Developer-filed "Balance changes" (italic rationale in the post): levels roughly 10 to 20 slowed, the curve flattened from 35 onward, "our median players, at 20 to 25 hours, will be around level 20", and "the top 5%" who want the "big ticket items" will have to grind. Artillery moves to Career 90 and Heavy Tank to Driver 35; Driver "rejigged to give a satisfying escalation through attack vehicles"; Forward Operating Base and Large Hammer vendor prices raised "to make them more of a choice".

"XP Bands": "Previously our balancing was designed specifically for weekend long beta tests. Now they will be in-line with where we believe they should be. Each season we will have a different XP curve with different item orders." Values are in the Baseline table below.

"XP Events": player kill using an air vehicle 300 to 250 XP; supply crate item sold under $75 25 XP to 1 XP.

"Economy Changes": 14 vendor and role-track price changes and a rescaled supply-crate purchase curve (Baseline table). "Season 1.0 Unlocks" lists Career, Medic, Support and Driver level moves (Baseline table). No weapon damage, recoil or range change appears in this post.

### 2. Launch Stability Hotfix #1 (10 Sep 2026) [10]

Client hotfix for server joins, kicks and login queue. No balance or damage content.

### 3. Patch 0.11 (announced 12 Sep, deployed 14 Sep 2026) [7]

Server browser, community-server discoverability, Asian capacity, and an economy-abuse policy. No weapon, damage or unlock changes. The only balance-adjacent items are "Various cash exploits have been fixed", a temporary "5% End of Match cash bonus" on community servers "for the next week", and the abuse sanctions (timed ban plus cash and XP reset for exploits; permanent ban for exploit tutorials and XP-farming servers). The post says Season 2 content is not affected by the quality-of-life queue.

### 4. Update 0.1.2 (30 Sep 2026, maintenance at 08:00 UTC) [8]

Balance- or combat-relevant items only:

- Revive action validity checks now fully server authoritative.
- Vehicle fly-through exploit fixed; rewards capped.
- Buildable-destruction rewards now scale with build progress, so destroying a placed schematic no longer gives a full reward.
- Depositing pallets into a FOB outside the zone awards reduced rewards.
- Throwables (grenades, smoke, C4) can no longer be used from enclosed vehicle seats.
- Adaptive crosshair now hides while aiming down sights.
- Buildable crit spots no longer reappear in the same place, get pushed into corners, or jump to the far side; they favour a spot reachable from the player's position.
- Havoc bug fixed that "caus[ed] increased damage taken from 20mm and 30mm cannon fire".

The post states that Season 02 will include "balance reworks" [8]. No numeric weapon values are given.

### 5. Security & Stability Hotfix notice (2 Oct 2026) [14]

Scheduled 08:00 UTC, about one hour downtime, for minor security and stability issues. No balance content.

### 6. IR Goggles & CIWS Balance Hotfix (2 Oct 2026, 15:39 UTC) [9]

- IR Rangefinders will be disabled in the vendor, once servers restart across regions within 12 hours, "until Season 02, where they will require batteries to use". Reason given: "we agree with player sentiment and they cross the line into being too overpowered."
- The CIWS "now destroys the havoc in around 6 seconds as opposed to 12". "We acknowledge we overcorrected this in the previous patch."
- "No new client download or server downtime is required."

## Baseline values (as of the 2 Oct 2026 hotfix, pre-Season-02)

All values are official (Steam news posts) unless the Source column says otherwise. "Before" values are the beta-era figures the post lists as the previous state; "as-of" is the value after the patch.

### Combat-relevant

| Value | As-of value | As-of version | Source |
|-------|-------------|---------------|--------|
| CIWS time to destroy a Havoc | about 6 s (was about 12 s) | 2 Oct 2026 hotfix | [9] |
| IR Rangefinders in vendor | Disabled until Season 02 | 2 Oct 2026 hotfix | [9] |
| Air-vehicle player kill XP | 250 XP (was 300) | Season 1 changelog, 10 Sep 2026 | [6] |
| Z20 Lakota chase-camera rotation rattle | reduced by 6 dB | Season 1 changelog | [6] |
| Havoc damage taken from 20mm and 30mm cannon | bug fixed; no numeric value published | 0.1.2, 30 Sep 2026 | [8] |
| Players per match / teams / zone / win score | 100 / 3 / 2x2 km zone in a 256 km2 map / 100 points | Feb 2026 post, store snapshot 2026-10-08 | [1][4] |
| Starting cash | $10,000 | store snapshot 2026-10-08 | [1] |

### Role-track XP bands

| Level | As-of XP | Previous XP | Change stated in post | Source |
|-------|----------|-------------|-----------------------|--------|
| Below 6 | unchanged | unchanged | none | [6] |
| 6 | 9,250 | 8,750 | 5.7% slower | [6] |
| 10 | 35,000 | 25,000 | 40.0% slower | [6] |
| 15 | 110,000 | 54,750 | 100.9% slower | [6] |
| 20 | 250,000 | 111,500 | 124.2% slower | [6] |
| 25 | 325,000 | 192,000 | 69.3% slower | [6] |
| 30 | 400,000 | 293,750 | 36.2% slower | [6] |
| 35 | 500,000 | 416,500 | 20.0% slower | [6] |
| 40 | 650,000 | 551,250 | 17.9% slower | [6] |
| 45 | 800,000 | 689,500 | 16.0% slower | [6] |
| 50 | 1,000,000 | 838,000 | 19.3% slower | [6] |

All as-of version: Season 1 changelog, 10 Sep 2026.

### XP events and supply crates

| Value | As-of | Previous | Source |
|-------|-------|----------|--------|
| Supply crate item sold under $75 | 1 XP | 25 XP | [6] |
| Supply crate purchase curve | 1 to 200 | 25 to 250 | [6] |

### Vendor and track prices (Season 1 changelog, 10 Sep 2026)

| Item | As-of | Previous | Source |
|------|-------|----------|--------|
| Vendor, Forward Operating Base | $7,500 | $2,500 | [6] |
| Vendor, Large Hammer | $2,400 | $1,600 | [6] |
| Career, Artillery Tank | $500,000 | $400,000 | [6] |
| Recon, 6-10x MRAD scope | $40,000 | $25,000 | [6] |
| Recon, 6-10x MOA scope | $45,000 | $30,000 | [6] |
| Support, Medium Hammer | $25,000 | $10,000 | [6] |
| Support, Large Hammer | $75,000 | $25,000 | [6] |
| Pilot, small armoured supply crate | $10,000 | $5,000 | [6] |
| Pilot, Little Bird with miniguns | $50,000 | $25,000 | [6] |
| Pilot, Z20 Lakota | $35,000 | $50,000 | [6] |
| Driver, URAL | $35,000 | $50,000 | [6] |
| Driver, Dune Buggy | $25,000 | $35,000 | [6] |
| Driver, Kodiak Flatbed | $35,000 | $15,000 | [6] |
| Driver, Music Tape H | $2,500 | $5,000 | [6] |

### Unlock levels (Season 1 changelog, 10 Sep 2026)

| Track | Item | As-of level | Previous level | Source |
|-------|------|-------------|----------------|--------|
| Career | Sports Parachute | 35 | 36 | [6] |
| Career | Large Backpack | 55 | 56 | [6] |
| Career | 762x54mm AP | 82 | 83 | [6] |
| Career | 556mm AP | 83 | 85 | [6] |
| Career | Deagle | 85 | 90 | [6] |
| Career | Artillery Tank | 90 | 55 | [6] |
| Medic | PP-19 50 round drum magazine | 29 | 33 | [6] |
| Support | Large Hammer | 8 | 7 | [6] |
| Driver | URAL | 3 | 4 | [6] |
| Driver | Kodiak Assault | 6 | 8 | [6] |
| Driver | Dune Buggy | 8 | 10 | [6] |
| Driver | Kodiak Flatbed | 10 | 2 | [6] |
| Driver | Large Supply Crate | 16 | 20 | [6] |
| Driver | URAL Covered | 18 | 30 | [6] |
| Driver | Music Tape H | 23 (moved from Pilot 28) | Pilot 28 | [6] |
| Driver | URAL Attack | 25 | 40 | [6] |
| Driver | Humvee with minigun | 30 | 35 | [6] |
| Driver | Heavy Tank | 35 (moved from Career 35) | Career 35 | [6] |

### Temporary or policy values

| Value | As-of | Source |
|-------|-------|--------|
| Community-server end-of-match cash bonus | 5% for one week from 14 Sep 2026 | [7] |
| Cash and XP after exploit sanction | reset to 0 | [7] |

# Early Access Changes & Known Issues

| Date (UTC) | Change | Source |
|------------|--------|--------|
| 2026-09-09/10 | Season 1 changelog: progression, price and unlock rebalance; deployables take more loadout space; turret rotation cap; Z20 balance pass | [6] |
| 2026-09-12/14 | Patch 0.11: no combat balance; cash exploits fixed; community-server bonus | [7] |
| 2026-09-30 | Update 0.1.2: server-authoritative revives, reward caps, crit-spot fix, Havoc cannon-damage bug fix | [8] |
| 2026-10-02 | Hotfix: IR Rangefinders removed from vendor until Season 02; CIWS time-to-kill on Havoc about 12 s to about 6 s | [9] |
| 2026-10-09 | Season 02 Preview: announced the rework using pre-release names (Heavy and Super Heavy helmets) | [16] |
| 2026-10-14 | Season 02 patch notes: Damage Update (calibre reductions, archetype and armour changes), suppression rebuild, bow, slug, turret, recoil and per-weapon changes | [15] |
| 2026-10-15 | Update 0.2.0 released, servers back online | [17] |

Known issues: the 0.2.0 notes state that some weapon inspects are silent and that this is known [15]. The 2 Oct 2026 post conceded a previous CIWS tuning "overcorrected" [9]. No other open combat bugs are listed in the saved posts.

# Admin & Technical Notes

None found for damage or ballistics; the 0.2.0 notes list no server-side damage or suppression setting. The 0.1.2 post lists admin features (scheduled restarts, RCON restrictions) that are unrelated to balance [8]. No server-side setting for damage, ballistics or friendly fire is documented in the saved posts.

# Risks & Caveats

- The documented balance record is thin and mostly progression tuning; do not read it as a weapon-balance history [6].
- The 21 May 2026 "real-world ballistics" claim is pre-launch marketing; its video content was not captured [2].
- Season 1 tables are history; the 0.2.0 values are current only as of 15 Oct 2026 and may change per hotfix or at the next season [6][15].
- The 0.2.0 notes give percentages and rules but no absolute damage; do not derive per-shot damage from them without the Season 1 base values, which the developer never published.
- The Season 1 changelog mixes price rises and cuts (for example Z20 Lakota and URAL fall to $35,000 while the Large Hammer rises). The values are recorded as posted, and the Support Large Hammer price ($25,000 to $75,000) and the vendor Large Hammer price ($1,600 to $2,400) are both listed without the post saying how they relate [6].
- Press coverage of the same posts (for example the Gfinity and BisectHosting reproductions cited by the foundation) may omit lines; this document uses the saved official text.
- Posts are marketing and ops text, written by the developer; no independent test of any statement has been done.

# Open Questions

- **Store-page wording (resolved in 1.0.1).** An earlier version of this document recorded a conflict with the foundation over the store-page wording, because the saved storefront-API JSON omitted several fields. The live capture of 2026-10-08 contains "Realistic gunplay balanced for gameplay rather than simulation" and "tactical gunplay" [1], so the foundation's quote was correct and no conflict remains. Residual point: the foundation's exact phrase "tuned for gameplay" differs by a word from the live "balanced for gameplay rather than simulation"; the live wording prevails.
- **Post identifier conflict.** The foundation cites the Season 1 changelog under a different Steam post id than the one in the saved index (gid 1843481262690549) [6].
- **Patch dating conflict.** The foundation dates the Season 1 changelog 10 Sep 2026; the saved post is stamped 2026-09-09 22:46 UTC (pre-load) [6]. The foundation also treats "0.11" as an unverified snippet; the official post exists as "Patch 0.11", published 12 Sep and deployed 14 Sep [7].
- **Foundation says the official Steam text was not retrievable and patch content rests on press.** The saved official text now exists; where the foundation and this document differ, the official text prevails.
- Which patch is "the previous patch" in which the CIWS was overcorrected [9]. The 0.1.2 notes do not list a CIWS change [8]; the change may be unlisted, or "previous patch" may mean a server-side change.
- Whether bullet drop and travel time exist as simulated mechanics, and with what parameters. Only press supports it [13]. Resolution: an in-game measurement or a developer statement.
- Damage values, headshot multipliers, armor ratings and ammo-type (AP) effects: not published.
- Hit registration model (client-side, server-authoritative or hybrid) for gunfire: not stated.
- What the "Killcam" change in the 16 Jun 2026 devlog was, and whether killcam exists in Early Access [3].
- Whether Season 02 reset account progression: the 0.2.0 notes do not mention a wipe or reset, so it is unconfirmed either way [15].
- Whether the "-25%" style calibre reductions are multiplicative on the previous base damage (the notes say "base damage reductions" without a formula) [15].
- Which weapons the Level 3 and 4 suppression reductions (68%, 80%) are measured against; the notes give no baseline [15].
- The armour reduction for Level 1 and 2 items and for other tiers is not stated.
- A Russian-language press headline in the Steam news index (30 Sep 2026) reports a developer saying balance will not be fixed by the start of Season 2; the article body was not captured, so it is not used here.

# References

**Primary Sources**

- [1] **Valve / Bulkhead (Steam)** — *WARDOGS* store page (live capture 2026-10-08, browser-rendered; supersedes the earlier storefront-API JSON, which omitted several fields). https://store.steampowered.com/app/1867240/WARDOGS/. Accessed 2026-10-08.
- [2] **Bulkhead (Steam news)** — *WARDOGS - Tactical Depth & Teamplay* (21 May 2026). https://store.steampowered.com/news/app/1867240/view/1833334318569240. Accessed 2026-10-08.
- [3] **Bulkhead (Steam news)** — *WARDOGS | Addressing Feedback* (16 Jun 2026). https://store.steampowered.com/news/app/1867240/view/1835236783575445. Accessed 2026-10-08.
- [4] **Bulkhead (Steam news)** — *WARDOGS - TOP QUESTIONS* (18 Feb 2026). https://store.steampowered.com/news/app/1867240/view/1825093633182385. Accessed 2026-10-08.
- [5] **Bulkhead (Steam news)** — *WARDOGS - Answering Your Questions* (3 Mar 2026). https://store.steampowered.com/news/app/1867240/view/1825727806721330. Accessed 2026-10-08.
- [6] **Bulkhead (Steam news)** — *Pre-Load Live & Season 1 Changelog* (9 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1843481262690549. Accessed 2026-10-08.
- [7] **Bulkhead (Steam news)** — *SCHEDULED MAINTENANCE & PATCH 0.11* (12 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1843481262698449. Accessed 2026-10-08.
- [8] **Bulkhead (Steam news)** — *WARDOGS | Update 0.1.2 (Minor Patch)* (30 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1845383656376490. Accessed 2026-10-08.
- [9] **Bulkhead (Steam news)** — *IR Goggles & CIWS Balance Hotfix* (2 Oct 2026). https://store.steampowered.com/news/app/1867240/view/1845383656386801. Accessed 2026-10-08.
- [10] **Bulkhead (Steam news)** — *Launch Stability Hotfix #1* (10 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1843481262693332. Accessed 2026-10-08.
- [11] **Bulkhead (Steam news)** — *WARDOGS | Season 02 Teaser* (22 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1844115010504839. Accessed 2026-10-08.
- [12] **Bulkhead (Steam news)** — *WARDOGS - Gameplay Trailer* (6 Jun 2026). https://store.steampowered.com/news/app/1867240/view/1834602721194537. Accessed 2026-10-08.
- [15] **Bulkhead (Steam news)** — *WARDOGS | Season 02 Patch Notes* (14 Oct 2026). https://store.steampowered.com/news/app/1867240/view/1846651706674560. Accessed 2026-10-30.
- [16] **Bulkhead (Steam news)** — *WARDOGS | Season 02 Preview* (9 Oct 2026). https://store.steampowered.com/news/app/1867240/view/1846018067933823. Accessed 2026-10-30.
- [17] **Bulkhead (Steam news)** — *WARDOGS | SEASON 02 IS NOW LIVE* (15 Oct 2026). https://store.steampowered.com/news/app/1867240/view/1846651706677015. Accessed 2026-10-30.
- [14] **Bulkhead (Steam news)** — *WARDOGS | Security & Stability Hotfix* (2 Oct 2026). https://store.steampowered.com/news/app/1867240/view/1845383656384445. Accessed 2026-10-08.

**Press & Secondary**

- [13] **allthings.how** — *Wardogs beta: weapons, prices and progression* (beta-era data, not final; cited via the foundation). https://allthings.how/?p=121341. Accessed 2026-10-08.

**Player-Reported Evidence**

None cited.

# Further Reading

- Team17 press release: https://www.gamedeveloper.com/press-release/wardogs-is-coming-to-steam-early-access-on-10-september

# Related Documents

- combat-loadouts-foundation
- weapons-catalogue
- gadgets-armor-and-equipment
- patch-history

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft, pre-Season-02 baseline. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after independent re-verification of validate, markdownlint, links (0 dead) and Steam post ids. Pre-Season-02 baseline. | Standing mandate (auto-approve on green QA) |
| 1.0.1 | 2026-10-08 | Research Pipeline (revision worker) | Corrected against live store-page capture; store page does say "Realistic gunplay balanced for gameplay rather than simulation" and "tactical gunplay", store-page wording conflict with foundation resolved and made Primary, melee combat and planned "expanded weapon categories" noted, reference [1] updated to live capture. | Standing mandate (auto-approve on green QA) |
| 1.1.0 | 2026-10-30 | Research Pipeline (virtual agent) | Revised for Update 0.2.0 from the official Season 02 patch notes, preview and live posts: calibre base damage reductions, DMR/AR/LMG/Scout Rifle/slug/bow/turret changes, Level 3 and 4 armour and helmet changes, suppression rebuild, MP5/Super-45/MGL-40/Mosin recoil and per-weapon changes, Little Bird bench MGL penalty, molotov and rangefinder battery summary; Season 1 baseline kept as history; forward-looking Season 02 sentences replaced by the known outcome. | — |
