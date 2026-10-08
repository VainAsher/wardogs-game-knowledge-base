---
id: rcon-and-server-admin
title: "RCON & Server Administration"
version: 1.0.0
status: frozen
confidence: Low
category: Technical & Servers
topic: "RCON interface, ServerSettings, admin tooling, security hardening"
market: Global
game_version: "Season 1, patch 0.1.2 plus hotfixes to 2 Oct 2026"
document_type: depth
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [technical-servers-foundation, server-hosting-and-browser, system-requirements-and-performance]
tags: [rcon, serversettings, admin, security, warcon]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rcon-and-server-admin |
| Version | 1.0.0 |
| Status | frozen |
| Confidence | Low |
| Category | Technical & Servers |
| Game version | Season 1, patch 0.1.2 plus hotfixes to 2 Oct 2026 |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

This depth document goes below the admin summary in technical-servers-foundation: the RCON HTTP API, the `ServerSettings.ini` keys, the 0.1.2 hardening, the 2 October hotfix, third-party admin tooling and moderation. It is verified against Season 1, patch 0.1.2 plus hotfixes to 2 Oct 2026.

Only two things rest on press or provider secondary sources: the 0.1.2 admin changes (daily restart time in UTC, an `AllowedHosts` RCON setting, capped message lengths, Standard response detail by default, `ServerImageURL` validated at load) [1][2], and the existence and timing of the 2 October hotfix, whose contents were not disclosed [1]. Everything else (port, auth, endpoints, ini keys and defaults, the CL-501228 removals) comes from an unofficial fan reference [3] and a tracker guide written by a tool vendor [4].

Confidence is Low. No official RCON or server-settings document was found, and the main reference was last updated before 0.1.2 shipped.

# Key Takeaways

- The RCON interface is reported to be a versioned HTTP/JSON API (`/v1`), default port 7776, off by default, authenticated by a single shared bearer token with no read-only role (player-reported, reference v0.39 of 2026-09-21) [3][4].
- Update 0.1.2 (30 Sep 2026) added an RCON access-restriction setting named AllowedHosts, capped RCON message and broadcast lengths, and made Standard the default response detail [2].
- The fan reference does not mention AllowedHosts at all, because it predates 0.1.2; its key defaults may therefore be stale [3].
- Eight write endpoints were reported removed in build CL-501228 (14 Sep 2026) and replaced by edits to the config document [3].
- The listed `MaxPlayers` default of 128 is unexplained: the game is a 100-player format and no source gives a reason for 128 (see Detail and Open Questions) [3].
- The 2 Oct 2026 hotfix was announced in 26 words with no specifics; any link to RCON is unknown [1].
- Warcon and BattleMetrics are the named third-party panels; Warcon bans work only while the panel runs [4][5].

# Scope

Covered: RCON transport, authentication, endpoints, config document semantics, `ServerSettings.ini` keys and defaults, 0.1.2 and hotfix hardening, admin tools, banning and moderation, at the game version in the front matter. Excluded: hosting providers and the browser (server-hosting-and-browser), client hardware (system-requirements-and-performance), and running your own server binary, which is reportedly not offered [6]. Source classes used below: S = press or provider secondary; PR = player-reported or vendor. No primary source exists for this topic.

# Definitions

- **RCON:** remote administration of a running server. Here it is an HTTP/JSON API, not a Source-style socket protocol [4].
- **Config document:** the whole `ServerSettings.ini` text as read and replaced through `/v1/config` [3].
- **Revision:** a token returned with the config, sent back in `If-Match` to avoid overwriting newer edits [3].

# Current State

State at Season 1 / 0.1.2 plus hotfixes, checked 2026-10-08.

- No official RCON or server-settings documentation was found. The vendor guide says so directly (guide dated 2026-09-14, PR) [4]. A fan site relaying a hosting-policy thread (checked 2026-09-01, PR) says Bulkhead was developing an RCON tool and that moderation details were unpublished at that time [6].
- Update 0.1.2 on 30 Sep 2026: a daily restart time in UTC, an RCON access restriction (AllowedHosts), capped RCON message and broadcast lengths, Standard default response detail, config replies no longer revealing internal server information, and `ServerImageURL` validation at config load (S, quoting the patch notes) [2]. In-Game News reports the restricted RCON access and scheduled restarts too [1].
- The same update added server-authoritative revive checks against XP and cash exploits [1].
- Security and Stability Hotfix, posted 00:13 UTC on 2 Oct 2026, described as addressing "minor security and stability issues", with no gameplay, balance or UI changes and a one-hour maintenance window (S) [1].

# Detail

## Transport and authentication (PR, reference v0.39, 2026-09-21) [3]

| Item | Reported value |
|------|----------------|
| Base URL | `http://<host>:<port>/v1/` |
| Default port | 7776, settable in config or with `-RCONPort=` |
| Transport | Plain HTTP; HTTPS refuses the connection |
| Auth | `Authorization: Bearer <rcon-password>` on every request |
| Roles | One token, full read and write, no read-only key |
| Body format | JSON; the two config-document endpoints use `text/plain` |
| Errors | Non-2xx with `{error:{code,message}}`; 412 stale revision, 422 rejected value, 404 removed route |
| Rate limit | None published |

Conflict: the vendor guide says any listener bound beyond loopback "must use TLS" and that hosts provide an https address [4], while the fan reference says an earlier claim that a network listener needs a certificate was corrected and HTTPS is refused [3]. Both are player-reported. Assessment (confidence Low): terminate TLS in a reverse proxy or use a tunnel rather than expecting the game to do it.

## Endpoints (PR) [3]

| Group | Reported routes |
|-------|-----------------|
| Read | status, players, capabilities, bans, reserved-slots, audit (limit 1-500, default 50), config, rotation, catalog (maps, lightings, experiences, alternators), sponsor, server-id, health |
| Player writes | kick (reason), kill, message, faction change (only if listed in capabilities) |
| Match writes | broadcast, map change, match end, match restart, lighting |
| Bans | POST ban (steamId, optional reason), DELETE ban |
| Config | validate (dry run), PUT replace with `If-Match`, optional `force=true`, `fullApply=true` |

The vendor guide counts "around 35 endpoints" [4]. Clients should read `GET /v1/capabilities` rather than assume a route exists [3].

## Config document semantics (PR) [3]

- `PUT /v1/config` replaces the whole document; omitted sections are removed.
- Every value is revalidated on each apply; one bad value blocks all edits, and a non-empty `errors` array means nothing was applied.
- Array keys follow Unreal operators: `!Key=ClearArray` empties, `.Key=value` appends.
- Ban, reserve and rotation commands edit and persist back to the ini. Only whitelisted sections and keys are honoured.

## ServerSettings.ini keys (PR; defaults as listed, not verified in-game) [3]

| Section | Key | Listed default | Applies |
|---------|-----|----------------|---------|
| WDRCONSettings | `bEnabled` | listener off by default; the key list shows `true` (inconsistent) | startup |
| WDRCONSettings | `BindAddress` | 127.0.0.1 (0.0.0.0 = all interfaces) | startup |
| WDRCONSettings | `Port` | 7776 | startup |
| WDRCONSettings | `Password`, `PasswordHash` | empty password auto-generates to `Saved/RCON/ADMIN-PASSWORD.txt`; hash from `-GenerateRCONHash=` takes precedence | startup |
| WDGameSession | `ServerName` | none | immediately |
| WDGameSession | `ServerPassword` | empty (open) | next restart |
| WDGameSession | `ServerMin/MaxPlayerCash`, `ServerMin/MaxPlayerLevel` | 0 (no limit) | next restart |
| WDGameSession | `ServerImageURL` | none; 1024x256 PNG or JPEG on an allow-list | pending |
| WDGameSession | `MaxReservedSlots` | 20 | immediately |
| WDGameSession | `DefaultReservedPlayerIds`, `DefaultBannedPlayerIds` | one SteamID64 per line | n/a |
| Engine.GameSession | `MaxPlayers` | 128, clamped by a developer-set min and max | immediately |
| PreMatch PlayerCount | `MinimumRequiredPlayers` | 60 | next match |
| KOTH | `ScorePeriod` | 24 s, range 18-30 | next match |
| WDGameStateSession | `bLockOverpopulatedTeamsConfig`, `OverpopulatedTeamThresholdConfig` | true, 2 | next match |
| MapRotationSettings | `bEnabled`, `RotationMode`, `+RotationEntries` | true, Ordered (or Random) | immediately |

The reference states the RCON listener is off by default yet lists `bEnabled` as `true`; this inconsistency is unresolved, so treat the true default as unknown [3].

## MaxPlayers 128 versus a 100-player game

- The game format is 100 players in three teams (Steam page, via the foundation document). A web search of hosting wikis found no source for 128; those pages were not opened and are not relied on.
- The reference says the value is "clamped by a developer-set min and max" [3]. So 128 is at most a stored default, and the effective cap could be lower.
- Assessment (confidence Low): 128 is probably an engine-level or template default, not a supported player count. This is inference. Do not set it above 100 expecting more players, and confirm the clamp with your host.

## Build CL-501228 removals (PR, build dated 2026-09-14) [3]

Removed routes (now 404 on current builds, still served by older builds): `PATCH /v1/settings`, `POST` and `DELETE /v1/reserved-slots`, `POST` and `DELETE /v1/rotation/entries`, `POST /v1/rotation/entries/{i}/move`, `POST /v1/rotation/save`, `PUT /v1/sponsor`. The functions moved to config keys: `DefaultReservedPlayerIds`, `RotationEntries` with `bEnabled` and `RotationMode`, `ScorePeriod`, `ServerImageURL`. The build date coincides with patch 0.11, but no source read ties the two explicitly.

## Hardening in 0.1.2 and the hotfix

| Change | Class | Note |
|--------|-------|------|
| AllowedHosts restricts who can reach RCON | S [1][2] | Value format, wildcard and default are undocumented in every source read |
| Message and broadcast length caps | S [2] | Cap values not published |
| Standard response detail by default | S [2] | Whether Full is still selectable is not documented |
| Config replies stop exposing server internals | S [2] | |
| `ServerImageURL` checked at load | S [2] | Consistent with the reference's allow-list note [3] |
| Server-authoritative revive checks | S [1] | Gameplay exploit fix, not RCON |
| 2 Oct hotfix | S [1] | Contents undisclosed |

## Admin tooling and moderation

- **Warcon** (PR, repository page): self-hosted panel (Bun, SvelteKit, Postgres, Docker Compose), MIT code, with map imagery excluded from the licence and owned by Bulkhead. Per-server roles viewer, operator and admin; stored RCON passwords encrypted (AES-GCM); audit log exportable to CSV or JSON; automation triggers. No game version is stated and commit dates were not visible [5]. The page says the protocol was reverse-engineered, so it can break when builds change [5].
- **Warcon bans** are enforced by the panel's worker, not the game: a banned player is removed when seen, and bans only hold while Warcon runs and reaches the server. Bans made outside the panel appear as "local" [5].
- **BattleMetrics** is reported to support WARDOGS RCON, paid after a free tier, and it stores your RCON password [4]. The vendor guide is by Warcon's publisher, so it is promotional [4].
- **Native bans:** by Steam ID, persisted in the ban list and `DefaultBannedPlayerIds` [3][4].

# Early Access Changes & Known Issues

| Date | Change | Source |
|------|--------|--------|
| 2026-09-14 | Build CL-501228: eight write endpoints removed in favour of config edits | PR [3] |
| 2026-09-21 | Fan reference at v0.39; no AllowedHosts entry | PR [3] |
| 2026-09-30 | 0.1.2: restart time, AllowedHosts, message caps, response detail, ServerImageURL check | S [1][2] |
| 2026-10-02 | Security and Stability Hotfix, 00:13 UTC post, about one hour of maintenance | S [1] |

Known gaps: no official admin documentation, no read-only RCON role, and no TLS on the listener per [3].

# Admin & Technical Notes

- Treat the RCON password as full control. Keep it off the public internet: loopback or a VPN, SSH tunnel or TLS proxy [3][4], and set AllowedHosts (effect per [1][2]; exact syntax unverified).
- Hosting reality: server code is reportedly not released for self-hosting and RCON access depends on the host [4][6]. Ask the host whether you can edit the ini, whether bans and rotation survive restarts, and whether third-party panels are allowed [4].
- Hosted third-party consoles hold full-access credentials once you give them the password [4].
- Scripts written against the fan reference should call `/v1/capabilities` first and handle 404, 412 and 422 [3].
- Assessment (confidence Low): the fan reference may be stale after 0.1.2, so re-diff your tooling against a live server after each patch.

# Risks & Caveats

- Staleness: the main reference (2026-09-21) predates 0.1.2 and the 2 Oct hotfix; key defaults, routes and response-detail behaviour may have changed.
- Every API and ini detail is player-reported. The document is Low because no official source covers it.
- The vendor guide and Warcon share a publisher, a conflict of interest.
- Pages were read through a fetch summariser; the Warcon page was read only to character 100,000 of about 150,000.
- Season 2 (reported 15 Oct 2026) may change builds and admin tooling.

# Open Questions

- What is AllowedHosts' syntax, default and failure behaviour? A hosting panel screenshot or official note would resolve it.
- Why does the ini list `MaxPlayers` 128 and what is the clamp? Host confirmation or a developer statement would resolve it.
- What did the 2 Oct hotfix fix, and was RCON involved?
- Does the RCON listener really lack TLS, given the vendor guide's contrary advice?
- Is the `bEnabled` default true or false?
- Will an official admin manual or read-only role ship?

# References

**Primary Sources**

None found for this topic.

**Press & Secondary**

- [1] **In-Game News** — *WARDOGS update 0.1.2 and security hotfix*. https://ingamenews.com/gaming-news/wardogs-update-0-1-2-and-security-hotfix-a-comparative-overview/. Accessed 2026-10-08.
- [2] **BisectHosting (hosting provider, secondary)** — *WARDOGS Update 0.1.2 patch notes*. https://www.bisecthosting.com/blog/wardogs-update-0-1-2-patch-notes-bug-fixes-improvements-flythrough-exploit-fob-pallet-delivery-xp. Accessed 2026-10-08.

**Player-Reported Evidence**

- [3] **wardogs.tech (unofficial)** — *Wardogs Server Reference*. https://wardogs.tech/rcon-reference. Accessed 2026-10-08.
- [4] **Wardog Servers (independent tracker, Warcon publisher)** — *WARDOGS RCON and admin tools*. https://wardogservers.com/guides/wardogs-rcon-and-admin-tools. Accessed 2026-10-08.
- [5] **Warcon project (GitHub)** — *warcon: self-hostable RCON panel for WARDOGS*. https://github.com/warcon-app/warcon. Accessed 2026-10-08.
- [6] **WARDOGS-game.com (unofficial fan site)** — *WARDOGS Servers, Regions & Hosting*. https://wardogs-game.com/servers. Accessed 2026-10-08.

# Further Reading

- Steam community announcements for app 1867240 for any official server documentation.

# Related Documents

- technical-servers-foundation
- server-hosting-and-browser
- system-requirements-and-performance

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after independent re-verification of validate, markdownlint and links (0 dead). | Standing mandate (auto-approve on green QA) |
