---
id: economy-foundation
title: "Economy: Foundation"
version: 1.3.0
status: frozen
confidence: Medium
category: Economy
topic: "Account balance, costs, rewards, death penalty"
market: Global
game_version: "Early Access Season 02, Update 0.2.0 (15 Oct 2026); official posts through 2026-10-15 (snapshot 2026-10-30)"
document_type: foundation
created: 2026-10-08
updated: 2026-10-30
review_due: 2026-11-20
sources_verified: 2026-10-30
supersedes: null
related: [gameplay-modes-foundation, combat-loadouts-foundation, vehicles-outposts-foundation, meta-release-foundation, cash-rewards-and-costs, price-tables-season-1, death-penalty-and-rebuy, season-reset-and-currencies, editions-pricing-platforms]
tags: [economy, cash, death-penalty, pricing, early-access]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | economy-foundation |
| Version | 1.3.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Economy |
| Game version | Early Access Season 02, Update 0.2.0 (15 Oct 2026); official posts through 2026-10-15 (snapshot 2026-10-30) |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-30 |
| Review due | 2026-11-20 |

# Executive Summary

WARDOGS runs a persistent cash economy. Every player starts with $10,000, team-play actions earn cash, cash carries from match to match, and each life the player buys a loadout of weapons, gear, utility and vehicles [1][5]. Bulkhead states that in-game cash and Gold Bars "must be earned through play" and will never be sold for real money [6][10]. Cash can also be exchanged for Gold Bars, the "endgame currency" for cosmetic unlocks in the Gold Market [5]. The UK Steam price is £36.99 (Standard), with a £45.99 Supporter Edition and a £11.99 Supporter Pack DLC that is cosmetic only [1][10].

Season 02 (Update 0.2.0) went live on 15 Oct 2026 [20]. Its official patch notes (posted 14 Oct) rebalance the economy broadly: new per-action cash and XP rewards, lower base logistics pay with new delivery streaks, around 30% lower spotting rewards, a full vendor price pass, a faster role-track XP curve for levels 10 to 50, and a build-cost pass [19]. They also add a Rebuy Last Loadout interface change, a Gold Market camo rotation with the Gold Market itself listed as a WARDOG-track unlock, Lonestar faction bonuses, a losing-team vendor discount, and a Wager Vendor that is not available at launch [19]. This KB holds the numbers in the depth documents (price-tables-season-1 and cash-rewards-and-costs); this foundation summarises them.

Two areas are still not settled by official text. The patch notes do not mention a death-penalty rule or a Season 02 progression wipe or automatic cash-to-Gold-Bar conversion; their silence is not evidence either way [19]. The wipe claim remains press and player-reported, traced to a 7 Apr 2026 devlog video that is not in any Steam post [17]. No official post after 2026-10-15 is in the 2026-10-30 snapshot, so later hotfixes are neither confirmed nor ruled out.

Document confidence is Medium: the loop, Season 02 changes, prices and monetisation are official, but the death penalty and seasonal wipe are unverified, so the document cannot be rated higher while they stay open.

# Key Takeaways

- Every player starts with $10,000, and "every teamplay action you perform rewards cash" (Steam page, 2026-10-08) [1].
- Cash persists between matches and can be spent or exchanged for Gold Bars (official FAQ, 18 Feb 2026) [5].
- Official: Bulkhead "will NEVER monetize in-game cash or gold bars" and will never sell camos directly (11 Aug 2026) [6].
- Early Access Standard is £36.99 on the UK Steam page; Supporter Edition £45.99; the Supporter Pack is cosmetic only [1][10].
- Season 02 (Update 0.2.0, live 15 Oct 2026) rebalanced rewards, vendor prices and build costs; numbers are in cash-rewards-and-costs and price-tables-season-1 [19][20].
- Season 02 adds a Rebuy Last Loadout interface change (visual loadout in the vendor, editable before purchase), Lonestar faction bonuses and a 20% losing-team vendor discount (at least 40 points behind second place) [19].
- The Wager Vendor (bet cash on your own performance) is not available at Season 02 launch and is described as not permanent [19].
- The Season 02 patch notes do not mention a wipe, an automatic Gold Bar conversion or a death-penalty rule (notes read 2026-10-30) [19].
- Season 1 (10 Sep 2026) raised and lowered vendor and vehicle prices; the Kodiak Flatbed rose from $15,000 to $35,000 and its unlock moved from level 2 to level 10 [4].
- Patch 0.11 and Update 0.1.2 closed cash exploits and set an economy abuse policy with timed and permanent bans; 0.1.2 scaled buildable-destruction rewards to build progress [2][3].
- The death penalty is not settled by official text, including the Season 02 notes; the "kit is lost, re-buy from the same balance" account is player-reported [15][19].
- Season-end cash and XP wipe and automatic cash-to-Gold-Bar conversion are in no official post, including the Season 02 notes; they are press and player-reported [17][19].

# Scope

Covers the in-match economy: starting balance, what costs money, what earns it, persistence between matches, the death penalty, currencies and monetization (edition pricing and purchases), as of Early Access Update 0.2.0 (Season 02, 15 Oct 2026), with Season 1 / Update 0.1.2 values kept as dated history. Excludes depth tables of every item or vehicle price (see price-tables-season-1), per-action rewards (cash-rewards-and-costs), the death and re-buy rule (death-penalty-and-rebuy), the seasonal reset (season-reset-and-currencies), edition and platform detail (editions-pricing-platforms), weapon stats (combat-loadouts-foundation), vehicle behaviour (vehicles-outposts-foundation) and mode rules (gameplay-modes-foundation). Release context sits in meta-release-foundation.

# Definitions

- **Cash**: the in-game currency earned and spent in matches, held in the account balance; never sold for real money [1][6].
- **Account balance**: the persistent cash total that outcomes feed into [1][12].
- **Loadout**: weapons, gear, utility and vehicles bought each life [1].
- **Track / Career / Driver / Pilot**: progression tracks that gate unlocks by level; unlock gates are separate from cash prices [4].
- **Gold Bars**: the "endgame currency" obtained by exchanging cash and spent on cosmetics in the Gold Market [5]; never sold for real money [6].
- **Gold Market**: the store for cosmetic unlocks bought with Gold Bars [5].

# Current State

All facts below are for Early Access, as of Update 0.2.0 (official posts through 2026-10-15; snapshot 2026-10-30) unless dated otherwise.

- Starting balance is $10,000 on the Steam page (checked 2026-10-08); the Season 02 notes do not state a starting balance [1][19].
- Every teamplay action rewards cash, the Hot Zone yields double cash, and cash persists between matches [1][5].
- Each life, the player buys a custom loadout of weapons, gear, utility and vehicles [1][5].
- Cash can be exchanged for Gold Bars, used for cosmetic unlocks in the Gold Market (18 Feb 2026 FAQ; not restated in later posts) [5].
- Bulkhead states: no monetization during Early Access apart from the optional Supporter Edition; cash and Gold Bars must be earned through play; camos cannot be bought directly [6][10].
- Steam lists Standard at £36.99, Supporter Edition at £45.99 and the Supporter Pack DLC at £11.99; the DLC contains cosmetics only (see editions-pricing-platforms) [1][10].
- The Steam page says the team plans lower Early Access pricing and may raise it nearer full release; Early Access is expected to last around 1 to 2 years [1].
- The latest official version in the snapshot is Update 0.2.0, released 15 Oct 2026 after a maintenance window of 08:00 to 09:30 UTC [19][20]. Before it, Update 0.1.2 (30 Sep) [2] and two 2 Oct posts, a security and stability hotfix notice and an IR Rangefinder and CIWS balance hotfix, applied [8][9]. The 2026-10-30 snapshot holds no official post after 15 Oct.
- Season 02 reward, price and build-cost changes are summarised in Detail and held in price-tables-season-1 and cash-rewards-and-costs [19].
- The Gold Market is listed as a WARDOG-track unlock at level 35 for $150k, and eight Gold Market camos are listed for Season 02 (Black & Gold AK removed) [19].
- Rebuy Last Loadout now pre-fills the equipment vendor with the previous loadout, editable before purchase [19].
- Lonestar has Season 02-only cash and XP win bonuses and teamplay multipliers; any team 40 or more points behind second place gets a 20% vendor discount [19].
- The Wager Vendor is not available at launch and will open later in Season 02 [19].

# Detail

## Season 02 economy changes at a glance

The Season 02 patch notes (14 Oct 2026, live as Update 0.2.0 on 15 Oct) change the economy in these areas; this document summarises and the depth documents hold the figures [19][20]:

| Area | What 0.2.0 changed | Detail document |
|------|--------------------|-----------------|
| Action rewards | New assault-weapon kill bonus ($1,500 to $2,000), FOB hacking teammate reward, Halligan door-breach reward, FOB destruction bonus | cash-rewards-and-costs |
| Logistics | Lower base pay plus delivery streaks (values revised in-post to include the zone multiplier) | cash-rewards-and-costs |
| Spotting and destroyed rewards | Spotting rewards around 30% lower than Season 1; per-variant vehicle-destroyed rewards; buildable rewards match build supply cost | cash-rewards-and-costs |
| Exploit fixes | Diminishing returns on selling from a supply crate; no reward for selling to an enemy player; FOB Supplied Assist split between assisting players | cash-rewards-and-costs |
| Vendor prices | New weapons, attachments, magazines, gear and vehicles; many increases and decreases | price-tables-season-1 |
| Role-track XP | Level 20 total XP 250,000 to 111,500 ("55% quicker") | progression-unlock-tables |
| Build costs | Full pass on build supply costs and speed; drill rig, Talon and Mortar rebalanced | fob-and-base-building |
| Faction and discounts | Lonestar bonuses; 20% losing-team vendor discount; server-seeding rewards and vendor discount (no values stated) | this document |
| Gold Market | Camo rotation; Gold Market listed as a level 35 WARDOG unlock | season-reset-and-currencies |
| Loadout | Rebuy Last Loadout interface change | death-penalty-and-rebuy |
| Wager Vendor | Not available at launch; opens later in Season 2 | this document |

The 0.2.0 notes do not state any change to the $10,000 starting balance, a Season 02 progression wipe, a Gold Bar conversion or a death-penalty rule [19].

## Faction bonuses, discounts and the Wager Vendor

Faction balance experiment (Season 02 only): the notes list a Lonestar cash and XP win bonus and Lonestar teamplay-action cash and XP multipliers, with no values stated; the notes also say community server hosts seen exploiting the faction bonus will be punished [19]. The preview post of 9 Oct 2026 lists the same items and frames them as a "social experiment" about the blue team's win rate [18]. A new vendor discount applies to the losing team: 20% off if they are at least 40 points behind second place, for all teams [19]. Players who join and populate empty servers earn rewards and a vendor discount once the match begins, with no values stated [19].

Wager Vendor: the notes say it lets a player bet their own cash on their own performance, with a live wager tracker above the minimap, and that it "is not available at Season 2 launch" and "will open later in Season 2"; it is "not a permanent addition" and is intended to come and go within a season [19]. The preview adds that players choose objectives, set how many deaths they will spend, and set a stake, with longer odds for stacked objectives, and that it may be pulled if exploitable [18]. Whether it has opened is unknown: the snapshot holds no official post after 15 Oct.

## Earning cash

Season 1 (to Update 0.1.2): official sources confirmed which actions pay (revives, transport, kills, spotting, "and MORE") and that the Hot Zone yields double cash [5], but published no per-action dollar amounts. The only official reward figure was a one-week 5% community-server end-of-match cash bonus from 14 Sep 2026 [3]. Season 02 (Update 0.2.0): the 14 Oct patch notes publish per-action amounts for the first time (for example assault kill bonus $1,500 to $2,000, Deploy Supply Pallet $2,500 to $1,250) [19]; they are held in cash-rewards-and-costs. Update 0.1.2 made revive checks server authoritative, capped vehicle fly-through rewards, scaled buildable-destruction rewards with build progress (a placed schematic no longer pays in full) and reduced pallet-deposit rewards outside a FOB zone, with no values stated [2]. Community guides add income sources and no amounts (player-reported) [15]. See cash-rewards-and-costs.

## Spending cash

Cash buys the per-life loadout [1]. Season 02 (Update 0.2.0) revised the vendor price list again, for example Basic Parachute $100 to $500, L2A6 $14,000 to $22,000 and new vehicles such as the T-72B3 at $16,000; the full Season 02 list is in price-tables-season-1 [19]. As dated history, the Season 1 launch changelog (post of 9 Sep 2026, Season 1.0 live 10 Sep) listed these official price changes [4]; some of these items were re-priced or re-gated in 0.2.0 (for example the Little Bird with miniguns now unlocks at level 8 for $125k) [19]:

| Item | Old | New |
|------|-----|-----|
| Forward Operating Base (vendor) | $2,500 | $7,500 |
| Large Hammer (vendor) | $1,600 | $2,400 |
| Support Medium Hammer | $10,000 | $25,000 |
| Support Large Hammer | $25,000 | $75,000 |
| Career Artillery Tank | $400,000 | $500,000 |
| Pilot Little Bird with miniguns | $25,000 | $50,000 |
| Pilot Z20 Lakota | $50,000 | $35,000 |
| Driver URAL | $50,000 | $35,000 |
| Driver Dune Buggy | $35,000 | $25,000 |
| Driver Kodiak Flatbed | $15,000 | $35,000 |

The same list also moves scope, small supply crate and Music Tape H prices and rescales the supply-crate purchase curve from 25 to 250 down to 1 to 200 [4]. The Kodiak Flatbed is an official increase, and its unlock level moved from 2 to 10 [4]; the full table is in price-tables-season-1. The changelog does not say whether a price is a one-time unlock payment or a per-life price.

Per-spawn vehicle prices (for example $500 for a Bobcat, about $8,000 for the SPH-2, about $18,000 for the Havoc) are community measurements, not an official table (player-reported) [16].

## Death penalty

Official pages say a loadout is bought each life and that outcomes feed the balance [1][12], but no official post, including the Season 02 patch notes, states the loss on death, any re-buy price, refund or zero-cash rule (all saved official posts checked, 2026-10-30) [19]. Update 0.2.0 did change the Rebuy Last Loadout interface: the old placeholder UI was removed and the vendor is pre-filled with the last loadout, which can be edited before purchase [19]. Community guides report that a downed player who is not revived loses the kit bought for that life, the next kit is paid from the same balance, and a helicopter crash can destroy pilot and passenger loadouts (player-reported) [15][16]. See death-penalty-and-rebuy.

## Currencies, persistence and seasons

Cash persists between matches and can be exchanged for Gold Bars [5]. Each season will have "a different XP curve with different item orders" [4]. Official: bans for cash exploits reset an offender's cash and XP to 0 [3]. Season 02 gold-related facts: the notes list eight Gold Market skins (Black & Gold Little Bird as a Season 2 exclusive; Chocolate Chip, Two-Tone Desert and Digital Wood families), remove the Black & Gold AK camo, and list "Gold Market (LVL 35, $150k)" among WARDOG-track additional unlocks [19]. Not in any official post, including the Season 02 notes (which do not mention it): that every player's cash and XP reset at season end and that leftover cash converts automatically to Gold Bars. This is relayed by press and a seller from a 7 Apr 2026 devlog video, not by the Steam post of that date, which only announces the planned Metagame (Black Market, Vault, skills and challenges) [11][17] (press and player-reported). The conversion rate is unpublished. See season-reset-and-currencies.

## Monetization

| Product | Price (Steam, 2026-10-08) |
|---------|---------------------------|
| WARDOGS | £36.99 [1] |
| Supporter Edition | £45.99 [1] |
| Supporter Pack (DLC) | £11.99 [1][10] |

The Supporter Pack holds three Starter Weapon camos (Valkyra A-91, Lonestar Bushmaster, Manticore KH-2002), a Littlebird "Taxi" camo, a hideable scoreboard supporter icon and two bobbleheads; no gameplay item is listed [10][6]. The launch press release quoted $39.99 USD for Early Access [12]; the 11 Aug post refers to "stair stepped pricing" without figures [6]. Regional prices are in editions-pricing-platforms.

# Early Access Changes & Known Issues

- 10 Sep 2026, Season 1.0 launch changelog (published 9 Sep): price rebalance of vendor and vehicle items, reworked role-track XP curve (level 20 from 111,500 to 250,000 XP), and unlock-level moves such as Artillery Tank 55 to 90 and Kodiak Flatbed 2 to 10 [4].
- 12 to 14 Sep 2026, Patch 0.11: various cash exploits fixed, a 5% end-of-match cash bonus on community servers for a week, and an economy abuse policy: timed bans and cash/XP reset to 0 for cash exploits, permanent bans for tutorialising exploits and for XP farming [3].
- 30 Sep 2026, Update 0.1.2: closed cash and XP exploits (server-authoritative revives, capped vehicle fly-through, buildable-destruction rewards scaled to build progress, reduced pallet rewards outside a FOB zone); first-offence leniency ended [2].
- 2 Oct 2026: two official posts, a notice of a security and stability hotfix at 08:00 UTC [9] and a balance hotfix that disables IR Rangefinders in the vendor until Season 02 and speeds up the CIWS [8].
- 9 Oct 2026: Season 02 preview post, naming the Wager Vendor, faction experiment and reward systems [18]. Preview names differ from final notes in places (for example the helmet name) [18][19].
- 14 Oct 2026, Season 02 patch notes (published ahead of release): economy changes summarised under Detail; one in-post update revised the logistics streak values to include the zone multiplier [19].
- 15 Oct 2026, Update 0.2.0 released after a 08:00 to 09:30 UTC maintenance window; servers back online [19][20].
- Known: the Wager Vendor is not available at Season 02 launch [19]. No official post after 15 Oct 2026 is in the 2026-10-30 snapshot.
- Superseded: Season 02 was teased for 15 Oct 2026 (22 Sep post) [7]; it shipped on that date [20].

# Admin & Technical Notes

Update 0.1.2 added community server tools including scheduled daily restarts and RCON AllowedHosts [2]. Patch 0.11 gave community servers a temporary 5% end-of-match cash bonus, described as an apology promotion rather than a setting [3]. The 0.2.0 notes warn that community server hosts seen exploiting the faction bonus will be punished, and say community admins can configure their own ping limits; no official server-side economy setting was found [19].

# Risks & Caveats

- Economy numbers change per patch and season; Season 02 already replaced many Season 1 prices [4][19]. No official post after 15 Oct 2026 is in the snapshot, so later hotfixes are unchecked.
- Official posts are now read in full from the 2026-10-08 snapshot; the Gold Bar exchange rests on one pre-launch FAQ (18 Feb 2026) that later posts do not restate [5].
- Community figures are measurements, not official data [15][16].
- Commercial source: Timesaver.gg sells cash; its seasonal claims are not evidence [17].
- Pricing differs by currency and region and may rise toward full release [1][6].

# Open Questions

- Exact cash lost on death, the re-buy price, and whether vehicles are refunded: no official statement in any saved post, including the Season 02 notes.
- The fly-through cap, the reduced pallet reward and the Lonestar and server-seeding bonus values: not stated in the notes.
- Whether cash and XP reset each season, whether leftover cash auto-converts, and the cash-to-Gold-Bar rate: not in official text; the Season 02 patch notes do not mention a wipe or conversion [17][19]. Resolve with an in-game account check or an official statement.
- Whether Season 02 changes the $10,000 starting balance: the notes do not say. (Season 1 prices were changed: see price-tables-season-1.)
- When the Wager Vendor opens, and whether it has: no official post after 15 Oct in the snapshot.
- Whether changelog vehicle prices are unlock prices or per-spawn prices.

# References

**Primary Sources**

- [1] **Valve / Bulkhead** — *WARDOGS on Steam*. https://store.steampowered.com/app/1867240/WARDOGS/. Accessed 2026-10-08.
- [2] **Bulkhead (Steam News)** — *WARDOGS | Update 0.1.2 (Minor Patch)*, 30 Sep 2026. https://store.steampowered.com/news/app/1867240/view/1845383656376490. Accessed 2026-10-08.
- [3] **Bulkhead (Steam News)** — *Scheduled Maintenance & Patch 0.11*, 12 Sep 2026. https://store.steampowered.com/news/app/1867240/view/1843481262698449. Accessed 2026-10-08.
- [4] **Bulkhead (Steam News)** — *Pre-Load Live & Season 1 Changelog*, 9 Sep 2026. https://store.steampowered.com/news/app/1867240/view/1843481262690549. Accessed 2026-10-08.
- [5] **Bulkhead (Steam News)** — *WARDOGS - TOP QUESTIONS*, 18 Feb 2026. https://store.steampowered.com/news/app/1867240/view/1825093633182385. Accessed 2026-10-08.
- [6] **Bulkhead (Steam News)** — *PRE-ORDER NOW!*, 11 Aug 2026. https://store.steampowered.com/news/app/1867240/view/1840310314354505. Accessed 2026-10-08.
- [7] **Bulkhead (Steam News)** — *WARDOGS | Season 02 Teaser*, 22 Sep 2026. https://store.steampowered.com/news/app/1867240/view/1844115010504839. Accessed 2026-10-08.
- [8] **Bulkhead (Steam News)** — *IR Goggles & CIWS Balance Hotfix*, 2 Oct 2026. https://store.steampowered.com/news/app/1867240/view/1845383656386801. Accessed 2026-10-08.
- [9] **Bulkhead (Steam News)** — *WARDOGS | Security & Stability Hotfix*, 2 Oct 2026. https://store.steampowered.com/news/app/1867240/view/1845383656384445. Accessed 2026-10-08.
- [18] **Bulkhead (Steam News)** — *WARDOGS | Season 02 Preview*, 9 Oct 2026. https://store.steampowered.com/news/app/1867240/view/1846018067933823. Accessed 2026-10-30.
- [19] **Bulkhead (Steam News)** — *WARDOGS | Season 02 Patch Notes*, 14 Oct 2026. https://store.steampowered.com/news/app/1867240/view/1846651706674560. Accessed 2026-10-30.
- [20] **Bulkhead (Steam News)** — *WARDOGS | SEASON 02 IS NOW LIVE*, 15 Oct 2026. https://store.steampowered.com/news/app/1867240/view/1846651706677015. Accessed 2026-10-30.
- [10] **Valve / Bulkhead** — *WARDOGS - Supporter Pack (DLC store entry)*. https://store.steampowered.com/app/4809960/. Accessed 2026-10-08.
- [11] **Bulkhead (Steam News)** — *WARDOGS - Early Access & Beyond*, 7 Apr 2026. https://store.steampowered.com/news/app/1867240/view/1828894815567544. Accessed 2026-10-08.
- [12] **Team17 (Game Developer)** — *WARDOGS is coming to Steam Early Access on 10 September*. https://www.gamedeveloper.com/press-release/wardogs-is-coming-to-steam-early-access-on-10-september. Accessed 2026-10-08.

**Press & Secondary**

- [13] **Gfinity Esports** — *WARDOGS Season 1 changelog, Early Access patch notes* (superseded by [4] for prices; one outlet's Kodiak Flatbed wording conflicted with the official post). https://www.gfinityesports.com/article/wardogs-season-1-changelog-early-access-patch-notes. Accessed 2026-10-08.
- [14] **Playday** — *WARDOGS Patch 0.11 focuses on server browsers, full notes* (superseded by [3]). https://playday.one/2026/09/14/wardogs-patch-11-focuses-on-server-browsers-full-notes/. Accessed 2026-10-08.

**Player-Reported Evidence**

- [15] **allthings.how** — *WARDOGS cash: how to stop losing money as a beginner*. https://allthings.how/wardogs-cash-how-to-stop-losing-money-as-a-beginner/. Accessed 2026-10-08.
- [16] **GameBrief** — *WARDOGS vehicles guide 2026*. https://www.gamebrief.net/blog/wardogs-vehicles-guide-2026. Accessed 2026-10-08.
- [17] **Timesaver.gg** — *WARDOGS Season 2 reset, cash, levels* (commercial cash seller; treat with caution). https://timesaver.gg/blog/wardogs-season-2-reset-cash-levels. Accessed 2026-10-08.

# Further Reading

Depth documents: cash-rewards-and-costs, price-tables-season-1, death-penalty-and-rebuy, season-reset-and-currencies, editions-pricing-platforms. Plus the official Steam news feed for later Season 02 posts. Press references [13] and [14] are retained for the earlier press-based versions of this document [13][14].

# Related Documents

- gameplay-modes-foundation
- combat-loadouts-foundation
- vehicles-outposts-foundation
- meta-release-foundation
- cash-rewards-and-costs
- price-tables-season-1
- death-penalty-and-rebuy
- season-reset-and-currencies
- editions-pricing-platforms

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after independent re-verification of validate, markdownlint and links (0 dead). | Standing mandate (auto-approve on green QA) |
| 1.0.1 | 2026-10-08 | Orchestrator | Corrected Update 0.1.2 date from 29 Sep to 30 Sep 2026 (five outlets agree; see patch-history). | Standing mandate (auto-approve on green QA) |
| 1.2.0 | 2026-10-08 | Research Pipeline (revision worker) | Revised against full official Steam text; Kodiak Flatbed upgraded to official $15,000 to $35,000 (unlock level 2 to 10); Gold Bars and cash exchange upgraded to official; 0.1.2 buildable reward corrected to scale with build progress; stale "posts not fetchable" risk removed; Supporter Pack contents added; 2 Oct hotfix split into two official posts; death penalty and season wipe kept as unverified. | Standing mandate (auto-approve on green QA) |
| 1.3.0 | 2026-10-30 | Research Pipeline (virtual agent) | Revised for Season 02 / Update 0.2.0 against the official preview, patch notes and release post: added Season 02 economy summary, faction bonuses and losing-team discount, Wager Vendor (not at launch), Gold Market camo rotation and level 35 unlock, Rebuy Last Loadout interface change; death penalty and wipe kept unconfirmed (notes silent); Season 1 values kept as dated history. | — |
