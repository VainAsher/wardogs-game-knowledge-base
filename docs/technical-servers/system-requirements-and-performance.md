---
id: system-requirements-and-performance
title: "System Requirements, Performance & Crashes"
version: 1.2.1
status: frozen
confidence: Medium
category: Technical & Servers
topic: "Hardware requirements, Linux/Proton, anti-cheat, crash codes, performance fixes"
market: Global
game_version: "Early Access Season 02, Update 0.2.0 (15 Oct 2026); official posts through 2026-10-15 (snapshot 2026-10-30)"
document_type: depth
created: 2026-10-08
updated: 2026-10-30
review_due: 2026-11-20
sources_verified: 2026-10-30
supersedes: null
related: [technical-servers-foundation, rcon-and-server-admin, meta-release-foundation, client-install-inspection]
tags: [system-requirements, performance, crashes, linux, proton, anti-cheat, dlss]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | system-requirements-and-performance |
| Version | 1.2.1 |
| Status | frozen |
| Confidence | Medium (High for the specification table) |
| Category | Technical & Servers |
| Game version | Early Access Season 02, Update 0.2.0 (15 Oct 2026); official posts through 2026-10-15 (snapshot 2026-10-30) |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-30 |
| Review due | 2026-11-20 |

# Executive Summary

This depth document goes beyond the specification table in technical-servers-foundation. It collects what is officially documented about client performance and stability in WARDOGS (Steam app 1867240): the Steam store requirements as shown on the live store page (live capture 2026-10-08) and returned by the store API in the US and GB storefronts, what the official posts say about upscaling and frame generation, the Linux and Proton position, the WD-L020 crash and its Windows 11 KB5124010 link, and a post-by-post list of performance and crash fixes through the 2 October 2026 hotfixes [1][2][3][4][5][6][7]. Version 1.2.0 adds Update 0.2.0 (patch notes 14 Oct 2026, released 15 Oct 2026): the requirements in the 2026-10-30 store data (US storefront) are unchanged from the 2026-10-08 reading [1][11][12].

Headline facts: the store lists a 50 GB install, 16 GB RAM and a 1080p Low 60 fps (upscaled) minimum, lists Windows only, and carries no DirectX, VRAM or storage-type line [1]. Update 0.1.2 (30 September 2026) officially names a "Windows 11 'WD-L020' Crash Error Fix" and attributes the crashes to Windows 11 update KB5124010 [5]. The only official upscaling or frame generation wording is a DLSS Frame Generation toggle fix in the Season 1 changelog [2]. The store page states "Uses Kernel Level Anti-Cheat: Elytra" and "STEAM DECK COMPATIBILITY: Unsupported" [1]; the developers' own posts say nothing about Linux, Proton or Steam Deck [10].

Confidence is Medium overall. The specification table, anti-cheat disclosure, Steam Deck label and language list are direct readings of the live store page and are rated High; the Linux and Proton timeline rests on one press article and the settings guidance is player-reported.

# Key Takeaways

- Specification (live store page capture 2026-10-08; store API US and GB identical): minimum Windows 10, Core i5 8600 or Ryzen 5 3500, 16 GB RAM, GTX 1660 or RX 590, 50 GB, 1080p Low at 60 fps (upscaled); recommended Windows 11, Core i7 12700k or Ryzen 7 5700x, 16 GB RAM, RTX 3070 or RX 6700 XT, 50 GB, 1440p Medium at 70 fps+ (native) or 4K Medium at 60 fps+ (upscaled) [1]. A fresh browser capture on 2026-10-30 shows identical requirements, the same "Uses Kernel Level Anti-Cheat: Elytra" line and "STEAM DECK COMPATIBILITY: Unsupported" [1].
- Both tiers say "Requires a 64-bit processor and operating system"; no DirectX version, VRAM figure or SSD/HDD statement is given [1].
- The store API reports platforms Windows true, Mac false, Linux false, and empty Mac and Linux requirement blocks; the live page shows "STEAM DECK COMPATIBILITY: Unsupported" [1].
- Anti-cheat: the live page states "Uses Kernel Level Anti-Cheat: Elytra" and "Requires agreement to a 3rd-party EULA: WARDOGS EULA" [1].
- Supported languages: 14 ("See all 14 supported languages"), with English shown with full audio [1].
- Update 0.2.0 (14-15 Oct 2026): the minimum and recommended requirements in the 2026-10-30 store data are identical to the 2026-10-08 reading (including the Additional Notes lines and the empty Mac and Linux blocks) [1]. The 0.2.0 notes list only "Many QoL improvements, bug fixes, and performance and stability improvements" with no detail, name no new crash code, and say nothing about Linux, Proton, Steam Deck, upscalers or requirements [11][12].
- Update 0.1.2 fixed "the issue caused by the latest Windows 11 update, KB5124010, causing the recent WD-L020 crashes" [5]. No official post describes the mechanism or affected hardware.
- The Season 1 changelog (published 9 Sep 2026, live for launch) lists a Performance and stability section: DLSS Frame Generation toggle without restart, configurable render target pool, fewer shadow cache refreshes, two frame generation crash paths fixed, more detailed GPU crash reports and several other crash fixes [2].
- Launch Stability Hotfix #1 (10 Sep 2026) targeted join failures, mid-game kicks and login queues, not graphics performance [3].
- Linux and Steam Deck: the store page labels Steam Deck compatibility Unsupported [1]; no official post covers Linux, and GamingOnLinux reports the developers cannot commit to Linux for Early Access (5 Sep 2026) [13]. The developers' only anti-cheat remark in the posts read is a tongue-in-cheek line that "you don't talk about anti-cheat" [10].

# Scope

Covered: Steam specification wording, graphics and upscaling settings as documented, platform status, anti-cheat disclosure, crash codes and performance and stability fixes by official post, at game version Season 02, Update 0.2.0 (15 Oct 2026), with Season 1 / 0.1.2 and the 2 Oct 2026 hotfixes as dated history. Excluded: server hosting and RCON (rcon-and-server-admin, technical-servers-foundation) and release and pricing (meta-release-foundation). No benchmark data was found, so none is given.

# Definitions

- **WD-L020:** a client crash error code named in the 0.1.2 patch notes as a Windows 11 crash [5].
- **KB5124010:** a Windows 11 update that the 0.1.2 notes identify as the cause of the WD-L020 crashes [5].
- **Frame Generation:** DLSS Frame Generation, named in the Season 1 changelog [2].
- **Upscaled:** rendered at lower internal resolution and scaled; the store page's Additional Notes use "Upscaled" and "Native" without naming a technology [1].
- **Elytra:** the anti-cheat product named on the live store page as the kernel-level anti-cheat [1].
- **Kernel-level anti-cheat:** anti-cheat software that runs a driver in the operating system kernel. The live Steam page states "Uses Kernel Level Anti-Cheat: Elytra" (live capture 2026-10-08); the storefront API JSON omits the field [1].

# Current State

At Season 02 / Update 0.2.0 (official posts through 2026-10-15; none seen in the 2026-10-30 snapshot after that). The bullets below were read on 2026-10-08 (Season 1 / 0.1.2); the requirements were re-checked against 2026-10-30 store data and are unchanged [1]:

- **Specifications.** Exactly as in the table under Detail [1]. The store lists Broadband internet and gives no DirectX line [1].
- **Languages.** 14 supported languages; English is shown with interface, full audio and subtitles [1].
- **Platforms.** The store API lists Windows only; Mac and Linux are false with empty requirement lists [1]. The live store page shows "STEAM DECK COMPATIBILITY: Unsupported", an official Steam label [1].
- **Engine.** The developers describe a custom "War Dynamics Framework" that "enhances UE5" and say performance and input latency are a major concern (18 Feb 2026) [9].
- **Anti-cheat.** The live store page states "Uses Kernel Level Anti-Cheat: Elytra" and "Requires agreement to a 3rd-party EULA: WARDOGS EULA" [1]. The developers' posts do not discuss it beyond a joke line [10].
- **Crash status.** WD-L020 was fixed in 0.1.2 on 30 Sep 2026 [5]. The 2 Oct 2026 hotfix is described only as addressing "minor security and stability issues affecting some players" with one hour of downtime [6].

# Detail

## Specification wording (live Steam store page, live capture 2026-10-08; matches store API US and GB) [1]

Confidence: High. The live page lines match the storefront payloads, which are identical for US and GB.

| Item | Minimum | Recommended |
|------|---------|-------------|
| Architecture | 64-bit processor and operating system | 64-bit processor and operating system |
| OS | Windows 10 | Windows 11 |
| CPU | Intel Core i5 8600, AMD Ryzen 5 3500 | Intel Core i7 12700k, AMD Ryzen 7 5700x |
| RAM | 16 GB | 16 GB |
| GPU | Nvidia GTX 1660, Radeon RX 590 | Nvidia RTX 3070, AMD Radeon RX 6700 XT |
| Storage | 50 GB available space | 50 GB available space |
| Network | Broadband Internet connection | Broadband Internet connection |
| ADDITIONAL NOTES | 1080p Low @ 60fps (Upscaled) | 1440p Medium @ 70fps+ (Native) or 4k Medium @ 60fps+ (Upscaled) |
| DirectX | Not listed | Not listed |

Gaps in the official figures: no VRAM, no storage type (SSD or HDD), and no DirectX or Vulkan statement [1]. The minimum tier pairs a GTX 1660 class GPU with an "Upscaled" target, so players near the minimum should expect to rely on an upscaler. The live page confirms upscaling is part of both the minimum target and the 4K recommended target, while the 1440p recommended target is stated as Native; no upscaling technology is named [1]. Assessment: that reading is an inference from the note wording, Confidence Medium, resting on [1].

Other store data: 14 supported languages. The page shows English with interface, full audio and subtitles, and French, Italian, German and Spanish - Spain with interface and subtitles; the full list in the store data is English, French, Italian, German, Spanish - Spain, Japanese, Korean, Portuguese - Brazil, Russian, Simplified Chinese, Traditional Chinese, Polish, Turkish and Ukrainian; accessibility tags include Camera Comfort and Custom Volume Controls [1]. The page also shows Steam Achievements: 10 [1].

## Graphics and upscaling settings

- **Documented officially:** the Season 1 changelog says DLSS Frame Generation can be turned off without restarting and the render target pool is configurable; shadow quality is clamped to Low on high benchmark scores rather than being switched off entirely; shadow cache refreshes were reduced, which cuts hitching when taking control of a character; dropped items no longer affect navigation, "which claws back a little performance"; a legacy graphics dependency was removed [2].
- **Official intent:** a 16 Jul 2026 devlog post states that performance "has been a priority for the entire team since day one", that the game was optimised "across a wide range of hardware" and that graphics options let players tune it to their PC; it gives no figures [8].
- **Not documented in the sources read:** an FSR or XeSS option list, DLSS quality modes, or a Reflex entry. No official post mentions FSR, XeSS, Reflex or VRAM [2][5].
- **Player-reported settings guide** (allthings.how, "Updated Sep 12, 2026"): lists an Overall Quality Custom profile; Global Illumination as the biggest single gain at roughly 20 percent on average; Shadows, Reflections, Shading, Post-Processing and Particle Spawn Rate at Low; Texture Streaming reduced first on VRAM warnings; DLSS on RTX cards and FSR on others, with Quality as the usual balance; Nvidia Reflex and a frame limit matching refresh rate [14]. These are one site's recommendations, not developer guidance, and the figure is not independently measured. Treat all settings advice as player-reported.

## Linux, Steam Deck and Proton

| Date | Statement | Source |
|------|-----------|--------|
| 2026-10-08 | Live store page: "STEAM DECK COMPATIBILITY: Unsupported" (official Steam label) | [1] |
| 2026-10-08 | Store API: platforms Windows true, Mac false, Linux false; Linux requirements empty | [1] |
| 5 Sep 2026 | Developers "cannot commit to having Linux support for our Early Access launch"; still working on Proton compatibility (press report) | [13] |
| 5 Sep 2026 | An earlier community-manager Discord post implying support was called a communication mistake; earlier Linux functionality in tests was accidental (press report) | [13] |
| 5 Sep 2026 | Buyers who expected Proton support on 10 Sep were told to refund (press report) | [13] |

Steam Deck is officially labelled Unsupported on the store page [1]. The Steam news posts in the snapshot (official posts, February to 2 October 2026) contain no mention of Linux, Proton or Steam Deck, so the Linux and Proton timeline above, given as context, rests on the GamingOnLinux report [13].

## Anti-cheat disclosure

- Fact: the live Steam store page states "Uses Kernel Level Anti-Cheat: Elytra" and "Requires agreement to a 3rd-party EULA: WARDOGS EULA" (live capture 2026-10-08). The storefront API JSON omits these fields, so the page capture is the evidence [1].
- The developers' 8 Sep 2026 post says "There's a rule in game development: you don't talk about anti-cheat" and points players to the in-game report function and community-hosted servers [10]. GamingOnLinux says the game previously used Easy Anti-Cheat and the developers appeared to be testing something else (press report) [13]; the product named on the current store page is Elytra [1].
- Moderation side: the Season 1 changelog added a report tracking system, weighted reports, and in-server announcements of cheater bans [2]; see technical-servers-foundation.
- Assessment: a kernel driver generally installs at game launch, needs administrator rights, and commonly conflicts with Linux compatibility layers unless the vendor enables Proton support. Confidence Low to Medium: this is general reasoning, not a WARDOGS-specific statement.

## WD-L020 and KB5124010

- The 0.1.2 post (30 Sep 2026) lists "Windows 11 'WD-L020' Crash Error Fix" as a key update, and states: "Fixed the issue caused by the latest Windows 11 update, KB5124010, causing the recent WD-L020 crashes." [5]
- It was part of a minor patch aimed mainly at XP and cash exploits and security issues, with about one hour of maintenance from 08:00 UTC [5].
- No official post describes the mechanism, which hardware was affected, or a pre-patch workaround. No source recommends uninstalling the Windows update; do not infer it.

# Early Access Changes & Known Issues

| Date and version | Item | Source |
|------------------|------|--------|
| 9 Sep 2026, Season 1 changelog (live 10 Sep) | Performance and stability: DLSS Frame Generation can be disabled without restart; render target pool configurable; fewer shadow cache refreshes; two frame generation crash paths fixed; GPU crash reports carry more detail; legacy graphics dependency removed; shadow quality clamped to Low rather than off on high benchmark scores; crashes fixed for off-thread network calls, chatbox tooltip close, buildables and firing a weapon whose owner had left; dropped items no longer affect navigation; startup reliability and clearer early-failure messages; voice chat recovery improved | [2] |
| 10 Sep 2026, Launch Stability Hotfix #1 | Forced client update and controlled login batches to address players unable to join servers, unexpected kicks and long login queues | [3] |
| 14 Sep 2026, 0.11 | "More GPU crashes addressed"; no GPU models or details; also server browser changes | [4] |
| 30 Sep 2026, 0.1.2 | Windows 11 WD-L020 crash fix (KB5124010); exploit fixes; "various server stability hotfixes" | [5] |
| 2 Oct 2026, security and stability hotfix | "Minor security and stability issues affecting some players"; 08:00 UTC, one hour downtime; specifics undisclosed | [6] |
| 2 Oct 2026, IR Goggles and CIWS hotfix | Balance only; no client download or server downtime required | [7] |
| 15 Oct 2026, Update 0.2.0 | Maintenance 08:00 to 09:30 UTC (about 90 minutes estimated); notes list only general "performance and stability improvements"; helmet Level 4 now fogs when sprinting (gameplay, not a performance fix); no requirement or crash-code change stated; released 15 Oct 09:59 UTC | [11][12] |

Known issues: Linux is not listed on the store and Steam Deck is labelled Unsupported on the store page [1]. No other open client crash codes are named in the official posts read; a missing report does not mean none exist.

# Admin & Technical Notes

No official post gives dedicated server hardware or performance requirements. For server restarts and RCON, see technical-servers-foundation and rcon-and-server-admin; the 0.1.2 post added a daily scheduled restart time (UTC) and RCON AllowedHosts for community admins [5]. Client-side only: a stable base frame rate is recommended before frame generation by one player guide; player-reported [14].

# Risks & Caveats

- The store page capture is a single dated read (2026-10-08); the page can change with any patch.
- The Linux stance rests on a single press article; the official posts are silent.
- The Season 1 changelog is dated 9 Sep 2026 (pre-load) and is described here as live for launch; its snapshot title is "Pre-load Live Season 1 Changelog".
- Settings advice and the 20 percent figure are single-site, player-reported and tied to an early build; they may be stale after any patch [14].
- The anti-cheat implications are general reasoning, not documented for this title.
- Requirements were unchanged at the 2026-10-30 store read, but new content (rain weather, vehicles, weapons) was added in 0.2.0 and the store text could change again; no benchmark or install-size change is documented.

# Open Questions

- Will Proton or Steam Deck support ship, given the Unsupported label and the kernel-level anti-cheat?
- What exactly caused WD-L020 beyond the KB5124010 attribution, and which systems were affected?
- Which upscalers (FSR, XeSS) and which DLSS modes does the in-game menu officially provide? The store page confirms upscaled targets but names no technology.
- What were the 2 Oct 2026 security and stability hotfix fixes?
- Is an SSD officially required, and what is the VRAM floor?

# References

**Primary Sources**

- [1] **Valve / Bulkhead** — *WARDOGS on Steam* (live captures 2026-10-08 and 2026-10-30 of the rendered store page, plus store API snapshots, US and GB). https://store.steampowered.com/app/1867240/WARDOGS/. Accessed 2026-10-08 and 2026-10-30.
- [2] **Bulkhead** — *Pre-load live Season 1 changelog*, Steam announcement, 2026-09-09. https://store.steampowered.com/news/app/1867240/view/1843481262690549. Accessed 2026-10-08.
- [3] **Bulkhead** — *Launch Stability Hotfix #1*, Steam announcement, 2026-09-10. https://store.steampowered.com/news/app/1867240/view/1843481262693332. Accessed 2026-10-08.
- [4] **Bulkhead** — *Scheduled Maintenance & Patch 0.11*, Steam announcement, 2026-09-12. https://store.steampowered.com/news/app/1867240/view/1843481262698449. Accessed 2026-10-08.
- [5] **Bulkhead** — *WARDOGS | Update 0.1.2 (Minor Patch)*, Steam announcement, 2026-09-30. https://store.steampowered.com/news/app/1867240/view/1845383656376490. Accessed 2026-10-08.
- [6] **Bulkhead** — *WARDOGS | Security & Stability Hotfix*, Steam announcement, 2026-10-02. https://store.steampowered.com/news/app/1867240/view/1845383656384445. Accessed 2026-10-08.
- [7] **Bulkhead** — *IR Goggles & CIWS Balance Hotfix*, Steam announcement, 2026-10-02. https://store.steampowered.com/news/app/1867240/view/1845383656386801. Accessed 2026-10-08.
- [8] **Bulkhead** — *WARDOGS | Level Design & Performance*, Steam announcement, 2026-07-16. https://store.steampowered.com/news/app/1867240/view/1838407329256924. Accessed 2026-10-08.
- [9] **Bulkhead** — *WARDOGS Top Questions*, Steam announcement, 2026-02-18. https://store.steampowered.com/news/app/1867240/view/1825093633182385. Accessed 2026-10-08.
- [10] **Bulkhead** — *The 11th Reason NOT to Buy WARDOGS*, Steam announcement, 2026-09-08. https://store.steampowered.com/news/app/1867240/view/1842846814456311. Accessed 2026-10-08.
- [11] **Bulkhead** — *WARDOGS Season 2 Patch Notes* (Steam post, 14 Oct 2026 14:59 UTC; Update 0.2.0 notes and maintenance-window notice). https://store.steampowered.com/news/app/1867240/view/1846651706674560. Accessed 2026-10-30.
- [12] **Bulkhead** — *WARDOGS Season 02 is now LIVE* (Steam post, 15 Oct 2026 09:59 UTC; Update 0.2.0 released, servers back online). https://store.steampowered.com/news/app/1867240/view/1846651706677015. Accessed 2026-10-30.

**Press & Secondary**

- [13] **GamingOnLinux** — *WARDOGS developers clarify Linux support via Proton may come later*. http://www.gamingonlinux.com/2026/09/wardogs-developers-clarify-linux-support-via-proton-may-come-later. Accessed 2026-10-08.

**Player-Reported Evidence**

- [14] **allthings.how** — *WARDOGS best settings for performance and visibility on PC* (updated 12 Sep 2026). https://allthings.how/wardogs-best-settings-for-performance-and-visibility-on-pc/. Accessed 2026-10-08.

# Further Reading

- Steam community announcements for app 1867240 for Season 02 requirement changes.

# Related Documents

- technical-servers-foundation
- rcon-and-server-admin
- meta-release-foundation
- client-install-inspection

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after independent re-verification of validate, markdownlint and links (0 dead). | Standing mandate (auto-approve on green QA) |
| 1.1.0 | 2026-10-08 | Research Pipeline (revision worker) | Revised against full official Steam text and store snapshot; spec table now from store API (US/GB identical), press patch summaries replaced by official posts, WD-L020/KB5124010 officially attributed, Linux and anti-cheat positions clarified, confidence re-rated | Standing mandate (auto-approve on green QA) |
| 1.1.1 | 2026-10-08 | Research Pipeline (revision worker) | Corrected against live store-page capture; anti-cheat now Primary and named (Elytra, plus WARDOGS EULA), Steam Deck labelled Unsupported, Additional Notes quoted exactly with upscaling confirmed in targets, 14 languages and English audio, removed unverified caveats and matching Open Questions | Standing mandate (auto-approve on green QA) |
| 1.2.0 | 2026-10-30 | Research Pipeline (virtual agent) | Revised for Update 0.2.0: requirements confirmed unchanged against the 2026-10-30 store data (US); 0.2.0 notes add only general performance and stability wording and no crash codes; 15 Oct 08:00-09:30 UTC maintenance recorded; references 11 and 12 now cited | — |
| 1.2.1 | 2026-10-30 | Research Pipeline (virtual agent) | Fresh browser capture of the live store page (2026-10-30): requirements, Elytra and Steam Deck lines unchanged since 2026-10-08. | — |
