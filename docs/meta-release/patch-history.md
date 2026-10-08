---
id: patch-history
title: "Patch & Update History"
version: 1.1.0
status: frozen
confidence: High
category: Meta & Release
topic: "Dated per-patch changelog from closed beta through 0.1.2 and hotfixes, rebuilt from official Steam posts"
market: Global
game_version: "Early Access Update 0.1.2 plus the 2 Oct 2026 hotfixes"
document_type: reference-data
created: 2026-10-08
updated: 2026-10-08
review_due: 2026-10-22
sources_verified: 2026-10-08
supersedes: null
related: [meta-release-foundation, technical-servers-foundation, economy-foundation, editions-pricing-platforms]
tags: [patch-history, changelog, early-access]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | patch-history |
| Version | 1.1.0 |
| Status | frozen |
| Confidence | High |
| Category | Meta & Release |
| Game version | Early Access Update 0.1.2 plus the 2 Oct 2026 hotfixes |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-08 |
| Review due | 2026-10-22 |

# Executive Summary

This reference lists every dated WARDOGS build change posted by BULKHEAD on Steam News between the August 2026 closed beta and 8 October 2026. Version 1.1.0 is rebuilt from the full text of the official posts saved in the 2026-10-08 snapshot, replacing the 1.0.0 draft that was written from press summaries because the posts were then unreadable [1]. Every entry below is labelled Official and cites its Steam post. Press-only items are moved to a separate unconfirmed list.

The official titles settle the version labels: "Patch 0.11" (post titled "SCHEDULED MAINTENANCE & PATCH 0.11") and "Update 0.1.2 (Minor Patch)" [9][10]. The two 2 Oct entries are two separate official posts: a security and stability hotfix announcement at 00:13 UTC and an IR Goggles and CIWS balance hotfix post at 15:39 UTC [11][12]. Season 02 is announced for 15 Oct 2026 and is not live [13].

Confidence is High: the changelog rests entirely on first-party Steam posts. The weakest points (how the 2 Oct security hotfix was carried out, beta dates not stated in post text) are flagged inline.

# Key Takeaways

- Official labels: "Pre-Load Live & Season 1 Changelog" (9 Sep 2026), "PATCH 0.11" (posted 12 Sep, deployed 14 Sep) and "Update 0.1.2 (Minor Patch)" (30 Sep). No official post in the snapshot uses "0.1.1" [7][9][10].
- 0.1.2 was posted 30 Sep 2026 at 06:57 UTC; maintenance began at 08:00 UTC and was estimated at one hour [10].
- 0.1.2 targets cash and XP exploits: revive checks fully server authoritative, fly-through rewards capped, buildable rewards scaled by build progress, reduced FOB pallet rewards, and an end to first-offence leniency [10].
- The two 2 Oct posts are separate: a hotfix notice for 08:00 UTC with one hour of downtime (00:13 UTC post), and a balance hotfix (15:39 UTC post) that disables IR Rangefinders in the vendor until Season 02 and cuts the CIWS time to destroy a Havoc from about 12 s to about 6 s [11][12].
- Season 1.0 slowed levels 10-20 (level 10 needs 35,000 XP instead of 25,000; level 20 needs 250,000 instead of 111,500) and repriced many vendor items (9 Sep 2026) [7].
- Patch 0.11 split the browser into Community and Official, made Community Server IDs persistent and stated an economy-abuse sanctions policy (14 Sep 2026) [9].
- Season 02 is announced for 15 Oct 2026 and is not live at 8 Oct 2026 [13].

# Scope

Covers the closed beta posts, the open beta post, the pre-load and Season 1 changelog, Launch Stability Hotfix #1, Patch 0.11, Update 0.1.2, the 2 Oct 2026 hotfixes and the Season 02 teaser, as of 8 Oct 2026. Excludes marketing, sales and wishlist posts, and Season 02 content. Release dates, prices and platforms are in meta-release-foundation and editions-pricing-platforms; in-game economy rules are in economy-foundation; server administration is in technical-servers-foundation.

# Definitions

- **Official**: published by BULKHEAD on the WARDOGS Steam News feed and saved in the 2026-10-08 snapshot [1].
- **Season 1.0**: the label the 9 Sep changelog uses for its unlock-level changes [7].
- **Patch 0.11**: the label in the title of the 12 Sep post that announced the 14 Sep update [9].
- **WD-L020**: crash error that BULKHEAD attributes to Windows 11 update KB5124010 [10].
- **CIWS**: close-in weapon system; the 2 Oct post gives its effect on the Havoc [12].
- **RCON**: remote console used by community server admins.

# Current State

At 8 Oct 2026 the live build is Update 0.1.2 as changed by the 2 Oct 2026 hotfixes [10][11][12]. The balance hotfix needed no client download or server downtime and was due to reach all regions within 12 hours of its 15:39 UTC post as servers restarted [12]. Season 02 is planned for 15 Oct 2026 and is not live [13].

# Detail

## Version labels (resolved from official titles)

| Date posted (UTC) | Official post title | Label in text | Source |
|-------------------|---------------------|---------------|--------|
| 9 Sep 2026 22:46 | Pre-Load Live & Season 1 Changelog | "Season 1.0 Unlocks" headings | [7] |
| 12 Sep 2026 22:26 | SCHEDULED MAINTENANCE & PATCH 0.11 | Patch 0.11 | [9] |
| 30 Sep 2026 06:57 | WARDOGS / Update 0.1.2 (Minor Patch) | Update 0.1.2 | [10] |

The 1.0.0 draft wondered whether "0.11" meant "0.1.1". The official title is "PATCH 0.11", so this KB uses 0.11 as the official label. No snapshot post is titled 0.1.1. BULKHEAD gives no explanation for the numbering. Confidence High for the labels, which are quoted from the titles.

## Entry index

| Date (UTC) | Label | Post time (UTC) | Status | Source |
|------------|-------|-----------------|--------|--------|
| 20 Aug 2026 | Closed Beta Schedule | 21:32 | Official | [3] |
| 21-23 Aug 2026 | Closed Beta weekend | Window stated in the 24 Aug recap | Official | [4] |
| 24 Aug 2026 | Beta Recap & Next Steps | 20:30 | Official | [4] |
| 1 Sep 2026 | Closed Beta 02 Announcement | 16:07 | Official | [5] |
| 5-6 Sep 2026 | Open beta (ends Sunday 08:00 UTC) | 5 Sep 21:08 | Official | [6] |
| 9 Sep 2026 | Pre-Load Live & Season 1 Changelog | 22:46 | Official | [7] |
| 10 Sep 2026 | Launch Stability Hotfix #1 | 20:20 | Official | [8] |
| 14 Sep 2026 | Patch 0.11 (announced 12 Sep) | 12 Sep 22:26 | Official | [9] |
| 30 Sep 2026 | Update 0.1.2 (Minor Patch) | 06:57 | Official | [10] |
| 2 Oct 2026 | Security & Stability Hotfix | 00:13 | Official | [11] |
| 2 Oct 2026 | IR Goggles & CIWS Balance Hotfix | 15:39 | Official | [12] |
| 15 Oct 2026 | Season 02 (teaser posted 22 Sep) | 22 Sep 16:53 | Official, not live | [13] |

## Beta dates from the official posts

- **Closed Beta weekend**: the 20 Aug post says the closed beta is "this weekend", that the NDA is lifted, that a first wave of invites went out and that 'WARDOGS Playtest' can be pre-loaded; the schedule itself is an image, so no dates are in the text [3]. The 24 Aug recap names pre-order access "between August 21st - 23rd" and says that weekend's closed beta is over [4]. 21-23 Aug 2026 is therefore the official closed beta window.
- **Closed Beta 02**: announced 1 Sep 2026 "ahead of The FPS Games Show" (3 Sep, 18:00 UTC) as a scale test, with access in waves for pre-orders, and tests named as server scaling and browsing, Twitch Drops, DLC entitlements, VOIP and the login queue [5]. The post gives no start or end date. A press-reported 3-6 Sep window is in the unconfirmed list.
- **Open beta**: on 5 Sep 2026 at 21:08 UTC the closed beta became an open beta "until the Beta ends - Sunday at 08:00 UTC" [6]. The Sunday after that post is 6 Sep 2026 (derived from the post date).
- The recap announces The FPS Games Show for 3 Sep 2026, 18:00 UTC [4]. The 14 Aug closed beta notes found earlier are not in the official feed; see the Unconfirmed list.

## 9 Sep 2026, Pre-Load Live & Season 1 Changelog (Official) [7]

The post is the Early Access launch changelog (launch 10 Sep 2026 [2]).

- Exploits: fixed an exploit reaching an unintended church roof position.
- Reporting and moderation: new report tracking system; reports weighted so repeat and bad-faith reporters carry less influence; cheater bans announced in server when match termination is off; the "kicked from server" message appears only if actually banned.
- Server browser and front end: reworked server browser filtering; community server images no longer scale incorrectly; Host a server button links to the hosting page.
- Voice chat: fixed voice cutting out permanently after a failed join (stale channel rejoins, push to talk targeting and re-login recover); improved reliability under load and added a visible communication status.
- Gameplay and vehicles: Z20 Lakota balance pass and sluggish pitch fix; helicopter input damping on every input device; maximum operator rotation speed for vehicle turrets; 155mm, 122mm and flare deployables take more loadout room; tank aiming DPI fix; Z20 Lakota chase camera rotation rattle reduced by 6 dB.
- Performance and stability: DLSS Frame Generation can be turned off without restart and the render target pool is configurable; fewer shadow cache refreshes; two frame generation crash paths fixed; more detailed GPU crash reports; a legacy graphics dependency removed; shadow quality clamped to Low on high benchmark scores; fixed crashes from off-thread network calls, closing a chatbox entry tooltip, buildables, and firing a weapon whose owner had left; dropped items no longer affect navigation; better startup reliability and messages.
- Progression: levels 10 to 20 slowed and the curve flattened from 35 onward; Artillery to Career level 90; Heavy Tank to Driver level 35; Forward Operating Base and Large Hammer vendor prices raised.

Baseline values, XP bands (XP required, before and after, with the stated slowdown):

| Level | Before | After | Slower |
|-------|--------|-------|--------|
| Below 6 | unchanged | unchanged | - |
| 6 | 8,750 | 9,250 | 5.7% |
| 10 | 25,000 | 35,000 | 40.0% |
| 15 | 54,750 | 110,000 | 100.9% |
| 20 | 111,500 | 250,000 | 124.2% |
| 25 | 192,000 | 325,000 | 69.3% |
| 30 | 293,750 | 400,000 | 36.2% |
| 35 | 416,500 | 500,000 | 20.0% |
| 40 | 551,250 | 650,000 | 17.9% |
| 45 | 689,500 | 800,000 | 16.0% |
| 50 | 838,000 | 1,000,000 | 19.3% |

Baseline values, XP events: player kill using an air vehicle 300 XP to 250 XP; supply crate item sold under $75 25 XP to 1 XP [7].

Baseline values, prices (before and after) [7]:

| Item | Before | After |
|------|--------|-------|
| Vendor, Forward Operating Base | $2,500 | $7,500 |
| Vendor, Large Hammer | $1,600 | $2,400 |
| Career, Artillery Tank | $400,000 | $500,000 |
| Recon, 6-10x MRAD scope | $25,000 | $40,000 |
| Recon, 6-10x MOA scope | $30,000 | $45,000 |
| Support, Medium Hammer | $10,000 | $25,000 |
| Support, Large Hammer | $25,000 | $75,000 |
| Pilot, small armoured supply crate | $5,000 | $10,000 |
| Pilot, Little Bird with miniguns | $25,000 | $50,000 |
| Pilot, Z20 Lakota | $50,000 | $35,000 |
| Driver, URAL | $50,000 | $35,000 |
| Driver, Dune Buggy | $35,000 | $25,000 |
| Driver, Kodiak Flatbed | $15,000 | $35,000 |
| Driver, Music Tape H | $5,000 | $2,500 |

The same post says the role track XP curve was rebalanced from level 6 upward and the supply crate purchase curve rescaled from 25 to 250 down to 1 to 200 [7].

Baseline values, Season 1.0 unlock levels (before to after) [7]:

| Role | Changes |
|------|---------|
| Career | Sports Parachute 36 to 35; Large Backpack 56 to 55; 762x54mm AP 83 to 82; 556mm AP 85 to 83; Deagle 90 to 85; Artillery Tank 55 to 90 |
| Medic | PP-19 50 round drum magazine 33 to 29 |
| Support | Large Hammer 7 to 8 |
| Driver | URAL 4 to 3; Kodiak Assault 8 to 6; Dune Buggy 10 to 8; Kodiak Flatbed 2 to 10; Large Supply Crate 20 to 16; URAL Covered 30 to 18; Music Tape H from Pilot 28 to Driver 23; URAL Attack 40 to 25; Humvee with minigun 35 to 30; Heavy Tank from Career 35 to Driver 35 |

## 10 Sep 2026, Launch Stability Hotfix #1 (Official) [8]

- A small client update. Logged-in players were forced to close and restart, then prompted to download the update; all players returned to the login queue and were admitted in controlled batches, gradually increased as players successfully populated servers.
- Targets: players unable to join servers, players kicked unexpectedly during play, extended login queue times.
- No gameplay or economy values changed in the post.

## 14 Sep 2026, Patch 0.11 (Official) [9]

Announced in the 12 Sep 22:26 UTC post. Maintenance on Monday 14 Sep 2026 at 08:00 UTC (01:00 US Pacific), about one hour.

- Server browser: front end split into Community and Official browsers; unnecessary filtering removed from Official (no official modified game modes); filtering reliability improved on Community; text search added to Community; Show Empty/Full added to the quick bar; Host button directed to the correct location.
- Community Server IDs persist between matches and restarts, and each server has a unique ID (longer for security); they were previously wiped on map change and restart.
- Server names: must sort alphabetically regardless of special characters and numbers; more than one space at a time is no longer allowed.
- Apology bonus: community servers give a 5% End of Match cash bonus for the next week.
- Other fixes: various cash exploits fixed; more GPU crashes addressed.
- Capacity: server capacity in Asia increased.
- Economy abuse sanctions: cash exploit or bug abuse gets a timed ban scaled to prior bans and a cash and XP reset to 0; content that tutorialises exploits without reporting is treated as advertising cheats (permanent ban); XP farming gets the most serious bans, with permanent bans for joining XP-farming servers for more than a few minutes.
- Listed as not yet ready: community server favouriting, tiered priority queues for Community servers, Message of the Day prompt, improved warmup activities, disabling AFK kicking during seeding, team switching controls.

## 30 Sep 2026, Update 0.1.2 (Minor Patch) (Official) [10]

Posted 06:57 UTC; maintenance at 08:00 UTC, estimated one hour.

- Crash fix: WD-L020 crash caused by Windows 11 update KB5124010.
- Cash and XP exploits: revive validity checks fully server authoritative; vehicle fly-through exploit fixed with capped rewards; buildable destruction rewards scale with build progress (destroying a placed schematic no longer gives a full reward); depositing pallets into a FOB outside the zone awards reduced rewards.
- Sanctions: players caught abusing cash and XP exploits or Real Money Trading had cash and progression reset and risk permanent bans; leniency for first-time offenders is over.
- Server browser and UI: new DEPLOY flow (Official, Community, Infantry Mode, Low-Level); Advanced Filters back on the Official list; long server names no longer truncated (hover for the full name); Join shows connecting then queue position; Anonymous mode hides the server name on the loading screen and in the pause menu unless shown; region select shows how many regions are selected; gamepad support on DEPLOY.
- Server admins: daily restart time (UTC); RCON AllowedHosts; RCON message and broadcast lengths capped; RCON defaults to Standard response detail rather than Full, and config responses no longer expose server internals; ServerImageURL checked when config loads.
- Server stability: various stability hotfixes and increased server security.
- Bugs: throwables (grenades, smoke, C4) blocked from enclosed vehicle seats; adaptive crosshair hides when aiming down sights; buildable crit spots no longer reappear in place, get pushed into corners or jump to the far side, and favour a reachable spot; Havoc bug causing extra damage from 20mm and 30mm cannon fire fixed; localisation improved.
- Forward look: Season 02 is described as a larger content update with new map conditions, equipment, balance reworks and features.

## 2 Oct 2026, two official posts

| Post | Time (UTC) | Contents |
|------|-----------|----------|
| WARDOGS / Security & Stability Hotfix [11] | 00:13 | Heads-up that a hotfix is planned "tomorrow, Friday 2nd" at 08:00 UTC for minor security and stability issues affecting some players; expected downtime one hour |
| IR Goggles & CIWS Balance Hotfix [12] | 15:39 | Two balance changes within 12 hours as regional servers restart; no new client download or server downtime |

- Security and stability hotfix [11]: the post gives no detail of the issues and does not mention gameplay, balance or economy. The date wording ("tomorrow, Friday 2nd") sits oddly with a post time of 2 Oct 00:13 UTC; the hotfix time is stated as 08:00 UTC on Friday 2 Oct, so the post was presumably written the evening before in an Americas time zone. Assessment: Medium confidence, inferred from the post time.
- Balance hotfix [12]: IR Rangefinders disabled in the vendor until Season 02, where they will require batteries; the CIWS now destroys the Havoc in around 6 seconds instead of 12. BULKHEAD says it overcorrected the CIWS in the previous patch and hotfixed it "this morning".
- Whether the 08:00 UTC security hotfix and the CIWS "this morning" hotfix are the same operation is not stated; the posts are treated as separate.

## Season 02 teaser (Official, not live) [13]

Posted 22 Sep 2026 at 16:53 UTC: "WARDOGS Season 02 is coming", dated 15 October 2026, "Stay tuned for more details". The 0.1.2 post adds that Season 02 is a larger content update with new map conditions, equipment, balance reworks and additional features [10]. Nothing else is official.

## Unconfirmed (press or player-reported only)

These items are not in the official snapshot text. They do not establish facts.

| Item | Where it appears | Why unconfirmed |
|------|------------------|-----------------|
| Closed beta patch notes dated 14 Aug 2026 (pistol damage, AK74/Galil/M4/FAL handling, Gepard removal, level-up cost raises, HOTAS bindings and more) | Community repost, player-reported [16] | No official patch-notes post for 14 Aug (the official 14 Aug post is a wishlist announcement); not tied to the 21-23 Aug beta |
| Second closed beta on 3-6 Sep 2026 | Gfinity changelog article [14] | Official posts give only the 1 Sep announcement and the open beta end of Sunday 08:00 UTC; no start date |
| "September 29" as the 0.1.2 date | One secondary article citing a podcast [17] | Contradicted by the official post (30 Sep) |
| Press name "Sea Whiz" for the Havoc anti-air change; claim that the 2 Oct security hotfix made no gameplay, balance, economy or UI changes | MMOEXP and InGameNews [17][15] | The official posts say CIWS and give no such statement for the security hotfix |
| Season 02 wipe, rain, new weapons and other content | Timesaver.gg, which sells boosting services [18] | Only the date and the description in [10] and [13] are official |

# Early Access Changes & Known Issues

- This whole document is the change record; see Detail. Official posts through 2 Oct 2026 are included.
- Posted 14 Sep as not yet ready: community favouriting, tiered priority queues, Message of the Day, warmup activities, seeding AFK kick changes and team switching controls [9]. The 0.1.2 post lists none of them [10].
- No other official patch or hotfix post exists in the snapshot between 14 Sep and 30 Sep 2026 [1].
- IR Rangefinders are due back in Season 02 requiring batteries [12].

# Admin & Technical Notes

Admin-relevant entries: Community Server IDs persist and server names must sort alphabetically with single spaces (Patch 0.11, 14 Sep 2026) [9]; daily restart time in UTC, RCON AllowedHosts, RCON length caps, RCON Standard response default and ServerImageURL checks (Update 0.1.2, 30 Sep 2026) [10]. Config detail belongs in technical-servers-foundation.

# Risks & Caveats

- The snapshot is dated 2026-10-08; later posts, edits or removals are not reflected [1].
- Dates are Steam post times in UTC; the update itself ran at the stated maintenance times, not necessarily the post time.
- The 20 Aug beta schedule is an image whose contents are not in the text [3].
- Season 02 (15 Oct 2026) will supersede the Current State.
- Items in the Unconfirmed list can conflict with the official text; the official text wins.

# Open Questions

- Exact start and end of Closed Beta 02 (official text gives only the 1 Sep announcement and the 6 Sep 08:00 UTC end of the open beta).
- Whether the 14 Aug closed beta notes were ever posted officially.
- Whether the 2 Oct 08:00 UTC security hotfix ran as scheduled and whether it is the "this morning" hotfix cited in the balance post.
- Why BULKHEAD labels the patches "0.11" and "0.1.2".
- Whether any hotfix has shipped since the 2026-10-08 snapshot.

# References

**Primary Sources**

- [1] **Valve / BULKHEAD** — *WARDOGS Steam News Hub*. https://store.steampowered.com/news/app/1867240. Accessed 2026-10-08.
- [2] **Team17 / BULKHEAD** — *WARDOGS is coming to Steam Early Access on 10 September* (press release). https://www.gamedeveloper.com/press-release/wardogs-is-coming-to-steam-early-access-on-10-september. Accessed 2026-10-08.
- [3] **BULKHEAD** — *WARDOGS / Closed Beta Schedule* (Steam news, 2026-08-20 21:32 UTC). https://store.steampowered.com/news/app/1867240/view/1841579228666871. Accessed 2026-10-08.
- [4] **BULKHEAD** — *WARDOGS / Beta Recap & Next Steps* (Steam news, 2026-08-24 20:30 UTC). https://store.steampowered.com/news/app/1867240/view/1841579228676589. Accessed 2026-10-08.
- [5] **BULKHEAD** — *WARDOGS / Closed Beta 02 Announcement* (Steam news, 2026-09-01 16:07 UTC). https://store.steampowered.com/news/app/1867240/view/1842212951313938. Accessed 2026-10-08.
- [6] **BULKHEAD** — *THE CLOSED BETA IS NOW AN OPEN BETA!* (Steam news, 2026-09-05 21:08 UTC). https://store.steampowered.com/news/app/1867240/view/1842846814449809. Accessed 2026-10-08.
- [7] **BULKHEAD** — *Pre-Load Live & Season 1 Changelog* (Steam news, 2026-09-09 22:46 UTC). https://store.steampowered.com/news/app/1867240/view/1843481262690549. Accessed 2026-10-08.
- [8] **BULKHEAD** — *Launch Stability Hotfix #1* (Steam news, 2026-09-10 20:20 UTC). https://store.steampowered.com/news/app/1867240/view/1843481262693332. Accessed 2026-10-08.
- [9] **BULKHEAD** — *SCHEDULED MAINTENANCE & PATCH 0.11* (Steam news, 2026-09-12 22:26 UTC). https://store.steampowered.com/news/app/1867240/view/1843481262698449. Accessed 2026-10-08.
- [10] **BULKHEAD** — *WARDOGS / Update 0.1.2 (Minor Patch)* (Steam news, 2026-09-30 06:57 UTC). https://store.steampowered.com/news/app/1867240/view/1845383656376490. Accessed 2026-10-08.
- [11] **BULKHEAD** — *WARDOGS / Security & Stability Hotfix* (Steam news, 2026-10-02 00:13 UTC). https://store.steampowered.com/news/app/1867240/view/1845383656384445. Accessed 2026-10-08.
- [12] **BULKHEAD** — *IR Goggles & CIWS Balance Hotfix* (Steam news, 2026-10-02 15:39 UTC). https://store.steampowered.com/news/app/1867240/view/1845383656386801. Accessed 2026-10-08.
- [13] **BULKHEAD** — *WARDOGS / Season 02 Teaser* (Steam news, 2026-09-22 16:53 UTC). https://store.steampowered.com/news/app/1867240/view/1844115010504839. Accessed 2026-10-08.

**Press & Secondary**

- [14] **Gfinity Esports** — *WARDOGS Season 1 changelog*. https://www.gfinityesports.com/article/wardogs-season-1-changelog-early-access-patch-notes. Accessed 2026-10-08.
- [15] **InGameNews** — *WARDOGS update 0.1.2 and security hotfix: a comparative overview*. https://ingamenews.com/gaming-news/wardogs-update-0-1-2-and-security-hotfix-a-comparative-overview/. Accessed 2026-10-08.

**Player-Reported Evidence**

- [16] **Gaming with Daopa** — *Wardogs Closed Beta Patch Notes, August 14th* (community repost, published 21 Aug 2026). https://gamingwithdaopa.ellatha.com/wardogs/closed-beta-patch-notes-august-14th/. Accessed 2026-10-08.
- [17] **MMOEXP** — *WARDOGS October 2 update, Season 2 wipe, IR rangefinder nerf and new weapons* (single podcast source). https://www.mmoexp.com/News/wardogs-october-2-update-season-2-wipe-ir-rangefinder-nerf-and-new-weapons.html. Accessed 2026-10-08.
- [18] **Timesaver.gg** — *WARDOGS Season 2: everything we know* (sells boosting services). https://timesaver.gg/blog/wardogs-season-2-everything-we-know. Accessed 2026-10-08.

# Further Reading

- meta-release-foundation for the release timeline and Steam reception.
- Dexerto WARDOGS patch notes wiki: https://www.dexerto.com/wikis/wardogs/patch-notes/

# Related Documents

- meta-release-foundation
- technical-servers-foundation
- economy-foundation
- editions-pricing-platforms

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | - |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after independent re-verification of validate, markdownlint and links (0 dead). | Standing mandate (auto-approve on green QA) |
| 1.1.0 | 2026-10-08 | Research Pipeline (revision worker) | Rebuilt from full official Steam text; every entry cited to its Steam post and labelled Official; version labels taken from post titles (Patch 0.11, Update 0.1.2); 2 Oct entries resolved as two posts with UTC times; beta dates from official posts; press-only items moved to an Unconfirmed list; full Season 1 XP, price and unlock baseline values added; confidence raised to High. | Standing mandate (auto-approve on green QA) |
