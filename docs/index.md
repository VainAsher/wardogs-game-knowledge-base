# WARDOGS Game Knowledge Base

!!! warning "Unofficial fan reference — verify against the current game version"
    This is an unofficial, source-cited reference produced by an automated pipeline. WARDOGS is in Steam Early Access, so facts change between patches: every document states the game version it was verified against. Not affiliated with Bulkhead or Team17.

Evidence-based, source-cited reference for WARDOGS (Bulkhead / Team17) - gameplay, combat, vehicles, economy, maps and server administration.

**13 documents** across **13 topics** — every factual claim carries a citation to a vendor or authoritative source, assessed gaps are labelled and confidence-rated, and links, citations and structure are checked automatically in CI.

*Confidence: 0 High · 9 Medium · 4 Low.*  *Market: Global 13.*

## Class 1 — Category foundations

- [Combat & Loadouts: Foundation](combat-loadouts/combat-loadouts-foundation.md) — *Weapons, gadgets, classes, damage and ballistics* (Global)
- [Economy: Foundation](economy/economy-foundation.md) — *Account balance, costs, rewards, death penalty* (Global)
- [Gameplay & Modes: Foundation](gameplay-modes/gameplay-modes-foundation.md) — *Match structure, objectives, three-team model, progression* (Global)
- [Maps & Environment: Foundation](maps-environment/maps-environment-foundation.md) — *Map list, destructibility, points of interest* (Global)
- [Meta & Release: Foundation](meta-release/meta-release-foundation.md) — *Early Access roadmap, patch history, platforms and pricing, community* (Global)
- [Technical & Servers: Foundation](technical-servers/technical-servers-foundation.md) — *System requirements, settings, netcode, dedicated and community servers, modding* (Global)
- [Vehicles & Outposts: Foundation](vehicles-outposts/vehicles-outposts-foundation.md) — *Vehicle roster, purchasing, outpost construction, destruction* (Global)

## Class 2 — Depth documents

- [Launch Maps Reference](maps-environment/launch-maps-reference.md) — *Per-map profiles: Bakurani, Ozeti, Zestafona and unconfirmed maps* (Global)
- [Editions, Pricing & Platforms](meta-release/editions-pricing-platforms.md) — *Editions, regional pricing, Supporter Pack contents, platform roadmap, Early Access policy* (Global)
- [Patch & Update History](meta-release/patch-history.md) — *Dated per-patch changelog from closed beta through 0.1.2 and hotfixes* (Global)
- [RCON & Server Administration](technical-servers/rcon-and-server-admin.md) — *RCON interface, ServerSettings, admin tooling, security hardening* (Global)
- [Server Hosting & Server Browser](technical-servers/server-hosting-and-browser.md) — *Official vs community servers, approved hosts, regions, browser behaviour, restarts* (Global)
- [System Requirements, Performance & Crashes](technical-servers/system-requirements-and-performance.md) — *Hardware requirements, Linux/Proton, anti-cheat, crash codes, performance fixes* (Global)

## Knowledge graph

??? note "Cross-reference graph (click to expand)"

    ```mermaid
    graph LR
      subgraph Tier1["Tier 1"]
        combat_loadouts_foundation["combat-loadouts-foundation"]
        economy_foundation["economy-foundation"]
        gameplay_modes_foundation["gameplay-modes-foundation"]
        maps_environment_foundation["maps-environment-foundation"]
        meta_release_foundation["meta-release-foundation"]
        technical_servers_foundation["technical-servers-foundation"]
        vehicles_outposts_foundation["vehicles-outposts-foundation"]
      end
      subgraph Tier2["Tier 2"]
        editions_pricing_platforms["editions-pricing-platforms"]
        launch_maps_reference["launch-maps-reference"]
        patch_history["patch-history"]
        rcon_and_server_admin["rcon-and-server-admin"]
        server_hosting_and_browser["server-hosting-and-browser"]
        system_requirements_and_performance["system-requirements-and-performance"]
      end
      gameplay_modes_foundation -->|related| combat_loadouts_foundation
      gameplay_modes_foundation -->|related| economy_foundation
      combat_loadouts_foundation -->|related| economy_foundation
      gameplay_modes_foundation -->|related| maps_environment_foundation
      gameplay_modes_foundation -->|related| meta_release_foundation
      combat_loadouts_foundation -->|related| vehicles_outposts_foundation
      economy_foundation -->|related| vehicles_outposts_foundation
      economy_foundation -->|related| meta_release_foundation
      vehicles_outposts_foundation -->|related| gameplay_modes_foundation
      vehicles_outposts_foundation -->|related| combat_loadouts_foundation
      vehicles_outposts_foundation -->|related| economy_foundation
      vehicles_outposts_foundation -->|related| maps_environment_foundation
      maps_environment_foundation -->|related| gameplay_modes_foundation
      maps_environment_foundation -->|related| vehicles_outposts_foundation
      maps_environment_foundation -->|related| technical_servers_foundation
      maps_environment_foundation -->|related| meta_release_foundation
      technical_servers_foundation -->|related| gameplay_modes_foundation
      technical_servers_foundation -->|related| maps_environment_foundation
      technical_servers_foundation -->|related| meta_release_foundation
      meta_release_foundation -->|related| gameplay_modes_foundation
      meta_release_foundation -->|related| economy_foundation
      meta_release_foundation -->|related| technical_servers_foundation
      meta_release_foundation -->|related| maps_environment_foundation
      server_hosting_and_browser -->|related| technical_servers_foundation
      server_hosting_and_browser -->|related| rcon_and_server_admin
      server_hosting_and_browser -->|related| meta_release_foundation
      rcon_and_server_admin -->|related| technical_servers_foundation
      rcon_and_server_admin -->|related| server_hosting_and_browser
      rcon_and_server_admin -->|related| system_requirements_and_performance
      system_requirements_and_performance -->|related| technical_servers_foundation
      system_requirements_and_performance -->|related| rcon_and_server_admin
      system_requirements_and_performance -->|related| meta_release_foundation
      patch_history -->|related| meta_release_foundation
      patch_history -->|related| technical_servers_foundation
      patch_history -->|related| economy_foundation
      patch_history -->|related| editions_pricing_platforms
      editions_pricing_platforms -->|related| meta_release_foundation
      editions_pricing_platforms -->|related| economy_foundation
      editions_pricing_platforms -->|related| patch_history
      editions_pricing_platforms -->|related| system_requirements_and_performance
      launch_maps_reference -->|related| maps_environment_foundation
      launch_maps_reference -->|related| gameplay_modes_foundation
      launch_maps_reference -->|related| vehicles_outposts_foundation
      combat_loadouts_foundation -->|related| gameplay_modes_foundation
      economy_foundation -->|related| gameplay_modes_foundation
      economy_foundation -->|related| combat_loadouts_foundation
    ```

## Machine-readable exports

Generated artefacts live in the repository's `exports/` directory: a knowledge graph (JSON + Mermaid), a capability/gap matrix (CSV/JSON), a coverage report, and a section-level RAG export (`exports/rag/`).

*Site generated by `scripts/build_site.py` — do not edit by hand.*

