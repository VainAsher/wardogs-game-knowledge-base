---
id: death-penalty-and-rebuy
title: "Death Penalty, Loadout Loss & Re-buy"
version: 1.1.0
status: frozen
confidence: Low
category: Economy
topic: "What dying costs, loadout loss, re-buy, insurance-like mechanics, negative balances"
market: Global
game_version: "Early Access Season 02, Update 0.2.0 (15 Oct 2026); official posts through 2026-10-15 (snapshot 2026-10-30)"
document_type: depth
created: 2026-10-08
updated: 2026-10-30
review_due: 2026-11-20
sources_verified: 2026-10-30
supersedes: null
related: [economy-foundation, cash-rewards-and-costs, price-tables-season-1, combat-loadouts-foundation, season-reset-and-currencies]
tags: [economy, death-penalty, rebuy, loadout, vehicles, season-02, early-access]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | death-penalty-and-rebuy |
| Version | 1.1.0 |
| Status | frozen |
| Confidence | Low |
| Category | Economy |
| Game version | Early Access Season 02, Update 0.2.0 (15 Oct 2026); official posts through 2026-10-15 (snapshot 2026-10-30) |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-30 |
| Review due | 2026-11-20 |

# Executive Summary

The official Steam text fixes the frame of the death penalty but not its size. Every player starts with $10,000, buys a custom loadout "each life", and cash persists from match to match [1]. Bulkhead's own launch-era posts say that "every decision affects YOUR account balance" and that players can min/max their "return on investment every life" [2][3]. No official post, patch note or Q&A in the saved Steam news feed states what is lost on death, what a Re-buy Loadout costs, whether a refund or insurance exists, or what happens at zero cash (checked 2026-10-08) [1][2][3][4][5][6][7].

The detail that does exist is player-reported: an unrevived death forfeits the kit bought for that life, the next kit is paid from the same balance, and a "Re-buy Loadout" vendor option rebuilds the previous kit [9][10]. A vehicle guide says a destroyed vehicle must be paid for again at its spawn price [11]. Season 02 (Update 0.2.0, notes 14 Oct, live 15 Oct 2026) confirmed one related change: the "Rebuy Last Loadout" button now fills the equipment vendor UI visually with the last loadout, which the player can add to or remove items from before purchase, and the old placeholder rebuy UI was removed [13][14][15]. That is an interface change; the notes state no death penalty, re-buy price, refund or zero-cash rule, and that silence is not evidence either way [14]. The Season 1 / 0.1.2 text is kept as dated history.

Confidence is Low: the answer to the core question (what dying costs) still rests entirely on player-reported guides dated before Season 02, and none gives a re-buy price.

# Key Takeaways

- Official text does not settle the death penalty, including the Season 02 notes. It says only that a loadout is bought each life and that outcomes feed the account balance (Steam, checked 2026-10-08 and 2026-10-30) [1][3][14].
- Official (Update 0.2.0, 14 Oct 2026): Rebuy Last Loadout now populates the equipment vendor UI with your last loadout, editable before purchase; the old placeholder rebuy UI is removed [14].
- Official: the starting balance is $10,000 and cash persists between matches [1].
- Official: there is no per-life cost stated anywhere in the Season 1 changelog; it lists price changes but not what a death costs [5].
- Player-reported: if nobody revives you, the kit is gone and the next kit comes out of the same wallet (guide updated 12 Sep 2026) [9].
- Player-reported (Season 1): a "Re-buy Loadout" option at the vendor rebuilds the previous kit; no price is given (guide dated 17 Sep 2026, before the 0.2.0 interface change) [10].
- Player-reported: a helicopter crash takes the pilot's and passengers' loadouts [9].
- Official: Bulkhead says in-game cash and gold bars will never be sold for real money [4].
- No source describes negative balances, a zero-cash floor or insurance; these are unverified (checked 2026-10-30).
- Season 02 changed some costs that bear on a rebuy (for example Basic Parachute $100 to $500, Medical Bag $2,000 to $1,800, and vehicle prices); see price-tables-season-1 [14].

# Scope

Covers the per-life loadout model, what is lost on death, the Re-buy Loadout option, low and zero cash, vehicle loss costs, and anything in the saved official Steam posts and Q&A bearing on them, as of Update 0.2.0 (Season 02), with Update 0.1.2 and the 2 Oct 2026 hotfixes kept as dated history. Excludes full price tables (see price-tables-season-1), earning rates (see cash-rewards-and-costs), weapon and kit contents (see combat-loadouts-foundation) and the broader economy frame (see economy-foundation). In-game behaviour was not tested by this pipeline.

# Definitions

- **Per-life loadout**: the weapons, gear, utility and vehicles bought with cash for one life [1].
- **Re-buy Loadout / Rebuy Last Loadout**: a vendor button that rebuilds the previous kit; its existence and the 0.2.0 interface change are official [14]; its price and exact effect on death are not stated (guide descriptions are player-reported) [10].
- **Unrevived death**: dying without being picked up by a medic or squadmate; the case in which guides report the kit is lost (player-reported) [9].
- **Account balance**: the persistent cash total that outcomes feed into [3].
- **Gold Bars**: the endgame currency, obtainable by exchanging cash, used for cosmetics in the Gold Market [2].

# Current State

As of Early Access Update 0.2.0 (official posts through 2026-10-15; snapshot 2026-10-30):

- Every player starts with $10,000 on the store page (checked 2026-10-08) and, each life, purchases a custom loadout from weapons, gear, utility and vehicles [1]. The Season 02 notes state no starting balance [14].
- Cash persists from match to match, and the store page says spending big on better gear or a vehicle at the right time "could yield massive returns" [1].
- Bulkhead's 21 May 2026 post says "every bullet fired, every loadout built, and every second-to-second choice has real consequences for your account balance" [3].
- Bulkhead's 18 Feb 2026 Q&A says players can build a loadout "to min/max your return on investment every life" and that cash earned can be saved, spent, or exchanged for Gold Bars [2].
- Bulkhead states it will never monetize in-game cash or gold bars [4].
- Update 0.2.0 (14 Oct 2026 notes): "Old placeholder rebuy UI has been removed"; clicking "Rebuy Last Loadout" populates the equipment vendor UI visually with your last loadout, which you can add to or remove items from before purchase [14]. The same notes reduce the hold time when selecting "Purchase Loadout" on controller [14].
- Update 0.1.2 (30 Sep 2026): revive validity checks are server-authoritative [7]. Revives matter to the death penalty only through the player-reported claim that a revive preserves the paid-for kit [9].
- No official text, including the Season 02 notes, states a death cost, re-buy price, refund, insurance or negative-balance rule (all saved official posts checked, to 2026-10-15) [1][2][3][4][5][6][7][14][15].
- No official post after 15 Oct 2026 is in the 2026-10-30 snapshot.

# Detail

## Official text: what it does and does not say

| Question | Official answer | Source |
|----------|-----------------|--------|
| Is a loadout bought per life? | Yes: "Each life, you purchase a custom loadout" | [1] |
| Does cash persist between matches? | Yes | [1][2] |
| Is there an exact loss on death? | Not stated, including in the Season 02 notes | [1][2][3][4][5][6][7][14] |
| Is there a Rebuy Last Loadout feature? | Yes: confirmed by the 0.2.0 notes as a button that pre-fills the vendor with the last loadout (editable); no price stated | [14] |
| Is there a Re-buy price or cost difference? | Not stated | [1][2][3][4][5][6][7][14] |
| Insurance, refunds, grace for low cash? | Not mentioned | [1][2][3][4][5][6][7][14] |
| Negative balance or zero-cash floor? | Not mentioned | [1][2][3][4][5][6][7][14] |
| Can cash be spent on anything besides loadouts? | Yes: exchangeable for Gold Bars (cosmetics) | [2] |
| Is there a per-round or seasonal reset? | The Patch 0.11 and 0.1.2 posts say bans reset cash and XP to 0 but state no routine reset; the Season 02 notes do not mention a wipe (silence is not evidence either way) | [6][7][14] |

The only official text that touches the penalty is framing: stakes are "high" and "every decision" affects the balance [1][3]. A 7 Apr 2026 post adds that a metagame (a Black Market and Vault, and a skills and challenge system) is being built during Early Access, with no economic detail [8].

## Player-reported mechanics

All items in this section are player-reported, dated before Season 02 (12 to 17 Sep 2026), and not confirmed officially. The 0.2.0 interface change to Rebuy Last Loadout [14] may have altered how the "Re-buy Loadout" option described below looks and works.

| Claim | Source and date | Notes |
|-------|-----------------|-------|
| Unrevived death: "that kit is gone and the next one comes out of the same wallet" | allthings.how, updated 12 Sep 2026 [9] | No dollar figure given |
| Being revived "keeps the loadout you already paid for" | [9] | Consistent with the revive-as-income framing |
| "Re-buy Loadout" rebuilds the previous kit at the vendor | KeenGamer, 17 Sep 2026 [10] | No price stated; whether it costs more than a manual purchase is unknown |
| A helicopter crash "takes your loadout, their loadout, and everyone else in the cabin" | [9] | Wording for pilot and passengers; not tested |
| Repeated deaths can drain reserves | [10] | Qualitative only |
| Destroyed or abandoned vehicle: pay the spawn price again | GameBrief, 17 Sep 2026, figures for the 14 Sep 2026 patch [11] | Repair at a Repair Station with Mechanical Supplies avoids repaying [11] |
| Basic Parachute $100, described as inexpensive insurance against losing a loadout in a damaged aircraft | [10] | Not an actual insurance mechanic |
| Emergency Resuscitator free, usable once per life | [10] | Not tested |
| Defibrillator $1,600 when bought for a loadout | [10] | Also in combat-loadouts-foundation |

## Low and zero cash

No source describes what the game does when the balance cannot cover a loadout, whether a minimal free kit exists, or whether the balance can go negative. The allthings.how guide notes only that there is "no per-round reset to bail you out" and advises checking the balance before each rebuy [9]. The KeenGamer guide advises not building a loadout so expensive that "several deaths destroy your cash reserves" [10]. Neither describes a floor (player-reported). Two other facts bear indirectly: Bulkhead resets cash and XP to 0 as an anti-exploit penalty, which implies zero is a valid state [6][7], and the Emergency Resuscitator is reported free [10].

## Vehicle loss costs

Vehicles are bought per life at a spawn price (player-reported) [11]. Official Season 1 changelog prices for vehicle-class items are in the baseline table [5]; Season 02 re-priced many vehicles (for example L2A6 $14,000 to $22,000 and Havoc $18,000 to $28,000 in vendor prices, and new vehicles such as the T-72B3 at $16,000), held in price-tables-season-1 [14]. The changelog does not say whether each figure is a one-time unlock payment or the recurring per-life price, so the repayment cost after a loss cannot be derived from official text alone (see Open Questions).

## Baseline values (Season 1 history)

All values are from the Season 1.0 changelog (10 Sep 2026, pre-load post dated 9 Sep) unless stated. "As-of version" is the build the value was verified against, Update 0.1.2 with hotfixes to 2 Oct 2026. Several were changed by Season 02 (0.2.0); see price-tables-season-1 and cash-rewards-and-costs for current numbers [14].

| Value | As-of version | Source |
|-------|---------------|--------|
| Starting balance $10,000 | 0.1.2 | [1] |
| Death cost: not stated officially | 0.1.2 and 0.2.0 | [1][2][3][4][5][6][7][14] |
| Re-buy Loadout price: not stated officially | 0.1.2 and 0.2.0 | [1][2][3][4][5][6][7][14] |
| Rebuy Last Loadout UI pre-fills vendor, editable | 0.2.0 (14 Oct 2026) | [14] |
| Vendor, Forward Operating Base $7,500 (was $2,500) | 0.1.2 | [5] |
| Vendor, Large Hammer $2,400 (was $1,600) | 0.1.2 | [5] |
| Support, Medium Hammer $25,000 (was $10,000) | 0.1.2 | [5] |
| Support, Large Hammer $75,000 (was $25,000) | 0.1.2 | [5] |
| Career, Artillery Tank $500,000 (was $400,000) | 0.1.2 | [5] |
| Pilot, Little Bird with miniguns $50,000 (was $25,000) | 0.1.2 | [5] |
| Pilot, Z20 Lakota $35,000 (was $50,000) | 0.1.2 | [5] |
| Pilot, small armoured supply crate $10,000 (was $5,000) | 0.1.2 | [5] |
| Driver, URAL $35,000 (was $50,000) | 0.1.2 | [5] |
| Driver, Dune Buggy $25,000 (was $35,000) | 0.1.2 | [5] |
| Driver, Kodiak Flatbed $35,000 (was $15,000) | 0.1.2 | [5] |
| Driver, Music Tape H $2,500 (was $5,000) | 0.1.2 | [5] |
| Recon, 6-10x MRAD scope $40,000 (was $25,000); MOA scope $45,000 (was $30,000) | 0.1.2 | [5] |
| Supply crate purchase curve rescaled to 1 to 200 (was 25 to 250) | 0.1.2 | [5] |
| Community server end-of-match cash bonus +5% for one week from 14 Sep 2026 | 0.11 (expired by 0.1.2) | [6] |
| Cash and XP set to 0 for cash-exploit bans | 0.1.2 | [6][7] |
| Bobcat about $500 per spawn (player-reported) | Season 1, 14 Sep 2026 | [11] |
| SPH-2 about $8,000 per spawn (player-reported) | Season 1, 14 Sep 2026 | [11] |
| Basic Parachute $100 (player-reported) | Season 1, 17 Sep 2026 | [10] |
| Defibrillator $1,600 per loadout (player-reported) | Season 1, 17 Sep 2026 | [10] |
| Emergency Resuscitator free (player-reported) | Season 1, 17 Sep 2026 | [10] |

# Early Access Changes & Known Issues

- 18 Feb 2026 Q&A (pre-release): cash persists, may be exchanged for Gold Bars, and loadouts are bought each life [2].
- 10 Sep 2026, Season 1.0 changelog: many price changes and slowed XP curves; no change to a death rule is listed [5].
- 14 Sep 2026, Patch 0.11: various cash exploits fixed and a five percent community end-of-match cash bonus for one week [6].
- 30 Sep 2026, Update 0.1.2: revive checks made server-authoritative, fly-through vehicle rewards capped, buildable-destruction and out-of-zone pallet rewards reduced [7]. This changes income, not the death cost.
- Superseded: Season 02 was planned for 15 Oct 2026 [12]; it shipped on that date [15].
- 14 Oct 2026, Season 02 patch notes: Rebuy Last Loadout UX improvement (old placeholder rebuy UI removed; vendor pre-filled with last loadout, editable before purchase); reduced controller hold time on "Purchase Loadout"; many price changes. No death-penalty, refund or cash-reset change is listed [14].
- 9 Oct 2026 preview post: no death-penalty detail [13].
- 15 Oct 2026: Update 0.2.0 released, servers back online [15]. No official post after this date is in the 2026-10-30 snapshot.

# Admin & Technical Notes

None found. No official server setting for death cost, re-buy or balance was found in the saved notes, including the Season 02 notes [7][14]; the 0.1.2 admin changes cover scheduled restarts and RCON restrictions only [7].

# Risks & Caveats

- The central claims are player-reported and may describe behaviour that patches have since changed; the guides date from 12 to 17 Sep 2026 [9][10][11].
- Guides are single-source for each claim; no second independent guide for the crash rule was retrieved.
- Season 02 changed prices and the rebuy interface; the guides pre-date it, so their descriptions may be stale. Later hotfixes after 15 Oct are unchecked (none in the snapshot). The Black Market and Vault are not in the 0.2.0 notes [8][14].
- The changelog price lines do not label unlock versus per-life price.

# Open Questions

- What exactly is lost on death, and is the loss total or partial? No official statement, including the Season 02 notes; resolve with an in-game test or an official statement [14].
- Does Rebuy Last Loadout cost the same as the original kit? Unknown; the 0.2.0 notes describe only the interface [14].
- What happens when the balance is below the cost of a loadout or can go negative? No source.
- Is there any insurance, refund or free fallback kit? None found; the Basic Parachute (now $500 in vendor prices [14]) is described as cheap protection only by a pre-Season-02 guide [10].
- Are changelog vehicle prices unlock prices or per-spawn prices? The posts do not say.
- Do the player-reported death mechanics still hold in Update 0.2.0? Untested by this pipeline.
- Note: the official 18 Feb Q&A states cash can be exchanged for Gold Bars used for cosmetics in the Gold Market [2]; whether leftover cash converts automatically at a season wipe remains unconfirmed (see season-reset-and-currencies).

# References

**Primary Sources**

- [1] **Valve / Bulkhead (Steam)** — *WARDOGS* store page. https://store.steampowered.com/app/1867240/WARDOGS/. Accessed 2026-10-08.
- [2] **Bulkhead (Steam news)** — *WARDOGS - TOP QUESTIONS*, 18 Feb 2026. https://store.steampowered.com/news/app/1867240/view/1825093633182385. Accessed 2026-10-08.
- [3] **Bulkhead (Steam news)** — *WARDOGS: Tactical Depth & Teamplay*, 21 May 2026. https://store.steampowered.com/news/app/1867240/view/1833334318569240. Accessed 2026-10-08.
- [4] **Bulkhead (Steam news)** — *Pre-Order Now*, 11 Aug 2026 (monetisation stance, Supporter Edition). https://store.steampowered.com/news/app/1867240/view/1840310314354505. Accessed 2026-10-08.
- [5] **Bulkhead (Steam news)** — *Pre-Load Live & Season 1 Changelog*, 9 Sep 2026. https://store.steampowered.com/news/app/1867240/view/1843481262690549. Accessed 2026-10-08.
- [6] **Bulkhead (Steam news)** — *Scheduled Maintenance & Patch 0.11*, 12 Sep 2026. https://store.steampowered.com/news/app/1867240/view/1843481262698449. Accessed 2026-10-08.
- [7] **Bulkhead (Steam news)** — *WARDOGS | Update 0.1.2 (Minor Patch)*, 30 Sep 2026. https://store.steampowered.com/news/app/1867240/view/1845383656376490. Accessed 2026-10-08.
- [8] **Bulkhead (Steam news)** — *WARDOGS Early Access & Beyond*, 7 Apr 2026. https://store.steampowered.com/news/app/1867240/view/1828894815567544. Accessed 2026-10-08.
- [13] **Bulkhead (Steam news)** — *WARDOGS | Season 02 Preview*, 9 Oct 2026. https://store.steampowered.com/news/app/1867240/view/1846018067933823. Accessed 2026-10-30.
- [14] **Bulkhead (Steam news)** — *WARDOGS | Season 02 Patch Notes*, 14 Oct 2026. https://store.steampowered.com/news/app/1867240/view/1846651706674560. Accessed 2026-10-30.
- [15] **Bulkhead (Steam news)** — *WARDOGS | SEASON 02 IS NOW LIVE*, 15 Oct 2026. https://store.steampowered.com/news/app/1867240/view/1846651706677015. Accessed 2026-10-30.
- [12] **Bulkhead (Steam news)** — *WARDOGS Season 02 teaser*, 22 Sep 2026 (15 Oct 2026). https://store.steampowered.com/news/app/1867240/view/1844115010504839. Accessed 2026-10-08.

**Press & Secondary**

None cited.

**Player-Reported Evidence**

- [9] **allthings.how** — *WARDOGS cash: how to stop losing money as a beginner*, updated 12 Sep 2026. https://allthings.how/wardogs-cash-how-to-stop-losing-money-as-a-beginner/. Accessed 2026-10-08.
- [10] **KeenGamer** — *WARDOGS progression guide*, 17 Sep 2026. https://www.keengamer.com/articles/guides/wardogs-progression-guide/. Accessed 2026-10-08.
- [11] **GameBrief** — *WARDOGS vehicles guide 2026*, 17 Sep 2026. https://www.gamebrief.net/blog/wardogs-vehicles-guide-2026. Accessed 2026-10-08.

# Further Reading

The saved official Q&A posts of 18 Feb and 3 Mar 2026 (the latter is a video with no text answers); official Steam news posts after 15 Oct 2026 (none in the 2026-10-30 snapshot).

# Related Documents

- economy-foundation
- cash-rewards-and-costs
- price-tables-season-1
- combat-loadouts-foundation
- season-reset-and-currencies

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft; pre-Season 02 baseline. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after independent re-verification of validate, markdownlint, links (0 dead) and Steam post ids. Pre-Season-02 baseline. | Standing mandate (auto-approve on green QA) |
| 1.1.0 | 2026-10-30 | Research Pipeline (virtual agent) | Revised for Season 02 / Update 0.2.0 against the official preview, patch notes and release post: added the confirmed Rebuy Last Loadout interface change; death-penalty rules, re-buy price and zero-cash behaviour kept unconfirmed (notes silent); player-reported mechanics labelled as pre-Season-02; Season 1 values kept as dated history. | — |
