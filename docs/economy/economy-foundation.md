---
id: economy-foundation
title: "Economy: Foundation"
version: 1.0.1
status: frozen
confidence: Medium
category: Economy
topic: "Account balance, costs, rewards, death penalty"
market: Global
game_version: "Early Access Update 0.1.2 (30 Sep 2026) plus hotfixes to 2 Oct 2026"
document_type: foundation
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [gameplay-modes-foundation, combat-loadouts-foundation, vehicles-outposts-foundation, meta-release-foundation]
tags: [economy, cash, death-penalty, pricing, early-access]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | economy-foundation |
| Version | 1.0.1 |
| Status | frozen |
| Confidence | Medium |
| Category | Economy |
| Game version | Early Access Update 0.1.2 (30 Sep 2026) plus hotfixes to 2 Oct 2026 |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

WARDOGS runs a persistent cash economy. Every player starts with $10,000, team-play actions earn cash, cash carries from match to match, and each life the player buys a loadout of weapons, gear, utility and vehicles [1]. The publisher states that cash "determines the risks players can take" and that outcomes are reflected in the account balance, and that in-game cash cannot be bought with real money [3]. As of the Steam Early Access launch the price is £36.99 (Standard) on the UK Steam page, with a £45.99 Supporter Edition [1].

Official sources confirm the broad loop but publish no full price or reward table. Specific price changes come from the Season 1 launch changelog as reproduced by press [4]; the death penalty, per-action rewards and full vehicle costs are described only in community guides and are labelled player-reported here. Verified against the Steam store page and the Steam news feed as of 2026-10-08, latest minor patch 0.1.2 [1][2].

Document confidence is Medium: the core loop is official, but most numbers rest on secondary reproductions and community measurements.

# Key Takeaways

- Every player starts with $10,000, and "every teamplay action you perform rewards cash" (Steam page, 2026-10-08) [1].
- Cash persists from match to match, so spending on gear, equipment or a vehicle at the right time matters [1].
- In-game cash, gold bars and status-based camouflage are not for sale for real money (Team17 press release, pre-launch) [3].
- Early Access Standard price is £36.99 on the Steam page; the launch press release quoted $39.99 USD; a Supporter Edition is £45.99 [1][3].
- Death costs the loadout bought for that life (player-reported) [6].
- Season 1 launch notes raised and lowered many vendor and vehicle prices and reworked XP curves (Season 1.0, 10 Sep 2026) [4].
- Patches 0.11 and 0.1.2 closed cash exploits and set an economy abuse policy with timed and permanent bans [2][5].
- Seasonal cash wipe and Gold Bar conversion are player-reported only; unverified [8].

# Scope

Covers the in-match economy: starting balance, what costs money, what earns it, persistence between matches, the death penalty, and monetization (edition pricing and purchases), as of Early Access Update 0.1.2 and hotfixes to 2 Oct 2026. Excludes depth tables of every item or vehicle price, weapon stats (see combat-loadouts-foundation), vehicle behaviour (see vehicles-outposts-foundation) and mode rules (see gameplay-modes-foundation). Release and business context sits in meta-release-foundation.

# Definitions

- **Cash**: the in-game currency earned and spent in matches, held in the account balance [1][3].
- **Account balance**: the persistent cash total that outcomes feed into [3].
- **Loadout**: weapons, gear, utility and vehicles bought each life [1].
- **Track / Career / Driver / Pilot**: progression tracks that gate unlocks by level; unlock gates are separate from cash prices [4].
- **Gold Bars**: a second currency referred to in the press release as not purchasable for real money [3]; its seasonal role is unverified.

# Current State

All facts below are for Early Access, as of 2026-10-08.

- Starting balance is $10,000 [1].
- Every teamplay action rewards cash, and cash persists between matches [1].
- Each life, the player buys a loadout of weapons, gear, utility and vehicles [1].
- The Team17 press release says cash is "not simply a score" and determines the risks a player can take, with every outcome reflected in the account balance [3].
- In-game cash, gold bars and status-based camouflage are not available for purchase [3].
- The studio committed to "no in-game monetisation during Early Access" apart from an optional cosmetic Supporters Edition [3].
- Steam lists Standard at £36.99, Supporter Edition at £45.99, and the Supporter Pack DLC at £11.99; the page describes no in-game purchases [1].
- The Steam page says the team plans lower Early Access pricing and may raise it nearer full release; Early Access is expected to last around 1 to 2 years [1].
- The latest posted version is Update 0.1.2 (30 Sep); hotfixes followed on 1 and 2 Oct, and Season 02 is teased for 15 Oct 2026 [2].

# Detail

## Earning cash

Official sources say only that teamplay actions reward cash and that an end-of-match bonus exists [1][5]. A community guide lists kills and assists, revives and heals, teammate tips, spotting, ground transport and supply runs, FOB building, holding the Control Zone, Hot Zone actions (reported as paying double) and destroying enemy vehicles as income sources, with no amounts (player-reported) [6]. Patch 0.1.2 reduced rewards for destroying buildables and for depositing outside a FOB zone, and closed vehicle fly-through exploits [2].

## Spending cash

Cash buys the per-life loadout [1]. The Season 1 launch changelog (10 Sep 2026) lists these changes [4]:

| Item | Old | New |
|------|-----|-----|
| Forward Operating Base (vendor) | $2,500 | $7,500 |
| Large Hammer (vendor) | $1,600 | $2,400 |
| Support Large Hammer | $25,000 | $75,000 |
| Career Artillery Tank | $400,000 | $500,000 |
| Pilot Little Bird with miniguns | $25,000 | $50,000 |
| Pilot Z20 Lakota | $50,000 | $35,000 |
| Driver URAL | $50,000 | $35,000 |
| Driver Dune Buggy | $35,000 | $25,000 |
| Driver Kodiak Flatbed | $15,000 | $35,000 |

Other lines in the same changelog cover scope, hammer and crate prices and a rescaled supply-crate purchase curve [4]. Another outlet described the Kodiak Flatbed as a reduction, which conflicts with the figures above; see Open Questions.

Per-spawn vehicle prices (for example $500 for a Bobcat, about $8,000 for the SPH-2, about $18,000 for the Havoc) are community measurements, not an official table, and the source warns they may change (player-reported) [7].

## Death penalty

Official pages say a player buys a loadout each life and that outcomes feed the balance [1][3], but do not state the exact loss on death. Community guides report that if a downed player is not revived the kit bought for that life is lost, the next kit is paid from the same balance, and helicopter crashes can destroy the loadouts of the pilot and passengers (player-reported) [6][7].

## Persistence and seasons

Cash persists between matches [1]. Community guides claim cash and XP reset each season and that leftover cash converts to Gold Bars; this is not confirmed in any official source retrieved (player-reported, see Open Questions) [8].

## Monetization

| Product | Price (Steam, 2026-10-08) |
|---------|---------------------------|
| WARDOGS | £36.99 [1] |
| Supporter Edition | £45.99 [1] |
| Supporter Pack (DLC) | £11.99 [1] |

The launch press release quoted $39.99 USD for Early Access [3].

# Early Access Changes & Known Issues

- 10 Sep 2026, Season 1.0 launch changelog: price rebalance of vendor and vehicle items, reworked role-track XP curve (for example level 20 from 111,500 to 250,000 XP), and unlock-level moves such as Artillery Tank 55 to 90 [4].
- 12 to 14 Sep 2026, Patch 0.11: cash exploit fixes, temporary 5% end-of-match cash bonus on community servers for a week, and an economy abuse policy: timed bans and cash/XP reset to 0 for cash exploits, permanent bans for XP farming [2][5].
- 30 Sep 2026, Update 0.1.2: closed cash and XP exploits (vehicle fly-through, reduced rewards for destroying buildables and depositing outside a FOB zone) [2].
- 2 Oct 2026, hotfix: IR Rangefinders disabled until Season 02 and CIWS balance tweak [2].
- Planned: Season 02 teased for 15 Oct 2026 [2].

# Admin & Technical Notes

Update 0.1.2 added community server tools including scheduled daily restarts and RCON access restrictions [2]. Patch 0.11 gave community servers a temporary 5% end-of-match cash bonus [5]. No official server-side economy settings were found.

# Risks & Caveats

- Economy numbers change per patch and season; the Season 1 prices may not survive Season 02.
- Official posts could not be fetched individually (the news feed lists posts without per-post URLs); price tables rely on press reproductions [4].
- Community figures are measurements, not official data [6][7].
- Pricing differs by currency and region and may rise toward full release [1][3].

# Open Questions

- Exact cash lost on death, and whether vehicles are refunded: no official statement found.
- Per-action reward amounts: unpublished in sources found.
- Whether cash resets each season and the cash-to-Gold-Bar rate: community only [8]; resolve via the Season 02 patch notes.
- Kodiak Flatbed price direction: press sources conflict; resolve with the official Season 1 post.
- Contents of the Supporter Pack and Supporter Edition: not retrieved.

# References

**Primary Sources**

- [1] **Valve / Bulkhead** — *WARDOGS on Steam*. https://store.steampowered.com/app/1867240/WARDOGS/. Accessed 2026-10-08.
- [2] **Bulkhead (Steam Community)** — *WARDOGS news feed (0.11, 0.1.2, hotfixes)*. https://steamcommunity.com/app/1867240/allnews/. Accessed 2026-10-08.
- [3] **Team17 (Game Developer)** — *WARDOGS is coming to Steam Early Access on 10 September*. https://www.gamedeveloper.com/press-release/wardogs-is-coming-to-steam-early-access-on-10-september. Accessed 2026-10-08.

**Press & Secondary**

- [4] **Gfinity Esports** — *WARDOGS Season 1 changelog, Early Access patch notes*. https://www.gfinityesports.com/article/wardogs-season-1-changelog-early-access-patch-notes. Accessed 2026-10-08.
- [5] **Playday** — *WARDOGS Patch 0.11 focuses on server browsers, full notes*. https://playday.one/2026/09/14/wardogs-patch-11-focuses-on-server-browsers-full-notes/. Accessed 2026-10-08.

**Player-Reported Evidence**

- [6] **allthings.how** — *WARDOGS cash: how to stop losing money as a beginner*. https://allthings.how/wardogs-cash-how-to-stop-losing-money-as-a-beginner/. Accessed 2026-10-08.
- [7] **GameBrief** — *WARDOGS vehicles guide 2026*. https://www.gamebrief.net/blog/wardogs-vehicles-guide-2026. Accessed 2026-10-08.
- [8] **Timesaver.gg** — *WARDOGS Season 2 reset, cash, levels* (commercial cash seller; treat with caution). https://timesaver.gg/blog/wardogs-season-2-reset-cash-levels. Accessed 2026-10-08.

# Further Reading

Gold Bar and cosmetics guides on community sites; the official Steam news feed for Season 02.

# Related Documents

- gameplay-modes-foundation
- combat-loadouts-foundation
- vehicles-outposts-foundation
- meta-release-foundation

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after independent re-verification of validate, markdownlint and links (0 dead). | Standing mandate (auto-approve on green QA) |
| 1.0.1 | 2026-10-08 | Orchestrator | Corrected Update 0.1.2 date from 29 Sep to 30 Sep 2026 (five outlets agree; see patch-history). | Standing mandate (auto-approve on green QA) |
