---
id: season-reset-and-currencies
title: "Seasons, Resets & Currencies"
version: 1.1.0
status: frozen
confidence: Medium
category: Economy
topic: "Season structure, what resets, Gold Bars, what persists, cosmetics"
market: Global
game_version: "Early Access Season 02, Update 0.2.0 (15 Oct 2026); official posts through 2026-10-15 (snapshot 2026-10-30)"
document_type: depth
created: 2026-10-08
updated: 2026-10-30
review_due: 2026-11-20
sources_verified: 2026-10-30
supersedes: null
related: [economy-foundation, progression-and-role-tracks, season-2-announcements, patch-history, price-tables-season-1, cash-rewards-and-costs, progression-unlock-tables]
tags: [economy, seasons, wipe, gold-bars, cosmetics, season-02, early-access]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | season-reset-and-currencies |
| Version | 1.1.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Economy |
| Game version | Early Access Season 02, Update 0.2.0 (15 Oct 2026); official posts through 2026-10-15 (snapshot 2026-10-30) |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-30 |
| Review due | 2026-11-20 |

# Executive Summary

This document covers seasons and currencies as of Update 0.2.0 (Season 02, live 15 October 2026), keeping the 2026-10-08 pre-Season-02 baseline as dated history. Official Steam posts confirm that cash persists from match to match, that cash can be exchanged for Gold Bars, that Gold Bars are the "endgame currency" for cosmetic unlocks in a "Gold Market", that Gold Bars and cash will never be sold for real money, and that each season gets its own XP curve and item order [2][3][4]. The Season 02 patch notes (14 Oct 2026) add Gold Market content: eight new weapon and vehicle skins, the removal of the Black & Gold AK camo, and a "Gold Market (LVL 35, $150k)" entry among WARDOG-track unlocks [14]. They also publish a new, faster role-track XP curve for levels 10 to 50, a Season 02 curve change in line with the "different XP curve each season" statement [4][14].

The explicit rule that a season end resets cash and XP, auto-converts leftover cash to Gold Bars, and keeps Gold Bars and cosmetics permanently is NOT in any Steam post in the local snapshot, and the Season 02 patch notes and release post do not mention a wipe, a reset or a Gold Bar conversion [14][15]. That silence is not evidence either way. The claim is attributed to a 7 April 2026 BULKHEAD devlog and is relayed by Vice, KeenGamer and Timesaver.gg [10][11][12]. The conversion rate is unpublished everywhere. No official post after 2026-10-15 is in the 2026-10-30 snapshot.

Confidence is Medium: the currency model and the Season 02 Gold Market changes are official, but the wipe mechanics are second-hand and unconfirmed.

# Key Takeaways

- Official: "Cash earned persists in your account from match to match", and cash can be exchanged "for GOLD BARS - the endgame currency used to obtain cosmetic unlocks in the GOLD MARKET" (Steam post, 18 Feb 2026) [2].
- Official: BULKHEAD "will NEVER monetize in-game cash or gold bars" and will never allow direct purchase of camos (Steam post, 11 Aug 2026) [3].
- Official: "Each season we will have a different XP curve with different item orders" (Season 1 changelog, 9 Sep 2026) [4].
- Official: Season 02 (Update 0.2.0) went live 15 October 2026 after a 08:00 to 09:30 UTC maintenance window [14][15].
- Official (Season 02 patch notes, 14 Oct 2026): eight Gold Market skins across four camo families (Black & Gold Little Bird is a Season 2 exclusive), the Black & Gold AK camo removed from the Gold Market, and Gold Market listed as a WARDOG-track unlock at level 35 for $150k [14].
- Official: Season 02 changed the role-track XP curve for levels 10 to 50 (for example level 20: 250,000 to 111,500 total XP) [14].
- The Season 02 notes and release post do not mention a progression wipe, a cash and XP reset, or an automatic cash-to-Gold-Bar conversion [14][15].
- Press (quoting a devlog not in the snapshot): at season end cash and XP reset, leftover cash auto-converts to Gold Bars, and Gold Bars and cosmetics persist permanently [10][11][12]. Still unconfirmed officially.
- Not published anywhere found: the cash-to-Gold-Bar rate, and whether the starting cash is again $10,000 (the notes state no starting balance) [14].
- Official: exploit sanctions already reset cash and XP to 0 for individuals, a separate mechanism from any seasonal reset [5][6].

# Scope

Covers what is officially said about season structure, the seasonal reset, cash and XP carry-over, Gold Bars and cosmetics, plus a numeric baseline of the Season 1 state so diffs are mechanical. Version: Update 0.2.0 (Season 02), with Update 0.1.2 and the 2 Oct 2026 hotfixes kept as the dated baseline. Excludes the wider Season 02 content list (see season-2-announcements), track and unlock detail (see progression-and-role-tracks), release history (see patch-history), base economy rules (see economy-foundation), vendor prices (see price-tables-season-1) and cash and XP rewards (see cash-rewards-and-costs).

# Definitions

- **Season**: a content and progression cycle; "Season 1.0" is the label for the 10 Sep 2026 launch changelog [4].
- **Cash**: persistent in-game currency, earned by teamplay and spent on loadouts [2][9].
- **Gold Bars**: the "endgame currency" obtained by exchanging cash, spent on cosmetics [2].
- **Gold Market**: the named store for cosmetic unlocks bought with Gold Bars [2].
- **Wipe / reset**: loss of cash and XP progression; in this KB "seasonal reset" is the press-reported end-of-season event, distinct from the exploit-sanction reset [5][10]. Not mentioned in the Season 02 notes [14].

# Current State

As of Update 0.2.0 (official posts through 2026-10-15; snapshot 2026-10-30):

- Season 02 (Update 0.2.0) is live: the patch notes were posted 14 Oct 2026 and the release post on 15 Oct 2026 says servers were back online [14][15]. No official post after 15 Oct is in the snapshot, so later hotfixes are neither confirmed nor ruled out.
- Cash persists between matches [2][9].
- Cash can be exchanged for Gold Bars; Gold Bars buy cosmetics in the Gold Market (18 Feb 2026 FAQ, not restated in later posts, including the Season 02 notes) [2][14].
- The Season 02 notes list eight new Gold Market skins, remove the Black & Gold AK camo, and list "Gold Market (LVL 35, $150k)" under WARDOG-track additional unlocks [14].
- Neither cash nor Gold Bars is ever to be sold, and camos are not to be purchasable directly [3].
- The only real-money item is the optional Supporter Edition (cosmetics) [3][9].
- The Season 02 XP curve for levels 10 to 50 is faster than Season 1 (see Detail) [14].
- The Season 02 notes mention no progression wipe, reset or Gold Bar conversion; whether one happened at the 15 Oct launch is unconfirmed officially [14][15].
- The studio frames progression as "continue earning, progressing and adding value to your account even when not in a match" via a planned Metagame, including a Black Market and Vault and a Skills and Challenge system, built during Early Access [7]. The Season 02 notes do not list these [14].
- Superseded: the 22 Sep teaser (only "WARDOGS Season 02 is coming. 15th October 2026.") [1] and the 30 Sep promise of more information "next week" [5] are resolved by the 9 Oct preview, 14 Oct notes and 15 Oct release [13][14][15].

# Detail

## Officially confirmed versus not (as of 2026-10-30)

| Claim | Status | Source class | Source |
|-------|--------|--------------|--------|
| Cash persists match to match | Confirmed | Primary | [2][9] |
| Cash exchangeable for Gold Bars | Confirmed (pre-launch FAQ, not restated since) | Primary | [2] |
| Gold Bars buy cosmetics in the Gold Market | Confirmed | Primary | [2] |
| Cash and Gold Bars never sold for real money | Confirmed | Primary | [3] |
| Camos never directly purchasable | Confirmed | Primary | [3] |
| Each season has a different XP curve and item order | Confirmed | Primary | [4] |
| Season 02 live 15 Oct 2026 (Update 0.2.0) | Confirmed | Primary | [14][15] |
| Season 02 Gold Market camos, Black & Gold AK removed, Gold Market at WARDOG level 35 ($150k) | Confirmed (0.2.0 notes) | Primary | [14] |
| Season 02 role-track XP curve changed (levels 10 to 50) | Confirmed (0.2.0 notes) | Primary | [14] |
| Season 02 wipe, reset or conversion mentioned in the notes | Not mentioned; silence is not evidence either way | Primary (absence) | [14][15] |
| Cash and XP reset at season end | Press-relayed, devlog not in snapshot | Press | [10][11] |
| Leftover cash auto-converts to Gold Bars | Press-relayed, devlog not in snapshot | Press | [10][11] |
| Gold Bars and cosmetics persist across seasons | Press-relayed, devlog not in snapshot | Press | [10][11] |
| Conversion rate | Not published; one seller says it "fluctuates daily" | Player-reported | [12] |
| Spend cash before the wipe because "zero downside" | Seller inference, unsupported | Player-reported | [12] |
| Season 02 prices, build costs, XP curve | Published in the 14 Oct notes; see price-tables-season-1 and cash-rewards-and-costs | Primary | [14] |

## Gold Bars: the Timesaver claim

Timesaver.gg claims leftover cash converts to Gold Bars and that Gold Bars and cosmetics are "the only things that survive" the wipe, and sells in-game cash [12]. Assessment: partly confirmed, confidence Medium. The Gold Bar currency, the cash exchange and the cosmetic role are in an official Steam post [2], and Vice and KeenGamer independently relay the same end-of-season rule [10][11]. The part still without a readable official text is the automatic conversion and permanence; Timesaver cites the 7 April devlog for it [12]. The official 7 April Steam post only announces the Metagame and links a video [7]. The Season 02 patch notes, released after this claim circulated, do not mention conversion [14]. Timesaver also has a commercial interest in cash, so its "spend first" advice and rate remarks are not evidence.

Rain: Vice reported BULKHEAD said on X that rain is an additional per-map weather state [10]. The official notes list a "New Rain Weather Preset" in Season 02 [14]. Not economy; see the weather docs.

## Season 02 Gold Market and unlock changes (Update 0.2.0)

From the 14 Oct 2026 patch notes [14]:

| Item | Season 02 (0.2.0) |
|------|-------------------|
| New Gold Market skins | Eight, in four families: Black & Gold (Little Bird, "Season 2 Exclusive Gold Market Camo"); Chocolate Chip (Evo-3 Ultra, M14, TCX-SPR); Two-Tone Desert (Galil, Mosin, Havoc); Digital Wood (M500) |
| Removed | Black & Gold AK camo removed from the Gold Market |
| Gold Market unlock | WARDOG track, level 35, $150k (listed under additional unlocks) |

The notes do not say how the Gold Market is accessed before level 35, what Gold Bar prices apply, or whether owned Gold Market cosmetics carry over (not stated). Before this, the Gold Market was described only in the pre-launch FAQ [2].

## Season 02 XP curve (Update 0.2.0)

Total XP required per role-track level, as listed in the 14 Oct 2026 notes ("from" values are as the notes state them) [14]:

| Level | Season 1 (per notes) | Season 02 | Change stated |
|-------|----------------------|-----------|---------------|
| 10 | 35,000 | 25,000 | 29% quicker |
| 15 | 110,000 | 54,750 | 50% quicker |
| 20 | 250,000 | 111,500 | 55% quicker |
| 25 | 365,000 | 206,600 | 43% quicker |
| 30 | 500,000 | 318,200 | 36% quicker |
| 35 | 750,000 | 525,000 | 30% quicker |
| 40 | 975,000 | 712,500 | 27% quicker |
| 45 | 1,225,000 | 920,850 | 25% quicker |
| 50 | 1,500,000 | 1,150,000 | 23% quicker |

The notes' "from" values for levels 25 to 50 differ from the Season 1.0 changelog values recorded in the baseline table below (for example level 25: 325,000 in [4]); the level 10 to 20 values agree. The reason is not stated in either post. Full unlock tables are in progression-unlock-tables.

## What persists, what resets

| Item | Season end (press-relayed; not mentioned in the 0.2.0 notes) | Source |
|------|----------------------------|--------|
| Cash balance | Resets; converts to Gold Bars | [10][11] |
| XP and level progression | Reset | [10][11] |
| Role-track unlocks | Follow level; order may change per season | [4][10] |
| Gold Bars | Persist | [10][11] |
| Cosmetics bought with Gold Bars | Persist ("intended to remain") | [10][11] |
| Supporter Edition cosmetics | Not stated; they are sold items, not season rewards | [3] |

## Baseline values (Season 1, history)

Every value below is as of Season 1 / Update 0.1.2 plus 2 Oct hotfixes unless stated. Season 02 (0.2.0) replaced many of them; current values are in price-tables-season-1, cash-rewards-and-costs and progression-unlock-tables [14].

| Value | As-of version | Source |
|-------|---------------|--------|
| Starting cash $10,000 | Steam page, 2026-10-08 | [9] |
| Hot Zone pays double cash and counts players double | Pre-launch FAQ, 18 Feb 2026 (not restated in later posts) | [2] |
| Progression tracks: 6 | FAQ, 18 Feb 2026 | [2] |
| Level 6 XP: 9,250 (was 8,750) | Season 1.0, 10 Sep | [4] |
| Level 10 XP: 35,000 (was 25,000) | Season 1.0 | [4] |
| Level 15 XP: 110,000 (was 54,750) | Season 1.0 | [4] |
| Level 20 XP: 250,000 (was 111,500) | Season 1.0 | [4] |
| Level 25 XP: 325,000 (was 192,000) | Season 1.0 | [4] |
| Level 30 XP: 400,000 (was 293,750) | Season 1.0 | [4] |
| Level 35 XP: 500,000 (was 416,500) | Season 1.0 | [4] |
| Level 40 XP: 650,000 (was 551,250) | Season 1.0 | [4] |
| Level 45 XP: 800,000 (was 689,500) | Season 1.0 | [4] |
| Level 50 XP: 1,000,000 (was 838,000) | Season 1.0 | [4] |
| Below level 6 XP: unchanged | Season 1.0 | [4] |
| Player kill using air vehicle: 250 XP (was 300) | Season 1.0 | [4] |
| Supply crate item sold under $75: 1 XP (was 25) | Season 1.0 | [4] |
| Supply crate purchase curve 1 to 200 (was 25 to 250) | Season 1.0 | [4] |
| Vendor Forward Operating Base $7,500 (was $2,500) | Season 1.0 | [4] |
| Vendor Large Hammer $2,400 (was $1,600) | Season 1.0 | [4] |
| Career Artillery Tank $500,000 (was $400,000); unlock Career level 90 (was 55) | Season 1.0 | [4] |
| Recon 6-10x MRAD scope $40,000 (was $25,000); MOA $45,000 (was $30,000) | Season 1.0 | [4] |
| Support Medium Hammer $25,000 (was $10,000); Large Hammer $75,000 (was $25,000) | Season 1.0 | [4] |
| Pilot small armoured supply crate $10,000 (was $5,000) | Season 1.0 | [4] |
| Pilot Little Bird with miniguns $50,000 (was $25,000) | Season 1.0 | [4] |
| Pilot Z20 Lakota $35,000 (was $50,000) | Season 1.0 | [4] |
| Driver URAL $35,000 (was $50,000); unlock level 3 (was 4) | Season 1.0 | [4] |
| Driver Dune Buggy $25,000 (was $35,000); unlock level 8 (was 10) | Season 1.0 | [4] |
| Driver Kodiak Flatbed $35,000 (was $15,000); unlock level 10 (was 2) | Season 1.0 | [4] |
| Driver Music Tape H $2,500 (was $5,000); now Driver level 23 (was Pilot 28) | Season 1.0 | [4] |
| Heavy Tank unlock Driver level 35 (was Career 35) | Season 1.0 | [4] |
| Median player at 20-25 hours is "around level 20" (developer note) | Season 1.0 | [4] |
| IR Rangefinders removed from vendor until Season 02 | Hotfix 2 Oct 2026 (0.2.0 notes list the Infrared Range Finder at $3,200 and battery powered [14]) | [8] |
| Standard edition £36.99 (GB store) | 2026-10-08 | [9] |
| Steam reviews 109,396 total, 81,290 positive, "Mostly Positive" | Snapshot 2026-10-08 | [9] |

Other unlock moves in the same changelog (for example Sports Parachute 36 to 35, Deagle 90 to 85, Large Supply Crate 20 to 16) are in progression-and-role-tracks [4].

## Account checks to settle the wipe question

Because the notes are silent, these in-game checks would resolve it (none has been done by this pipeline):

1. Own account: cash balance, per-track level and XP for all six tracks, Gold Bar count, owned cosmetics, compared with any values noted before 15 Oct.
2. Whether the Gold Market UI shows an exchange rate or a conversion notice (no rate is published) [2][11].
3. Whether starting cash is again $10,000 [9].
4. Whether a progression reset notice appeared at the 0.2.0 deploy.

## Exploit-reset precedent

Separate from seasons, the 0.11 and 0.1.2 posts state that exploiters receive a timed ban and "We will reset your cash and XP to 0", and that anyone caught with economy exploits or real-money trading "has had their cash and progression reset" [5][6].

# Early Access Changes & Known Issues

- 18 Feb 2026: FAQ states cash-to-Gold-Bar exchange and Gold Market [2].
- 7 Apr 2026: Metagame announced (Black Market and Vault, Skills and Challenge); the devlog reset rule is attributed to this date by press [7][10].
- 11 Aug 2026: no-monetisation pledges on cash and Gold Bars [3].
- 10 Sep 2026: Season 1.0 XP curve and prices rebased; "each season" a different curve [4].
- 14 Sep and 30 Sep 2026: economy abuse resets and zero-tolerance policy [5][6].
- 2 Oct 2026: IR Rangefinders disabled until Season 02, where they "will require batteries" [8]; the 0.2.0 notes confirm the battery change (about 80s of active use) [14].
- Superseded: the 22 Sep 2026 teaser scheduled Season 02 for 15 Oct 2026 [1]; it shipped on that date [15].
- 9 Oct 2026: Season 02 preview post [13].
- 14 Oct 2026: Season 02 patch notes: eight Gold Market skins, Black & Gold AK camo removed, Gold Market as a WARDOG level 35 unlock ($150k), faster role-track XP curve (levels 10 to 50); no wipe or conversion mentioned [14].
- 15 Oct 2026: Update 0.2.0 released, servers back online [15]. No official post after this date is in the 2026-10-30 snapshot.

# Admin & Technical Notes

None found. No official statement on how a seasonal reset affects community servers, or whether account data is stored per server; unresolved. The 0.2.0 notes warn that community server hosts seen exploiting the faction bonus will be punished [14].

# Risks & Caveats

- Season 02 values supersede the Baseline table; later hotfixes after 2026-10-15 are unchecked (none seen in the snapshot).
- The reset rule is press-relayed from a video devlog; wording may differ from BULKHEAD's original.
- The Gold Bar exchange appears only in a February pre-launch FAQ; behaviour may have changed.
- Commercial sources (Timesaver) are conflicted and used only for labelled claims.
- Absence of a wipe statement in the notes is not proof that none occurred.
- Team17 itself made no seasonal statement found; the statements are BULKHEAD's.

# Open Questions

- Did an end-of-season reset happen at the Season 02 launch? The 0.2.0 notes and release post do not mention one; press said "expect one"; no official post says so [14][15]. Resolve with an in-game account check or an official statement.
- What is the cash-to-Gold-Bar rate, and is it fixed or variable? Unpublished; the "fluctuates daily" claim is unsourced [12].
- Official text contradiction: the FAQ says players can "exchange" cash for Gold Bars (a player action) [2], while press describes automatic conversion at season end [10][11]. Both may be true; unresolved.
- How does a player reach the Gold Market, and what does the level 35 / $150k unlock do relative to the FAQ's exchange description? Not stated [14].
- Do Supporter Edition cosmetics persist? Not stated.
- Do the Black Market, Vault and Skills and Challenge metagame features exist yet? Not in the Season 02 notes [7][14].
- Why do the 0.2.0 notes' Season 1 XP totals for levels 25 to 50 differ from the 9 Sep changelog? Not stated [4][14].

# References

**Primary Sources**

- [1] **BULKHEAD (Steam news)** — *WARDOGS | Season 02 Teaser*, 22 Sep 2026. https://store.steampowered.com/news/app/1867240/view/1844115010504839. Accessed 2026-10-08.
- [2] **BULKHEAD (Steam news)** — *WARDOGS Top Questions*, 18 Feb 2026. https://store.steampowered.com/news/app/1867240/view/1825093633182385. Accessed 2026-10-08.
- [3] **BULKHEAD (Steam news)** — *PRE-ORDER NOW!*, 11 Aug 2026. https://store.steampowered.com/news/app/1867240/view/1840310314354505. Accessed 2026-10-08.
- [4] **BULKHEAD (Steam news)** — *Pre-Load Live & Season 1 Changelog*, 9 Sep 2026. https://store.steampowered.com/news/app/1867240/view/1843481262690549. Accessed 2026-10-08.
- [5] **BULKHEAD (Steam news)** — *WARDOGS | Update 0.1.2 (Minor Patch)*, 30 Sep 2026. https://store.steampowered.com/news/app/1867240/view/1845383656376490. Accessed 2026-10-08.
- [6] **BULKHEAD (Steam news)** — *Scheduled Maintenance & Patch 0.11*, 12 Sep 2026. https://store.steampowered.com/news/app/1867240/view/1843481262698449. Accessed 2026-10-08.
- [7] **BULKHEAD (Steam news)** — *WARDOGS - Early Access & Beyond*, 7 Apr 2026. https://store.steampowered.com/news/app/1867240/view/1828894815567544. Accessed 2026-10-08.
- [8] **BULKHEAD (Steam news)** — *IR Goggles & CIWS Balance Hotfix*, 2 Oct 2026. https://store.steampowered.com/news/app/1867240/view/1845383656386801. Accessed 2026-10-08.
- [13] **BULKHEAD (Steam news)** — *WARDOGS | Season 02 Preview*, 9 Oct 2026. https://store.steampowered.com/news/app/1867240/view/1846018067933823. Accessed 2026-10-30.
- [14] **BULKHEAD (Steam news)** — *WARDOGS | Season 02 Patch Notes*, 14 Oct 2026. https://store.steampowered.com/news/app/1867240/view/1846651706674560. Accessed 2026-10-30.
- [15] **BULKHEAD (Steam news)** — *WARDOGS | SEASON 02 IS NOW LIVE*, 15 Oct 2026. https://store.steampowered.com/news/app/1867240/view/1846651706677015. Accessed 2026-10-30.
- [9] **Valve / BULKHEAD** — *WARDOGS on Steam* (store data snapshot 2026-10-08). https://store.steampowered.com/app/1867240/WARDOGS/. Accessed 2026-10-08.

**Press & Secondary**

- [10] **Vice** — *WARDOGS Season 2: rain, progression wipe*. https://www.vice.com/en/article/wardogs-season-2-rain-progression-wipe/. Accessed 2026-10-08.
- [11] **KeenGamer** — *WARDOGS Season 2: confirmed features, rumors, changes*. https://www.keengamer.com/articles/guides/wardogs-season-2-confirmed-features-rumors-changes/. Accessed 2026-10-08.

**Player-Reported Evidence**

- [12] **Timesaver.gg** — *WARDOGS Season 2: everything we know* (commercial seller of boosting and cash; conflict of interest). https://timesaver.gg/blog/wardogs-season-2-everything-we-know. Accessed 2026-10-08.

# Further Reading

BULKHEAD's 7 April 2026 devlog video (linked from [7]) is the claimed origin of the reset rule; it was not transcribed here. Official Steam news posts after 15 Oct 2026 (none in the 2026-10-30 snapshot).

# Related Documents

- economy-foundation
- progression-and-role-tracks
- season-2-announcements
- patch-history
- price-tables-season-1
- cash-rewards-and-costs
- progression-unlock-tables

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial pre-Season-02 baseline draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after independent re-verification of validate, markdownlint, links (0 dead) and Steam post ids. Pre-Season-02 baseline. | Standing mandate (auto-approve on green QA) |
| 1.1.0 | 2026-10-30 | Research Pipeline (virtual agent) | Revised for Season 02 / Update 0.2.0 against the official preview, patch notes and release post: added Gold Market camos (eight skins, Black & Gold AK removed) and Gold Market level 35 WARDOG unlock, Season 02 XP curve, outcome of the Season 02 teaser; wipe and Gold Bar conversion kept unconfirmed (notes silent); Season 1 baseline kept as dated history; flagged XP "from" value mismatch. | — |
