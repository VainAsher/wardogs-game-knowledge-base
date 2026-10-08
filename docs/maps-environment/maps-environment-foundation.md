---
id: maps-environment-foundation
title: "Maps & Environment: Foundation"
version: 1.0.0
status: frozen
confidence: Low
category: Maps & Environment
topic: "Map list, destructibility, points of interest"
market: Global
game_version: "Early Access Season 01, patch 0.1.2 (30 Sep 2026) plus 2 Oct 2026 hotfixes; Season 02 announced for 15 Oct 2026"
document_type: foundation
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related:
  - gameplay-modes-foundation
  - vehicles-outposts-foundation
  - technical-servers-foundation
  - meta-release-foundation
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
| Version | 1.0.0 |
| Status | frozen |
| Confidence | Low |
| Category | Maps & Environment |
| Game version | Early Access Season 01, patch 0.1.2 plus 2 Oct 2026 hotfixes |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

Officially, WARDOGS launched in Early Access on 10 September 2026 with three maps, each with three variations, set in "derelict industrial mountains of Eastern Europe" on a destructible battlefield [1][2]. The Steam page does not name the maps, give a map size, or define "variations". Every match is played around a randomised 2x2 km Control Zone inside a larger battlefield [1].

The map names (Bakurani, Ozeti, Zestafona), their points of interest and the relative sizes come only from community-run references and are player-reported [9][10][11]. Bulkhead has announced rain as an extra weather state per map for Season 02 (15 Oct 2026), not a mid-match event [3][4]. No fourth map is announced [4][8].

Confidence is Low. The official sources give counts and a setting but no names or dimensions. The named detail rests on community directories that disagree with each other on play-area size.

# Key Takeaways

- Launch content is three maps, each with three variations (Team17 press release, 10 Sep 2026) [2].
- The Steam page calls the game a "militaristic sandbox" for up to 100 players, set on a destructible battlefield; rocket launchers can destroy apartment blocks [1]. "Sandbox" describes building and destruction freedom, not a separate map type (Assessment: Medium, see Detail) [1].
- Official sources do not name the maps. Community directories list Bakurani, Ozeti and Zestafona (player-reported, Season 01) [9][10][11].
- A third-party roadmap piece gives a 256 km2 destructible map; a community guide gives about 16 km edge to edge. These agree arithmetically but neither is official [7][11].
- The play area is the randomised 2x2 km Control Zone [1]; one community guide instead claims 500 m radius circles, a conflict left open [11].
- Season 02 (15 Oct 2026) adds rain as a per-map weather state, not a dynamic mid-match event [3][4]. No new map is announced [4][8].
- More maps are planned for 1.0, with no names or dates [1][7].

# Scope

Covers the map roster and its variations, size, setting and biomes, destructibility, weather and time of day, points of interest, and planned maps. Game version verified: Season 01, patch 0.1.2 and the 2 Oct 2026 hotfixes, with Season 02 teaser information. Excluded: Control Zone scoring rules (see gameplay-modes-foundation), vehicles and outpost building (see vehicles-outposts-foundation), server map settings (see technical-servers-foundation), release facts (see meta-release-foundation).

# Definitions

- **Control Zone**: the randomised 2x2 km objective area inside a larger map [1].
- **Variation**: Bulkhead's unexplained term for three versions of each map [2]. Its meaning is unverified; see Open Questions.
- **Play area (community usage)**: a community term for the named rotation circle where a match is fought, player-reported [11].

See also `GLOSSARY.md`.

# Current State

Verified 2026-10-08.

- The setting is "derelict industrial mountains of Eastern Europe"; the battlefield is destructible and includes towns and apartment blocks [1].
- Early Access maps are described as large-scale with dynamic objective zones [1].
- Players can destroy apartment blocks with rocket launchers and drive armoured vehicles through towns [1].
- Players can build and fortify key locations, for example a forward operating base at a chokepoint [1].
- The launch set is three maps, each with three variations [2].
- The only official size statement is that the Control Zone is a randomised 2x2 km area inside a larger battlefield; total map size is not stated on the Steam page [1].
- More maps are planned alongside weapons, vehicles and fighter jets; no map is named [1].
- Season 02 is dated 15 Oct 2026 in Bulkhead's Steam teaser, and rain is "an additional weather state per map and not a dynamic event mid match" per a Bulkhead post quoted by press [3][4]. An unofficial wiki says the 30 Sep 2026 announcement mentions "new map conditions" without detail [8]; this is player-reported.
- The 0.1.2 notes and Season 1 changelog contain no new map, terrain or weather entries [5][6].

# Detail

## Reconciling "sandbox" and "3 maps x 3 variations"

The Steam page says "sandbox" and "maps" with no count [1]. The press release gives the count: three maps with three variations each [2]. These are compatible: "sandbox" describes the build-and-destroy freedom, while the press release counts discrete map assets. Assessment: Medium confidence that this is the intended reading, because neither official source defines either term.

The word "variations" is not defined. A community guide lists about three or four named areas per map (for example Default, Farmland, Lumberyard on Bakurani) that come up from a rotation, with some defined areas never selected [11]. This plausibly matches the "three variations" count but is an inference; no source confirmed sunrise or cloudy variants of the maps. Treat the equivalence as unverified.

## Community-reported map roster (Season 01, player-reported)

| Map | Region label | Described terrain | Relative size | Source |
|-----|--------------|-------------------|---------------|--------|
| Bakurani | Kavkazi | River valley, town, factory district, snow-capped northern mountains | Smallest | [9][10][11] |
| Ozeti | Europe | Wooded river basin, hill town, walled football stadium, church, farmland | About 4x Bakurani | [9][10][11] |
| Zestafona | North America | River bend, warehouse and rail districts, shipping, farmland, forest | About 4x Bakurani | [9][10][11] |

A further "Bakurani Outskirts, Jutari" sniper map and "Saburtulo" appear in one roster but are listed as not confirmed playable or not playable [11]. They are not counted as launch maps.

## Points of interest (player-reported)

| Map | Named features | Source |
|-----|----------------|--------|
| Bakurani | Hill Town, Apartments, Sunflower complex and church, Lumberyard, Water Silos, Bridge Hill, numbered towers | [10] |
| Ozeti | Stadium complex, hillside churches, Shops, Pool, Industrial, Lumberyard, farms, numbered towers | [10] |
| Zestafona | Brick and numbered warehouses, large factories, train sheds and tracks, Bus Depot, Offices, Water Towers, farmland | [10] |

One guide counts 171 control zones across the three maps [10]. Another records three or four zone positions per map and three live tower objectives on Zestafona [9]. These counts differ, so no figure is given as fact.

## Size

| Claim | Value | Class | Source |
|-------|-------|-------|--------|
| Control Zone | Randomised 2x2 km inside a larger battlefield | Official | [1] |
| Whole map | 256 km2, fully destructible | Third-party roadmap | [7] |
| Whole world | About 16 km edge to edge | Community | [11] |
| Play circle | 500 m radius (550 m Ozeti) | Community | [11] |

Assessment: 16 km x 16 km equals 256 km2, so the two whole-map figures agree, but both are unofficial (Low confidence). The 500 m radius play-circle claim conflicts with the official 2x2 km zone and is not adopted [1][11].

## Destructibility

Official: a destructible battlefield where rocket launchers destroy apartment blocks [1]; the press release lists destruction as a core pillar alongside construction [2]. No source gives a per-structure destruction model, which terrain can be deformed, or whether damage persists across matches. A third-party piece says terrain as well as buildings can be reshaped [7]; the official sources only mention buildings.

## Weather and time of day

Rain is the only announced weather addition, shown in the Season 02 teaser as heavy rain and storm imagery [3][4][8]. Bulkhead says it is a per-map state fixed for the match [3]. One press piece reports it is unconfirmed whether rain affects visibility or vehicles [4]. No day/night cycle is documented in any source read; a claim of existing sunrise, cloudy and sunny states was seen only in a search summary and is not relied on.

# Early Access Changes & Known Issues

| Date | Change | Source |
|------|--------|--------|
| 2026-09-10 | Launch with three maps, three variations each | [2] |
| 2026-09-23 | Bulkhead clarifies rain is a per-map state, not mid-match | [3] |
| 2026-09-30 | Patch 0.1.2: buildable-destruction rewards capped by construction progress; Season 02 teases "new map conditions" | [6][8] |
| Season 01 changelog | Fix for an exploit reaching an unintended position on a church roof; Forward Operating Base vendor cost $2,500 to $7,500; dropped items no longer affect navigation | [5] |
| 2026-10-15 | Season 02 due; rain state announced; no new map announced | [3][4] |

No map-specific known-issue list was found. The reports of the 2 Oct 2026 hotfixes contain no map items in the sources read [6].

# Admin & Technical Notes

Server IDs persist across map changes since patch 0.11, per a community guide; how the next map is chosen is not documented [9]. Server map configuration is covered in technical-servers-foundation.

# Risks & Caveats

- The map names, sizes and points of interest are community-sourced and a community directory states it is not a Bulkhead publication [9].
- Early Access: maps, rotations and weather can change each patch, and Season 02 lands 15 Oct 2026.
- Steam news post bodies do not render to fetchers, so official patch text could not be read [1].
- Sources disagree on play-area size and control-zone counts [9][10][11].
- Several guide sites are commercial or SEO-oriented; nothing here rests on them alone for a core claim.

# Open Questions

- What does "three variations" mean (areas, weather, time of day, layouts)? Resolve via a Bulkhead post or in-game check.
- Official map names and total size.
- Does destruction reach terrain, and does it persist?
- Does rain change visibility, vehicles or aircraft?
- Will Season 02 add a map beyond "new map conditions"?

# References

**Primary Sources**

- [1] **Valve / Bulkhead Studios** — *WARDOGS on Steam*. https://store.steampowered.com/app/1867240/WARDOGS/. Accessed 2026-10-08.
- [2] **Team17 / Bulkhead** — *WARDOGS is coming to Steam Early Access on 10 September* (press release). https://www.gamedeveloper.com/press-release/wardogs-is-coming-to-steam-early-access-on-10-september. Accessed 2026-10-08.

**Press & Secondary**

- [3] **Vice** — *WARDOGS developer confirms Season 2 rain will not change mid-match* (quotes a Bulkhead post). https://www.vice.com/en/article/wardogs-season-2-rain-progression-wipe/. Accessed 2026-10-08.
- [4] **KeenGamer** — *WARDOGS Season 2: confirmed features, rumors, changes*. https://www.keengamer.com/articles/guides/wardogs-season-2-confirmed-features-rumors-changes/. Accessed 2026-10-08.
- [5] **Gfinity Esports** — *WARDOGS Season 1 changelog: Early Access patch notes*. https://www.gfinityesports.com/article/wardogs-season-1-changelog-early-access-patch-notes. Accessed 2026-10-08.
- [6] **InGameNews** — *WARDOGS update 0.1.2 and security hotfix: a comparative overview*. https://ingamenews.com/gaming-news/wardogs-update-0-1-2-and-security-hotfix-a-comparative-overview/. Accessed 2026-10-08.
- [7] **XGamingServer** — *WARDOGS roadmap: everything confirmed coming to Early Access*. https://xgamingserver.com/blog/?p=23236. Accessed 2026-10-08.

**Player-Reported Evidence**

- [8] **wardogswiki.com (unofficial)** — *WARDOGS Season 2: release date and confirmed details*. https://www.wardogswiki.com/en/guides/wardogs-season-2. Accessed 2026-10-08.
- [9] **Gamebrief** — *WARDOGS maps guide: 3 playable maps and rotation*. https://www.gamebrief.net/blog/wardogs-maps-guide-2026. Accessed 2026-10-08.
- [10] **XGamingServer** — *WARDOGS map guide: all 3 maps and control zones*. https://xgamingserver.com/blog/wardogs-map-guide/. Accessed 2026-10-08.
- [11] **allthings.how** — *WARDOGS maps: every location and what each one fights over*. https://allthings.how/wardogs-maps-every-location-and-what-each-one-fights-over/. Accessed 2026-10-08.

# Further Reading

Steam News Hub for Season 02 details as they publish: https://store.steampowered.com/news/app/1867240

# Related Documents

- gameplay-modes-foundation
- vehicles-outposts-foundation
- technical-servers-foundation
- meta-release-foundation

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after independent re-verification of validate, markdownlint and links (0 dead). | Standing mandate (auto-approve on green QA) |
