# WARDOGS Game Knowledge Base

!!! warning "Unofficial fan reference — verify against the current game version"
    This is an unofficial, source-cited reference produced by an automated pipeline. WARDOGS is in Steam Early Access, so facts change between patches: every document states the game version it was verified against. Not affiliated with Bulkhead or Team17.

Evidence-based, source-cited reference for WARDOGS (Bulkhead / Team17) - gameplay, combat, vehicles, economy, maps and server administration.

**30 documents** across **30 topics** — every factual claim carries a citation to a vendor or authoritative source, assessed gaps are labelled and confidence-rated, and links, citations and structure are checked automatically in CI.

*Confidence: 4 High · 22 Medium · 4 Low.*  *Market: Global 30.*

## Class 1 — Category foundations

- [Combat & Loadouts: Foundation](combat-loadouts/combat-loadouts-foundation.md) — *Weapons, gadgets, classes, damage and ballistics* (Global)
- [Economy: Foundation](economy/economy-foundation.md) — *Account balance, costs, rewards, death penalty* (Global)
- [Gameplay & Modes: Foundation](gameplay-modes/gameplay-modes-foundation.md) — *Match structure, objectives, three-team model, progression* (Global)
- [Maps & Environment: Foundation](maps-environment/maps-environment-foundation.md) — *Map list, destructibility, points of interest* (Global)
- [Meta & Release: Foundation](meta-release/meta-release-foundation.md) — *Early Access roadmap, patch history, platforms and pricing, community* (Global)
- [Technical & Servers: Foundation](technical-servers/technical-servers-foundation.md) — *System requirements, settings, netcode, dedicated and community servers, modding* (Global)
- [Vehicles & Outposts: Foundation](vehicles-outposts/vehicles-outposts-foundation.md) — *Vehicle roster, purchasing, outpost construction, destruction* (Global)

## Class 2 — Depth documents

- [Damage, Ballistics & Balance Changes](combat-loadouts/damage-ballistics-and-balance.md) — *Damage model, ballistics, hit registration, and the balance-change history* (Global)
- [Cash Rewards & Costs](economy/cash-rewards-and-costs.md) — *How cash is earned and lost per action, and exploit fixes* (Global)
- [Death Penalty, Loadout Loss & Re-buy](economy/death-penalty-and-rebuy.md) — *What dying costs, loadout loss, re-buy, insurance-like mechanics, negative balances* (Global)
- [Seasons, Resets & Currencies](economy/season-reset-and-currencies.md) — *Season structure, what resets, Gold Bars, what persists, cosmetics* (Global)
- [Control Zone & Match Flow](gameplay-modes/control-zone-and-match-flow.md) — *Match lifecycle, Control Zone and Hot Zone scoring, win conditions, spawning, team balance* (Global)
- [Progression & Role Tracks](gameplay-modes/progression-and-role-tracks.md) — *XP curves, role tracks, WARDOG level, season resets* (Global)
- [Destructibility & Level Design](maps-environment/destructibility-and-level-design.md) — *Destruction model, level design philosophy, map scale, performance trade-offs, weather* (Global)
- [Launch Maps Reference](maps-environment/launch-maps-reference.md) — *Per-map profiles: Bakurani, Ozeti, Zestafona and unconfirmed maps* (Global)
- [Community Channels & Source Reliability Register](meta-release/community-and-source-reliability.md) — *Official channels, community hubs, and a reliability rating for every source class and outlet used* (Global)
- [Editions, Pricing & Platforms](meta-release/editions-pricing-platforms.md) — *Editions, regional pricing, Supporter Pack contents, platform roadmap, Early Access policy* (Global)
- [Patch & Update History](meta-release/patch-history.md) — *Dated per-patch changelog from closed beta through 0.1.2 and hotfixes, rebuilt from official Steam posts* (Global)
- [Season 02: Pre-Release Claims Scored Against Update 0.2.0](meta-release/season-2-announcements.md) — *Everything officially and unofficially said about Season 02 and the 1.0 roadmap before launch* (Global)
- [Windows Client Install Inspection (Update 0.2.0)](technical-servers/client-install-inspection.md) — *Installed client: build id, executables, packaging, third-party components, size* (Global)
- [RCON & Server Administration](technical-servers/rcon-and-server-admin.md) — *RCON interface, ServerSettings, admin tooling, security hardening* (Global)
- [Server Hosting & Server Browser](technical-servers/server-hosting-and-browser.md) — *Official vs community servers, approved hosts, regions, browser behaviour, restarts* (Global)
- [System Requirements, Performance & Crashes](technical-servers/system-requirements-and-performance.md) — *Hardware requirements, Linux/Proton, anti-cheat, crash codes, performance fixes* (Global)
- [Air Vehicles & Counter-Air](vehicles-outposts/air-and-counter-air.md) — *Helicopters, aircraft, anti-air systems (CIWS/Sea Whiz, Havoc), pilots, IR countermeasures* (Global)
- [FOBs, Hammers & Base Building](vehicles-outposts/fob-and-base-building.md) — *FOB deployment, supply types, hammer tiers, structures, pallet logistics, costs* (Global)

## Class 3 — Reference data & tables

- [Gadgets, Armor & Equipment](combat-loadouts/gadgets-armor-and-equipment.md) — *Gadgets, armor, backpacks, ammo types, sidearms, optics and IR gear* (Global)
- [Weapons Catalogue](combat-loadouts/weapons-catalogue.md) — *Firearms and launchers: roster, prices, unlock levels, attachments* (Global)
- [Season 1 Price Tables](economy/price-tables-season-1.md) — *Complete in-game price list as of Season 1 plus later patch changes* (Global)
- [Progression Unlock Tables (Season 1 and Season 02)](gameplay-modes/progression-unlock-tables.md) — *Level-by-level unlocks per role and account* (Global)
- [Vehicle Roster & Prices](vehicles-outposts/vehicle-roster-and-prices.md) — *Land and air vehicles: roster, price, unlock level, crew, role* (Global)

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
        air_and_counter_air["air-and-counter-air"]
        cash_rewards_and_costs["cash-rewards-and-costs"]
        client_install_inspection["client-install-inspection"]
        community_and_source_reliability["community-and-source-reliability"]
        control_zone_and_match_flow["control-zone-and-match-flow"]
        damage_ballistics_and_balance["damage-ballistics-and-balance"]
        death_penalty_and_rebuy["death-penalty-and-rebuy"]
        destructibility_and_level_design["destructibility-and-level-design"]
        editions_pricing_platforms["editions-pricing-platforms"]
        fob_and_base_building["fob-and-base-building"]
        launch_maps_reference["launch-maps-reference"]
        patch_history["patch-history"]
        progression_and_role_tracks["progression-and-role-tracks"]
        rcon_and_server_admin["rcon-and-server-admin"]
        season_2_announcements["season-2-announcements"]
        season_reset_and_currencies["season-reset-and-currencies"]
        server_hosting_and_browser["server-hosting-and-browser"]
        system_requirements_and_performance["system-requirements-and-performance"]
      end
      subgraph Tier3["Tier 3"]
        gadgets_armor_and_equipment["gadgets-armor-and-equipment"]
        price_tables_season_1["price-tables-season-1"]
        progression_unlock_tables["progression-unlock-tables"]
        vehicle_roster_and_prices["vehicle-roster-and-prices"]
        weapons_catalogue["weapons-catalogue"]
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
      control_zone_and_match_flow -->|related| gameplay_modes_foundation
      control_zone_and_match_flow -->|related| progression_and_role_tracks
      control_zone_and_match_flow -->|related| maps_environment_foundation
      control_zone_and_match_flow -->|related| launch_maps_reference
      control_zone_and_match_flow -->|related| cash_rewards_and_costs
      progression_and_role_tracks -->|related| gameplay_modes_foundation
      progression_and_role_tracks -->|related| progression_unlock_tables
      progression_and_role_tracks -->|related| season_reset_and_currencies
      progression_and_role_tracks -->|related| combat_loadouts_foundation
      progression_and_role_tracks -->|related| economy_foundation
      progression_unlock_tables -->|related| progression_and_role_tracks
      progression_unlock_tables -->|related| weapons_catalogue
      progression_unlock_tables -->|related| vehicle_roster_and_prices
      progression_unlock_tables -->|related| gadgets_armor_and_equipment
      weapons_catalogue -->|related| combat_loadouts_foundation
      weapons_catalogue -->|related| gadgets_armor_and_equipment
      weapons_catalogue -->|related| damage_ballistics_and_balance
      weapons_catalogue -->|related| progression_unlock_tables
      weapons_catalogue -->|related| price_tables_season_1
      gadgets_armor_and_equipment -->|related| combat_loadouts_foundation
      gadgets_armor_and_equipment -->|related| weapons_catalogue
      gadgets_armor_and_equipment -->|related| damage_ballistics_and_balance
      gadgets_armor_and_equipment -->|related| progression_unlock_tables
      gadgets_armor_and_equipment -->|related| price_tables_season_1
      damage_ballistics_and_balance -->|related| combat_loadouts_foundation
      damage_ballistics_and_balance -->|related| weapons_catalogue
      damage_ballistics_and_balance -->|related| gadgets_armor_and_equipment
      damage_ballistics_and_balance -->|related| patch_history
      cash_rewards_and_costs -->|related| economy_foundation
      cash_rewards_and_costs -->|related| death_penalty_and_rebuy
      cash_rewards_and_costs -->|related| price_tables_season_1
      cash_rewards_and_costs -->|related| season_reset_and_currencies
      cash_rewards_and_costs -->|related| control_zone_and_match_flow
      price_tables_season_1 -->|related| economy_foundation
      price_tables_season_1 -->|related| weapons_catalogue
      price_tables_season_1 -->|related| gadgets_armor_and_equipment
      price_tables_season_1 -->|related| vehicle_roster_and_prices
      price_tables_season_1 -->|related| cash_rewards_and_costs
      death_penalty_and_rebuy -->|related| economy_foundation
      death_penalty_and_rebuy -->|related| cash_rewards_and_costs
      death_penalty_and_rebuy -->|related| price_tables_season_1
      death_penalty_and_rebuy -->|related| combat_loadouts_foundation
      season_reset_and_currencies -->|related| economy_foundation
      season_reset_and_currencies -->|related| progression_and_role_tracks
      season_reset_and_currencies -->|related| season_2_announcements
      season_reset_and_currencies -->|related| patch_history
      vehicle_roster_and_prices -->|related| vehicles_outposts_foundation
      vehicle_roster_and_prices -->|related| air_and_counter_air
      vehicle_roster_and_prices -->|related| fob_and_base_building
      vehicle_roster_and_prices -->|related| price_tables_season_1
      vehicle_roster_and_prices -->|related| progression_unlock_tables
      fob_and_base_building -->|related| vehicles_outposts_foundation
      fob_and_base_building -->|related| vehicle_roster_and_prices
      fob_and_base_building -->|related| air_and_counter_air
      fob_and_base_building -->|related| cash_rewards_and_costs
      fob_and_base_building -->|related| maps_environment_foundation
      air_and_counter_air -->|related| vehicles_outposts_foundation
      air_and_counter_air -->|related| vehicle_roster_and_prices
      air_and_counter_air -->|related| fob_and_base_building
      air_and_counter_air -->|related| gadgets_armor_and_equipment
      air_and_counter_air -->|related| damage_ballistics_and_balance
      destructibility_and_level_design -->|related| maps_environment_foundation
      destructibility_and_level_design -->|related| launch_maps_reference
      destructibility_and_level_design -->|related| fob_and_base_building
      destructibility_and_level_design -->|related| system_requirements_and_performance
      season_2_announcements -->|related| meta_release_foundation
      season_2_announcements -->|related| season_reset_and_currencies
      season_2_announcements -->|related| patch_history
      season_2_announcements -->|related| progression_and_role_tracks
      season_2_announcements -->|related| destructibility_and_level_design
      community_and_source_reliability -->|related| meta_release_foundation
      community_and_source_reliability -->|related| patch_history
      community_and_source_reliability -->|related| editions_pricing_platforms
      combat_loadouts_foundation -->|related| gameplay_modes_foundation
      combat_loadouts_foundation -->|related| weapons_catalogue
      combat_loadouts_foundation -->|related| gadgets_armor_and_equipment
      combat_loadouts_foundation -->|related| damage_ballistics_and_balance
      combat_loadouts_foundation -->|related| price_tables_season_1
      combat_loadouts_foundation -->|related| progression_unlock_tables
      combat_loadouts_foundation -->|related| patch_history
      economy_foundation -->|related| gameplay_modes_foundation
      economy_foundation -->|related| combat_loadouts_foundation
      economy_foundation -->|related| cash_rewards_and_costs
      economy_foundation -->|related| price_tables_season_1
      economy_foundation -->|related| death_penalty_and_rebuy
      economy_foundation -->|related| season_reset_and_currencies
      economy_foundation -->|related| editions_pricing_platforms
      gameplay_modes_foundation -->|related| control_zone_and_match_flow
      gameplay_modes_foundation -->|related| progression_and_role_tracks
      gameplay_modes_foundation -->|related| progression_unlock_tables
      gameplay_modes_foundation -->|related| season_reset_and_currencies
      gameplay_modes_foundation -->|related| season_2_announcements
      gameplay_modes_foundation -->|related| community_and_source_reliability
      gameplay_modes_foundation -->|related| patch_history
      launch_maps_reference -->|related| destructibility_and_level_design
      launch_maps_reference -->|related| control_zone_and_match_flow
      maps_environment_foundation -->|related| destructibility_and_level_design
      maps_environment_foundation -->|related| launch_maps_reference
      maps_environment_foundation -->|related| control_zone_and_match_flow
      maps_environment_foundation -->|related| season_2_announcements
      meta_release_foundation -->|related| patch_history
      meta_release_foundation -->|related| editions_pricing_platforms
      meta_release_foundation -->|related| season_2_announcements
      meta_release_foundation -->|related| community_and_source_reliability
      meta_release_foundation -->|related| season_reset_and_currencies
      technical_servers_foundation -->|related| server_hosting_and_browser
      technical_servers_foundation -->|related| rcon_and_server_admin
      technical_servers_foundation -->|related| system_requirements_and_performance
      technical_servers_foundation -->|related| patch_history
      technical_servers_foundation -->|related| community_and_source_reliability
      vehicles_outposts_foundation -->|related| vehicle_roster_and_prices
      vehicles_outposts_foundation -->|related| fob_and_base_building
      vehicles_outposts_foundation -->|related| air_and_counter_air
      vehicles_outposts_foundation -->|related| price_tables_season_1
      vehicles_outposts_foundation -->|related| progression_unlock_tables
      vehicles_outposts_foundation -->|related| destructibility_and_level_design
      vehicles_outposts_foundation -->|related| patch_history
      client_install_inspection -->|related| technical_servers_foundation
      client_install_inspection -->|related| system_requirements_and_performance
      client_install_inspection -->|related| patch_history
      client_install_inspection -->|related| server_hosting_and_browser
      vehicles_outposts_foundation -->|related| cash_rewards_and_costs
      technical_servers_foundation -->|related| client_install_inspection
      system_requirements_and_performance -->|related| client_install_inspection
      control_zone_and_match_flow -->|related| server_hosting_and_browser
      control_zone_and_match_flow -->|related| price_tables_season_1
      progression_unlock_tables -->|related| cash_rewards_and_costs
      progression_unlock_tables -->|related| price_tables_season_1
      cash_rewards_and_costs -->|related| fob_and_base_building
      cash_rewards_and_costs -->|related| progression_unlock_tables
      price_tables_season_1 -->|related| progression_unlock_tables
      death_penalty_and_rebuy -->|related| season_reset_and_currencies
      season_reset_and_currencies -->|related| price_tables_season_1
      season_reset_and_currencies -->|related| cash_rewards_and_costs
      season_reset_and_currencies -->|related| progression_unlock_tables
      vehicle_roster_and_prices -->|related| cash_rewards_and_costs
      air_and_counter_air -->|related| progression_unlock_tables
      air_and_counter_air -->|related| cash_rewards_and_costs
      season_2_announcements -->|related| community_and_source_reliability
      community_and_source_reliability -->|related| season_2_announcements
    ```

## Machine-readable exports

Generated artefacts live in the repository's `exports/` directory: a knowledge graph (JSON + Mermaid), a capability/gap matrix (CSV/JSON), a coverage report, and a section-level RAG export (`exports/rag/`).

*Site generated by `scripts/build_site.py` — do not edit by hand.*

