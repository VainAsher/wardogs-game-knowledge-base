---
id: client-install-inspection
title: "Windows Client Install Inspection (Update 0.2.0)"
version: 1.0.0
status: frozen
confidence: Medium
category: Technical & Servers
topic: "What the installed Steam client contains: build id, executables, packaging, third-party components, size"
market: Global
game_version: "Early Access Season 02, Update 0.2.0 (15 Oct 2026); Steam build id 25937608, client build ++Wardogs+Live-CL-516586; install observed 2026-10-30"
document_type: reference-data
created: 2026-10-30
updated: 2026-10-30
review_due: 2026-11-20
sources_verified: 2026-10-30
supersedes: null
related: [technical-servers-foundation, system-requirements-and-performance, patch-history, server-hosting-and-browser]
tags: [technical, install, build-id, anti-cheat, middleware, reference-data]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | client-install-inspection |
| Version | 1.0.0 |
| Status | frozen |
| Confidence | Medium |
| Category | Technical & Servers |
| Game version | Update 0.2.0 (15 Oct 2026); Steam build id 25937608; client CL-516586 |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-30 |
| Updated | 2026-10-30 |
| Review due | 2026-11-20 |

# Executive Summary

This document records what a read-only inspection of one installed copy of the WARDOGS Windows client shows, observed on 2026-10-30. It reads only file names, sizes, dates, executable version resources and the Steam app manifest. It does not unpack, decompile, or modify any game data, and it does not read saved settings or crash reports [1].

The install is the Season 02 / Update 0.2.0 build. Steam's manifest records build id 25937608, last updated 2026-10-15 09:57 UTC, about two minutes before BULKHEAD's "Season 02 is now live" post of 2026-10-15 09:59 UTC [1][3]. The client executable's version string is `++Wardogs+Live-CL-516586` [1]. The install occupies 48,905,446,067 bytes (about 48.9 GB, 45.5 GiB), consistent with the store page's "50 GB available space" requirement [1][2].

Confidence is Medium: the observations are first-hand and exact, but they come from a single machine, they show what is present rather than what is enabled, and the interpretations are labelled as inference.

# Key Takeaways

- Build identity (Update 0.2.0 install, observed 2026-10-30): Steam build id 25937608, one installed depot (1867242), client version string `++Wardogs+Live-CL-516586` [1].
- Size: 308 files, 48,905,460,048 bytes in the install folder; 66 files in `Content/Paks` account for 46,565,045,228 bytes [1]. The store lists 50 GB of storage for both minimum and recommended tiers [2].
- Anti-cheat: an `Elytra` folder holds `Elytra-Setup.exe` and a Steam install script that runs it silently on install and uninstall [1]. This is consistent with the store page's statement that the game uses kernel-level anti-cheat Elytra [2]; a present installer does not by itself show how the anti-cheat behaves at runtime.
- Only one game executable ships: `WardogsClient-Win64-Shipping.exe` (about 222 MB), plus a small `WardogsLauncher-Shipping.exe`. No dedicated-server executable is in the client install [1].
- Third-party components present: NVIDIA DLSS and Streamline, AMD FSR, Intel XeSS, Sentry (crash reporting), Vivox (voice), atmoky TrueSpatial (spatial audio), Bink video (`.bk2`) [1].
- BULKHEAD's own post of 2026-02-18 says its custom WAR DYNAMICS FRAMEWORK "enhances UE5" [4]. The install layout (`Engine`, `Wardogs/Content/Paks`, `.pak`/`.ucas`/`.utoc` files) is consistent with an Unreal Engine project [1]; the exact engine minor version was not determined.

# Scope

Covers: the Windows Steam client install of app 1867240 as observed on 2026-10-30 on one machine, at Update 0.2.0.

Does not cover: the contents of the pak archives, game logic, netcode internals, dedicated-server software (not part of this install), console builds, Linux/Proton, or any runtime behaviour. Nothing in this document was obtained by extracting, decompiling or debugging game data. Personal identifiers in the manifest (the Steam account id) and the local crash-report folder were deliberately not recorded.

# Definitions

- **Build id**: Steam's integer identifier for a published build of the app's depot, recorded in `appmanifest_1867240.acf`.
- **CL number**: the changelist suffix in the client's version string (`CL-516586`), identifying the source-control revision the client was built from [1].
- **Pak / IoStore**: Unreal Engine archive formats; `.pak` files with companion `.ucas`/`.utoc` files hold packaged game content.

# Current State

All facts below were observed on 2026-10-30 at Update 0.2.0 [1].

| Item | Observation |
|------|-------------|
| Steam app id / name / install dir | 1867240 / WARDOGS / `Wardogs` |
| Build id (installed and target) | 25937608 (installed equals target; no update pending) |
| Installed depot | 1867242 (one depot, 48,905,446,067 bytes) |
| Manifest last updated | 2026-10-15 09:57:40 UTC |
| Client executable | `Wardogs/Binaries/Win64/WardogsClient-Win64-Shipping.exe`, version `++Wardogs+Live-CL-516586`, company BULKHEAD |
| Executable and `runtime.dll` file dates | 15 Oct 2026 (local file time 10:42) |
| Other executables | `WardogsLauncher-Shipping.exe` (root), `Elytra/Elytra-Setup.exe`, `CrashReportClient.exe`, `EpicWebHelper.exe`, Sentry `crashpad_handler.exe` |
| Install script | `Elytra/InstallScript.vdf` runs `Elytra-Setup.exe /quiet /norestart` on install and `/uninstall /quiet /norestart` on uninstall |

The manifest update time falls on the same day and about two minutes before the official "Season 02 is now live" post, which announces Update 0.2.0 with servers back online [3]. Assessment: build id 25937608 is the Update 0.2.0 release build; Confidence Medium; the evidence is the time coincidence, not a statement from BULKHEAD naming the build id.

# Detail

## Third-party components found

Presence of a component means its files ship with the game. It does not show that the feature is enabled or how it is used [1].

| Component | Where | Reading |
|-----------|-------|---------|
| NVIDIA DLSS and Streamline | `Plugins/External/Nvidia` | upscaling / frame generation support files |
| AMD FSR | `Plugins/External/FSR` | upscaling support files |
| Intel XeSS | `Plugins/External/XeSS` | upscaling support files |
| Sentry | `Plugins/External/Sentry`, `.sentry-native` | crash reporting runtime |
| Vivox | `Plugins/Online/VivoxCore` (`vivoxsdk.dll`) | voice communication SDK |
| atmoky TrueSpatial | `Binaries/Win64/atmokyTrueSpatial.dll` | spatial audio middleware |
| Direct3D 12 | `Binaries/Win64/D3D12` (`D3D12Core.dll`, `d3d12SDKLayers.dll`) | a bundled Direct3D 12 runtime folder |
| Bink video | `Content/Binks` (`.bk2`) | pre-rendered videos |

Engine third-party folders (CEF3, MsQuic, Steamworks, Ogg, Vorbis and others) and `EOSSDK-Win64-Shipping.dll` also exist under `Engine`. Assessment: these are likely engine defaults rather than evidence of game features; Confidence Low; no use was observed [1].

Cross-checks against other documents: the Vivox SDK is consistent with the store page's proximity and local voice chat claims [2]; the upscaler plugins are consistent with the "Upscaled" notes in the store requirements [2]. The store page lists no DirectX version [2]; the bundled Direct3D 12 folder suggests, but does not prove, a Direct3D 12 renderer (Confidence Low).

## Content packaging

`Wardogs/Content/Paks` holds 66 files in 17 groups of `.pak`/`.ucas`/`.utoc`/`.sig` files, named `pakchunk<N>-WindowsClient` for N = 0, 5, 6, 10, 11, 12, 13, 20, 21, 22, 23, 30, 50, 51, 52, plus `pakchunk10optional` and the `global` pair [1]. The largest are pakchunk51 (about 11.1 GB), pakchunk52 (about 9.3 GB), pakchunk50 (about 8.1 GB) and pakchunk0 (about 5.6 GB with its `.pak`) [1]. What each chunk contains was not examined.

`Content/Binks` holds videos including the tutorial clips, the three faction end-game videos (named for Lonestar, Manticore and Valkyra), and a front-end video named `UI_FrontendVideo_S02` of about 539 MB [1]. Assessment: the "S02" file name suggests the home-screen video was replaced for Season 02; Confidence Low; inferred from the name alone.

## How to reproduce

Any owner can repeat the checks without special tools: read `steamapps/appmanifest_1867240.acf` in their Steam library for `buildid`, `LastUpdated` and `SizeOnDisk`; right-click `WardogsClient-Win64-Shipping.exe`, then Properties, then Details for the version string; list the folders named above [1].

# Early Access Changes & Known Issues

- Baseline for later comparison: build id 25937608 / CL-516586 at Update 0.2.0 (observed 2026-10-30) [1][3]. A later build id or CL number on the same install would indicate a post-0.2.0 patch even if no official post announces it.
- No official post after 2026-10-15 appears in the 2026-10-30 news snapshot (see patch-history), so this install has not been compared with any later official change list.

# Admin & Technical Notes

- The client install contains no dedicated-server executable [1]. Server software and its configuration are covered in server-hosting-and-browser and rcon-and-server-admin, not here.
- Plan for about 49 GB of disk for the client at 0.2.0 plus headroom for updates; the store figure is 50 GB [1][2].
- Steam's install-script mechanism runs the Elytra installer silently on install and uninstall [1]. Admins and players who need to know what a kernel-level anti-cheat does should rely on the publisher's documentation; this inspection did not examine it.

# Risks & Caveats

- One machine, one day. Another install could differ if it is on a different build or branch.
- Presence is not use: bundled SDKs and engine defaults do not prove features.
- File dates are shown in the machine's local time; the time zone was not verified, so only the manifest's UTC timestamp is used for comparison with posts.
- Interpretation of names (for example `S02`, chunk numbers) is inference.

# Open Questions

- Is build id 25937608 still the current public build? A comparison with an independent build tracker or a second install would resolve it.
- Which Unreal Engine 5 minor version does the client use? The official post names only "UE5" [4], and the executable's version resources did not say.
- What do the pak chunks contain? Answering would require extracting game data, which this document does not do.

# References

**Primary Sources**

- [1] **Maintainer, local read-only inspection** — Windows Steam install of app 1867240 (file listing, sizes and dates, executable version resource, `appmanifest_1867240.acf`), observed 2026-10-30. Not a public URL; reproducible by any owner of the game as described above. Accessed 2026-10-30.
- [2] **Valve / BULKHEAD (Steam)** — *WARDOGS* store page (requirements, anti-cheat and voice chat lines; storefront data in snapshots/2026-10-30/store-app-us.json). https://store.steampowered.com/app/1867240/WARDOGS/. Accessed 2026-10-30.
- [3] **BULKHEAD** — *WARDOGS | SEASON 02 IS NOW LIVE* (Steam news, 2026-10-15 09:59 UTC). https://store.steampowered.com/news/app/1867240/view/1846651706677015. Accessed 2026-10-30.
- [4] **Bulkhead** — *WARDOGS Top Questions* (Steam news, 2026-02-18). https://store.steampowered.com/news/app/1867240/view/1825093633182385. Accessed 2026-10-30.

**Press & Secondary**

None.

**Player-Reported Evidence**

None.

# Further Reading

- system-requirements-and-performance for the official specification wording and crash codes.

# Related Documents

- technical-servers-foundation
- system-requirements-and-performance
- patch-history
- server-hosting-and-browser

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 1.0.0 | 2026-10-30 | Research Pipeline (virtual agent) | Initial release from a read-only inspection of the Update 0.2.0 Windows install. | — |
