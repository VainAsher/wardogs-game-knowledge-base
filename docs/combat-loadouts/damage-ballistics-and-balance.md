---
id: damage-ballistics-and-balance
title: "Damage, Ballistics & Balance Changes"
version: 1.0.1
status: frozen
confidence: Medium
category: Combat & Loadouts
topic: "Damage model, ballistics, hit registration, and the balance-change history"
market: Global
game_version: "Early Access Season 1 (pre-Season-02 baseline): 10 Sep 2026 changelog through the 2 Oct 2026 balance hotfix; Season 02 due 15 Oct 2026"
document_type: depth
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-10-22
sources_verified: 2026-10-08
supersedes: null
related: [combat-loadouts-foundation, weapons-catalogue, gadgets-armor-and-equipment, patch-history]
tags: [combat, damage, ballistics, balance, patch-notes, baseline, early-access]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | damage-ballistics-and-balance |
| Version | 1.0.1 |
| Status | frozen |
| Confidence | Medium |
| Category | Combat & Loadouts |
| Game version | Season 1 baseline, through the 2 Oct 2026 balance hotfix (pre-Season-02) |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-10-22 |

# Executive Summary

The developer has never published a damage table, ballistic table, hit-registration description or armor rating for WARDOGS. What exists officially is a philosophy: the game is "a hardcore shooter that doesn't forget it's a game", with "real-world ballistics, audio and flight models" claimed in a May 2026 devlog summary [2][3][4]. No official text says what that means in numbers, and no official text mentions bullet drop or bullet travel time.

The official balance record is a short list of patch posts. The only post with a large, itemised balance section is the Season 1 changelog of 9 to 10 Sep 2026, and it is almost entirely progression and economy tuning (XP bands, unlock levels, prices), not weapon damage [6]. Combat-damage changes are rare: one Havoc cannon-damage bug fix in update 0.1.2 [8], and a 2 Oct 2026 hotfix that shortened the time the CIWS takes to destroy a Havoc from about 12 s to about 6 s and disabled IR Rangefinders in the vendor [9].

Document confidence is Medium. Every balance entry rests on official Steam posts (High), but the realism, ballistics and hit-registration sections rest on a few sentences of marketing-register text plus one beta-era press report, and the main conclusion is that the topic is largely undocumented.

# Key Takeaways

- Official stance: "WARDOGS is a hardcore shooter that doesn't forget it's a game", aiming to balance "gameplay depth and accessibility" (Feb 2026, Jun 2026) [3][4].
- Official claim, pre-launch: "Real-world ballistics, audio and flight models" (21 May 2026 post summary) [2]. The video behind it was not available as text, so the specifics are unknown.
- The Steam store page (live capture 2026-10-08) states, under the Early Access current state, "Realistic gunplay balanced for gameplay rather than simulation", and its About This Game text says "tactical gunplay" [1]. This is the developer's most direct Primary statement of the realism-versus-gameplay position. It gives no numbers.
- No official bullet drop, muzzle velocity, damage, headshot-multiplier or armor figure exists in any saved Steam post or in the store page [1][2][3][4][6][7][8][9].
- Combat-relevant balance changes in the official record: Havoc 20mm/30mm damage-taken bug fix (30 Sep 2026) [8]; CIWS-versus-Havoc kill time roughly 12 s to roughly 6 s and IR Rangefinders removed from the vendor until Season 02 (2 Oct 2026) [9].
- Season 1 changelog (10 Sep 2026) balance is progression-centred: 10 XP-band changes, 6 Career, 1 Medic, 1 Support and 10 Driver unlock-level moves, and 14 vendor price changes [6].
- The developer says each season will have "a different XP curve with different item orders", so these baseline values are expected to change at Season 02 [6][8][11].

# Scope

Covers what the developer has officially said about realism versus gameplay tuning, what is documented about bullet drop and travel, hit-registration and damage statements, and a chronological list of every balance-relevant change in each official Steam patch post up to 2 Oct 2026. It is a pre-Season-02 baseline: the Detail section carries a "Baseline values" table so a later diff can be mechanical.

Excluded: per-weapon stat tables (see weapons-catalogue), gadget and armor detail (see gadgets-armor-and-equipment), the full release timeline (see patch-history), and server, anti-cheat and stability fixes except where they touch damage or balance. Sources are the saved official Steam posts and store snapshot dated 2026-10-08; press is used only where it adds something the posts lack and is labelled.

# Definitions

- **Balance change**: a change the developer itself files under balance, XP bands, economy, unlocks, or a combat-affecting fix (see Detail for the exact filter).
- **Baseline values**: the figures as of this document's game version, kept so Season 02 changes can be diffed.
- **CIWS**: close-in weapon system, named in the 2 Oct 2026 hotfix post as an anti-Havoc defence; its mechanics are not described officially [9].
- **Havoc**: an aircraft named in the 0.1.2 and 2 Oct 2026 posts; the posts do not describe it further [8][9].
- **Crit spot**: a damage-weak point on a buildable, referenced in the 0.1.2 bug-fix list [8].

# Current State

- The developer describes the game as "a hardcore shooter that doesn't forget it's a game", "balance gameplay depth and accessibility", with the line "Play YOUR way" (post of 18 Feb 2026) [4].
- A 16 Jun 2026 devlog titled "Addressing Feedback" states "Every player's line between arcade and realistic is different. We've drawn ours" and that "This isn't just about Killcam. This is our approach going forward throughout Early Access & Beyond" [3]. The post text is two sentences; the substance is in a video not captured here.
- A 21 May 2026 post, "Tactical Depth & Teamplay", lists "Real-world ballistics, audio and flight models" and "Every decision affects YOUR account balance" as the pillars of tactical depth, and says "every bullet fired, every loadout built" has consequences for the account balance [2].
- The 6 Jun 2026 gameplay-trailer post says "Play it slow, tactical and methodical, OR embrace the hardcore shooter that doesn't forget it's a game" [12].
- The Steam store page (live capture 2026-10-08) lists, as the Early Access current state, "Realistic gunplay balanced for gameplay rather than simulation", and describes "tactical gunplay and combined arms combat with building and destruction mechanics" and rockets that "destroy apartment blocks" [1]. Its Mature Content Description reads "Wardogs contains killing with weapons and melee combat", so melee combat exists; no melee damage detail is published [1]. The page's planned-features answer lists "expanded weapon categories" and new vehicle types including fighter jets for the full version [1].
- The latest official balance statement in the saved record is the 2 Oct 2026 hotfix post: "we agree with player sentiment" that IR Rangefinders are too overpowered, and "we acknowledge we overcorrected" the CIWS in "the previous patch" [9].
- The 30 Sep 2026 post states that Season 02 "is planned to be a larger content update, with new map conditions, equipment, balance reworks and additional features" [8]. Season 02 is announced for 15 Oct 2026 [11].

# Detail

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
| Weapon damage values, headshot multipliers, falloff | Nothing (the store page gives only the qualitative "Realistic gunplay balanced for gameplay rather than simulation") | [1][2][3][4][6][8][9] |
| Armor ratings, plate or vest damage reduction | Nothing. The Season 1 changelog mentions only a Sports Parachute, Large Backpack and ammo-type unlocks, not armor stats | [6] |
| Ammo types | "762x54mm AP" and "556mm AP" exist as Career unlocks; their damage effect is not described | [6] |
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
| 2026-10-15 (planned) | Season 02, with "balance reworks" and a different XP curve and item order per season | [8][11][6] |

Known issues: none listed in the saved posts as open combat bugs. The 2 Oct 2026 post concedes a previous CIWS tuning "overcorrected" [9].

# Admin & Technical Notes

None found for damage or ballistics. The 0.1.2 post lists admin features (scheduled restarts, RCON restrictions) that are unrelated to balance [8]. No server-side setting for damage, ballistics or friendly fire is documented in the saved posts.

# Risks & Caveats

- The documented balance record is thin and mostly progression tuning; do not read it as a weapon-balance history [6].
- The 21 May 2026 "real-world ballistics" claim is pre-launch marketing; its video content was not captured [2].
- Numbers here are Season 1 values and are expected to change at Season 02 (15 Oct 2026) [6][11].
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
- Whether the Season 02 changes (IR Rangefinder batteries, "balance reworks") will reset the Season 1 XP and price tables [8][9].
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
