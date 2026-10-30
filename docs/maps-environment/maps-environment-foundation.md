---
id: maps-environment-foundation
title: "Maps & Environment: Foundation"
version: 1.2.0
status: frozen
confidence: Medium
category: Maps & Environment
topic: "Map list, destructibility, points of interest"
market: Global
game_version: "Early Access Season 02, Update 0.2.0 (15 Oct 2026); official posts through 2026-10-15 (snapshot 2026-10-30)"
document_type: foundation
created: 2026-10-08
updated: 2026-10-30
review_due: 2026-11-20
sources_verified: 2026-10-30
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
| Version | 1.2.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Maps & Environment |
| Game version | Early Access Season 02, Update 0.2.0 (15 Oct 2026); official posts through 2026-10-15 (snapshot 2026-10-30) |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-30 |
| Review due | 2026-11-20 |

# Executive Summary

Officially, WARDOGS is set in war-torn "Kolchia", where the fight is over a resource called PV-1, in "derelict industrial mountains of Eastern Europe" on a destructible battlefield [1][3]. Bulkhead's own 18 Feb 2026 FAQ states that three teams fight over "a randomized 2x2km Control Zone within a 256km² map" [3]. The Steam page repeats the 2x2 km zone, places it "within larger maps" and lists "large-scale maps with dynamic objective zones" as part of the current Early Access build, but does not give the 256 km² total, so that figure is official yet pre-release [1][3]. The count of "3 maps x 3 variations" appears only in the Team17 press release, and "variation" is never defined [2].

The map names (Bakurani, Ozeti, Zestafona), their points of interest and relative sizes remain player-reported [14][15][16]. Update 0.2.0 (Season 02, released 15 Oct 2026) now officially adds a rain weather preset, moves and rebuilds all three team spawns on Bakurani, and adds a Large Shelter buildable "for covering key assets or keeping the rain off" [17][18][19]. The official 0.2.0 notes name Bakurani (in the spawn change) but add no new named map; the Steam page still says only that "more maps" are planned [1][18]. The earlier press-reported rain claims are therefore officially confirmed in substance; the "fixed for the whole match" detail is still press-only [11][12][18].

Confidence is Medium (raised from Low in v1.0.0). Scale, setting, destruction headlines, the sandbox usage, the 0.2.0 rain preset and the Bakurani spawn move rest on official text (Steam page captured 2026-10-08; Season 02 posts of 9 to 15 Oct 2026); the other named map detail does not and is labelled player-reported. No official post after 2026-10-15 is in the 2026-10-30 snapshot. Depth is in launch-maps-reference and destructibility-and-level-design.

# Key Takeaways

- Official (18 Feb 2026, pre-release): the Control Zone is a randomised 2x2 km area within a 256 km² map [3]. The Steam page (live capture 2026-10-08) says "randomized 2x2km Control Zones within larger maps" and gives no total [1].
- Official: the setting is "Kolchia", a war-torn region where the conflict centres on PV-1, with "multiple locations and POIs" [3].
- Official: "sandbox" means the player-driven build-and-destroy play space ("a large-scale, up to 100-player militaristic sandbox" on the Steam page; "100% player-driven militaristic sandbox" in the 21 May 2026 post), not a map type [1][8][9].
- Official: the Steam page lists "large-scale maps with dynamic objective zones" in the current Early Access state and plans "more maps" and "additional objective variations" [1]. "Dynamic" is not defined.
- Official destruction statements are headline-level: a "destructible battlefield", apartment blocks destroyable by rocket launchers, and "Destruction & Build Mechanics" in Early Access [1][3]. Nothing official covers terrain deformation or persistence.
- The "3 maps x 3 variations" claim is from the Team17 press release only; "variation" is undefined [2].
- The 16 Jul 2026 "Level Design & Performance" post is a video devlog; its text mentions Georgian reference gathering and wide-hardware optimisation only [4].
- Update 0.2.0 (released 15 Oct 2026) adds a rain weather preset: wet surfaces, vehicles and characters; context-dependent rain sound; rain visible through destroyed roofs; server-synchronised thunder that can mask footsteps; spotting range affected; Molotov fire reduced [17][18]. The pre-release "new map conditions" wording (30 Sep 2026) [5] is now resolved as this preset.
- Update 0.2.0 moved and rebuilt all three team spawns on Bakurani, each with purpose-built routes to the zone [18]. It also added the Large Shelter buildable (250 build supply) [18].
- The 0.2.0 notes name no new map; any further named map remains unconfirmed [18].
- Map names and points of interest are player-reported [14][15][16].

# Scope

Covers the map roster and its variations, size, setting, destructibility, weather and time of day, points of interest, and planned maps. Game version verified: Early Access Season 02, Update 0.2.0 (official posts 9 to 15 Oct 2026), with the Season 1 baseline (patch 0.1.2 and the 2 Oct 2026 hotfixes) kept as dated history. Excluded: Control Zone scoring rules (see gameplay-modes-foundation and control-zone-and-match-flow), vehicles and outpost building (see vehicles-outposts-foundation), server map settings (see technical-servers-foundation), release facts (see meta-release-foundation). Per-map profiles are in launch-maps-reference; the destruction and scale discussion is in destructibility-and-level-design; Season 02 claims are graded in season-2-announcements.

# Definitions

- **Control Zone**: the randomised 2x2 km objective area inside a 256 km² map [3].
- **Kolchia**: Bulkhead's name for the war-torn setting, centred on the fight for PV-1 [3].
- **Sandbox (official usage)**: the player-driven build-and-destroy play space, not a map category [1][8][9].
- **Variation**: the Team17 press release's unexplained term for three versions of each map [2]. Meaning unverified; see Open Questions.
- **Play area (community usage)**: a community term for the named rotation circle where a match is fought, player-reported [16].

See also `GLOSSARY.md`.

# Current State

Verified 2026-10-30 against Update 0.2.0 (official posts 9 to 15 Oct 2026); items dated 2026-10-08 are the unchanged Season 1 baseline.

- Official: the setting is "derelict industrial mountains of Eastern Europe" with a destructible battlefield (Steam page, live capture 2026-10-08) [1]. The name "Kolchia" and the PV-1 conflict come from the FAQ (18 Feb 2026), not the Steam page [3].
- Official: the Steam page states the current Early Access build has "large-scale maps with dynamic objective zones" and a "100-player, three-team" experience [1].
- Official: the Steam page says the full version is planned to include "more maps" and "additional objective variations", alongside new vehicle types including fighter jets; no map is named and no date given (live capture 2026-10-08) [1]. "Additional objective variations" is not defined and is not shown to be the press release's "variations" [2].
- Official: the Control Zone is a randomised 2x2 km area within a 256 km² map (FAQ, 18 Feb 2026, pre-release). The Steam page repeats the 2x2 km zone "within larger maps" but not the total [1][3].
- Official: players can destroy apartment blocks with rocket launchers and tear through towns in armoured tanks; players can build and fortify key locations, for example a forward operating base at a chokepoint (Steam page, live capture 2026-10-08) [1].
- Official: Early Access includes "Destruction & Build Mechanics" (FAQ, 18 Feb 2026) [3].
- Press release (Team17, 10 Sep 2026): three maps, each with three variations [2]. No official Steam post in the snapshot repeats this count.
- Official: Season 02 was announced for 15 Oct 2026 (22 Sep 2026 teaser) as "a larger content update, with new map conditions, equipment, balance reworks and additional features" (30 Sep 2026) [5][7]. The Season 02 patch notes (14 Oct 2026) describe a "New Rain Weather Preset" and the 15 Oct 2026 post states Update 0.2.0 was released and servers were back online [18][19].
- Official (0.2.0, 14 to 15 Oct 2026): the rain preset makes surfaces, vehicles and characters visibly wet; rain sounds differ by what it falls on and whether you are under cover, indoors, in a vehicle or in the open; destroying a roof makes rain visibly come through it; thunder rolls in during heavier rain, every player on the server hears the same strike at the same time from the same direction, and it is loud enough to mask footsteps; spotting range is affected by rain; Molotov fire is reduced by rain [18]. The 9 Oct 2026 preview describes the preset as changing "visibility, engagement ranges and sound" and says rain "interacts with the environment, including damaged and destroyed structures" [17].
- Official (0.2.0): Bakurani's three team spawns "have been moved and rebuilt, each with purpose-built routes to the zone", which Bulkhead says "should provide a more balanced match across each team" [18]. The patch notes do not give new spawn coordinates or say which areas are affected [18].
- Official (0.2.0): a new Large Shelter buildable ("a large metal shelter for covering key assets or keeping the rain off"), buildable with the medium hammer and above, costing 250 build supply [18].
- Official: the posts through 2026-10-15 add no new named map; the Steam page's "more maps" remains an unspecified plan [1][18]. No official post after 2026-10-15 is in the 2026-10-30 snapshot.
- Press (pre-release): rain is "an additional weather state per map and not a dynamic event mid match", attributed by Vice to a Bulkhead post on X that was not viewed [11][12]. The official notes do not state whether the rain state can change within a match.
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

Since Update 0.2.0 (14 to 15 Oct 2026) the game has an officially documented rain weather preset [18]. Documented effects, all from the patch notes: wet surfaces, vehicles and characters; rain audio that depends on the surface and on whether you are under cover, indoors, in a vehicle or outdoors; rain visibly coming through destroyed roofs; server-synchronised thunder during heavier rain, loud enough to mask footsteps; a change to spotting range; reduced Molotov fire [18]. The Molotov entry also says it can burn destructible foliage and is affected by rain [18]. The preview adds that the preset changes "visibility, engagement ranges and sound" [17].

The notes give no numbers (spotting-range change, Molotov reduction, thunder timing), no statement of how a match gets the rain preset, and no statement that it is fixed for the match; the "not a dynamic event mid match" wording is press-only [11][18]. They do not mention a day/night cycle or other presets, and none is documented in any official text read. Assessment (confidence Medium): the Large Shelter's purpose line suggests rain matters for assets left uncovered, but the notes do not state a gameplay penalty. Season 1 (0.1.2) baseline: no weather state was documented, only "new map conditions" [5].

# Early Access Changes & Known Issues

| Date | Change | Source |
|------|--------|--------|
| 2026-02-18 | FAQ states the 2x2 km zone, 256 km² map and Kolchia setting (pre-release) | [3] |
| 2026-09-09 | Season 1 changelog: exploit reaching an unintended position on the church roof fixed; Forward Operating Base vendor cost $2,500 to $7,500; dropped items no longer affect navigation | [6] |
| 2026-09-10 | Launch with three maps, three variations each (press release) | [2] |
| 2026-09-30 | Patch 0.1.2: buildable-destruction rewards scale with build progress; Season 02 described with "new map conditions" | [5] |
| 2026-10-09 | Season 02 preview describes the rain preset, Bakurani spawn move and Large Shelter | [17] |
| 2026-10-14 | Season 02 patch notes (0.2.0): rain weather preset; Bakurani spawns moved and rebuilt; Large Shelter added; no new named map | [18] |
| 2026-10-15 | Update 0.2.0 released; servers back online. Rain claims that were press-only are now officially confirmed | [19] |

Season 1 (0.1.2) to Season 02 (0.2.0): weather went from none documented to a rain preset, and Bakurani spawns changed; the notes mention no spawn change on the other two maps [18]. No map-specific known-issue list was found, and no official post after 2026-10-15 is in the 2026-10-30 snapshot. The 2 Oct 2026 official hotfix posts contain no map items.

# Admin & Technical Notes

Community Server IDs persist between matches and restarts since the 12 Sep 2026 maintenance (patch 0.11); previously they were wiped on map change [10]. How the next map is chosen is not documented. Server map configuration is covered in technical-servers-foundation.

# Risks & Caveats

- Map names, sizes and points of interest are community-sourced; the Gamebrief directory states it is not a Bulkhead publication [14].
- The 256 km² figure is official but dated 18 Feb 2026 and is absent from the Steam page.
- Early Access: maps, rotations and weather can change each patch; this document reflects Update 0.2.0 and a snapshot with no official posts after 2026-10-15.
- Bakurani's spawn layout changed in 0.2.0, so player-reported Bakurani guides written before 15 Oct 2026 may describe outdated spawn positions and routes [14][15][16][18].
- Video content (the 16 Jul devlog, the Season 02 teaser) carries claims this document could not view [4][7].
- Sources disagree on play-area size and control-zone counts [14][15][16].
- Several guide sites are commercial or SEO-oriented; nothing here rests on them alone for a core claim.

# Open Questions

- What does "three variations" mean (areas, weather, time of day, layouts)? Resolve via a Bulkhead post or in-game check.
- Official map names.
- Is the whole map square (16 km edge), and does 256 km² still describe the shipped maps?
- Does destruction reach terrain, and does it persist?
- How much does rain change spotting range, visibility and Molotov fire, and is the rain state fixed for a match or can it change? The notes give no numbers.
- Do the 0.2.0 Bakurani spawn changes alter the player-reported area rotation or POI list? No official post says.
- Will any new named map be added? Nothing official names one; rumours stay unconfirmed.
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
- [17] **Bulkhead Studios** — *WARDOGS Season 02 Preview* (Steam news, 2026-10-09). https://store.steampowered.com/news/app/1867240/view/1846018067933823. Accessed 2026-10-30.
- [18] **Bulkhead Studios** — *WARDOGS Season 02 Patch Notes* (Steam news, 2026-10-14; includes an in-post update to logistics values). https://store.steampowered.com/news/app/1867240/view/1846651706674560. Accessed 2026-10-30.
- [19] **Bulkhead Studios** — *WARDOGS Season 02 is now LIVE* (Steam news, 2026-10-15). https://store.steampowered.com/news/app/1867240/view/1846651706677015. Accessed 2026-10-30.

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
| 1.2.0 | 2026-10-30 | Research Pipeline (virtual agent) | Cluster G revision for Update 0.2.0: rain weather preset (wet surfaces, sound, roofs, thunder masking footsteps, spotting range, Molotov) promoted from press-only to official; Bakurani spawns moved and rebuilt; Large Shelter; Season 1 baseline kept as history; no new named map; pre-release "Season 02 due" wording replaced; new sources [17]-[19]. | — |
