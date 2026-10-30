---
id: rcon-and-server-admin
title: "RCON & Server Administration"
version: 1.2.0
status: frozen
confidence: Low
category: Technical & Servers
topic: "RCON interface, ServerSettings, admin tooling, security hardening"
market: Global
game_version: "Early Access Season 02, Update 0.2.0 (15 Oct 2026); official posts through 2026-10-15 (snapshot 2026-10-30)"
document_type: depth
created: 2026-10-08
updated: 2026-10-30
review_due: 2026-11-20
sources_verified: 2026-10-30
supersedes: null
related: [technical-servers-foundation, server-hosting-and-browser, system-requirements-and-performance]
tags: [rcon, serversettings, admin, security, warcon]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | rcon-and-server-admin |
| Version | 1.2.0 |
| Status | frozen |
| Confidence | Low |
| Category | Technical & Servers |
| Game version | Early Access Season 02, Update 0.2.0 (15 Oct 2026); official posts through 2026-10-15 (snapshot 2026-10-30) |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-30 |
| Review due | 2026-11-20 |

# Executive Summary

This depth document goes below the admin summary in technical-servers-foundation: the RCON HTTP API, the `ServerSettings.ini` keys, the 0.1.2 hardening, the 2 October hotfix, third-party admin tooling and moderation. It is verified against Season 02, Update 0.2.0 (released 15 Oct 2026) for official statements, with the unofficial RCON reference still dating from before 0.1.2.

Revision 1.2.0 (30 Oct 2026): the 0.2.0 patch notes (14 Oct 2026) mention no RCON or ini change; the only server-admin items are that community admins "will be able to configure their own ping limits", a penalty for community hosts exploiting the faction bonus, and "Server stability & security improvements" with no detail [6]. The "now live" post (15 Oct) only confirms release and servers back online [7]. RCON and ini details therefore remain unconfirmed.

Revision 1.1.0 re-checks the topic against the full official Steam posts. The official text says four things about RCON and server admin, all in the 0.1.2 post of 30 Sep 2026 under "Community Servers (for Server Admins)": a daily restart time in UTC, "RCON AllowedHosts: you can now set this to restrict who can access RCON", capped RCON message and broadcast lengths, and a Standard default response detail with config responses that no longer expose server internals [1]. It also says `ServerImageURL` "is now checked when the config loads" [1]. The official posts give no syntax, default or failure behaviour for any of these, and none of the other official posts read mentions RCON or AllowedHosts [2][3][4][5].

The 2 October security hotfix post says only that it addresses "minor security and stability issues affecting some players"; its text does not mention RCON [2]. Everything else (port, auth, endpoints, ini keys and defaults, the CL-501228 removals) still comes from an unofficial fan reference [10] and a tracker guide written by a tool vendor [11].

Confidence stays Low. The official text confirms the existence of the 0.1.2 admin changes but nothing about how the interface works, and the main reference was last updated before 0.1.2 shipped.

# Key Takeaways

- Official: Update 0.1.2 (30 Sep 2026) lets server admins set "RCON AllowedHosts" to "restrict who can access RCON". The post gives no format, default or example [1].
- Official: 0.1.2 also caps RCON message and broadcast lengths (no values given) and makes Standard the default RCON response detail "instead of Full" [1].
- Official: the 2 Oct hotfix post links to "minor security and stability issues affecting some players" and does not mention RCON [2].
- Official (Update 0.2.0, 14-15 Oct 2026): community admins can configure their own ping limits; the notes give no setting name, ini key or RCON endpoint for it. They also say community hosts seen exploiting the faction bonus will be punished and list "Server stability & security improvements" without detail. The notes do not mention RCON or AllowedHosts [6][7].
- Unofficial: the RCON interface is reported to be a versioned HTTP/JSON API (`/v1`), default port 7776, off by default, authenticated by a single shared bearer token with no read-only role (player-reported, reference v0.39 of 2026-09-21) [10][11].
- The fan reference does not mention AllowedHosts, because it predates 0.1.2; its key defaults may therefore be stale [10].
- Eight write endpoints were reported removed in build CL-501228 (14 Sep 2026) and replaced by edits to the config document. No official post says so; the official 0.11 post of the same date does not mention RCON [3][10].
- The listed `MaxPlayers` default of 128 is unexplained: the game is a 100-player format and no source gives a reason for 128 (see Detail and Open Questions) [10].
- Warcon and BattleMetrics are the named third-party panels; Warcon bans work only while the panel runs [11][12].

# Scope

Covered: RCON transport, authentication, endpoints, config document semantics, `ServerSettings.ini` keys and defaults, 0.1.2 and hotfix hardening, admin tools, banning and moderation, at the game version in the front matter. Excluded: hosting providers and the browser (server-hosting-and-browser), client hardware (system-requirements-and-performance), and running your own server binary, which is reportedly not offered [13]. Source classes used below: O = official Steam post (Primary); S = press or provider secondary; PR = player-reported or vendor. No official RCON or server-settings document has been found; official statements are limited to the patch-note lines quoted below.

# Definitions

- **RCON:** remote administration of a running server. Here it is an HTTP/JSON API, not a Source-style socket protocol [11]. The official posts use the term without defining it [1].
- **Config document:** the whole `ServerSettings.ini` text as read and replaced through `/v1/config` [10].
- **Revision:** a token returned with the config, sent back in `If-Match` to avoid overwriting newer edits [10].

# Current State

State at Season 02 / Update 0.2.0 (official posts through 2026-10-15; none seen in the 2026-10-30 snapshot after that). The 0.1.2 and earlier items below are dated history, checked 2026-10-08.

- Update 0.2.0 patch notes (14 Oct 2026 14:59 UTC), maintenance 08:00 to 09:30 UTC on 15 Oct: "Community Server admins will be able to configure their own ping limits, allowing for cross regional play (or more stringent rules) if desired"; "Community server hosts being seen to exploit the faction bonus will be punished"; "Server stability & security improvements" [6]. Release confirmed 15 Oct 2026 09:59 UTC [7]. Nothing on RCON, AllowedHosts, restart time or ini keys; whether 0.1.2 admin settings changed is not stated.

- No official RCON or server-settings documentation was found. The vendor guide says so directly (guide dated 2026-09-14, PR) [11]. A fan site relaying a hosting-policy thread (checked 2026-09-01, PR) says Bulkhead was developing an RCON tool and that moderation details were unpublished at that time [13].
- Official, 0.1.2 post (30 Sep 2026, 06:57 UTC), section "Community Servers (for Server Admins)", quoted in full (O) [1]:
  - "Scheduled restarts: you can now set a daily restart time (UTC)."
  - "RCON AllowedHosts: you can now set this to restrict who can access RCON."
  - "RCON message and broadcast lengths are now capped."
  - "RCON now defaults to Standard response detail instead of Full, and config responses no longer expose server internals."
  - "ServerImageURL is now checked when the config loads."
- The same post lists, under "Server Stability Improvements", "Various server stability hotfixes" and "Increased server security to prevent exploitation", without saying whether these touch RCON [1]. Its summary says the update is aimed at thwarting XP and cash exploits "and security issues seen since the early access launch" [1].
- What the 0.1.2 post does not say: the AllowedHosts value format, wildcard support, default or failure behaviour; the cap values; what "Full" and "Standard" include; how to set the restart time [1].
- Also in 0.1.2: revive action validity checks are "now fully server authoritative" (an exploit fix, not RCON) [1].
- Security and Stability Hotfix: the Steam post is stamped 00:13 UTC on 2 Oct 2026 and announces a hotfix "planned for tomorrow, Friday 2nd, at 08:00 UTC, to address minor security and stability issues affecting some players", with "Expected downtime is one hour." Its text does not link the fix to RCON, AllowedHosts or server administration, and gives no other detail (O) [2]. A press outlet adds that it carried no gameplay, balance or UI changes (S) [8].
- Official moderation statements that apply to players rather than admins: the 0.11 post (12 Sep 2026) sets out penalties for economy abuse (timed bans with cash and XP reset, permanent bans for tutorialising exploits or XP farming) and says the studio tracks "every server you enter" [3]. The 0.1.2 post says leniency for first-time economy exploiters "is now over" [1]. The Season 1 changelog adds that cheater bans are announced in-server when match termination is turned off and that reports are weighted [5]. None of these describes admin-side ban tooling.
- The 8 Sep 2026 post says use the in-game report function on official servers and, for "the ultimate protection", play on community-hosted servers "where admins can instantly ban bad actors". It names three Approved Hosting Partners: QONZER, BisectHosting and xREALM [4]. It does not mention RCON.
- The 0.11 post (12 Sep 2026) is about the server browser: Community Server IDs persist between matches and restarts, server names are re-ordered and restricted. It does not mention RCON, AllowedHosts or build CL-501228 [3].

# Detail

## Transport and authentication (PR, reference v0.39, 2026-09-21) [10]

None of this table is stated in an official post.

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

Conflict: the vendor guide says any listener bound beyond loopback "must use TLS" and that hosts provide an https address [11], while the fan reference says an earlier claim that a network listener needs a certificate was corrected and HTTPS is refused [10]. Both are player-reported and neither is confirmed by an official post. Assessment (confidence Low): terminate TLS in a reverse proxy or use a tunnel rather than expecting the game to do it.

## Endpoints (PR) [10]

| Group | Reported routes |
|-------|-----------------|
| Read | status, players, capabilities, bans, reserved-slots, audit (limit 1-500, default 50), config, rotation, catalog (maps, lightings, experiences, alternators), sponsor, server-id, health |
| Player writes | kick (reason), kill, message, faction change (only if listed in capabilities) |
| Match writes | broadcast, map change, match end, match restart, lighting |
| Bans | POST ban (steamId, optional reason), DELETE ban |
| Config | validate (dry run), PUT replace with `If-Match`, optional `force=true`, `fullApply=true` |

The vendor guide counts "around 35 endpoints" [11]. Clients should read `GET /v1/capabilities` rather than assume a route exists [10]. The official posts confirm that message and broadcast operations exist only indirectly, through "RCON message and broadcast lengths are now capped" [1].

## Config document semantics (PR) [10]

- `PUT /v1/config` replaces the whole document; omitted sections are removed.
- Every value is revalidated on each apply; one bad value blocks all edits, and a non-empty `errors` array means nothing was applied.
- Array keys follow Unreal operators: `!Key=ClearArray` empties, `.Key=value` appends.
- Ban, reserve and rotation commands edit and persist back to the ini. Only whitelisted sections and keys are honoured.

## ServerSettings.ini keys (PR; defaults as listed by the fan reference, not stated officially, not verified in-game) [10]

Only the existence of `ServerImageURL` as a config key with load-time checking is supported by an official post [1]. All other rows are player-reported.

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

The reference states the RCON listener is off by default yet lists `bEnabled` as `true`; this inconsistency is unresolved, so treat the true default as unknown [10]. No `AllowedHosts` key name, section or default appears in any source: the official post names the setting only as "RCON AllowedHosts" in prose [1].

## MaxPlayers 128 versus a 100-player game

- The game format is 100 players in three teams (Steam page, via the foundation document). No official post read gives a server `MaxPlayers` value, and a web search of hosting wikis found no source for 128; those pages were not opened and are not relied on.
- The reference says the value is "clamped by a developer-set min and max" [10]. So 128 is at most a stored default, and the effective cap could be lower.
- Assessment (confidence Low): 128 is probably an engine-level or template default, not a supported player count. This is inference. Do not set it above 100 expecting more players, and confirm the clamp with your host.

## Build CL-501228 removals (PR, build dated 2026-09-14) [10]

Removed routes (now 404 on current builds, still served by older builds): `PATCH /v1/settings`, `POST` and `DELETE /v1/reserved-slots`, `POST` and `DELETE /v1/rotation/entries`, `POST /v1/rotation/entries/{i}/move`, `POST /v1/rotation/save`, `PUT /v1/sponsor`. The functions moved to config keys: `DefaultReservedPlayerIds`, `RotationEntries` with `bEnabled` and `RotationMode`, `ScorePeriod`, `ServerImageURL`. The build date coincides with the maintenance window of patch 0.11 (announced for 14 Sep 2026) [3], but the 0.11 post does not mention RCON or these removals, so no source ties the two explicitly.

## Hardening in 0.1.2 and the hotfix

| Change | Class | Note |
|--------|-------|------|
| "RCON AllowedHosts: you can now set this to restrict who can access RCON" | O [1] | Value format, wildcard and default are not stated in any source read |
| RCON message and broadcast lengths capped | O [1] | Cap values not published |
| Standard response detail by default "instead of Full" | O [1] | Whether Full is still selectable is not documented |
| Config responses no longer expose server internals | O [1] | Which fields were hidden is not documented |
| `ServerImageURL` checked when the config loads | O [1] | Consistent with the reference's allow-list note [10], which is not official |
| Scheduled daily restart time (UTC) | O [1] | How to set it is not documented |
| "Increased server security to prevent exploitation" | O [1] | Does not say RCON |
| Server-authoritative revive checks | O [1] | Gameplay exploit fix, not RCON |
| 2 Oct hotfix: "minor security and stability issues affecting some players" | O [2] | Text does not link to RCON; contents undisclosed |

## Admin tooling and moderation

- **Warcon** (PR, repository page): self-hosted panel (Bun, SvelteKit, Postgres, Docker Compose), MIT code, with map imagery excluded from the licence and owned by Bulkhead. Per-server roles viewer, operator and admin; stored RCON passwords encrypted (AES-GCM); audit log exportable to CSV or JSON; automation triggers. No game version is stated and commit dates were not visible [12]. The page says the protocol was reverse-engineered, so it can break when builds change [12].
- **Warcon bans** are enforced by the panel's worker, not the game: a banned player is removed when seen, and bans only hold while Warcon runs and reaches the server. Bans made outside the panel appear as "local" [12].
- **BattleMetrics** is reported to support WARDOGS RCON, paid after a free tier, and it stores your RCON password [11]. The vendor guide is by Warcon's publisher, so it is promotional [11].
- **Native bans:** by Steam ID, persisted in the ban list and `DefaultBannedPlayerIds` [10][11]. Officially, only the 8 Sep statement that community admins "can instantly ban bad actors" supports the existence of admin-side bans [4].

# Early Access Changes & Known Issues

| Date | Change | Source |
|------|--------|--------|
| 2026-09-08 | Official post: community-hosted servers "where admins can instantly ban bad actors"; three Approved Hosting Partners | O [4] |
| 2026-09-14 | Patch 0.11 maintenance window (server browser changes); no RCON mention in the post | O [3] |
| 2026-09-14 | Build CL-501228: eight write endpoints removed in favour of config edits | PR [10] |
| 2026-09-21 | Fan reference at v0.39; no AllowedHosts entry | PR [10] |
| 2026-09-30 | 0.1.2: restart time, AllowedHosts, message caps, response detail, ServerImageURL check | O [1] |
| 2026-10-02 | Security and Stability Hotfix, announced 00:13 UTC for 08:00 UTC, one hour of downtime; no RCON link in the post | O [2] |
| 2026-10-15 | Update 0.2.0: admin-configurable ping limits (no key named), faction-bonus exploitation penalty, server stability and security improvements; no RCON mention | O [6][7] |

Known gaps: no official admin documentation, no read-only RCON role, and no TLS on the listener per [10]. The last two are player-reported.

# Admin & Technical Notes

- Treat the RCON password as full control. Keep it off the public internet: loopback or a VPN, SSH tunnel or TLS proxy [10][11], and set AllowedHosts. The setting exists officially [1]; its exact syntax is unverified.
- Hosting reality: server code is reportedly not released for self-hosting and RCON access depends on the host [11][13]. The official hosting route named on 8 Sep is the three Approved Hosting Partners [4]. Ask the host whether you can edit the ini, whether bans and rotation survive restarts, and whether third-party panels are allowed [11].
- Hosted third-party consoles hold full-access credentials once you give them the password [11].
- Scripts written against the fan reference should call `/v1/capabilities` first and handle 404, 412 and 422 [10].
- Assessment (confidence Low): the fan reference is stale-risk after 0.1.2 (the official post says default response detail and config reply contents changed), so re-diff your tooling against a live server after each patch.

# Risks & Caveats

- Staleness: the main reference (2026-09-21, v0.39) predates 0.1.2 and the 2 Oct hotfix; key defaults, routes and response-detail behaviour may have changed, and the 0.1.2 post confirms at least the response-detail default and config reply contents did [1].
- Every API and ini detail beyond the five quoted 0.1.2 lines is player-reported. The document is Low because no official source describes how RCON works.
- The vendor guide and Warcon share a publisher, a conflict of interest.
- Pages were read through a fetch summariser; the Warcon page was read only to character 100,000 of about 150,000.
- Update 0.2.0 shipped on 15 Oct 2026 and added an admin ping-limit setting, so builds changed after the fan reference; the reference was not re-checked against 0.2.0.

# Open Questions

- What is AllowedHosts' syntax, default and failure behaviour? The official post does not say; a hosting panel screenshot or official note would resolve it.
- Why does the ini list `MaxPlayers` 128 and what is the clamp? Host confirmation or a developer statement would resolve it.
- What did the 2 Oct hotfix fix? The official text says "minor security and stability issues" and does not link to RCON; whether RCON was involved is unknown.
- Does the RCON listener really lack TLS, given the vendor guide's contrary advice?
- Is the `bEnabled` default true or false?
- What are the Standard and Full response detail levels, and what are the message and broadcast caps?
- What is the name, format and RCON exposure of the 0.2.0 admin ping-limit setting, and what is the faction-bonus exploitation penalty? The notes do not say.
- Will an official admin manual or read-only role ship?

# References

**Primary Sources**

- [1] **Bulkhead / Team17 (Steam announcement)** — *WARDOGS | Update 0.1.2 (Minor Patch)*, 2026-09-30. https://store.steampowered.com/news/app/1867240/view/1845383656376490. Accessed 2026-10-08.
- [2] **Bulkhead / Team17 (Steam announcement)** — *WARDOGS | Security & Stability Hotfix*, 2026-10-02. https://store.steampowered.com/news/app/1867240/view/1845383656384445. Accessed 2026-10-08.
- [3] **Bulkhead / Team17 (Steam announcement)** — *Scheduled Maintenance & Patch 0.11*, 2026-09-12. https://store.steampowered.com/news/app/1867240/view/1843481262698449. Accessed 2026-10-08.
- [4] **Bulkhead / Team17 (Steam announcement)** — *The 11th Reason NOT to Buy WARDOGS*, 2026-09-08. https://store.steampowered.com/news/app/1867240/view/1842846814456311. Accessed 2026-10-08.
- [5] **Bulkhead / Team17 (Steam announcement)** — *Pre-load live: Season 1 changelog*, 2026-09-09. https://store.steampowered.com/news/app/1867240/view/1843481262690549. Accessed 2026-10-08.
- [6] **Bulkhead** — *WARDOGS Season 2 Patch Notes* (Steam post, 14 Oct 2026 14:59 UTC; Update 0.2.0 notes and maintenance-window notice). https://store.steampowered.com/news/app/1867240/view/1846651706674560. Accessed 2026-10-30.
- [7] **Bulkhead** — *WARDOGS Season 02 is now LIVE* (Steam post, 15 Oct 2026 09:59 UTC; Update 0.2.0 released, servers back online). https://store.steampowered.com/news/app/1867240/view/1846651706677015. Accessed 2026-10-30.

**Press & Secondary**

- [8] **In-Game News** — *WARDOGS update 0.1.2 and security hotfix*. https://ingamenews.com/gaming-news/wardogs-update-0-1-2-and-security-hotfix-a-comparative-overview/. Accessed 2026-10-08.
- [9] **BisectHosting (hosting provider, secondary)** — *WARDOGS Update 0.1.2 patch notes*. https://www.bisecthosting.com/blog/wardogs-update-0-1-2-patch-notes-bug-fixes-improvements-flythrough-exploit-fob-pallet-delivery-xp. Accessed 2026-10-08. Reproduces the 0.1.2 admin lines; superseded here by [1].

**Player-Reported Evidence**

- [10] **wardogs.tech (unofficial)** — *Wardogs Server Reference*. https://wardogs.tech/rcon-reference. Accessed 2026-10-08.
- [11] **Wardog Servers (independent tracker, Warcon publisher)** — *WARDOGS RCON and admin tools*. https://wardogservers.com/guides/wardogs-rcon-and-admin-tools. Accessed 2026-10-08.
- [12] **Warcon project (GitHub)** — *warcon: self-hostable RCON panel for WARDOGS*. https://github.com/warcon-app/warcon. Accessed 2026-10-08.
- [13] **WARDOGS-game.com (unofficial fan site)** — *WARDOGS Servers, Regions & Hosting*. https://wardogs-game.com/servers. Accessed 2026-10-08.

# Further Reading

- Steam community announcements for app 1867240 for any official server documentation.
- BisectHosting's patch-notes post [9] mirrors the official 0.1.2 admin lines.

# Related Documents

- technical-servers-foundation
- server-hosting-and-browser
- system-requirements-and-performance

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after independent re-verification of validate, markdownlint and links (0 dead). | Standing mandate (auto-approve on green QA) |
| 1.1.0 | 2026-10-08 | Research Pipeline (revision worker) | Revised against full official Steam text; quoted the five 0.1.2 admin lines as primary, recorded that the 2 Oct hotfix post does not link to RCON and that no official post gives AllowedHosts syntax or defaults, added official 0.11, 8 Sep and Season 1 changelog statements, relabelled ini and API content as unofficial, review_due set to 2026-10-22. | Standing mandate (auto-approve on green QA) |
| 1.2.0 | 2026-10-30 | Research Pipeline (virtual agent) | Revised for Update 0.2.0: official notes add admin-configurable ping limits, faction-bonus exploitation penalty and server stability and security improvements; no RCON or ini change stated, so RCON and ini details stay unconfirmed and Low; references 6 and 7 now cited; verified-version wording updated | — |
