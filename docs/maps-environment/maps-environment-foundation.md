---
id: maps-environment-foundation
title: "Maps & Environment: Foundation"
version: 1.1.1
status: frozen
confidence: Medium
category: Maps & Environment
topic: "Map list, destructibility, points of interest"
market: Global
game_version: "Early Access Season 01, patch 0.1.2 (30 Sep 2026) plus 2 Oct 2026 hotfixes; Season 02 announced for 15 Oct 2026"
document_type: foundation
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-10-22
sources_verified: 2026-10-08
supersedes: null
related:
  - gameplay-modes-foundation
  - vehicles-outposts-foundation
  - technical-servers-foundation
  - meta-release-foundation
  - destructibility-and-level-design
  - launch-maps-reference
  - control-zone-and-match-flow
  - season-2-announcements
tags:
  - maps
  - environment
  - destructibility
  - weather
  - points-of-interest
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | maps-environment-foundation |
| Version | 1.1.1 |
| Status | frozen |
| Confidence | Medium |
| Category | Maps & Environment |
| Game version | Early Access Season 01, patch 0.1.2 plus 2 Oct 2026 hotfixes |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-10-22 |

# Executive Summary

Officially, WARDOGS is set in war-torn "Kolchia", where the fight is over a resource called PV-1, in "derelict industrial mountains of Eastern Europe" on a destructible battlefield [1][3]. Bulkhead's own 18 Feb 2026 FAQ states that three teams fight over "a randomized 2x2km Control Zone within a 256km² map" [3]. The Steam page repeats the 2x2 km zone, places it "within larger maps" and lists "large-scale maps with dynamic objective zones" as part of the current Early Access build, but does not give the 256 km² total, so that figure is official yet pre-release [1][3]. The count of "3 maps x 3 variations" appears only in the Team17 press release, and "variation" is never defined [2].

The map names (Bakurani, Ozeti, Zestafona), their points of interest and relative sizes remain player-reported [14][15][16]. The official 0.1.2 post says only that Season 02 (15 Oct 2026) brings "new map conditions" [5]. Rain as a per-map weather state is press reporting of a Bulkhead post on X that is not in the saved official text [11][12]. The Steam page says only that "more maps" are planned; no specific fourth map is announced [1].

Confidence is Medium (raised from Low in v1.0.0). Scale, setting, destruction headlines, the large-scale maps with dynamic objective zones and the sandbox usage rest on official text (the live Steam page, captured 2026-10-08); the named detail and the weather detail do not, and are labelled accordingly. Depth is in launch-maps-reference and destructibility-and-level-design.

# Key Takeaways

- Official (18 Feb 2026, pre-release): the Control Zone is a randomised 2x2 km area within a 256 km² map [3]. The Steam page (live capture 2026-10-08) says "randomized 2x2km Control Zones within larger maps" and gives no total [1].
- Official: the setting is "Kolchia", a war-torn region where the conflict centres on PV-1, with "multiple locations and POIs" [3].
- Official: "sandbox" means the player-driven build-and-destroy play space ("a large-scale, up to 100-player militaristic sandbox" on the Steam page; "100% player-driven militaristic sandbox" in the 21 May 2026 post), not a map type [1][8][9].
- Official: the Steam page lists "large-scale maps with dynamic objective zones" in the current Early Access state and plans "more maps" and "additional objective variations" [1]. "Dynamic" is not defined.
- Official destruction statements are headline-level: a "destructible battlefield", apartment blocks destroyable by rocket launchers, and "Destruction & Build Mechanics" in Early Access [1][3]. Nothing official covers terrain deformation or persistence.
- The "3 maps x 3 variations" claim is from the Team17 press release only; "variation" is undefined [2].
- The 16 Jul 2026 "Level Design & Performance" post is a video devlog; its text mentions Georgian reference gathering and wide-hardware optimisation only [4].
- Season 02 officially adds "new map conditions" (30 Sep 2026 post) [5]; rain as a per-map state is press-reported [11][12].
- Map names and points of interest are player-reported [14][15][16].

# Scope

Covers the map roster and its variations, size, setting, destructibility, weather and time of day, points of interest, and planned maps. Game version verified: Season 01, patch 0.1.2 and the 2 Oct 2026 hotfixes, with Season 02 teaser information. Excluded: Control Zone scoring rules (see gameplay-modes-foundation and control-zone-and-match-flow), vehicles and outpost building (see vehicles-outposts-foundation), server map settings (see technical-servers-foundation), release facts (see meta-release-foundation). Per-map profiles are in launch-maps-reference; the destruction and scale discussion is in destructibility-and-level-design; Season 02 claims are graded in season-2-announcements.

# Definitions

- **Control Zone**: the randomised 2x2 km objective area inside a 256 km² map [3].
- **Kolchia**: Bulkhead's name for the war-torn setting, centred on the fight for PV-1 [3].
- **Sandbox (official usage)**: the player-driven build-and-destroy play space, not a map category [1][8][9].
- **Variation**: the Team17 press release's unexplained term for three versions of each map [2]. Meaning unverified; see Open Questions.
- **Play area (community usage)**: a community term for the named rotation circle where a match is fought, player-reported [16].

See also `GLOSSARY.md`.

# Current State

Verified 2026-10-08.

- Official: the setting is "derelict industrial mountains of Eastern Europe" with a destructible battlefield (Steam page, live capture 2026-10-08) [1]. The name "Kolchia" and the PV-1 conflict come from the FAQ (18 Feb 2026), not the Steam page [3].
- Official: the Steam page states the current Early Access build has "large-scale maps with dynamic objective zones" and a "100-player, three-team" experience [1].
- Official: the Steam page says the full version is planned to include "more maps" and "additional objective variations", alongside new vehicle types including fighter jets; no map is named and no date given (live capture 2026-10-08) [1]. "Additional objective variations" is not defined and is not shown to be the press release's "variations" [2].
- Official: the Control Zone is a randomised 2x2 km area within a 256 km² map (FAQ, 18 Feb 2026, pre-release). The Steam page repeats the 2x2 km zone "within larger maps" but not the total [1][3].
- Official: players can destroy apartment blocks with rocket launchers and tear through towns in armoured tanks; players can build and fortify key locations, for example a forward operating base at a chokepoint (Steam page, live capture 2026-10-08) [1].
- Official: Early Access includes "Destruction & Build Mechanics" (FAQ, 18 Feb 2026) [3].
- Press release (Team17, 10 Sep 2026): three maps, each with three variations [2]. No official Steam post in the snapshot repeats this count.
- Official: Season 02 is dated 15 Oct 2026 (22 Sep 2026 teaser, a video with a one-line text) and is described as "a larger content update, with new map conditions, equipment, balance reworks and additional features" (30 Sep 2026, patch 0.1.2 post) [5][7]. No rain statement appears in that official text.
- Press: rain is "an additional weather state per map and not a dynamic event mid match", attributed by Vice to a Bulkhead post on X that was not viewed [11][12].
- Official: patch 0.1.2 changed buildable-destruction rewards and buildable crit-spot behaviour; it has no map, terrain or weather entry [5]. The Season 1 changelog has one map-related fix (below) [6].

# Detail

## Reconciling "sandbox" and "3 maps x 3 variations"

Official usage of "sandbox" is consistent across posts: "a large-scale, up to 100-player militaristic sandbox" with "building and destruction mechanics" on the Steam page, "100% player-driven militaristic sandbox" in the 21 May 2026 post, "makes the sandbox 100% player-driven" in the FAQ (about proximity chat), and a "100 player Tactical All Out Warfare sandbox" in the announcement trailer post [1][3][8][9]. It describes freedom of play, not a type of map. The map count comes only from the press release: three maps with three variations each [2]. The two are compatible.

"Variation" is undefined in every official text read [1][2][3][4]. A community guide lists about three named areas per map (for example Default, Farmland, Lumberyard on Bakurani) that come up from a rotation [16]. This plausibly matches "three variations" but is an inference, and the FAQ's "multiple locations and POIs" in Kolchia is an equally plausible referent [3]. Treat the equivalence as unverified.

## Player-reported map roster (Season 01)

Player-reported; see launch-maps-reference for the full profiles and the source conflicts.

| Map | Region label | Described terrain | Relative size | Source |
|-----|--------------|-------------------|---------------|--------|
| Bakurani | Kavkazi | River valley, town, factory district, snow-capped northern mountains | Smallest | [14][15][16] |
| Ozeti | Europe | Wooded river basin, hill town, walled football stadium, church, farmland | About 4x Bakurani | [14][15][16] |
| Zestafona | North America | River bend, warehouse and rail districts, shipping, farmland, forest | About 4x Bakurani | [14][15][16] |

A further "Bakurani Outskirts, Jutari" sniper map and "Saburtulo" appear in one roster but are listed as not confirmed playable [16]. They are not counted as launch maps. The "Georgia" in the devlog is a real-world reference-gathering trip, not a map name [4]. Assessment: the Georgian-sounding map names fit that trip, but no official text links them (confidence Low).

## Points of interest (player-reported)

| Map | Named features | Source |
|-----|----------------|--------|
| Bakurani | Hill Town, Apartments, Sunflower complex and church, Lumberyard, Water Silos, Bridge Hill, numbered towers | [15] |
| Ozeti | Stadium complex, hillside churches, Shops, Pool, Industrial, Lumberyard, farms, numbered towers | [15] |
| Zestafona | Brick and numbered warehouses, large factories, train sheds and tracks, Bus Depot, Offices, Water Towers, farmland | [15] |

One guide counts 171 control zones across the three maps [15]. Another records three or four zone positions per map and three live tower objectives on Zestafona [14]. These counts differ, so no figure is given as fact. The only official statement about locations is "multiple locations and POIs" [3].

## Size

| Claim | Value | Class | Source |
|-------|-------|-------|--------|
| Control Zone | Randomised 2x2 km | Official (Steam page and FAQ) | [1][3] |
| Whole map | 256 km² | Official (FAQ, 18 Feb 2026, pre-release) | [3] |
| Whole map, repeated | 256 km², fully destructible | Third-party roadmap | [13] |
| Whole world | About 16 km edge to edge | Player-reported | [16] |
| Play circle | 500 m radius (550 m Ozeti) | Player-reported | [16] |

Assessment: 16 km x 16 km equals 256 km², so the community figure is consistent with the official area if the map is square, which the official text does not say. Medium confidence that 256 km² still holds: it dates from seven months before launch and is absent from the Steam page. The 2x2 km zone is 4 km², about 1.6% of the map (arithmetic from [3]). The 500 m radius play-circle claim conflicts with the official 2x2 km zone and is not adopted [1][16].

## Destructibility

Official: a destructible battlefield where rocket launchers destroy apartment blocks and tanks tear through towns, and "the world around you reacts to your presence" [1]. "Destruction & Build Mechanics" is a listed Early Access pillar [3], and "Base Building & Destruction" is a trailer feature [9]. Since 0.1.2, rewards for destroying buildables scale with build progress [5]. No official source gives a per-structure destruction model, which terrain can be deformed, or whether damage persists across matches. A third-party piece says terrain as well as buildings can be reshaped [13]; official sources mention only buildings. See destructibility-and-level-design.

## Weather and time of day

The official Season 02 text says only "new map conditions" [5]; the teaser is a date and a video [7]. Rain as an additional per-map weather state, fixed for the match, is press reporting of a Bulkhead X post [11]. One press piece reports it is unconfirmed whether rain affects visibility or vehicles [12]. No day/night cycle is documented in any official text read. Whether "new map conditions" means rain, time of day or something else is unconfirmed.

# Early Access Changes & Known Issues

| Date | Change | Source |
|------|--------|--------|
| 2026-02-18 | FAQ states the 2x2 km zone, 256 km² map and Kolchia setting (pre-release) | [3] |
| 2026-09-09 | Season 1 changelog: exploit reaching an unintended position on the church roof fixed; Forward Operating Base vendor cost $2,500 to $7,500; dropped items no longer affect navigation | [6] |
| 2026-09-10 | Launch with three maps, three variations each (press release) | [2] |
| 2026-09-30 | Patch 0.1.2: buildable-destruction rewards scale with build progress; Season 02 described with "new map conditions" | [5] |
| 2026-10-15 | Season 02 due; rain reported by press; no new map announced | [7][11] |

No map-specific known-issue list was found. The 2 Oct 2026 official hotfix posts contain no map items.

# Admin & Technical Notes

Community Server IDs persist between matches and restarts since the 12 Sep 2026 maintenance (patch 0.11); previously they were wiped on map change [10]. How the next map is chosen is not documented. Server map configuration is covered in technical-servers-foundation.

# Risks & Caveats

- Map names, sizes and points of interest are community-sourced; the Gamebrief directory states it is not a Bulkhead publication [14].
- The 256 km² figure is official but dated 18 Feb 2026 and is absent from the Steam page.
- Early Access: maps, rotations and weather can change each patch, and Season 02 lands 15 Oct 2026.
- Video content (the 16 Jul devlog, the Season 02 teaser) carries claims this document could not view [4][7].
- Sources disagree on play-area size and control-zone counts [14][15][16].
- Several guide sites are commercial or SEO-oriented; nothing here rests on them alone for a core claim.

# Open Questions

- What does "three variations" mean (areas, weather, time of day, layouts)? Resolve via a Bulkhead post or in-game check.
- Official map names.
- Is the whole map square (16 km edge), and does 256 km² still describe the shipped maps?
- Does destruction reach terrain, and does it persist?
- What does "new map conditions" cover, and does rain affect visibility, vehicles or aircraft?
- What do "dynamic objective zones" and the planned "additional objective variations" mean in practice?

# References

**Primary Sources**

- [1] **Valve / Bulkhead Studios** — *WARDOGS on Steam* (store page, live capture 2026-10-08, browser-rendered; the storefront-API JSON omits several fields). https://store.steampowered.com/app/1867240/WARDOGS/. Accessed 2026-10-08.
- [2] **Team17 / Bulkhead** — *WARDOGS is coming to Steam Early Access on 10 September* (press release). https://www.gamedeveloper.com/press-release/wardogs-is-coming-to-steam-early-access-on-10-september. Accessed 2026-10-08.
- [3] **Bulkhead Studios** — *WARDOGS - TOP QUESTIONS* (Steam news, 2026-02-18). https://store.steampowered.com/news/app/1867240/view/1825093633182385. Accessed 2026-10-08.
- [4] **Bulkhead Studios** — *WARDOGS | Level Design & Performance* (Steam news, 2026-07-16, video post). https://store.steampowered.com/news/app/1867240/view/1838407329256924. Accessed 2026-10-08.
- [5] **Bulkhead Studios** — *WARDOGS Update 0.1.2 (minor patch)* (Steam news, 2026-09-30). https://store.steampowered.com/news/app/1867240/view/1845383656376490. Accessed 2026-10-08.
- [6] **Bulkhead Studios** — *Pre-load live: Season 1 changelog* (Steam news, 2026-09-09). https://store.steampowered.com/news/app/1867240/view/1843481262690549. Accessed 2026-10-08.
- [7] **Bulkhead Studios** — *WARDOGS Season 02 Teaser* (Steam news, 2026-09-22). https://store.steampowered.com/news/app/1867240/view/1844115010504839. Accessed 2026-10-08.
- [8] **Bulkhead Studios** — *WARDOGS tactical depth and teamplay* (Steam news, 2026-05-21). https://store.steampowered.com/news/app/1867240/view/1833334318569240. Accessed 2026-10-08.
- [9] **Bulkhead Studios** — *WARDOGS Official Announcement Trailer* (Steam news, 2026-02-09). https://store.steampowered.com/news/app/1867240/view/1823825466504264. Accessed 2026-10-08.
- [10] **Bulkhead Studios** — *Scheduled Maintenance, Patch 0.11* (Steam news, 2026-09-12). https://store.steampowered.com/news/app/1867240/view/1843481262698449. Accessed 2026-10-08.

**Press & Secondary**

- [11] **Vice** — *WARDOGS developer confirms Season 2 rain will not change mid-match* (quotes a Bulkhead post on X). https://www.vice.com/en/article/wardogs-season-2-rain-progression-wipe/. Accessed 2026-10-08.
- [12] **KeenGamer** — *WARDOGS Season 2: confirmed features, rumors, changes*. https://www.keengamer.com/articles/guides/wardogs-season-2-confirmed-features-rumors-changes/. Accessed 2026-10-08.
- [13] **XGamingServer** — *WARDOGS roadmap: everything confirmed coming to Early Access*. https://xgamingserver.com/blog/?p=23236. Accessed 2026-10-08.

**Player-Reported Evidence**

- [14] **Gamebrief** — *WARDOGS maps guide: 3 playable maps and rotation*. https://www.gamebrief.net/blog/wardogs-maps-guide-2026. Accessed 2026-10-08.
- [15] **XGamingServer** — *WARDOGS map guide: all 3 maps and control zones*. https://xgamingserver.com/blog/wardogs-map-guide/. Accessed 2026-10-08.
- [16] **allthings.how** — *WARDOGS maps: every location and what each one fights over*. https://allthings.how/wardogs-maps-every-location-and-what-each-one-fights-over/. Accessed 2026-10-08.

# Further Reading

Steam News Hub for Season 02 details as they publish: https://store.steampowered.com/news/app/1867240

# Related Documents

- gameplay-modes-foundation
- vehicles-outposts-foundation
- technical-servers-foundation
- meta-release-foundation
- destructibility-and-level-design
- launch-maps-reference
- control-zone-and-match-flow
- season-2-announcements

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after independent re-verification of validate, markdownlint and links (0 dead). | Standing mandate (auto-approve on green QA) |
| 1.1.0 | 2026-10-08 | Research Pipeline (revision worker) | Revised against full official Steam text; map size 256 km² and Kolchia setting upgraded to official; sandbox usage defined from official posts; 3x3 variations marked press-release-only; 0.1.2 text limited to "new map conditions"; rain relabelled press; unsupported live-page claims demoted; confidence Low to Medium. | Standing mandate (auto-approve on green QA) |
| 1.1.1 | 2026-10-08 | Research Pipeline (revision worker) | Corrected against live store-page capture; restored as Primary the page claims of large-scale maps with dynamic objective zones, more maps and additional objective variations planned, 100-player militaristic sandbox, destructible battlefield and Eastern Europe setting; removed the not-verified caveat and the live-page Open Question; Kolchia attributed to the FAQ only; 256 km² kept as FAQ-only; 3x3 variations still press-release-only; confidence stays Medium (map names and POIs remain player-reported). | Standing mandate (auto-approve on green QA) |
