---
id: gameplay-modes-foundation
title: "Gameplay & Modes: Foundation"
version: 1.2.0
status: frozen
confidence: High
category: Gameplay & Modes
topic: "Match structure, objectives, three-team model, progression"
market: Global
game_version: "Early Access Season 02, Update 0.2.0 (15 Oct 2026); official posts through 2026-10-15 (snapshot 2026-10-30)"
document_type: foundation
created: 2026-10-08
updated: 2026-10-30
review_due: 2026-11-20
sources_verified: 2026-10-30
supersedes: null
related:
  - combat-loadouts-foundation
  - economy-foundation
  - maps-environment-foundation
  - meta-release-foundation
  - control-zone-and-match-flow
  - progression-and-role-tracks
  - progression-unlock-tables
  - season-reset-and-currencies
  - season-2-announcements
  - community-and-source-reliability
  - patch-history
tags:
  - gameplay
  - modes
  - control-zone
  - progression
  - three-team
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | gameplay-modes-foundation |
| Version | 1.2.0 |
| Status | frozen |
| Confidence | High |
| Category | Gameplay & Modes |
| Game version | Early Access Season 02, Update 0.2.0 (15 Oct 2026); official posts through 2026-10-15 (snapshot 2026-10-30) |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-30 |
| Review due | 2026-11-20 |

# Executive Summary

WARDOGS is a 100-player, three-team tactical shooter in Steam Early Access since 10 September 2026 [1][2]. Its core mode is the Control Zone: three teams contest a randomised 2x2 km zone inside a 256 km2 map, the team with the most players inside earns points, and the first to 100 points wins [1][2]. A shifting Hot Zone inside it counts each player double and pays double cash [1][2]. Proximity voice chat is listed in the Early Access state and local voice chat in the game description, both on the store page [1][2].

Progression is cash-based, with cash persisting from match to match and exchangeable for Gold Bars, plus XP across six role tracks (Career, Medic, Recon, Support, Driver, Pilot) that gate unlocks [2][3]. The developer states that each season gets a different XP curve and item order [3]. Season 02 (Update 0.2.0) went live on 15 October 2026 [20]. The 14 Oct patch notes add team-switching restrictions, a victim-driven Forgive/Punish team-kill vote, a Squad Intent UI, server seeding rewards with pre-match entertainment, a rain weather preset, new weapons, vehicles and buildables, a Lonestar faction experiment, and a Wager Vendor that is not open at launch [18]. The notes do not mention a progression wipe.

Confidence is High for the core claims, which rest on the live store page (live capture 2026-10-08), the Top Questions post, the Season 1 changelog, the 0.11 and 0.1.2 posts, the two 2 Oct posts and the Season 02 patch notes [18]. Level caps, scoring tick, tower mechanics and any Season 02 wipe are not in official text and are kept as player-reported or press-reported. No official post after 2026-10-15 is in the 2026-10-30 snapshot; hotfixes after that date are neither confirmed nor ruled out.

# Key Takeaways

- Format: up to 100 players in three teams (Lonestar, Valkyra, Manticore) on a 256 km2 map; Early Access launched with three maps, each with three variations [1][2][12].
- Objective: a randomised 2x2 km Control Zone; the team with the most players inside earns points; first to 100 wins [1][2].
- Hot Zone: a shifting sub-zone where players count as double and cash is doubled [1][2].
- Voice: the store page uses both phrases, "Online multiplayer with proximity voice chat" in its Early Access state list and "local voice chat" in About This Game, and the developer FAQ says proximity chat [1][2]; the claim that it carries across all three teams rests on the Team17 press release [12].
- Progression: cash persists between matches and can be exchanged for Gold Bars [2]; XP accrues across six role tracks named Career, Medic, Recon, Support, Driver and Pilot [3].
- Seasons: each season has its own XP curve and item order [3]; Season 02 (Update 0.2.0) went live 15 Oct 2026 and the patch notes lower the XP needed per level (summary below; numbers owned by progression-and-role-tracks) [18][20]. The notes do not mention a wipe; a progression wipe is press-reported only [13].
- Update 0.2.0 match-flow changes (14 Oct 2026 notes): team-switch limits once a team is more than 10 points ahead, a Forgive/Punish vote on team kills, Squad Intent UI, server seeding rewards and pre-match entertainment, and a 20% vendor discount for a team at least 40 points behind second place [18]. Detail is in control-zone-and-match-flow.
- Modes: the Control Zone is still the only named core mode; Official servers run no modified modes, while Community servers can; since 0.1.2 a Deploy flow offers Official, Community, Infantry Mode and Low-Level servers [4][5].
- 1.0: no date; the store page plans around 1 to 2 years in Early Access, a higher full-release price and a broader feature set [1]; the 7 Apr 2026 post commits to building a metagame (Black Market and Vault, Player Skills and Challenge System) during Early Access [10].

# Scope

Covers match format, the three-team model, the Control Zone objective, voice chat, progression and unlocks, modes available at Early Access, and what is stated about 1.0. Game version verified: Season 02, Update 0.2.0 (official posts through 2026-10-15), with Season 01 (patch 0.1.2 and the 2 Oct 2026 hotfixes) kept as dated history. Excluded: weapon and loadout detail (see combat-loadouts-foundation), prices and economy detail (see economy-foundation), map detail (see maps-environment-foundation), release and business facts (see meta-release-foundation), and the depth documents listed under Related Documents.

# Definitions

- **Control Zone**: the randomised 2x2 km objective area in each match [1][2].
- **Hot Zone**: a shifting sub-zone of the Control Zone where players count as double towards the player count and cash is doubled [2].
- **Role track**: a per-role XP track; the official names are Career, Medic, Recon, Support, Driver and Pilot [2][3].
- **Gold Bars**: the endgame currency, bought by exchanging cash, used for cosmetic unlocks in the Gold Market [2].
- **Season**: a period with its own XP curve and item order [3].

See also `GLOSSARY.md`.

# Current State

Season 01 statements were verified 2026-10-08 and the 0.2.0 statements 2026-10-30, each against the sources shown.

- Early Access began 10 Sep 2026; the developer describes it as fully playable and representing the core vision [2]. Setting is the war-torn region of Kolchia [2]; the store page describes the derelict industrial mountains of Eastern Europe and a destructible battlefield, and calls the game a militaristic sandbox [1].
- Matches support up to 100 players split across three rival teams on a 256 km2 map; squad size is unlimited [2].
- Teams fight for a randomised 2x2 km Control Zone; the team with the most players in the zone earns points and the first to 100 wins [1][2].
- The Hot Zone counts players double and yields double cash [1][2].
- Every player starts with $10,000 and buys a loadout each life; teamplay actions such as reviving, transporting friendlies and controlling the objective earn cash; cash persists between matches [1].
- Cash can be exchanged for Gold Bars, used for cosmetics in the Gold Market; the developer says cash and Gold Bars will never be sold for real money [2][9].
- Voice: the store page says "Online multiplayer with proximity voice chat" in its Early Access state list and "local voice chat" in About This Game; the FAQ says proximity chat, including loudspeakers players can construct [1][2].
- Launch content is three maps, each with three variations, with infantry and vehicle combat [12].
- The Season 1 changelog (9 Sep 2026, pre-load) slowed the XP curve and moved unlocks; it also fixed voice dropping after a failed join, push-to-talk targeting and re-login recovery, and added a visible communication status [3].
- Patch 0.11 (14 Sep 2026) split the server browser into Official and Community lists, removed filters from the Official list, and gave Community servers a 5% end-of-match cash bonus for one week [4].
- Patch 0.1.2 (30 Sep 2026) made revive checks server authoritative, capped fly-through rewards, scaled buildable-destruction rewards by build progress, reduced rewards for FOB pallet deposits outside the zone, added the Deploy flow, and added Advanced Filters back to the Official list [5].
- 2 Oct 2026 brought two official posts: a security and stability hotfix at 08:00 UTC with no gameplay detail, and a balance hotfix disabling IR Rangefinders in the vendor until Season 02 (where they will need batteries) and cutting the CIWS kill time on the Havoc from about 12 s to about 6 s [6][7].
- Season 02 was dated 15 Oct 2026 by the official teaser of 22 Sep 2026 and released as Update 0.2.0 on 15 Oct 2026 (servers back online after a maintenance window announced for 08:00 to 09:30 UTC) [8][18][20]. The Season 01 statements above are the history baseline; the 0.2.0 facts follow.
- 0.2.0 (14 Oct 2026 notes): once a team is more than 10 points ahead, a player cannot switch teams again for 15 minutes after joining one, their map stays obscured until they first reach the Control Zone, and they cannot use the spawn vehicle until then [18].
- 0.2.0: team kills trigger a Forgive or Punish prompt for the victim; Punish marks accumulate towards kicks and escalating bans, Forgive removes a potential mark, and respawning then leaving the safe zone without voting forgives automatically [18].
- 0.2.0: squad leaders can set a team-visible squad intent from a pre-defined list, visible on the squad list before joining; squad invites and other timed prompts now queue [18].
- 0.2.0: players who join and populate empty servers earn rewards and a vendor discount once the match begins; pre-match entertainment (guns with targets, a football and a hidden radio in each spawn) is available before the match [18].
- 0.2.0: Lonestar faction experiment for Season 2 only, with Lonestar win bonuses and teamplay multipliers, and a new 20% vendor discount for any losing team at least 40 points behind second place; the notes do not state the bonus sizes [18].
- 0.2.0: Wager Vendor (bet your own cash on your own performance) is not available at launch; it will open later in Season 2 and is not a permanent addition [18][19].
- 0.2.0: the rain weather preset, four new weapons, four new vehicles and three new buildables are listed in the notes (owner documents hold the detail), and the assistance ping timer rose from 20 s to 60 s [18].
- 0.2.0: parachutes take longer to open and do not open below about 10 m; opening below roughly 50 m while falling fast causes fall damage; the Basic Parachute rose from $100 to $500 and the Sport Parachute fell from $1,000 to $700 (prices owned by price-tables-season-1) [18].
- 0.2.0: controller changes include an Aim Assist strength slider (Settings > Controller > Advanced; default 1, 0 turns it off), adjusted sensitivity and aim acceleration, and several rebinds; the full bind list is in the notes [18].

# Detail

## Match format and objectives

| Element | Fact at Season 01 | Source |
|---------|-------------------|--------|
| Players | Up to 100 | [1][2] |
| Teams | 3: Lonestar, Valkyra, Manticore | [2] |
| Map size | 256 km2 | [2] |
| Zone | Randomised 2x2 km Control Zone per match | [1][2] |
| Win condition | First team to 100 points | [1][2] |
| Scoring basis | Team with the most players in the zone earns points | [1][2] |
| Hot Zone | Shifting sub-zone; players count double; double cash | [1][2] |
| Squads | Unlimited size; extra UI, comms and vehicle locking | [2] |
| Maps | 3, each with 3 variations | [12] |

Player-reported mechanics (not stated in any official post): a tick of roughly one point every 30 seconds, three to five tower capture points inside the Control Zone, and a code from towers that lets a team drag the Hot Zone toward a held tower [16][17]. Treat these as player-reported. See control-zone-and-match-flow for the full baseline and the unpublished gaps (respawn, spawn rules, team balance).

## Cross-team voice chat

The store page uses both phrases: "Online multiplayer with proximity voice chat" in the Early Access state list and "local voice chat" in About This Game (live capture 2026-10-08); the developer FAQ also calls it proximity chat [1][2]. The two wordings describe the same feature and are not treated as a contradiction. Audibility across teams rests on the Team17 press release, which says it is audible across all three teams [12]. The Season 1 changelog lists fixes to voice cutting out after a failed join, stale channel rejoins, push-to-talk targeting and re-login, and a visible communication status [3].

## Progression and unlocks

| Element | Detail | Source |
|---------|--------|--------|
| Starting cash | $10,000 per player; a loadout is bought each life | [1] |
| Cash earning | Teamplay actions (revives, transport, kills, spotting, objective); Hot Zone doubles cash | [1][2] |
| Cash persistence | Persists match to match; exchangeable for Gold Bars | [2] |
| Role tracks | Six: Career, Medic, Recon, Support, Driver, Pilot (the 0.2.0 notes also use "Assault" and "WARDOG" track headings; see progression-and-role-tracks) | [2][3][18] |
| Track cap | Level 100 per track and account level to 600: player-reported only; no official cap | [15] |
| Unlock cost | Reaching a level makes an item buyable; the changelog moves items between levels and tracks | [3] |
| Per-season curve | "Each season we will have a different XP curve with different item orders" | [3] |
| Season reset | Not stated in official text, including the 0.2.0 notes, which do not mention a wipe; press reports cash and XP reset with leftover cash converted to Gold Bars | [13][18] |
| Season 02 XP curve | 0.2.0 notes lower total XP per level; they state level 20 now takes less than half the Season 1 playtime. Numbers: progression-and-role-tracks | [18] |

The official Season 1 changelog (history) slowed levels around 10 to 20 and flattened the curve from level 35: level 10 rose from 25,000 to 35,000 XP, level 15 from 54,750 to 110,000, level 20 from 111,500 to 250,000 and level 50 from 838,000 to 1,000,000; an air-vehicle player kill pays 250 XP, down from 300 [3]. The developer targets a median player at 20 to 25 hours being around level 20 [3]. The official name "Career" is used in the changelog; "Assault" is a player-guide name [3][15]. Economy abuse penalties (timed ban with cash and XP reset to 0; permanent ban for exploit tutorials and XP farming) are official from 0.11 and were reaffirmed in 0.1.2 [4][5]. The 14 Oct 2026 notes reverse that slowdown for Season 02; their own "before" figures for levels 10 to 20 match the Season 1 changelog figures quoted here, but give 1,500,000 rather than 1,000,000 as the old level 50 value, so the figures conflict at level 50 [3][18]. Full tables are in progression-and-role-tracks, progression-unlock-tables and season-reset-and-currencies.

## Modes available at Early Access

The only core mode named in official text is the Control Zone [1][2]; the 0.2.0 notes add no new mode, but a Wager Vendor feature is due later in Season 2 (below) [18]. Official servers do not run modified game modes, while Community servers can [4]. The 0.1.2 Deploy flow lets players choose Official, Community, Infantry Mode or Low-Level servers, described as a first step to signpost servers running these modifiers; the post does not define the rules of either modifier [5]. Assessment: a full catalogue of community-server modes is unavailable; confidence Low.

## Wager Vendor (not open at 0.2.0 launch)

The 14 Oct notes state the Wager Vendor is not available at Season 2 launch and will open later in Season 2; it lets a player bet their own cash on their own performance, with a live wager tracker above the minimap, and it is not a permanent addition but is meant to come and go through a season [18]. The 9 Oct preview describes it as experimental, with chosen objectives, a death budget and longer odds as objectives stack [19]. No opening date is given; none is seen in the 2026-10-30 snapshot.

## Planned for 1.0

The 7 Apr 2026 post says the Metagame (the frontend experience to keep earning and progressing outside a match) is designed and will be built throughout Early Access, including the Black Market and Vault and a Player Skills and Challenge System [10]. The store page (live capture 2026-10-08) plans to expand in several areas: more maps, weapons, vehicles and gameplay variety; more in-depth progression systems; a stronger seasonal meta game; new vehicle types including fighter jets; expanded weapon categories; and additional objective variations [1]. It expects Early Access to last around 1 to 2 years, with the duration liable to change, and plans to price the game lower during Early Access and higher at full release [1]. These are developer plans, not dated commitments. A third-party roadmap article adds new objective types and says no dated roadmap will be published, but does not say which items are official [14].

# Early Access Changes & Known Issues

| Date | Change | Source |
|------|--------|--------|
| 2026-09-09/10 | Season 1 changelog (pre-load) and launch: XP curve slowed, unlocks moved, voice fixes | [3] |
| 2026-09-14 | Patch 0.11: Official and Community server browsers, filters removed from Official, 5% community cash bonus for one week, economy-abuse policy | [4] |
| 2026-09-30 | Patch 0.1.2: revive checks, reward caps, Deploy flow, Advanced Filters back on Official | [5] |
| 2026-10-02 | Security and stability hotfix (no gameplay detail) | [6] |
| 2026-10-02 | Balance hotfix: IR Rangefinders disabled until Season 02; CIWS kill on Havoc about 12 s to about 6 s | [7] |
| 2026-10-09 | Season 02 Preview post | [19] |
| 2026-10-14 | Season 02 Patch Notes posted: team-switch limits, Forgive/Punish, Squad Intent UI, server seeding and pre-match entertainment, Lonestar experiment and losing-team discount, parachute and controller changes, Wager Vendor announced for later in Season 2, ping timer 20 s to 60 s | [18] |
| 2026-10-15 | Update 0.2.0 released, servers back online | [20] |
| after 2026-10-15 | No official post in the 2026-10-30 snapshot; later hotfixes neither confirmed nor excluded | [20] |

Announced but unreleased as of 0.11: community server favouriting, tiered priority queues, message of the day, improved warmup, disabling AFK kicking during seeding, team switching controls [4]. None was confirmed shipped in the 0.1.2 post [5]. In 0.2.0, team switching restrictions and server seeding rewards shipped [18]; the notes do not mention favouriting, priority queues, message of the day or AFK-kick changes.

# Admin & Technical Notes

Official servers have no modified modes; Community servers support text search and persistent server IDs (0.11) and, from 0.1.2, scheduled daily restarts (UTC), RCON AllowedHosts and capped RCON message lengths [4][5]. Three Approved Hosting Partners were named officially on 8 Sep 2026: QONZER, BisectHosting and xREALM [11]. See maps-environment-foundation, server-hosting-and-browser and rcon-and-server-admin for depth.

# Risks & Caveats

- Season 02 (0.2.0) is live, so Season 01 figures here are dated history and the 0.2.0 facts rest on a single official post, the patch notes [18]. A later hotfix would not appear here until the snapshot is refreshed.
- The 0.2.0 notes do not mention a progression wipe; that remains press-reported only [13]. Rain is now official [18].
- The hot-zone tick and tower mechanics, and the level cap, are player-reported [15][16][17].
- The 1.0 list, Early Access length and pricing plan are developer intentions on the store page, undated and liable to change [1].

# Open Questions

- Whether Season 02 wipes cash and XP, and the cash to Gold Bar rate: the 0.2.0 notes are silent; resolve from an official post or in-game observation.
- Size of the Lonestar win bonus and teamplay multipliers, the seeding reward and vendor discount, and when the Wager Vendor opens: not stated in the notes.
- Whether any official mode exists beyond the Control Zone, and what Infantry Mode and Low-Level servers change.
- Official level cap and the account-level formula.
- Whether the remaining 0.11 pipeline features (priority queues, favouriting, message of the day) have shipped; team switching restrictions did ship in 0.2.0 [18].
- Dated 1.0 plans; the third-party roadmap article [14] is not attributed.

# References

**Primary Sources**

- [1] **Valve / Bulkhead Studios** — *WARDOGS on Steam* (store page, live capture 2026-10-08, browser-rendered). https://store.steampowered.com/app/1867240/WARDOGS/. Accessed 2026-10-08.
- [2] **Bulkhead Studios** — *WARDOGS - TOP QUESTIONS* (Steam announcement, 18 Feb 2026). https://store.steampowered.com/news/app/1867240/view/1825093633182385. Accessed 2026-10-08.
- [3] **Bulkhead Studios** — *Pre-Load Live & Season 1 Changelog* (Steam announcement, 9 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1843481262690549. Accessed 2026-10-08.
- [4] **Bulkhead Studios** — *Scheduled Maintenance & Patch 0.11* (Steam announcement, 12 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1843481262698449. Accessed 2026-10-08.
- [5] **Bulkhead Studios** — *WARDOGS | Update 0.1.2 (Minor Patch)* (Steam announcement, 30 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1845383656376490. Accessed 2026-10-08.
- [6] **Bulkhead Studios** — *WARDOGS | Security & Stability Hotfix* (Steam announcement, 2 Oct 2026). https://store.steampowered.com/news/app/1867240/view/1845383656384445. Accessed 2026-10-08.
- [7] **Bulkhead Studios** — *IR Goggles & CIWS Balance Hotfix* (Steam announcement, 2 Oct 2026). https://store.steampowered.com/news/app/1867240/view/1845383656386801. Accessed 2026-10-08.
- [8] **Bulkhead Studios** — *WARDOGS Season 02 Teaser* (Steam announcement, 22 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1844115010504839. Accessed 2026-10-08.
- [9] **Bulkhead Studios** — *PRE-ORDER NOW!* (Steam announcement, 11 Aug 2026). https://store.steampowered.com/news/app/1867240/view/1840310314354505. Accessed 2026-10-08.
- [10] **Bulkhead Studios** — *WARDOGS - Early Access & Beyond* (Steam announcement, 7 Apr 2026). https://store.steampowered.com/news/app/1867240/view/1828894815567544. Accessed 2026-10-08.
- [11] **Bulkhead Studios** — *The 11th Reason NOT To Buy WARDOGS* (Steam announcement, 8 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1842846814456311. Accessed 2026-10-08.
- [18] **Bulkhead Studios** — *WARDOGS | Season 02 Patch Notes* (Steam announcement, posted 14 Oct 2026; includes an in-post update to logistics values). https://store.steampowered.com/news/app/1867240/view/1846651706674560. Accessed 2026-10-30.
- [19] **Bulkhead Studios** — *WARDOGS Season 02 Preview* (Steam announcement, 9 Oct 2026). https://store.steampowered.com/news/app/1867240/view/1846018067933823. Accessed 2026-10-30.
- [20] **Bulkhead Studios** — *WARDOGS | SEASON 02 IS NOW LIVE* (Steam announcement, 15 Oct 2026). https://store.steampowered.com/news/app/1867240/view/1846651706677015. Accessed 2026-10-30.
- [12] **Team17 / Bulkhead** — *WARDOGS is coming to Steam Early Access on 10 September* (press release). https://www.gamedeveloper.com/press-release/wardogs-is-coming-to-steam-early-access-on-10-september. Accessed 2026-10-08.

**Press & Secondary**

- [13] **Vice** — *WARDOGS developer confirms Season 2 rain won't change mid-match* (23 Sep 2026; relays a progression wipe not found in official text). https://www.vice.com/en/article/wardogs-season-2-rain-progression-wipe/. Accessed 2026-10-08.
- [14] **XGamingServer** — *WARDOGS roadmap: everything confirmed coming to Early Access* (unattributed). https://xgamingserver.com/blog/?p=23236. Accessed 2026-10-08.

**Player-Reported Evidence**

- [15] **allthings.how** — *WARDOGS roles: how to pick the best class for you*. https://allthings.how/wardogs-roles-how-to-pick-the-best-class-for-you/. Accessed 2026-10-08.
- [16] **allthings.how** — *WARDOGS beginner's guide: how the zone and cash systems work*. https://allthings.how/wardogs-beginner-s-guide-how-the-zone-and-cash-systems-work/. Accessed 2026-10-08.
- [17] **allthings.how** — *WARDOGS Hot Zone: how double presence and double cash work*. https://allthings.how/wardogs-hot-zone-how-double-presence-and-double-cash-work/. Accessed 2026-10-08.

# Further Reading

Pure Xbox and Push Square coverage of the console plans are listed in `SOURCE_REGISTRY.md`. Snapshots of official posts are under `snapshots/2026-10-08/steam-news/` and, for Season 02, `snapshots/2026-10-30/steam-news/`.

# Related Documents

- combat-loadouts-foundation
- economy-foundation
- maps-environment-foundation
- meta-release-foundation
- control-zone-and-match-flow (scoring, Hot Zone, spawn gaps, team switching, Forgive/Punish, seeding)
- progression-and-role-tracks (XP curve, tracks, caps)
- progression-unlock-tables (unlock levels)
- season-reset-and-currencies (Gold Bars, season reset)
- season-2-announcements (Season 02 claims graded)
- community-and-source-reliability (source ratings, hosting partners)
- patch-history (patch and hotfix timeline)

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after independent re-verification of validate, markdownlint and links (0 dead). | Standing mandate (auto-approve on green QA) |
| 1.1.0 | 2026-10-08 | Research Pipeline (revision worker) | Revised against full official Steam text; official role-track names (Career not Assault); Season 1 changelog gid corrected; 2 Oct hotfix split into two official posts with balance detail confirmed; Hot Zone, 256 km2 map, Kolchia, Gold Bars and team names upgraded to Primary; Advanced Filters and Deploy flow from 0.1.2; Season 02 wipe downgraded to press-only; hosting partners confirmed; local voice chat wording fixed; confidence raised to High | Standing mandate (auto-approve on green QA) |
| 1.1.1 | 2026-10-08 | Research Pipeline (revision worker) | Corrected against live store-page capture; voice chat recorded as both store-page phrases (proximity in the Early Access list, local in About This Game) and the contradiction dropped; roadmap bullets, 1 to 2 year Early Access, price plan, fighter jets now Primary and unverified caveats and matching open questions removed; $10,000 start, Hot Zone double cash, militaristic sandbox and Eastern Europe setting added from the page; confidence reassessed (High kept) | Standing mandate (auto-approve on green QA) |
| 1.2.0 | 2026-10-30 | Research Pipeline (revision worker) | Revised for Update 0.2.0 (Season 02, live 15 Oct 2026) from the 14 Oct patch notes, 9 Oct preview and 15 Oct live post: team-switch limits, Forgive/Punish, Squad Intent UI, seeding and pre-match entertainment, Lonestar experiment and losing-team discount, Wager Vendor (not at launch), XP curve summary; Season 01 values kept as dated history; wipe still unstated; no official posts after 2026-10-15 in snapshot | — |
