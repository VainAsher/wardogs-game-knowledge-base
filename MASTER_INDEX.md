# WARDOGS Knowledge Base — Master Index

Catalogue of every document. Generated site and exports read the table below.

## Documents

| ID | Title | Topic | Tier | Market | Version | Status | Confidence | Path |
|----|-------|-------|------|--------|---------|--------|------------|------|
| gameplay-modes-foundation | Gameplay & Modes: Foundation | Match structure, objectives, three-team model, progression | 1 | Global | 1.0.0 | frozen | Medium | `docs/gameplay-modes/gameplay-modes-foundation.md` |
| combat-loadouts-foundation | Combat & Loadouts: Foundation | Weapons, gadgets, classes, damage and ballistics | 1 | Global | 1.0.0 | frozen | Medium | `docs/combat-loadouts/combat-loadouts-foundation.md` |
| economy-foundation | Economy: Foundation | Account balance, costs, rewards, death penalty | 1 | Global | 1.0.0 | frozen | Medium | `docs/economy/economy-foundation.md` |
| vehicles-outposts-foundation | Vehicles & Outposts: Foundation | Vehicle roster, purchasing, outpost construction, destruction | 1 | Global | 1.0.0 | frozen | Medium | `docs/vehicles-outposts/vehicles-outposts-foundation.md` |
| maps-environment-foundation | Maps & Environment: Foundation | Map list, destructibility, points of interest | 1 | Global | 1.0.0 | frozen | Low | `docs/maps-environment/maps-environment-foundation.md` |
| technical-servers-foundation | Technical & Servers: Foundation | System requirements, settings, netcode, dedicated and community servers, modding | 1 | Global | 1.0.0 | frozen | Medium | `docs/technical-servers/technical-servers-foundation.md` |
| meta-release-foundation | Meta & Release: Foundation | Early Access roadmap, patch history, platforms and pricing, community | 1 | Global | 1.0.0 | frozen | Medium | `docs/meta-release/meta-release-foundation.md` |

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
