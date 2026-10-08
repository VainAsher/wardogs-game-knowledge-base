# WARDOGS Knowledge Base — Master Index

Catalogue of every document. Generated site and exports read the table below.

## Documents

| ID | Title | Topic | Tier | Market | Version | Status | Confidence | Path |
|----|-------|-------|------|--------|---------|--------|------------|------|
| gameplay-modes-foundation | Gameplay & Modes: Foundation | Match structure, objectives, three-team model, progression | 1 | Global | 1.0.0 | frozen | Medium | `docs/gameplay-modes/gameplay-modes-foundation.md` |
| combat-loadouts-foundation | Combat & Loadouts: Foundation | Weapons, gadgets, classes, damage and ballistics | 1 | Global | 1.0.0 | frozen | Medium | `docs/combat-loadouts/combat-loadouts-foundation.md` |
| economy-foundation | Economy: Foundation | Account balance, costs, rewards, death penalty | 1 | Global | 1.0.1 | frozen | Medium | `docs/economy/economy-foundation.md` |
| vehicles-outposts-foundation | Vehicles & Outposts: Foundation | Vehicle roster, purchasing, outpost construction, destruction | 1 | Global | 1.0.0 | frozen | Medium | `docs/vehicles-outposts/vehicles-outposts-foundation.md` |
| maps-environment-foundation | Maps & Environment: Foundation | Map list, destructibility, points of interest | 1 | Global | 1.0.0 | frozen | Low | `docs/maps-environment/maps-environment-foundation.md` |
| technical-servers-foundation | Technical & Servers: Foundation | System requirements, settings, netcode, dedicated and community servers, modding | 1 | Global | 1.0.0 | frozen | Medium | `docs/technical-servers/technical-servers-foundation.md` |
| meta-release-foundation | Meta & Release: Foundation | Early Access roadmap, patch history, platforms and pricing, community | 1 | Global | 1.0.0 | frozen | Medium | `docs/meta-release/meta-release-foundation.md` |
| server-hosting-and-browser | Server Hosting & Server Browser | Official vs community servers, approved hosts, regions, browser behaviour, restarts | 2 | Global | 1.0.0 | frozen | Low | `docs/technical-servers/server-hosting-and-browser.md` |
| rcon-and-server-admin | RCON & Server Administration | RCON interface, ServerSettings, admin tooling, security hardening | 2 | Global | 1.0.0 | frozen | Low | `docs/technical-servers/rcon-and-server-admin.md` |
| system-requirements-and-performance | System Requirements, Performance & Crashes | Hardware requirements, Linux/Proton, anti-cheat, crash codes, performance fixes | 2 | Global | 1.0.0 | frozen | Medium | `docs/technical-servers/system-requirements-and-performance.md` |
| patch-history | Patch & Update History | Dated per-patch changelog from closed beta through 0.1.2 and hotfixes | 2 | Global | 1.0.0 | frozen | Medium | `docs/meta-release/patch-history.md` |
| editions-pricing-platforms | Editions, Pricing & Platforms | Editions, regional pricing, Supporter Pack contents, platform roadmap, Early Access policy | 2 | Global | 1.0.0 | frozen | Medium | `docs/meta-release/editions-pricing-platforms.md` |
| launch-maps-reference | Launch Maps Reference | Per-map profiles: Bakurani, Ozeti, Zestafona and unconfirmed maps | 2 | Global | 1.0.0 | frozen | Low | `docs/maps-environment/launch-maps-reference.md` |

## Proposed taxonomy (approved 2026-10-08)

Tier 1 = one foundation doc per category; Tier 2 = depth docs; Tier 3 = reference data; Tier 4 = meta.

| Category | Foundation doc id (planned) | Depth topics (planned) |
|----------|-----------------------------|------------------------|
| Gameplay & Modes | gameplay-modes-foundation | match flow, objectives, three-team dynamics, progression, local voice chat |
| Combat & Loadouts | combat-loadouts-foundation | weapons, gadgets, classes, damage and ballistics |
| Vehicles & Outposts | vehicles-outposts-foundation | vehicle roster, purchasing, outpost construction, destruction |
| Economy | economy-foundation | account balance, costs, rewards, death penalty |
| Maps & Environment | maps-environment-foundation | map list, destructibility, points of interest |
| Technical & Servers | technical-servers-foundation | system requirements, settings, netcode, dedicated and community servers, modding |
| Meta & Release | meta-release-foundation | Early Access roadmap, patch history, platforms and pricing, community |

First cluster: Gameplay & Modes, Combat & Loadouts, Economy.

## Knowledge graph

- `gameplay-modes-foundation` related to `combat-loadouts-foundation`, `economy-foundation`
- `combat-loadouts-foundation` related to `economy-foundation`
- `gameplay-modes-foundation` related to `maps-environment-foundation`
- `gameplay-modes-foundation` related to `meta-release-foundation`
- `combat-loadouts-foundation` related to `vehicles-outposts-foundation`
- `economy-foundation` related to `vehicles-outposts-foundation`
- `economy-foundation` related to `meta-release-foundation`
- `vehicles-outposts-foundation` related to `gameplay-modes-foundation`, `combat-loadouts-foundation`, `economy-foundation`, `maps-environment-foundation`
- `maps-environment-foundation` related to `gameplay-modes-foundation`, `vehicles-outposts-foundation`, `technical-servers-foundation`, `meta-release-foundation`
- `technical-servers-foundation` related to `gameplay-modes-foundation`, `maps-environment-foundation`, `meta-release-foundation`
- `meta-release-foundation` related to `gameplay-modes-foundation`, `economy-foundation`, `technical-servers-foundation`, `maps-environment-foundation`
- `server-hosting-and-browser` deepens `technical-servers-foundation`
- `server-hosting-and-browser` related to `rcon-and-server-admin`, `meta-release-foundation`
- `rcon-and-server-admin` deepens `technical-servers-foundation`
- `rcon-and-server-admin` related to `server-hosting-and-browser`, `system-requirements-and-performance`
- `system-requirements-and-performance` deepens `technical-servers-foundation`
- `system-requirements-and-performance` related to `rcon-and-server-admin`, `meta-release-foundation`
- `patch-history` deepens `meta-release-foundation`
- `patch-history` related to `technical-servers-foundation`, `economy-foundation`, `editions-pricing-platforms`
- `editions-pricing-platforms` deepens `meta-release-foundation`, `economy-foundation`
- `editions-pricing-platforms` related to `patch-history`, `system-requirements-and-performance`
- `launch-maps-reference` deepens `maps-environment-foundation`
- `launch-maps-reference` related to `gameplay-modes-foundation`, `vehicles-outposts-foundation`
