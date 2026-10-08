---
id: system-requirements-and-performance
title: "System Requirements, Performance & Crashes"
version: 1.0.0
status: frozen
confidence: Medium
category: Technical & Servers
topic: "Hardware requirements, Linux/Proton, anti-cheat, crash codes, performance fixes"
market: Global
game_version: "Season 1, patch 0.1.2 plus hotfixes to 2 Oct 2026"
document_type: depth
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-11-08
sources_verified: 2026-10-08
supersedes: null
related: [technical-servers-foundation, rcon-and-server-admin, meta-release-foundation]
tags: [system-requirements, performance, crashes, linux, proton, anti-cheat, dlss]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | system-requirements-and-performance |
| Version | 1.0.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Technical & Servers |
| Game version | Season 1, patch 0.1.2 plus hotfixes to 2 Oct 2026 |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-11-08 |

# Executive Summary

This depth document goes beyond the specification table in technical-servers-foundation. It collects what is documented about client performance and stability in WARDOGS (Steam app 1867240): the exact wording and gaps of the Steam requirements, what is and is not stated about upscaling and frame generation, the Linux and Proton position, what a "kernel level" anti-cheat implies for players, the WD-L020 crash and its Windows 11 KB5124010 link, and a patch-by-patch list of performance and crash fixes through the 2 October 2026 hotfix [1][2][3][4][5].

Headline facts: the Steam page lists a 50 GB install, 16 GB RAM and a 1080p Low 60 fps (upscaled) minimum, and does not list DirectX, Steam Deck or Linux [1]. WD-L020 was the main target of update 0.1.2 on 30 September 2026 and was tied by press to Windows 11 update KB5124010 [4][5]. Upscaling settings are confirmed only through a DLSS Frame Generation toggle in launch notes and a player-reported settings guide [2][7].

Confidence is Medium. The specification and anti-cheat line are primary, but patch contents rest on press summaries because Steam news bodies were not readable, and the settings guidance is player-reported.

# Key Takeaways

- The Steam page lists Windows 10 64-bit minimum, Windows 11 64-bit recommended, 16 GB RAM and 50 GB storage for both tiers; no DirectX version, VRAM figure or storage type is given (checked 2026-10-08) [1].
- The minimum is stated as 1080p Low at 60 fps upscaled; the recommended is 1440p Medium 70+ fps native or 4K Medium 60+ fps upscaled, so the minimum assumes an upscaler is on [1].
- The Steam page says "Uses Kernel Level Anti-Cheat" and does not name the product; GamingOnLinux says the studio used Easy Anti-Cheat earlier and appeared to be testing something else (5 Sep 2026) [1][6].
- Linux is unsupported; on 5 Sep 2026 the developers said they cannot commit to Linux for Early Access, that earlier Linux working was accidental, and invited refunds [6]. The Steam page does not mention Steam Deck [1].
- WD-L020 crash fix shipped in update 0.1.2 (30 Sep 2026), described as the patch's main issue and linked to Windows 11 update KB5124010 [4][5].
- Launch patch (10 Sep 2026) made DLSS Frame Generation switchable without a restart and fixed two frame generation crash paths [2]. Patch 0.11 (14 Sep 2026) added only "more GPU crashes addressed" with no detail [3].
- Player-reported guides rate Global Illumination as the largest single frame-rate cost and recommend installing on an SSD (guide updated 12 Sep 2026) [7].

# Scope

Covered: Steam specification wording, graphics and upscaling settings as documented, Linux and Steam Deck status, the implications of kernel-level anti-cheat, crash codes and performance and stability fixes by patch, at game version Season 1, patch 0.1.2 plus hotfixes to 2 Oct 2026. Excluded: server hosting and RCON (rcon-and-server-admin, technical-servers-foundation), release and pricing (meta-release-foundation), and Season 2 (reported for 15 Oct 2026), which is outside the verified version. No benchmark data was found, so none is given.

# Definitions

- **WD-L020:** a client crash error code named in the 0.1.2 patch notes as reported by press [4][5].
- **KB5124010:** a Windows 11 cumulative update identified by press as the trigger for WD-L020 [4][5].
- **Frame Generation:** DLSS Frame Generation, named in the launch changelog [2].
- **Upscaled:** rendered at lower internal resolution and scaled; the Steam notes use "upscaled" without naming a technology [1].
- **Kernel-level anti-cheat:** anti-cheat software that runs a driver in the operating system kernel; term used verbatim on the Steam page [1].

# Current State

At Season 1 / patch 0.1.2, checked 2026-10-08:

- **Specifications.** Exactly as in the table under Detail. The Steam page lists Broadband internet as the network requirement and gives no DirectX line [1].
- **Platforms.** The page lists Windows only. Neither Linux nor Steam Deck is mentioned [1]. GamingOnLinux reports the developers do not officially support Linux and are still working on Proton compatibility [6].
- **Anti-cheat.** Kernel-level, unnamed [1][6].
- **Crash status.** WD-L020 is reported fixed by 0.1.2 on 30 Sep 2026 [4][5]. The 2 Oct 2026 hotfix lists "minor security and stability issues" without specifics [4].

# Detail

## Specification wording (Steam, 2026-10-08) [1]

| Item | Minimum | Recommended |
|------|---------|-------------|
| OS | Windows 10, 64-bit | Windows 11, 64-bit |
| CPU | Intel Core i5 8600 or AMD Ryzen 5 3500 | Intel Core i7 12700K or AMD Ryzen 7 5700X |
| RAM | 16 GB | 16 GB |
| GPU | Nvidia GTX 1660 or AMD Radeon RX 590 | Nvidia RTX 3070 or AMD Radeon RX 6700 XT |
| Storage | 50 GB available | 50 GB available |
| Network | Broadband | Broadband |
| Note | 1080p Low, 60 fps (upscaled) | 1440p Medium 70+ fps (native), or 4K Medium 60+ fps (upscaled) |
| DirectX | Not listed | Not listed |

Gaps in the official figures: no VRAM, no storage type (SSD or HDD), no Windows 11 requirement for the minimum tier, and no DirectX or Vulkan statement [1]. The minimum tier mixes a 2018-era GTX 1660 class GPU with an "upscaled" target, so players below it should expect to rely on an upscaler. Assessment: that reading is an inference from the note wording, Confidence Medium, resting on [1].

## Graphics and upscaling settings

- **Documented officially:** DLSS Frame Generation can be turned off without restarting the game and the render target pool is configurable (10 Sep 2026 launch changelog, press summary) [2]. Shadow quality is clamped to Low on high benchmark scores instead of being disabled, and shadow cache refreshes were reduced to cut hitching when taking control of a character [2].
- **Not documented in the sources read:** an FSR or XeSS option list, DLSS quality modes, or a Reflex entry. The launch changelog does not mention FSR, general upscaling options or memory changes [2].
- **Player-reported settings guide** (allthings.how, "Updated Sep 12, 2026"): lists an Overall Quality Custom profile; Global Illumination as the biggest single gain at roughly 20 percent on average; Shadows, Reflections, Shading, Post-Processing and Particle Spawn Rate at Low; Texture Streaming reduced first on VRAM warnings; DLSS on RTX cards and FSR on others, with Quality as the usual balance; Nvidia Reflex and a frame limit matching refresh rate [7]. These are one site's recommendations, not developer guidance, and the figure is not independently measured.
- A search of other community guides found disagreement on Global Illumination (off versus kept on with lower Shadows) and on DLSS Performance versus Quality mode; that search summary is not cited as fact. Treat all settings advice as player-reported.

## Linux, Steam Deck and Proton

| Date | Statement | Source |
|------|-----------|--------|
| 5 Sep 2026 | Developers "cannot commit to having Linux support for our Early Access launch"; still working on Proton compatibility; stance unchanged since before release | [6] |
| 5 Sep 2026 | An earlier community-manager Discord post implying support was called a communication mistake; earlier Linux functionality in alpha and beta tests was accidental | [6] |
| 5 Sep 2026 | Buyers who expected Proton support on 10 Sep were told to refund | [6] |
| 25 Sep 2026 | A reader comment on the article quotes the developers as having no new information and still wanting Linux support via Proton (player-reported, unverified) | [6] |

Steam Deck: the Steam page and GamingOnLinux article give no Steam Deck status [1][6]. No Deck Verified rating was found; treat Deck as unsupported and untested.

## Kernel-level anti-cheat and what it implies

- Fact: the Steam page states the game "Uses Kernel Level Anti-Cheat" [1]. GamingOnLinux says the game previously used Easy Anti-Cheat, the developers appear to be testing something else, and the product is not named; the site said it would check at release [6]. This document does not name the product. A reader comment on that article names one, which is unverified and not repeated here.
- Assessment: a kernel driver generally installs at game launch, needs administrator rights, and limits some virtualization and driver-level tools; kernel anti-cheat also commonly conflicts with Linux compatibility layers unless the vendor enables Proton support. Confidence Low to Medium: this is general reasoning, not a WARDOGS-specific statement, and the sources above do not confirm the mechanism for this game.
- Player-reported: a reader comment says the beta ran on Windows only with the new anti-cheat and had many cheaters, and that Linux ran better in the previous beta [6]. Anecdotal.
- Moderation side (not kernel-specific): a report-weighting system and ban announcements were added at launch [2]; see technical-servers-foundation.

## WD-L020 and KB5124010

- Update 0.1.2 on 30 Sep 2026 lists a "Windows 11 'WD-L020' Crash Error Fix"; MP1st calls it "the main issue tackled by this patch" and says the update KB5124010 caused the recent WD-L020 crashes [5].
- In-Game News independently reports the WD-L020 fix and links it to KB5124010, and says the notes contain no other GPU, DLSS or FSR items [4].
- No source read describes the mechanism, which hardware was affected, or a pre-patch workaround. Uninstalling the Windows update is not recommended by any source; do not infer it.

# Early Access Changes & Known Issues

| Date and version | Item | Source |
|------------------|------|--------|
| 10 Sep 2026, launch | DLSS Frame Generation can be disabled without restart; render target pool configurable; shadow cache and clamp changes; dropped items no longer affect navigation; startup reliability, clearer early-failure messages and recovery path; legacy graphics dependency removed; two frame generation crash paths, off-thread network call, chatbox tooltip, buildables and orphaned-weapon fire crashes fixed; GPU crash reports carry more detail; voice chat recovery improved | [2] |
| 14 Sep 2026, 0.11 | "More GPU crashes addressed"; no GPU models or details | [3] |
| 30 Sep 2026, 0.1.2 | WD-L020 crash fix (Windows 11 KB5124010); server stability hotfixes | [4][5] |
| 2 Oct 2026, hotfix | "Minor security and stability issues"; no gameplay, balance or UI changes; about one hour of maintenance; specifics undisclosed | [4] |

Known issues: Linux and Steam Deck unsupported [6]. No other open client crash codes were found in the sources read; a missing report does not mean none exist.

# Admin & Technical Notes

None found for dedicated server performance. For server restarts and RCON, see technical-servers-foundation and rcon-and-server-admin. Client-side only: a stable base frame rate is recommended before frame generation by one player guide; player-reported [7].

# Risks & Caveats

- Patch contents rest on press summaries; Steam news bodies did not render, so official notes were not read directly [2].
- The Steam page is bot-prone and was read through a summariser [1].
- Settings advice and the 20 percent figure are single-site, player-reported and tied to an early build; they may be stale after any patch [7].
- The anti-cheat implications are general reasoning, not documented for this title.
- Season 2 (reported for 15 Oct 2026) may change requirements and settings.

# Open Questions

- Which anti-cheat product is used? A developer statement would resolve it.
- Will Proton or Steam Deck support ship, and does the anti-cheat allow it?
- What exactly caused WD-L020 and which systems were affected?
- Which upscalers (FSR, XeSS) and which DLSS modes does the in-game menu officially provide?
- What were the 2 Oct 2026 hotfix fixes?
- Is an SSD officially required, and what is the VRAM floor?

# References

**Primary Sources**

- [1] **Valve / Bulkhead** — *WARDOGS on Steam*. https://store.steampowered.com/app/1867240/WARDOGS/. Accessed 2026-10-08.

**Press & Secondary**

- [2] **Gfinity Esports** — *WARDOGS Season 1 changelog (Early Access patch notes)*. https://www.gfinityesports.com/article/wardogs-season-1-changelog-early-access-patch-notes. Accessed 2026-10-08.
- [3] **PlayDay** — *WARDOGS patch 0.11 focuses on server browsers (full notes)*. https://playday.one/2026/09/14/wardogs-patch-11-focuses-on-server-browsers-full-notes/. Accessed 2026-10-08.
- [4] **In-Game News** — *WARDOGS update 0.1.2 and security hotfix*. https://ingamenews.com/gaming-news/wardogs-update-0-1-2-and-security-hotfix-a-comparative-overview/. Accessed 2026-10-08.
- [5] **MP1st** — *WARDOGS update 0.1.2 deployed on September 30*. https://mp1st.com/title-updates-and-patches/wardogs-update-0-1-2-deployed-on-september-30-as-servers-go-down. Accessed 2026-10-08.
- [6] **GamingOnLinux** — *WARDOGS developers clarify Linux support via Proton may come later*. http://www.gamingonlinux.com/2026/09/wardogs-developers-clarify-linux-support-via-proton-may-come-later. Accessed 2026-10-08.

**Player-Reported Evidence**

- [7] **allthings.how** — *WARDOGS best settings for performance and visibility on PC* (updated 12 Sep 2026). https://allthings.how/wardogs-best-settings-for-performance-and-visibility-on-pc/. Accessed 2026-10-08.

# Further Reading

- Steam community announcements for app 1867240 for Season 02 requirement changes.

# Related Documents

- technical-servers-foundation
- rcon-and-server-admin
- meta-release-foundation

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after independent re-verification of validate, markdownlint and links (0 dead). | Standing mandate (auto-approve on green QA) |
