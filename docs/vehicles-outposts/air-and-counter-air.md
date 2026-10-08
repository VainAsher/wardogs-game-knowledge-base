---
id: air-and-counter-air
title: "Air Vehicles & Counter-Air"
version: 1.0.1
status: frozen
confidence: Medium
category: Vehicles & Outposts
topic: "Helicopters, aircraft, anti-air systems (CIWS/Sea Whiz, Havoc), pilots, IR countermeasures"
market: Global
game_version: "Early Access Update 0.1.2 (30 Sep 2026) plus 2 Oct 2026 security hotfix and IR Rangefinder/CIWS balance hotfix; pre-Season-02 baseline"
document_type: depth
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [vehicles-outposts-foundation, vehicle-roster-and-prices, fob-and-base-building, gadgets-armor-and-equipment, damage-ballistics-and-balance]
tags: [helicopters, pilot-track, anti-air, ciws, havoc, ir-rangefinder, baseline, early-access]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | air-and-counter-air |
| Version | 1.0.1 |
| Status | frozen |
| Confidence | Medium |
| Category | Vehicles & Outposts |
| Game version | Update 0.1.2 plus 2 Oct 2026 hotfixes (pre-Season-02 baseline) |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

This document goes deeper than the parent foundation on WARDOGS aircraft (all helicopters in Early Access) and the systems that counter them. The Steam page lists helicopters in Early Access and fighter jets only for the full release [1]. Official Steam posts name only a few air facts: the Havoc, the Z20 Lakota, flare deployables, a vehicle fly-through reward cap, a Havoc cannon-damage bug fix, and a 2 Oct 2026 hotfix that disabled IR Rangefinders in the vendor and cut the time for the CIWS to destroy a Havoc from about 12 s to about 6 s [2][3][4].

The official 2 Oct balance post settles a press conflict: there were two separate hotfixes that day, a no-gameplay security and stability hotfix and, later, a balance hotfix [3][5]. The official post says "IR Rangefinders" (its title says "IR Goggles") [3].

The roster, prices and Pilot levels come only from player-reported guides, which conflict, so confidence is Medium. All values are a baseline before the Season 02 wipe due 15 Oct 2026 [6].

# Key Takeaways

- Early Access air vehicles are helicopters. The earlier claim that fighter jets are planned for full release is unverified: it is not in the saved store data or any official post, and needs a live-page check.
- 2 Oct 2026, official: IR Rangefinders disabled in the vendor until Season 02, when they will require batteries; the CIWS now destroys the Havoc in around 6 s instead of 12 [3].
- Official: Bulkhead says it "overcorrected" the CIWS in "the previous patch"; the post does not say which patch [3].
- Update 0.1.2 (30 Sep 2026), official: vehicle fly-through exploit fixed with rewards capped, and a Havoc bug that raised damage taken from 20mm and 30mm cannon fire was fixed [2].
- Pilot track gates helicopters (player-reported: Pilot 4, 10/25, 20, 35); guides conflict on the Lakota [8][9].
- Anti-air options reported: Flakpanzer Gepard, and FOB-built CIWS and SAM; costs are guide-sourced [8][9][10].
- Sling-loading is unconfirmed in every source read.

# Scope

Covers helicopter and air roster, Pilot-track gating, anti-air (vehicle and base-built), countermeasures, the 0.1.2 flythrough fix, the 2 Oct 2026 hotfix and sling-loading status. Excludes general ground vehicles and prices (vehicle-roster-and-prices), FOB mechanics (fob-and-base-building), handheld gadgets (gadgets-armor-and-equipment) and damage models (damage-ballistics-and-balance). Version: Update 0.1.2 plus the 2 Oct hotfixes.

# Definitions

- **Pilot track**: progression track unlocking helicopters; player-reported that only helicopter time advances it [8][9].
- **Havoc**: the top attack helicopter; official posts name it [2][3].
- **CIWS**: close-in weapon system; the community calls it "Sea Whiz" [3][7].
- **IR Rangefinder**: vendor item disabled on 2 Oct 2026; the post title says "IR Goggles" [3].
- **Countermeasures**: vendor-tile field and key `V` in one guide [9].

# Current State

As of 2026-10-08.

- The Steam page promotes helicopters that ferry supplies to teammates [1]. A claim of fighter jets planned for the full release is unverified (not in the saved store data or any official post).
- IR Rangefinders were to be disabled in the vendor within 12 hours of 2 Oct 2026 as regional servers restarted, "until Season 02, where they will require batteries to use". Bulkhead said it agreed with player sentiment that they were too overpowered. No client download or server downtime was required [3].
- The CIWS destroys the Havoc in around 6 seconds, down from 12 [3].
- Since the 10 Sep 2026 Season 1 changelog, flare deployables take more loadout room and all helicopters apply input damping on every input device [4].
- Since 0.1.2, vehicle fly-through rewards are capped and the Havoc bug is fixed [2].

# Detail

## Air roster and Pilot-track gating (player-reported)

The Steam news posts do not list a roster; the table merges two guides that disagree [8][9]. Official posts independently confirm only the names Havoc and Z20 Lakota [2][4].

| Aircraft | Spawn price | Pilot level | Unlock fee | Source class |
|----------|-------------|-------------|------------|--------------|
| MH-6 (transport) | about $6,250 | not stated | not stated | player-reported [8] |
| AH-6M miniguns | $7,000 | 4 | $50,000 | player-reported [9]; price only [8] |
| Z20 Lakota | about $7,400 (transport) [8]; $8,000 (miniguns) [9] | 10 [8]; 25 [9] | $75,000 [9] | player-reported, conflicting |
| AH-6R rockets | $12,500 | 20 | $250,000 | player-reported [9]; price [8] |
| Havoc | $18,000 | 35 | not stated | player-reported [8][9] |

Guide [8] counts six helicopters and says transport types carry no offensive armament; [9] says only helicopter time advances Pilot level and that a free large transport helicopter and an SUV appear at team spawn a few minutes into a match [9].

## Anti-air options

| Option | Reported cost | Source class |
|--------|---------------|--------------|
| Flakpanzer Gepard (AA tank) | about $8,000 [8]; $10,000 [9] | player-reported, conflicting |
| CIWS (FOB build, Large Hammer, ammo supply) | 901 supplies | player-reported [10] |
| SAM (FOB build, ammo supply) | not stated | player-reported [10][11] |

The foundation lists anti-air among Large Hammer builds and Ammo as the supply for CIWS and SAM [11]. Official text names only the CIWS [3]. [9] shows a Counter Measures field on vendor tiles with key `V`; [8] does not discuss flares.

## 2 Oct 2026 hotfix and the press conflict

The official post "IR Goggles & CIWS Balance Hotfix" (15:39 UTC) is separate from the "Security & Stability Hotfix" announced for 08:00 UTC that day [3][5].

| Claim | Outlet | Official check |
|-------|--------|----------------|
| 2 Oct hotfix had no gameplay or balance changes | InGameNews [7] | True only of the security hotfix; a second, balance post exists [3][5] |
| IR rangefinder nerf and CIWS 12 s to 6 s | Timesaver.gg, MMOEXP (player-reported) [12][13] | Matches the official post [3] |
| Sea Whiz | player term | Official text says CIWS [3] |

## Baseline values

| Value | As-of version | Source |
|-------|---------------|--------|
| CIWS time to destroy Havoc: about 6 s (was about 12 s) | Hotfix 2 Oct 2026 | official [3] |
| IR Rangefinder: removed from vendor until Season 02; batteries required on return | 2 Oct 2026 | official [3] |
| Fly-through reward: capped (no figure published) | 0.1.2 | official [2] |
| Havoc 20mm/30mm damage-taken bug: fixed | 0.1.2 | official [2] |
| Flare deployable loadout space: increased (no figure) | Season 1, 10 Sep 2026 | official [4] |
| AH-6M $7,000, Pilot 4, unlock $50,000 | Season 1 | player-reported [9] |
| AH-6R $12,500, Pilot 20, unlock $250,000 | Season 1 | player-reported [9] |
| Z20 Lakota $7,400 / Pilot 10 [8] or $8,000 / Pilot 25 / $75,000 [9] | Season 1 | player-reported, conflict |
| MH-6 about $6,250 | Season 1 | player-reported [8] |
| Havoc $18,000, Pilot 35 | Season 1 | player-reported [8][9] |
| Gepard about $8,000 [8] / $10,000 [9] | Season 1 | player-reported, conflict |
| CIWS build cost 901 supplies | Season 1 | player-reported [10] |

## Sling-loading

Unconfirmed. The official posts, the Steam page and both vehicle guides never mention it; guides describe supply drops from the seat (`G` drops a crate) and say transports move "pallets" [1][8][9]. Treat external sling-loading as unconfirmed.

# Early Access Changes & Known Issues

- 10 Sep 2026: Lakota balance and pitch fix, helicopter input damping, flare deployables take more room [4].
- 30 Sep 2026, 0.1.2: fly-through exploit fix with capped rewards; Havoc cannon-damage bug fix [2].
- 2 Oct 2026 00:13 UTC: security hotfix announced, one hour of downtime, no gameplay detail [5].
- 2 Oct 2026 15:39 UTC: IR Rangefinder removal and CIWS 12 s to 6 s [3].
- Planned: Season 02 on 15 Oct 2026 with new map conditions, equipment, balance reworks and features [2][6].

# Admin & Technical Notes

None found. No server setting for air vehicles was seen.

# Risks & Caveats

- All prices and levels are player-reported and conflict; Season 02 may wipe or rebalance them [2][6].
- The post title and body differ (Goggles vs Rangefinders); this document follows the body.
- The sole numeric balance values (12 s and 6 s) are approximate, stated "around" [3].

# Open Questions

- Official text says the CIWS was "overcorrected" in "the previous patch", but 0.1.2 lists no CIWS change; the Havoc bug fix [2] may be related, which is inference only. Resolve with Season 1 or 0.1.2 full notes.
- Does the IR item mean goggles or rangefinders? The title and body differ [3].
- Lakota unlock (Pilot 10 vs 25) and Gepard price are contested [8][9].
- Does the roster include the MH-6 and six helicopters in total [8]? No official list.
- Is external sling-loading present? Unconfirmed.
- Foundation says the 2 Oct hotfix added no gameplay changes [5]; that is true only of the security hotfix.

# References

**Primary Sources**

- [1] **Valve / Bulkhead** — *WARDOGS on Steam*. https://store.steampowered.com/app/1867240/WARDOGS/. Accessed 2026-10-08.
- [2] **BULKHEAD** — *WARDOGS | Update 0.1.2 (Minor Patch)*, Steam announcement, 30 Sep 2026. https://store.steampowered.com/news/app/1867240/view/1845383656376490. Accessed 2026-10-08.
- [3] **BULKHEAD** — *IR Goggles & CIWS Balance Hotfix*, Steam announcement, 2 Oct 2026. https://store.steampowered.com/news/app/1867240/view/1845383656386801. Accessed 2026-10-08.
- [4] **BULKHEAD** — *Season 1 changelog (pre-load live)*, Steam announcement, 9 Sep 2026. https://store.steampowered.com/news/app/1867240/view/1843481262690549. Accessed 2026-10-08.
- [5] **BULKHEAD** — *WARDOGS | Security & Stability Hotfix*, Steam announcement, 2 Oct 2026. https://store.steampowered.com/news/app/1867240/view/1845383656384445. Accessed 2026-10-08.
- [6] **BULKHEAD** — *WARDOGS | Season 02 Teaser*, Steam announcement, 22 Sep 2026. https://store.steampowered.com/news/app/1867240/view/1844115010504839. Accessed 2026-10-08.

**Press & Secondary**

- [7] **InGameNews** — *WARDOGS update 0.1.2 and security hotfix, a comparative overview*. https://ingamenews.com/gaming-news/wardogs-update-0-1-2-and-security-hotfix-a-comparative-overview/. Accessed 2026-10-08.

**Player-Reported Evidence**

- [8] **GameBrief** — *WARDOGS vehicles guide 2026*. https://www.gamebrief.net/blog/wardogs-vehicles-guide-2026. Accessed 2026-10-08.
- [9] **allthings.how** — *WARDOGS: how to get a vehicle, prices and unlock levels*. https://allthings.how/wardogs-how-to-get-a-vehicle-prices-and-unlock-levels/. Accessed 2026-10-08.
- [10] **allthings.how** — *WARDOGS: how to build structures with hammers and FOBs*. https://allthings.how/wardogs-how-to-build-structures-with-hammers-and-fobs/. Accessed 2026-10-08.
- [11] **KeenGamer** — *How to build a FOB in WARDOGS: supplies and costs*. https://www.keengamer.com/articles/guides/how-to-build-a-fob-in-wardogs-supplies-and-costs/. Accessed 2026-10-08.
- [12] **Timesaver.gg** — *WARDOGS IR goggles and CWIS hotfix* (sells boosting services). https://timesaver.gg/blog/wardogs-ir-goggles-cwis-hotfix. Accessed 2026-10-08.
- [13] **MMOEXP** — *WARDOGS October 2 update, Season 2 wipe, IR rangefinder nerf and new weapons* (single podcast source). https://www.mmoexp.com/News/wardogs-october-2-update-season-2-wipe-ir-rangefinder-nerf-and-new-weapons.html. Accessed 2026-10-08.

# Further Reading

Steam News hub: https://store.steampowered.com/news/app/1867240 for Season 02 notes.

# Related Documents

- vehicles-outposts-foundation
- vehicle-roster-and-prices
- fob-and-base-building
- gadgets-armor-and-equipment
- damage-ballistics-and-balance

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft; pre-Season-02 baseline. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after independent re-verification of validate, markdownlint, links (0 dead) and Steam post ids. Pre-Season-02 baseline. | Standing mandate (auto-approve on green QA) |
| 1.0.1 | 2026-10-08 | Orchestrator | Relabelled the fighter-jets claim as unverified (absent from the saved store data and all official posts). | Standing mandate (auto-approve on green QA) |
