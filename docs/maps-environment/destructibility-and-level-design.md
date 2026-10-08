---
id: destructibility-and-level-design
title: "Destructibility & Level Design"
version: 1.0.0
status: frozen
confidence: Medium
category: Maps & Environment
topic: "Destruction model, level design philosophy, map scale, performance trade-offs, weather"
market: Global
game_version: "Early Access Season 01, patch 0.1.2 (30 Sep 2026) plus 2 Oct 2026 hotfixes; pre-Season-02 baseline (Season 02 due 15 Oct 2026)"
document_type: depth
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related:
  - maps-environment-foundation
  - launch-maps-reference
  - fob-and-base-building
  - system-requirements-and-performance
tags:
  - destruction
  - level-design
  - map-size
  - performance
  - weather
  - baseline
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | destructibility-and-level-design |
| Version | 1.0.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Maps & Environment |
| Game version | Season 01, patch 0.1.2 plus 2 Oct 2026 hotfixes (pre-Season-02 baseline) |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

This depth document goes beyond maps-environment-foundation on how WARDOGS describes its destruction, its level design and its map scale, using the full text of Bulkhead's official Steam posts saved locally on 2026-10-08. It is a pre-Season-02 baseline: Season 02 is dated 15 Oct 2026 and a progression wipe is expected, so every number below is stamped with the version it applies to.

The headline finding is that the official "Level Design & Performance" devlog (16 Jul 2026) is a short video post. Its text says nothing about map size, map count, destruction rules or the "sandbox" term; it only says the team gathered references "firsthand in Georgia", optimised across a wide range of hardware, and offers graphics options [3]. The map-size and sandbox questions are answered by other official text. An 18 Feb 2026 Bulkhead post states that the Control Zone is a randomised 2x2 km area "within a large-scale 256km² map" [2]. This contradicts the frozen foundation, which treats 256 km² as a third-party figure only (see Open Questions). The Steam store page calls the game a "large-scale, up to 100-player militaristic sandbox" with "building and destruction mechanics" and "larger maps" [1]. The "3 maps x 3 variations" count appears only in the Team17 press release as quoted by the foundation [9].

Confidence is Medium. The scale, sandbox and destruction claims rest on official Bulkhead text, but no official source describes the destruction model, terrain deformation, persistence or the performance cost of destruction, and the Season 02 rain details are press-reported.

# Key Takeaways

- Official text resolves "sandbox": the Steam page and Bulkhead's posts use it for the player-driven, build-and-destroy play space ("a large-scale, up to 100-player militaristic sandbox", "100% player-driven militaristic sandbox"), not for a map type [1][4][5]. It does not conflict with a fixed roster of maps (Season 01) [1][9].
- Official text states a 256 km² map and a randomised 2x2 km Control Zone inside it, in a Bulkhead post of 18 Feb 2026 (pre-release) [2]. The Steam page itself says only "larger maps" and gives no total size [1].
- A 256 km² area is 16 km x 16 km if square, which matches the community "about 16 km edge to edge" claim arithmetically; the official text does not state the shape [2][13].
- The official destruction statements are: a "destructible battlefield" [1], rocket launchers can destroy apartment blocks [1], and "the world around you reacts to your presence" [1]. Nothing official says terrain is deformable or that damage persists across matches.
- The "Level Design & Performance" post is about performance, not destruction rules: Georgian reference gathering, hardware optimisation, and graphics options [3]. Bulkhead says the engine is UE5 enhanced by a custom "WAR DYNAMICS FRAMEWORK" for 100-player density [2].
- Patch 0.1.2 (30 Sep 2026) made destroying buildables scale with build progress, so a placed schematic no longer pays a full reward [7].
- Season 02 (15 Oct 2026) is officially "a larger content update, with new map conditions" [7][8]. The rain-as-per-map-state detail is press-reported only [10][11].

# Scope

Covers destruction as officially described, level design and map-scale statements, the performance links Bulkhead has stated, and weather. Game version verified: Season 01, patch 0.1.2 and 2 Oct 2026 hotfixes. Excluded: per-map profiles and points of interest (launch-maps-reference), building mechanics and FOB rules (fob-and-base-building), hardware requirements and crash codes (system-requirements-and-performance), Control Zone scoring.

# Definitions

- **Control Zone**: the randomised 2x2 km objective area inside a larger map [1][2].
- **Sandbox (official usage)**: Bulkhead's word for the "100% player-driven" open play space, not a map category [1][4][5].
- **Buildable**: a player-placed structure; destroying one now pays in proportion to its build progress [7].
- **WAR DYNAMICS FRAMEWORK**: Bulkhead's name for its UE5 enhancements for high-density 100-player combat [2].

See also `GLOSSARY.md`.

# Current State

Verified 2026-10-08 against official Steam text.

- The Steam page describes "building and destruction mechanics in a large-scale, up to 100-player militaristic sandbox" [1].
- The page says players can "destroy apartment blocks with rocket launchers or tear your way through towns in heavily armoured tanks" and that "the world around you reacts to your presence" [1].
- The short description reads "on a destructible battlefield" [1].
- Zones are randomised 2x2 km areas "within larger maps" [1]. Bulkhead's 18 Feb 2026 Top Questions post states the map as 256 km² [2].
- Bulkhead's Early Access content list includes "Destruction & Build Mechanics" [2].
- The 16 Jul 2026 devlog states performance has been a priority "since day one", references were gathered "firsthand in Georgia", and graphics options let players tune performance [3].
- Patch 0.1.2 changed buildable-destruction rewards and fixed buildable crit spots that jumped or reappeared in the same place [7].
- Season 02 is dated 15 Oct 2026 [8] and is described officially as a larger update with "new map conditions" [7].

# Detail

## Settling "sandbox" versus "3 maps x 3 variations"

| Question | Official answer | Source |
|----------|-----------------|--------|
| What does "sandbox" mean? | Player-driven play space with build and destroy freedom; "100% player-driven militaristic sandbox"; clips recorded in a "100 player Tactical All Out Warfare sandbox" | [1][4][5] |
| Is there an open-world sandbox map? | No official text says so. The mode is a King of the Hill style fight over a Control Zone "within larger maps" | [1][2] |
| How many maps? | Three maps with three variations each (Team17 press release, quoted via the foundation; not re-read here) | [9] |
| What is a "variation"? | Not defined in any official text read | [1][2][3] |

Assessment: Medium confidence that "sandbox" and "3 maps x 3 variations" are compatible. "Sandbox" describes freedom of play inside a map; the press release counts map assets. The official 18 Feb post describes "multiple locations and POIs" in the setting "Kolchia" [2], which could be what a "variation" refers to, but this is an inference and unconfirmed.

## Map scale: what official text says

| Value | As-of version | Source |
|-------|---------------|--------|
| Control Zone size: randomised 2x2 km | Steam page, Season 01 (checked 2026-10-08); also 18 Feb 2026 post | [1][2] |
| Map size: 256 km² | 18 Feb 2026 post (pre-release); not repeated on the Steam page | [2] |
| Max players per match: 100 | Season 01 | [1] |
| Teams: 3 | Season 01 | [1][2] |
| Points to win: 100 | Season 01 | [1][2] |

Assessment: Medium confidence that 256 km² remains current. It is official but dated seven months before launch, and the Steam page uses only "larger maps". The 2x2 km zone is 4 km², about 1.6% of 256 km² (arithmetic from [2]). Community figures (about 16 km edge to edge, 500 m radius play circles) are player-reported or unattributed, and the 500 m figure conflicts with the 2x2 km zone [12][13].

## Level design philosophy as stated

Official statements are thin. The 16 Jul 2026 devlog gives three points: real-world reference gathering in Georgia, continuous optimisation across a wide range of hardware, and tunable graphics options [3]. The 21 May 2026 Debrief lists "real-world ballistics, audio and flight models" and "100% player-driven militaristic sandbox" [5]. The Top Questions post says the setting offers "varied, grounded militaristic gameplay" with "multiple locations and POIs" [2]. No official text describes sightline, chokepoint or zone-placement design rules. Playtesters are quoted as surprised at performance, which is Bulkhead's own characterisation [3].

## What can be destroyed

| Item | Status | Source |
|------|--------|--------|
| Apartment blocks | Destroyable by rocket launchers | [1] |
| Towns and buildings generally | "Destructible battlefield"; tanks can "tear your way through towns" | [1] |
| Player buildables (FOB parts, schematics) | Destroyable; destruction reward scales with build progress since 0.1.2 | [7] |
| Terrain deformation | No official statement; a third-party roadmap claims terrain is destructible | [12] |
| Persistence across matches | No official statement | - |
| Which structures are indestructible | No official list | - |

Destruction is also a listed Early Access pillar: "Destruction & Build Mechanics" [2], and "Infantry, Vehicles, Base Building & Destruction" in the announcement trailer post [4]. The roles list includes Demolitions [4]. The gameplay trailer post lists "building, destruction" among the features [6]. Player-built structure rules are in fob-and-base-building.

## Destruction and performance

No official source ties destruction to a performance cost, a debris cap or a server tick budget. What is official: Bulkhead built a custom framework on UE5 to handle 100 players [2]; performance was prioritised from day one [3]; graphics options exist [3]. The Steam requirements and minimum spec are in system-requirements-and-performance. Assessment: Low confidence that destruction limits exist; the KB neither confirms nor denies them.

## Weather and rain (Season 02)

The official Season 02 teaser gives only the date, 15 Oct 2026 [8]. The 0.1.2 notes say Season 02 brings "new map conditions" [7]. Press reports that rain is an extra per-map weather state, not a dynamic mid-match event, quoting Bulkhead [10][11]. The Bulkhead text itself was not available in the saved official posts, so rain remains press-reported (confidence Medium). Whether rain affects visibility, vehicles or aircraft is unconfirmed [11].

## Baseline values (pre-Season-02)

| Value | As-of version | Source |
|-------|---------------|--------|
| Control Zone 2x2 km (4 km²), randomised | Season 01, checked 2026-10-08 | [1][2] |
| Map area 256 km² | 18 Feb 2026 official post | [2] |
| Max players 100; teams 3 | Season 01 | [1] |
| Points to win 100 | Season 01 | [1] |
| Maps 3, variations 3 each | Season 01 launch, press release | [9] |
| Minimum spec: GTX 1660 / RX 590, 16 GB RAM, 50 GB, 1080p Low 60 fps (upscaled) | Steam page, 2026-10-08 | [1] |
| Recommended spec: RTX 3070 / RX 6700 XT, 1440p Medium 70+ fps native or 4K Medium 60+ upscaled | Steam page, 2026-10-08 | [1] |
| Starting cash $10,000 | Season 01 | [1] |
| Buildable destruction reward scales with build progress | Patch 0.1.2, 30 Sep 2026 | [7] |
| Weather states at baseline: none documented; rain announced | Pre-Season-02 | [8][10] |
| Season 02 date 15 Oct 2026 | Teaser 22 Sep 2026 | [8] |

# Early Access Changes & Known Issues

| Date | Change | Source |
|------|--------|--------|
| 2026-02-18 | 256 km² map and 2x2 km zone stated by Bulkhead | [2] |
| 2026-07-16 | Level Design & Performance devlog | [3] |
| 2026-09-10 | Early Access launch, three maps (press release) | [9] |
| 2026-09-30 | 0.1.2: buildable destruction rewards scale with build progress; buildable crit spots fixed; Season 02 "new map conditions" announced | [7] |
| 2026-10-02 | Hotfixes: no map, terrain or destruction entries in the official posts read | [7] |
| 2026-10-15 | Season 02 due | [8] |

No known-issue list for destruction was found in official text.

# Admin & Technical Notes

None found. No official source documents server-side destruction settings, debris limits or weather configuration.

# Risks & Caveats

- Season 02 on 15 Oct 2026 may change maps, weather and values; this is a baseline.
- The 256 km² figure is official but pre-release.
- Rain details rest on press quoting Bulkhead; the original post was not in the saved snapshot.
- The press-release claim of "3 variations" was taken from the foundation citation and not re-read.
- Destruction rules are undocumented officially; community statements are labelled player-reported.

# Open Questions

- Contradiction with the foundation: maps-environment-foundation lists 256 km² as a third-party-only figure and says the Steam page gives no total size. Bulkhead's 18 Feb 2026 post [2] states 256 km² officially. The foundation should be revised; the Steam page itself still gives no size [1].
- The foundation lists the setting as Eastern Europe only; the official post names the fictional "Kolchia" [2].
- What is a "variation"? Resolve via an official post or in-game check.
- Does destruction include terrain, and does it persist across a match or between matches?
- Is there a destruction or debris performance cap?
- What exactly will rain do to visibility, vehicles and aircraft in Season 02?

# References

**Primary Sources**

- [1] **Valve / Bulkhead Studios** — *WARDOGS on Steam* (store page and store API snapshot). https://store.steampowered.com/app/1867240/WARDOGS/. Accessed 2026-10-08.
- [2] **Bulkhead** — *WARDOGS - TOP QUESTIONS* (Steam news, 18 Feb 2026). https://store.steampowered.com/news/app/1867240/view/1825093633182385. Accessed 2026-10-08.
- [3] **Bulkhead** — *WARDOGS | Level Design & Performance* (Steam news, 16 Jul 2026). https://store.steampowered.com/news/app/1867240/view/1838407329256924. Accessed 2026-10-08.
- [4] **Bulkhead** — *WARDOGS - Official Announcement Trailer* (Steam news, 9 Feb 2026). https://store.steampowered.com/news/app/1867240/view/1823825466504264. Accessed 2026-10-08.
- [5] **Bulkhead** — *WARDOGS - Tactical Depth & Teamplay* (Steam news, 21 May 2026). https://store.steampowered.com/news/app/1867240/view/1833334318569240. Accessed 2026-10-08.
- [6] **Bulkhead** — *WARDOGS - Gameplay Trailer* (Steam news, 6 Jun 2026). https://store.steampowered.com/news/app/1867240/view/1834602721194537. Accessed 2026-10-08.
- [7] **Bulkhead** — *WARDOGS | Update 0.1.2 (Minor Patch)* (Steam news, 30 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1845383656376490. Accessed 2026-10-08.
- [8] **Bulkhead** — *WARDOGS | Season 02 Teaser* (Steam news, 22 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1844115010504839. Accessed 2026-10-08.
- [9] **Team17 / Bulkhead** — *WARDOGS is coming to Steam Early Access on 10 September* (press release). https://www.gamedeveloper.com/press-release/wardogs-is-coming-to-steam-early-access-on-10-september. Accessed 2026-10-08.

**Press & Secondary**

- [10] **Vice** — *WARDOGS Season 2 rain, progression wipe*. https://www.vice.com/en/article/wardogs-season-2-rain-progression-wipe/. Accessed 2026-10-08.
- [11] **KeenGamer** — *WARDOGS Season 2: confirmed features, rumors, changes*. https://www.keengamer.com/articles/guides/wardogs-season-2-confirmed-features-rumors-changes/. Accessed 2026-10-08.
- [12] **XGamingServer** — *WARDOGS roadmap* (unattributed; claims destructible terrain). https://xgamingserver.com/blog/?p=23236. Accessed 2026-10-08.

**Player-Reported Evidence**

- [13] **allthings.how** — *WARDOGS maps: every location and what each one fights over*. https://allthings.how/wardogs-maps-every-location-and-what-each-one-fights-over/. Accessed 2026-10-08.

# Further Reading

Steam News Hub for Season 02 details: https://store.steampowered.com/news/app/1867240

# Related Documents

- maps-environment-foundation
- launch-maps-reference
- fob-and-base-building
- system-requirements-and-performance

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft, pre-Season-02 baseline. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after independent re-verification of validate, markdownlint, links (0 dead) and Steam post ids. Pre-Season-02 baseline. | Standing mandate (auto-approve on green QA) |
