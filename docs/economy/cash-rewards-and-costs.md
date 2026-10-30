---
id: cash-rewards-and-costs
title: "Cash Rewards & Costs"
version: 1.1.0
status: frozen
confidence: High
category: Economy
topic: "How cash and XP are earned per action, logistics streaks, destroyed rewards, spotting, exploit fixes and build supply costs"
market: Global
game_version: "Early Access Season 02, Update 0.2.0 (15 Oct 2026); official posts through 2026-10-15 (snapshot 2026-10-30)"
document_type: depth
created: 2026-10-08
updated: 2026-10-30
review_due: 2026-11-20
sources_verified: 2026-10-30
supersedes: null
related: [economy-foundation, death-penalty-and-rebuy, price-tables-season-1, season-reset-and-currencies, control-zone-and-match-flow, fob-and-base-building, progression-unlock-tables]
tags: [economy, cash, rewards, hot-zone, logistics, spotting, exploits, build-costs, season-2, update-0-2-0, early-access]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | cash-rewards-and-costs |
| Version | 1.1.0 |
| Status | frozen |
| Confidence | High |
| Category | Economy |
| Game version | Early Access Season 02, Update 0.2.0 (15 Oct 2026); official posts through 2026-10-15 (snapshot 2026-10-30) |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-30 |
| Review due | 2026-11-20 |

# Executive Summary

Until Season 02 the studio published no per-action cash amounts; the Season 1 and 0.1.2 posts described reward changes only qualitatively [1][3]. The Season 02 Patch Notes (posted 14 Oct 2026, released as Update 0.2.0 on 15 Oct 2026) change that: their "Cash & XP Reward Changes" section prints dollar and XP values for new action rewards, logistics deliveries and streaks, vehicle, buildable and supply-crate destruction, drill tower capture and spotting, and lists seven exploit fixes [14][15]. The notes also give new build supply costs [14].

The Hot Zone still pays double cash and cash persists between matches [4][5]. In Season 02 only, the Lonestar faction gets a cash and XP win bonus and teamplay multipliers, and a losing team 40 points behind gets a 20% vendor discount [14]. The notes contain an in-post update: the logistics streak values were revised after first posting to include the zone multiplier, and this document uses the updated values [14].

Confidence is High: every number comes from the official Season 02 Patch Notes or earlier official posts. Two player-reported guides are kept only as labelled background. Several points the notes do not state stay in Open Questions, among them the Lonestar multiplier values, the death-penalty rules and any progression wipe.

# Key Takeaways

- 0.2.0 (15 Oct 2026): assault-archetype weapon kill bonus rose $1,500 to $2,000; FOB hacking pays the hacker $2,500 / 250 XP and teammates in the FOB radius $1,000 / 250 XP [14].
- Logistics: base rewards were lowered and new delivery streaks add per-delivery bonuses, for example crates +$100 / +50 XP each up to 10 (updated values) [14].
- Vehicle destroyed rewards are now per variant: Humvee default $600 but Humvee [Minigun] $5,000; armed variants give 1.5x the XP of the default [14].
- Spotting rewards are about 30% lower than Season 1 and scale with the value of the target; a spotted target destroyed by an enemy faction now pays 25% of the reward, down from 50% [14].
- Build supply costs changed: Door 22 to 80, Gate 85 to 200, L81 Mortar 150 to 600, Talon 9K-SAM 1,000 to 650, Hot Zone Magnet 2,250 to 2,750 [14].
- Exploit fixes: supply-crate selling has diminishing returns per buyer, selling to an enemy gives no cash or XP, FOB Supplied Assist is split between assisting players [14].
- Still unpublished: Hot Zone multiplier scope, Lonestar bonus values, whether cash converts to Gold Bars automatically at Season 02 start [4][14].

# Scope

Covers how cash and XP are earned and lost per action as of Update 0.2.0, with the Season 1 (0.1.2) values kept as dated history: new rewards, role-reward reassignment, logistics (base values and streaks), capture, vehicle, buildable and supply-crate destroyed rewards, spotting, exploit fixes, build supply costs, the Season 02 faction experiment, and the exploit policy. Excludes vendor prices (see price-tables-season-1), role-track unlocks and the XP curve (progression-unlock-tables), the death penalty and rebuy (death-penalty-and-rebuy), the seasonal reset and Gold Bar rate (season-reset-and-currencies), buildable behaviour and drill rig mechanics (fob-and-base-building) and match flow (control-zone-and-match-flow). It deepens economy-foundation without restating it.

# Definitions

- **Teamplay action**: an action that the developer says rewards cash, such as reviving, transporting or spotting [4].
- **Hot Zone**: a shifting sub-zone of the Control Zone where players count double towards presence and earn double cash [4].
- **Build supply cost**: the supplies a buildable consumes; in 0.2.0 the destroyed-buildable cash reward matches this cost [14].
- **Delivery streak**: a bonus added for each consecutive delivery in a row, up to a cap, introduced in 0.2.0 [14].
- **End-of-match bonus**: a cash bonus at match end, referenced by the 5% community-server promotion (Patch 0.11) [2].
- **Economy abuse**: cash or XP exploits, tutorialising them, XP farming or real money trading as defined in the developer policy [1][2].

# Current State

- Teamplay actions award cash; the official examples are reviving squadmates, transporting friendlies to the zone and controlling the objective (Steam page, 2026-10-08) [5].
- The Hot Zone yields double cash and players count double towards zone presence (Steam news, 18 Feb 2026) [4].
- Cash persists between matches and can be spent or exchanged for Gold Bars, the endgame cosmetic currency (18 Feb 2026) [4]. In-game cash and Gold Bars will never be sold for real money (11 Aug 2026) [6].
- Update 0.2.0 is live (15 Oct 2026, servers back online) and contains the reward values in the Detail section [14][15].
- Wager Vendor: announced as a way to "bet your own cash on your own performance"; it is not available at Season 02 launch and "will open later in Season 2" [14].
- No official post after 2026-10-15 was seen in the 2026-10-30 snapshot.

# Detail

## Earning actions: what was published, by source

| Source class | Actions listed | Amount |
|--------------|----------------|--------|
| Official (Steam news, 18 Feb 2026) | Revives, transport, kills, spotting, "and MORE" [4] | Not published at the time |
| Official (Steam page) | Reviving squadmates, transporting friendlies to the zone, controlling the objective [5] | Not published |
| Official (0.1.2 notes, 30 Sep 2026) | Revive actions, vehicle fly-through, destroying buildables, depositing pallets into a FOB [1] | Not published |
| Official (0.2.0 notes, 14 Oct 2026) | New action rewards, logistics, destroyed rewards, drill tower capture, spotting [14] | Published; tables below |
| Player-reported (allthings.how) | Kills, assists, revives, heals, spotting, resupplying, repairing vehicles, FOB building, hauling supplies, driving or flying teammates, tips, holding the Control Zone, destroying enemy vehicles [11] | Not published |

The player-reported guide's own dollar figures are limited to the $10,000 starting balance [11]. A second guide gives item costs only (for example Galil unlock $35,000), which are costs, not income (player-reported) [12].

## Hot Zone double cash

Official: the Hot Zone is a shifting sub-zone inside the Control Zone, players inside count double for presence and it "yields DOUBLE CASH" [4]. The Steam page repeats "chase the 'Hot Zone' to earn double the cash" [5]. Player-reported: standard cash applies in the Control Zone outside the Hot Zone, with no payout figures given [13]. The 0.2.0 notes do not restate the Hot Zone multiplier; the updated streak values include a "zone multiplier" for deliveries dropped in the Control Zone without giving its size [14]. Whether the multiplier applies to every action is not stated (see Open Questions).

## New and changed action rewards (0.2.0)

All rows: Season 02 Patch Notes, 14 Oct 2026, live 15 Oct 2026 [14]. Season 1 (0.1.2) values are shown where the notes print an old value.

| Action | Season 1 (0.1.2) | Season 02 (0.2.0) |
|--------|------------------|-------------------|
| Kill with an assault-archetype weapon (bonus) | $1,500 | $2,000 |
| FOB hacking, hacker | $2,500 / 250 XP (the notes say the hacker "still gets" this) | $2,500 / 250 XP |
| FOB hacking, teammates in the FOB radius | not paid | $1,000 / 250 XP |
| Door breached with the Halligan Bar | not paid | $100, once per door; Halligan Bar uses 5 to 7 |
| Friendly FOB door closed | not paid | $75 |
| Destroying a FOB | not stated | Bonus up to +$7,500 / +250 XP by supplies held (maxed at 25,000 supplies) |
| Capturing a hostile drill tower | $750 / 250 XP | $1,500 / 300 XP |
| Barbed wire kills | Contributed cash and XP | No longer contribute cash or XP |

### Role reward reassignment (0.2.0)

Role XP now flows differently [14]:

- Destroying a buildable gives assault XP instead of support.
- Artillery gives driver XP instead of support.
- IED and C4 give assault XP instead of support.
- Repair XP goes to the driver or pilot track depending on the vehicle repaired, instead of a flat support amount.

Track unlocks themselves are in progression-unlock-tables.

## Logistics (0.2.0)

The notes state that base logistics rewards are lower and that delivery streaks add a bonus for every consecutive run, so logistics players are rewarded for return trips [14].

### Delivery streaks (new)

Values below are the updated figures. The notes say the originally posted values were "base design values without a zone multiplier" and were later replaced by "the actual values players will receive when dropped in the Control Zone". The original numbers are not preserved in the post [14].

| Streak | Bonus per delivery in a row | Cap |
|--------|-----------------------------|-----|
| Crates | +$100 / +50 XP | 10 |
| Pallets | +$250 / +100 XP | 10 |
| Players | +$25 / +5 XP | 25 |
| Return trips | +$50 / +25 XP | 10 |

### Base logistics values

| Action | Season 1 (0.1.2) | Season 02 (0.2.0) |
|--------|------------------|-------------------|
| Player delivered | $150, 50 XP | $100, 25 XP |
| Player delivered (ground vehicle) | $500 | $350 |
| Return trip (ground vehicle) | $250, 100 XP | $150, 50 XP |
| Deploy supply crate, small | $500, 250 XP | $250, 200 XP |
| Deploy supply crate, large | $1,000, 500 XP | $500, 400 XP |
| Deploy supply crate, small (air vehicle) XP | 200 XP | 150 XP |
| Deploy supply crate, large (air vehicle) XP | 400 XP | 300 XP |
| Deploy supply pallet | $2,500, 500 XP | $1,250, 400 XP |
| Deploy supply pallet XP from a ground vehicle | 750 XP | 500 XP |

Source: [14]. The Season 1 values are the "old" figures printed in the notes.

## Vehicle destroyed (0.2.0)

Every variant now has its own reward; armed variants give 1.5x the XP of the default variant, and Attack Vehicle rewards rise with their kill count [14]. Old to new where the notes print both.

| Vehicle | Season 1 (0.1.2) | Season 02 (0.2.0) |
|---------|------------------|-------------------|
| Kodiak | $1,250 | $500 default, $600 Pickup, $3,400 [M249] |
| Wolf-110 | new | $450; [M2 Browning] $3,900 |
| Humvee | $1,500 | $600 default, $4,250 [M249], $5,000 [Minigun] |
| Ural | $2,500 | $1,000 default, $3,600 Defender, $4,750 Defender [M249] |
| Bobcat | $250 | $100 |
| Dune Buggy | $750 | $300 |
| MH-6 | $3,125 | $1,250 |
| Little Bird AH-6M [Miniguns] | not stated | $6,000 |
| Little Bird AH-6R [Rockets] | not stated | $9,400 |
| Z20 Lakota | $3,700 | $1,500; [Miniguns] $7,500 |
| Havoc | $18,000 | $14,000 |
| L2A6 | $14,000 | $11,000 |
| SPH-2 | $14,000 | $8,000 |
| Flakpanzer Gepard | new | $7,000 |
| T-72B3 | new | $8,000 |

Source for every row: [14].

## Buildable destroyed (0.2.0)

Cash now matches each buildable's build supply cost and XP is roughly 25% of the cash reward [14]. Destroying a buildable also now pays based on how built it is (see exploit fixes) [14].

| Buildable | Season 1 (0.1.2) | Season 02 (0.2.0) |
|-----------|------------------|-------------------|
| L81 Mortar | $300 | $650 |
| Stingray | $300 | $650 |
| Hot Zone Magnet | $4,500 | $2,750 |
| Vanguard CIWS | $3,000 | $1,200 |
| Talon 9K-SAM | $2,000 | $650 |
| Repair / Refuel Station | $400 | $200 |
| Door | $500 | $100 |
| Gate | $170 | $200 |
| MG Nest | new | $650 |
| Large Shelter | new | $250 |
| Wood Base | new | $15 |

Source: [14]. Note that the L81 Mortar and Stingray rewards ($650) differ from their build supply costs (600 and 650) listed below, so "matches" is the notes' general statement rather than a per-item identity [14].

## Supply crate destroyed (0.2.0)

| Crate | Season 1 (0.1.2) | Season 02 (0.2.0) |
|-------|------------------|-------------------|
| Small | $500 | $300 |
| Large | $1,000 | $600 |
| Small Armored | $500 | $1,000 |
| Large Armored | $1,000 | $1,600 |
| Supply Pallets | $1,000 | $800 |

Source: [14]. Destroying an empty enemy crate now rewards half cash and half XP, and deploy and destroy rewards scale with the value of the supplies inside [14].

## Spotting (0.2.0)

The notes say spotting rewards are "around 30% lower than Season 1" because spotting was the lowest-risk, highest-paying way to earn, and they now scale with the value of each vehicle variant, buildable and crate. A spotted target destroyed by an enemy faction now pays 25% of the reward, down from 50% [14]. Spotting range is affected by rain (new rain weather preset) [14]. No absolute spotting dollar amount is published.

## Build supply costs (0.2.0)

The notes call these "build supply costs" and say the pass aims to make structures "a considered investment rather than something you spam" [14]. Season 1 to Season 02:

| Buildable | Season 1 (0.1.2) | Season 02 (0.2.0) |
|-----------|------------------|-------------------|
| Wood Base | new | 15 |
| Bremmer wall | 15 | 32 |
| Door | 22 | 80 |
| Gate | 85 | 200 |
| Large Shelter | new | 250 |
| Air raid shelter, bunker, crow's nest | 100 | 200 |
| L81 Mortar | 150 | 600 |
| Stingray | 150 | 650 |
| MG Nest | new | 650 |
| Talon 9K-SAM | 1,000 | 650 |
| Vanguard CIWS | 1,500 | 1,200 |
| Hot Zone Magnet | 2,250 | 2,750 |

Source: [14]. Build speed (medium hammer contributes less per swing, critical spots give a smaller bonus, large hammer unchanged), drill rig, Talon and Mortar changes are owned by fob-and-base-building.

## Exploit fixes (0.2.0)

All from the notes' "Exploit Fixes" section [14]:

- Spotting added and removed rewards scale with build progress, to stop farming spots on unfinished buildables.
- Destroying a buildable pays based on how built it is.
- Selling from a supply crate has diminishing returns per buyer; after enough sales you break even with no profit or XP.
- Selling an item from a supply crate to an enemy player (for example after they switch teams) gives no cash or XP.
- Destroying an empty enemy crate rewards half cash and half XP.
- Supply crate deploy and destroy rewards scale with the value of the supplies inside.
- FOB Supplied Assist is split between the number of assisting players, so a whole team can no longer each receive the full kickback.

Related 0.2.0 anti-abuse changes outside the reward tables: team-switching restrictions (once a team is more than 10 points ahead), and a victim-driven Team-Kill Punish / Forgive vote; see control-zone-and-match-flow [14].

## Season 02 faction experiment and discounts

The notes announce a "social experiment" for Season 2: a Lonestar cash and XP win bonus and Lonestar teamplay action cash and XP multipliers, "Season 2 only", with no values stated. A new vendor discount gives the losing team 20% off when at least 40 points behind second place, relevant to all teams. Community server hosts seen exploiting the faction bonus "will be punished" [14]. Server-seeding players earn rewards and a vendor discount once the match begins, amounts not stated [14].

## 0.1.2 reward changes (history)

| Change (30 Sep 2026) | Official wording | Value |
|----------------------|------------------|-------|
| Revive validity | Checks "now fully server authoritative" [1] | n/a |
| Vehicle fly-through | "rewards are now capped" [1] | Cap not stated |
| Destroying buildables | Rewards "scale with their build progress"; a placed schematic no longer gives a full reward [1] | Not stated; superseded by 0.2.0 buildable values |
| FOB pallet deposit outside zone | "now awards reduced rewards" [1] | Not stated |

Press coverage (BisectHosting) repeated these points and stated no values (press) [10].

## Exploit and abuse policy

| Offence | Official consequence | Date |
|---------|----------------------|------|
| Abusing cash exploits and bugs | Timed ban scaled to prior bans; cash and XP reset to 0 [2] | 14 Sep 2026 |
| Creating content that tutorialises exploits | Treated as advertising cheats; permanent ban [2] | 14 Sep 2026 |
| XP farming (joining farming servers more than a few minutes) | Permanent ban [2] | 14 Sep 2026 |
| Repeatable unintended exploits, real money trading | Cash and progression reset; risk of permanent ban without warning; first-offence leniency ended [1] | 30 Sep 2026 |

The developer states that testing an exploit "once or twice" is acceptable, but repeating it is abuse [2]. The 0.2.0 notes do not restate this policy.

## Season 1 economy changes versus beta

The Season 1.0 changelog (10 Sep 2026) states the previous balance "was designed specifically for weekend long beta tests" and that each season will have a different XP curve and item order [3]. It changed prices and XP, not documented per-action cash. Item prices are in price-tables-season-1.

## Income per hour

No sourced income-per-hour figure exists. The only quantified pacing statement in the notes is XP-based: reaching level 20 "now takes less than half the playtime it did in Season 1" [14].

## Baseline values

| Value | As-of version | Source |
|-------|---------------|--------|
| Starting balance $10,000 | Early Access, 2026-10-08 | [5] (also [11]) |
| Hot Zone cash multiplier: x2 | Feb 2026 statement, repeated on Steam page; not restated in 0.2.0 | [4][5] |
| Community-server end-of-match cash bonus: +5% for one week | Patch 0.11, 14 Sep 2026 | [2] |
| Player kill using an air vehicle: 300 XP to 250 XP | Season 1.0, 10 Sep 2026 | [3] |
| Supply crate item sold under $75: 25 XP to 1 XP | Season 1.0, 10 Sep 2026 | [3] |
| Assault kill bonus $1,500 to $2,000 | 0.2.0, 14-15 Oct 2026 | [14] |
| Logistics streaks (crates/pallets/players/returns) | 0.2.0, updated values | [14] |
| Spotting rewards about 30% lower; destroyed-by-enemy share 50% to 25% | 0.2.0, 14-15 Oct 2026 | [14] |
| Level 20 XP requirement 250,000 to 111,500 | 0.2.0 (Season 1.0 had changed 111,500 to 250,000) | [3][14] |

# Early Access Changes & Known Issues

- 10 Sep 2026, Season 1.0: price and XP rebalance, supply-crate curve rescaled "so low value items are priced sensibly and cannot be abused" [3].
- 14 Sep 2026, Patch 0.11: "Various cash exploits have been fixed"; economy abuse policy; 5% community-server end-of-match bonus for one week [2].
- 30 Sep 2026, Update 0.1.2: revive, fly-through, buildable and pallet reward fixes; zero-tolerance statement [1].
- 2 Oct 2026 hotfix: IR Rangefinders disabled and CIWS tweak; no reward change [8].
- 14 Oct 2026 notes / 15 Oct 2026 release, Update 0.2.0: new action rewards, role-XP reassignment, reduced base logistics plus new delivery streaks (values revised in-post to include the zone multiplier), per-variant vehicle-destroyed rewards, buildable-destroyed rewards matching build supply cost, crate-destroyed changes, spotting about 30% lower, drill tower capture doubled in cash, seven exploit fixes, new build supply costs, Lonestar experiment and losing-team discount [14][15].
- Wager Vendor announced for later in Season 2; not available at launch [14].
- The developer has called the economy interlinked "even more so when we bring the meta into the game" [2], and a Black Market, Vault and challenge system are planned for Early Access [9]. The Season 02 Teaser had flagged the 15 Oct date [7]; the notes confirm it.

# Admin & Technical Notes

The 5% bonus (Patch 0.11) applied to community servers only and was a developer promotion, not a server setting [2]. The 0.2.0 notes say community server admins can configure their own ping limits, and that hosts exploiting the faction bonus will be punished; they state no setting for reward tuning [14]. None found for per-action reward tuning.

# Risks & Caveats

- The streak values were revised in the post after first publication; the original numbers are not preserved and the post's "17:00 UTC" original time differs from the feed timestamp (14:59 UTC), so the exact revision timing is unclear [14].
- Reward lines state "Season 2 only" for the faction bonus; values are unpublished.
- Official posts were read from locally saved snapshots (2026-10-08 and 2026-10-30); links use the Steam news form. The release post links to the notes by a gid not in the snapshot and is not cited for that [15].
- Guide pages are third-party and may be out of date relative to 0.2.0.
- No official post after 2026-10-15 was seen in the 2026-10-30 snapshot; later hotfixes may exist or not.

# Open Questions

- Hot Zone x2: whether it applies to all actions, and whether it is unchanged in 0.2.0: not stated.
- Lonestar win bonus and teamplay multiplier values, and the size of the delivery "zone multiplier": not stated.
- Whether cash converts to Gold Bars automatically at a Season 02 start, and whether a progression wipe occurred: the 0.2.0 notes do not mention either; the Feb 2026 FAQ says cash can be exchanged for Gold Bars [4]. See season-reset-and-currencies.
- Absolute spotting reward amounts: not stated.
- The vehicle fly-through cap and the reduced FOB pallet reward values: not restated in 0.2.0.
- Death-penalty and rebuy changes: the notes cover only the rebuy UI; see death-penalty-and-rebuy.
- Conflict with economy-foundation: it describes reduced rewards for "destroying buildables" generally; the 0.1.2 text says rewards scale with build progress [1], and 0.2.0 publishes per-buildable values [14].
- Whether the 5% bonus returns.

# References

**Primary Sources**

- [1] **Bulkhead (Steam News)** — *WARDOGS | Update 0.1.2 (Minor Patch)*. https://store.steampowered.com/news/app/1867240/view/1845383656376490. Accessed 2026-10-08.
- [2] **Bulkhead (Steam News)** — *Scheduled Maintenance & Patch 0.11*. https://store.steampowered.com/news/app/1867240/view/1843481262698449. Accessed 2026-10-08.
- [3] **Bulkhead (Steam News)** — *Pre-Load Live & Season 1 Changelog*. https://store.steampowered.com/news/app/1867240/view/1843481262690549. Accessed 2026-10-08.
- [4] **Bulkhead (Steam News)** — *WARDOGS - Top Questions*. https://store.steampowered.com/news/app/1867240/view/1825093633182385. Accessed 2026-10-08.
- [5] **Valve / Bulkhead** — *WARDOGS on Steam*. https://store.steampowered.com/app/1867240/WARDOGS/. Accessed 2026-10-08.
- [6] **Bulkhead (Steam News)** — *Pre-Order Now*. https://store.steampowered.com/news/app/1867240/view/1840310314354505. Accessed 2026-10-08.
- [7] **Bulkhead (Steam News)** — *WARDOGS | Season 02 Teaser*. https://store.steampowered.com/news/app/1867240/view/1844115010504839. Accessed 2026-10-08.
- [8] **Bulkhead (Steam News)** — *IR Goggles & CIWS Balance Hotfix*. https://store.steampowered.com/news/app/1867240/view/1845383656386801. Accessed 2026-10-08.
- [9] **Bulkhead (Steam News)** — *WARDOGS - Early Access & Beyond*. https://store.steampowered.com/news/app/1867240/view/1828894815567544. Accessed 2026-10-08.
- [14] **Bulkhead (Steam News)** — *WARDOGS | Season 02 Patch Notes* (14 Oct 2026, includes an in-post update to logistics values). https://store.steampowered.com/news/app/1867240/view/1846651706674560. Accessed 2026-10-30.
- [15] **Bulkhead (Steam News)** — *WARDOGS | SEASON 02 IS NOW LIVE* (15 Oct 2026). https://store.steampowered.com/news/app/1867240/view/1846651706677015. Accessed 2026-10-30.

**Press & Secondary**

- [10] **BisectHosting** — *WARDOGS Update 0.1.2 patch notes*. https://www.bisecthosting.com/blog/wardogs-update-0-1-2-patch-notes-bug-fixes-improvements-flythrough-exploit-fob-pallet-delivery-xp. Accessed 2026-10-08.

**Player-Reported Evidence**

- [11] **allthings.how** — *WARDOGS cash: how to stop losing money as a beginner*. https://allthings.how/wardogs-cash-how-to-stop-losing-money-as-a-beginner/. Accessed 2026-10-08.
- [12] **KeenGamer** — *WARDOGS progression guide*. https://www.keengamer.com/articles/guides/wardogs-progression-guide/. Accessed 2026-10-08.
- [13] **allthings.how** — *WARDOGS Hot Zone: how double presence and double cash work*. https://allthings.how/wardogs-hot-zone-how-double-presence-and-double-cash-work/. Accessed 2026-10-08.

# Further Reading

The Steam news feed for posts after Season 02; economy-foundation for the loop overview.

# Related Documents

- economy-foundation
- death-penalty-and-rebuy
- price-tables-season-1
- season-reset-and-currencies
- control-zone-and-match-flow
- fob-and-base-building
- progression-unlock-tables

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft; pre-Season-02 baseline. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after independent re-verification of validate, markdownlint, links (0 dead) and Steam post ids. Pre-Season-02 baseline. | Standing mandate (auto-approve on green QA) |
| 1.1.0 | 2026-10-30 | Research Pipeline (virtual agent) | Update 0.2.0 revision: added published reward values (new action rewards, role-XP reassignment, logistics base and updated streaks, vehicle/buildable/crate destroyed, spotting, drill tower capture), exploit fixes, build supply costs, Lonestar experiment and losing-team discount, Wager Vendor status; Season 1 values kept as history; confidence raised to High. | — |
