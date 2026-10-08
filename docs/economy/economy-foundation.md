---
id: economy-foundation
title: "Economy: Foundation"
version: 1.2.0
status: frozen
confidence: Medium
category: Economy
topic: "Account balance, costs, rewards, death penalty"
market: Global
game_version: "Early Access Update 0.1.2 (30 Sep 2026) plus hotfixes to 2 Oct 2026"
document_type: foundation
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-10-22
sources_verified: 2026-10-08
supersedes: null
related: [gameplay-modes-foundation, combat-loadouts-foundation, vehicles-outposts-foundation, meta-release-foundation, cash-rewards-and-costs, price-tables-season-1, death-penalty-and-rebuy, season-reset-and-currencies, editions-pricing-platforms]
tags: [economy, cash, death-penalty, pricing, early-access]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | economy-foundation |
| Version | 1.2.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Economy |
| Game version | Early Access Update 0.1.2 (30 Sep 2026) plus hotfixes to 2 Oct 2026 |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-10-22 |

# Executive Summary

WARDOGS runs a persistent cash economy. Every player starts with $10,000, team-play actions earn cash, cash carries from match to match, and each life the player buys a loadout of weapons, gear, utility and vehicles [1][5]. Bulkhead states that in-game cash and Gold Bars "must be earned through play" and will never be sold for real money [6][10]. Cash can also be exchanged for Gold Bars, the "endgame currency" for cosmetic unlocks in the Gold Market [5]. The UK Steam price is £36.99 (Standard), with a £45.99 Supporter Edition and a £11.99 Supporter Pack DLC that is cosmetic only [1][10].

This revision reads the full official Steam posts, which are now in the local snapshot. They give an exact vendor and vehicle price-change list for Season 1 (10 Sep 2026) [4], the Patch 0.11 economy abuse policy [3] and the Update 0.1.2 reward fixes [2], none with per-action cash amounts. Two areas are still not settled by official text: the death penalty and re-buy rule (player-reported only), and the season-end cash and XP wipe with automatic Gold Bar conversion (press and player-reported, traced to a 7 Apr 2026 devlog video that is not in any Steam post). Depth is in the linked economy documents.

Document confidence is Medium: the loop, prices and monetisation are official, but the death penalty and seasonal wipe are unverified, so the document cannot be rated higher while they stay open.

# Key Takeaways

- Every player starts with $10,000, and "every teamplay action you perform rewards cash" (Steam page, 2026-10-08) [1].
- Cash persists between matches and can be spent or exchanged for Gold Bars (official FAQ, 18 Feb 2026) [5].
- Official: Bulkhead "will NEVER monetize in-game cash or gold bars" and will never sell camos directly (11 Aug 2026) [6].
- Early Access Standard is £36.99 on the UK Steam page; Supporter Edition £45.99; the Supporter Pack is cosmetic only [1][10].
- Season 1 (10 Sep 2026) raised and lowered vendor and vehicle prices; the Kodiak Flatbed rose from $15,000 to $35,000 and its unlock moved from level 2 to level 10 [4].
- Patch 0.11 and Update 0.1.2 closed cash exploits and set an economy abuse policy with timed and permanent bans; 0.1.2 scaled buildable-destruction rewards to build progress [2][3].
- The death penalty is not settled by official text; the "kit is lost, re-buy from the same balance" account is player-reported [15].
- Season-end cash and XP wipe and automatic cash-to-Gold-Bar conversion are in no official post; they are press and player-reported [17].

# Scope

Covers the in-match economy: starting balance, what costs money, what earns it, persistence between matches, the death penalty, currencies and monetization (edition pricing and purchases), as of Early Access Update 0.1.2 and the 2 Oct 2026 hotfixes. Excludes depth tables of every item or vehicle price (see price-tables-season-1), per-action rewards (cash-rewards-and-costs), the death and re-buy rule (death-penalty-and-rebuy), the seasonal reset (season-reset-and-currencies), edition and platform detail (editions-pricing-platforms), weapon stats (combat-loadouts-foundation), vehicle behaviour (vehicles-outposts-foundation) and mode rules (gameplay-modes-foundation). Release context sits in meta-release-foundation.

# Definitions

- **Cash**: the in-game currency earned and spent in matches, held in the account balance; never sold for real money [1][6].
- **Account balance**: the persistent cash total that outcomes feed into [1][12].
- **Loadout**: weapons, gear, utility and vehicles bought each life [1].
- **Track / Career / Driver / Pilot**: progression tracks that gate unlocks by level; unlock gates are separate from cash prices [4].
- **Gold Bars**: the "endgame currency" obtained by exchanging cash and spent on cosmetics in the Gold Market [5]; never sold for real money [6].
- **Gold Market**: the store for cosmetic unlocks bought with Gold Bars [5].

# Current State

All facts below are for Early Access, as of 2026-10-08.

- Starting balance is $10,000 [1].
- Every teamplay action rewards cash, the Hot Zone yields double cash, and cash persists between matches [1][5].
- Each life, the player buys a custom loadout of weapons, gear, utility and vehicles [1][5].
- Cash can be exchanged for Gold Bars, used for cosmetic unlocks in the Gold Market (18 Feb 2026 FAQ; not restated in later posts) [5].
- Bulkhead states: no monetization during Early Access apart from the optional Supporter Edition; cash and Gold Bars must be earned through play; camos cannot be bought directly [6][10].
- Steam lists Standard at £36.99, Supporter Edition at £45.99 and the Supporter Pack DLC at £11.99; the DLC contains cosmetics only (see editions-pricing-platforms) [1][10].
- The Steam page says the team plans lower Early Access pricing and may raise it nearer full release; Early Access is expected to last around 1 to 2 years [1].
- The latest posted version is Update 0.1.2 (30 Sep) [2]; two official posts on 2 Oct covered a security and stability hotfix notice and an IR Rangefinder and CIWS balance hotfix [8][9]; Season 02 is teased for 15 Oct 2026 [7].

# Detail

## Earning cash

Official sources confirm which actions pay (revives, transport, kills, spotting, "and MORE") and that the Hot Zone yields double cash [5], but publish no per-action dollar amounts. The only official reward figure is a one-week 5% community-server end-of-match cash bonus from 14 Sep 2026 [3]. Update 0.1.2 made revive checks server authoritative, capped vehicle fly-through rewards, scaled buildable-destruction rewards with build progress (a placed schematic no longer pays in full) and reduced pallet-deposit rewards outside a FOB zone, with no values stated [2]. Community guides add income sources and no amounts (player-reported) [15]. See cash-rewards-and-costs.

## Spending cash

Cash buys the per-life loadout [1]. The Season 1 launch changelog (post of 9 Sep 2026, Season 1.0 live 10 Sep) lists these official price changes [4]:

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

Official pages say a loadout is bought each life and that outcomes feed the balance [1][12], but no official post states the loss on death, any re-buy price, refund or zero-cash rule (all saved official posts checked). Community guides report that a downed player who is not revived loses the kit bought for that life, the next kit is paid from the same balance, and a helicopter crash can destroy pilot and passenger loadouts (player-reported) [15][16]. See death-penalty-and-rebuy.

## Currencies, persistence and seasons

Cash persists between matches and can be exchanged for Gold Bars [5]. Each season will have "a different XP curve with different item orders" [4]. Official: bans for cash exploits reset an offender's cash and XP to 0 [3]. Not in any official post: that every player's cash and XP reset at season end and that leftover cash converts automatically to Gold Bars. This is relayed by press and a seller from a 7 Apr 2026 devlog video, not by the Steam post of that date, which only announces the planned Metagame (Black Market, Vault, skills and challenges) [11][17] (press and player-reported). The conversion rate is unpublished. See season-reset-and-currencies.

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
- Planned: Season 02 teased for 15 Oct 2026 [7].

# Admin & Technical Notes

Update 0.1.2 added community server tools including scheduled daily restarts and RCON AllowedHosts [2]. Patch 0.11 gave community servers a temporary 5% end-of-match cash bonus, described as an apology promotion rather than a setting [3]. No official server-side economy settings were found.

# Risks & Caveats

- Economy numbers change per patch and season; the Season 1 prices may not survive Season 02 [4][7].
- Official posts are now read in full from the 2026-10-08 snapshot; the Gold Bar exchange rests on one pre-launch FAQ (18 Feb 2026) that later posts do not restate [5].
- Community figures are measurements, not official data [15][16].
- Commercial source: Timesaver.gg sells cash; its seasonal claims are not evidence [17].
- Pricing differs by currency and region and may rise toward full release [1][6].

# Open Questions

- Exact cash lost on death, the re-buy price, and whether vehicles are refunded: no official statement in any saved post.
- Per-action reward amounts, the fly-through cap and the reduced pallet reward: unpublished.
- Whether cash and XP reset each season, whether leftover cash auto-converts, and the cash-to-Gold-Bar rate: not in official text; resolve via the Season 02 patch notes [17].
- Whether Season 02 changes the $10,000 starting balance or Season 1 prices.
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

Depth documents: cash-rewards-and-costs, price-tables-season-1, death-penalty-and-rebuy, season-reset-and-currencies, editions-pricing-platforms. Plus the official Steam news feed for Season 02. Press references [13] and [14] are retained for the earlier press-based versions of this document [13][14].

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
