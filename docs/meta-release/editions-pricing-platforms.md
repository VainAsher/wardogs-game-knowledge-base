---
id: editions-pricing-platforms
title: "Editions, Pricing & Platforms"
version: 1.2.1
status: frozen
confidence: Medium
category: Meta & Release
topic: "Editions, regional pricing, Supporter Pack contents, platform roadmap, Early Access policy"
market: Global
game_version: "Early Access Season 02, Update 0.2.0 (15 Oct 2026); official posts through 2026-10-15 (snapshot 2026-10-30)"
document_type: reference-data
created: 2026-10-08
updated: 2026-10-30
review_due: 2026-11-20
sources_verified: 2026-10-30
supersedes: null
related: [meta-release-foundation, economy-foundation, patch-history, system-requirements-and-performance]
tags: [pricing, editions, platforms, early-access]
---

# Document Control

| Field | Value |
|-------|-------|
| Document ID | editions-pricing-platforms |
| Version | 1.2.1 |
| Status | frozen |
| Confidence | Medium |
| Category | Meta & Release |
| Game version | Early Access Season 02, Update 0.2.0 (15 Oct 2026); official posts through 2026-10-15 (snapshot 2026-10-30) |
| Owner | WARDOGS KB Research Pipeline |
| Created | 2026-10-08 |
| Updated | 2026-10-30 |
| Review due | 2026-11-20 |

# Executive Summary

WARDOGS is sold on Steam as two purchase options plus a separate DLC: the Standard game (package 671715), the Supporter Edition (package 1746527) and the Supporter Pack DLC (app 4809960) [1][2]. In the 2026-10-08 store snapshot the US prices are USD 39.99, 49.99 and 12.99 and the UK prices are GBP 36.99, 45.99 and 11.99, with no discount active [1][2]. A second storefront snapshot on 2026-10-30, after Update 0.2.0 (15 Oct 2026), shows the same US and UK prices, the same Windows-only platform flags and no discount for the base game and the Supporter Pack [19]. Store prices did not change with Season 02. The Supporter Pack is cosmetic content (camos, a scoreboard icon, two bobbleheads). The developer's stated policy is that it is the only monetisation during Early Access and that in-game cash, gold bars and camos will never be sold [2][4].

Steam lists Windows only and the live store page shows Steam Deck compatibility as "Unsupported" [1][18]. The official Steam posts in the snapshot say nothing about Linux, Xbox or PS5; those statements (Xbox and PS5 "sometime in 2028", Linux unsupported with Proton work ongoing) come from press reports and are labelled as such [13][14][15][16]. The store page's own Early Access section says the developers plan a lower price during Early Access and a higher price at full release, and expect Early Access to last around 1 to 2 years [18]. Official Steam posts record 1.25 million copies sold on 11 Sep, 2 million on 15 Sep and 3 million on 26 Sep 2026 [5][6][7]; the Season 02 Preview of 9 Oct says "3+ million sales and counting" (studio claim, no new figure) [20]. Reviews on 2026-10-08 differ by source: the reviews API gave 81,290 positive of 109,396 (74.3%) while the live store page showed 95,146 total in all languages, both "Mostly Positive"; the gap is unexplained [11][18].

Confidence is Medium. Prices, DLC contents, sales milestones, the monetisation and pricing policy and review counts rest on official Steam data. The console and Linux claims rest on press only and cap the document.

# Key Takeaways

- Steam purchase options: Standard (USD 39.99 / GBP 36.99), Supporter Edition (USD 49.99 / GBP 45.99) and the Supporter Pack DLC (USD 12.99 / GBP 11.99), all undiscounted on 2026-10-08 and, for the base game and Supporter Pack, unchanged on 2026-10-30 [1][2][19].
- The Supporter Edition was announced on 11 Aug 2026 alongside pre-orders, which granted guaranteed Closed Beta access [4].
- Supporter Pack contents: three "Starter Weapon" camos (Valkyra A-91, Lonestar Bushmaster, Manticore KH-2002), a Littlebird Helicopter "Taxi" camo, a hideable scoreboard Supporter Icon, a Grenade Bobblehead and a Helmet Bobblehead [2][4]. The cosmetic-only character is the developer's own statement.
- Developer policy: no monetisation during Early Access except this pack; cash and gold bars never sold; camos never directly purchasable [2][4]. Earlier FAQ: "No Battlepass. No Pay to Win" [9].
- Steam lists Windows only; no Mac or Linux support flag on the store [1]. Steam Deck compatibility is officially "Unsupported" on the live store page [18]. Console and Linux/Proton status is press-reported, not in the official posts.
- Official pricing policy (store page, Primary): priced lower during Early Access, higher at full release; the price may be raised closer to full release; Early Access expected to last around 1 to 2 years [18].
- Sales (official Steam posts): 1.25 million (11 Sep), 2 million (15 Sep), 3 million (26 Sep 2026) [5][6][7].
- Reviews (2026-10-08): API all-language 81,290 of 109,396 positive [11]; live store page English 63,179 and all-language total 95,146, both "Mostly Positive" [18]. The 109,396 versus 95,146 difference is unexplained. On 2026-10-30 the live page showed English 83,965 (73% positive) and 128,224 in all languages, rated Mixed [18]; the review API could not be re-fetched that day.

# Scope

Covers editions, Steam regional prices at a date stamp, Supporter Pack contents, the Early Access pricing and monetisation statements, platform status and roadmap, sales milestones and the review score snapshot. Excludes in-game cash prices (see economy-foundation), patch contents (see patch-history) and hardware requirements (see system-requirements-and-performance). Game version: Update 0.2.0 (Season 02); price values were last checked 2026-10-30 (US and GB only).

# Definitions

- **Standard**: the base game purchase option, Steam package 671715 [1].
- **Supporter Edition**: bundle of the base game and the Supporter Pack, Steam package 1746527 [1][2].
- **Supporter Pack**: separately sold cosmetic DLC (app 4809960, package 1671550) [2].
- **Regional pricing**: Steam shows a different price per country code; the US and GB prices are from the 2026-10-08 store snapshot, other codes from an earlier single-day API fetch [1][3].

# Current State

## Editions (snapshot 2026-10-08)

The store snapshot (US and GB storefronts) shows the Standard and Supporter Edition options on the main page and the Supporter Pack as DLC; the pack's own entry also offers the Supporter Edition as the bundle [1][2]. The main page lists two DLC app ids (4809960 and 4809930); only 4809960 (Supporter Pack) was captured, so the second is unidentified [1]. Neither storefront showed a discount [1][2].

## Supporter Pack contents

The DLC entry says the pack "offers additional cosmetic content" and lists three "Starter Weapon" camos (Valkyra Branded A-91 Rifle, Lonestar Branded Bushmaster, Manticore Branded KH-2002), a Littlebird Helicopter "Taxi" camo, a Supporter Icon on the scoreboard (can be hidden in settings), a Grenade Bobblehead and a Helmet Bobblehead [2]. The identical list appeared in the 11 Aug 2026 announcement [4]. The developer's three stated rules: no monetisation during Early Access, in-game cash and gold bars are never monetised, and camos can never be directly purchased [2][4]. The launch press release repeats that cash, gold bars and status-based camouflage are not for sale [12]. Nothing in these sources lists a gameplay advantage, so cosmetic-only is the developer's statement, not independently tested.

## Platforms

The store snapshot flags Windows true, Mac false, Linux false; minimum OS Windows 10, recommended Windows 11 [1]. The live store page (live capture 2026-10-08) shows "Steam Deck Compatibility: Unsupported", an official Valve status, and lists Kernel Level Anti-Cheat: Elytra [18]. The official Steam posts in the snapshot contain no statement on Linux, Xbox or PS5. A 3 Mar 2026 post lists "Console Release?" among questions answered, but the answer is in a video and not in the post text [10]. Press reports Xbox and PS5 versions for "sometime in 2028", and Xbox Store wishlists open on 10 Sep 2026 [13][14].

## Review snapshot

Steam's review summary (all languages, scope `language=all`) on 2026-10-08 was "Mostly Positive": 81,290 positive and 28,106 negative, 109,396 total, 74.3% positive [11]. The earlier English-only figure is a different scope and is not comparable. The live store page (live capture 2026-10-08) shows English reviews "Mostly Positive (63,179)" and "Total reviews in all languages: 95,146 (Mostly Positive)" [18]. This is 14,250 fewer than the API's 109,396 for the same day; the cause is unexplained, so both figures are recorded and neither is preferred. The page does not show the earlier "79%" English percentage, which is not repeated here. Push Square recorded "over 17,000" reviews, also "Mostly Positive", on 11 Sep 2026 [14]. Update 2026-10-30: Live page, 2026-10-30: English reviews Mostly Positive (83,965; 73% positive); all-language total 128,224, rated Mixed; last 30 days Mixed, 54% positive of 43,444 reviews; 161 curators [18]; the storefront appdetails recommendations total was 128,183 on 2026-10-30 against 95,106 on 2026-10-08, within 41 and 40 of the page's all-language totals (128,224 and 95,146), whereas the review API's 109,396 (2026-10-08, all purchase types) was the outlier; with two data points this is an observation, not an explanation [1]; the review API could not be re-fetched on 2026-10-30 (the endpoint returned an HTML page instead of JSON, both from a script and in the browser).

# Detail

## Steam prices by region

| Country code | Standard | Supporter Edition | Supporter Pack | Source |
|--------------|----------|-------------------|----------------|--------|
| us | USD 39.99 | USD 49.99 | USD 12.99 | [1][2] |
| gb | GBP 36.99 | GBP 45.99 | GBP 11.99 | [1][2] |
| de | EUR 39.99 | not retrieved | not retrieved | [3] |
| ca | CAD 49.99 | not retrieved | not retrieved | [3] |
| au | AUD 54.95 | not retrieved | not retrieved | [3] |
| br | BRL 119.99 | not retrieved | not retrieved | [3] |
| jp | JPY 4,980 | not retrieved | not retrieved | [3] |
| pl | PLN 164.99 | not retrieved | not retrieved | [3] |
| tr | USD 24.99 (Steam regional USD price) | not retrieved | not retrieved | [3] |

The US and GB rows come from the 2026-10-08 store snapshot; the other rows come from an earlier price-field fetch the same day and are not in the snapshot [3]. The Supporter Edition costs USD 10.00 / GBP 9.00 more than Standard, against USD 12.99 / GBP 11.99 for the pack alone, so the bundle saves USD 2.99 / GBP 2.99 versus buying both separately (arithmetic on the snapshot prices) [1][2]. Assessment: the Turkey price is far below the others; confidence High as a reading of the table, with no inference about intent.

## Early Access pricing and monetisation statements

The developer's 11 Aug 2026 post says its devlog covers "early access strategy, stair stepped pricing and long-term monetisation plans" but gives no price steps in the post text [4]. The press release describes a tiered model rewarding earlier backers and gives USD 39.99 [12]. No full-release price or Early Access end date appears in the snapshot posts or press release [4][12]. The live store page's Early Access section is the official statement: "we plan for WARDOGS to be priced lower during Early Access, with a higher price at full release"; asked whether pricing differs during and after Early Access, it answers "Yes" and adds "we may raise the price closer to full release"; and it expects Early Access to last "around 1 to 2 years", with the exact duration subject to change [18]. No full-release price or fixed date is given there either [18]. The 7 Apr 2026 post says a metagame (Black Market and Vault, Player Skills and Challenge System) will be built throughout Early Access; it states no pricing [8]. The 18 Feb 2026 FAQ states "No Battlepass. No Pay to Win. Earn cosmetics by playing." [9]. The developer also encourages refunds if the game or beta does not meet expectations [4].

## Store-page features

The live store page lists Online PvP, Steam Achievements (10) and Accessibility Features (4), the content note "Includes Interactive Elements (In-game chat, Online interactivity)", 14 supported languages (English has interface, full audio and subtitles; French, Italian, German and Spanish - Spain are among those listed) and the requirement to agree to the WARDOGS EULA [18].

## Pre-order and beta access

Pre-orders opened on 11 Aug 2026 for the 10 Sep Early Access launch and granted guaranteed access to the Closed Beta of 21 to 23 Aug; the developer said Steam key caps ended the old signup route [4].

## Platform roadmap and statements

| Platform | Status | Date of statement | Source and class |
|----------|--------|-------------------|------------------|
| Windows (Steam) | Live, Early Access since 10 Sep 2026; Windows flag true | 2026-10-08 | [1] official |
| Mac | Store flag false | 2026-10-08 | [1] official |
| Xbox | "Sometime in 2028"; wishlists open | 10 Sep 2026 | [13] press, not in official posts |
| PS5 | "Sometime in 2028" | 11 Sep 2026 | [14] press, not in official posts |
| Steam Deck | Compatibility "Unsupported" | 2026-10-08 | [18] official |
| Linux / SteamOS | Store Linux flag false; Proton work ongoing per press | Aug to 25 Sep 2026 | [1] official flag; [15][16] press |

On 5 Sep 2026 the developers were reported to say "We do not officially support Linux and we cannot commit to having support for launch", that earlier Linux success in tests was by chance, and that buyers who expected Proton support could ask for a refund [15]. A developer comment dated 25 Sep 2026 (in the reader comments of that article) says there is no new timeline [15]. In August a developer was reported on the Steam forums as working on Proton support [16]. The Steam Deck status is officially "Unsupported" [18]; the Linux and Proton items above are press-only context. The store page names Elytra as the kernel-level anti-cheat, but press reports linking an anti-cheat to the Linux block are unconfirmed [15][18].

## Sales milestones (official Steam posts)

| Milestone | Date (UTC) | Source |
|-----------|-----------|--------|
| 1.25 million copies sold | 11 Sep 2026 | [5] |
| 2 million copies sold | 15 Sep 2026 | [6] |
| 3 million copies sold, "in just over 2 weeks since launching into Early Access" | 26 Sep 2026 | [7] |
| "3+ million sales and counting" (no new number; studio claim) | 9 Oct 2026 | [20] |
| Peak 428,666 concurrent on Steam | about 13 Sep 2026 (press) | [17] |

Earlier drafts used press figures ("over 1 million" on 13 Sep and "3 million at 18 days"). The official posts supersede them: 3 million was announced 26 Sep, 16 days after the 10 Sep launch, not 18 [7][17]. The 1.25 million post carries no detail beyond the figure and an apology for delays [5]. The 2 million post's numbers snapshot is an image and was not read [6].

# Early Access Changes & Known Issues

- 11 Aug 2026: pre-orders and Supporter Edition announced [4].
- 5 Sep 2026: developers clarified Linux is unsupported at launch (press) [15].
- 10 to 11 Sep 2026: Early Access launch, console 2028 reports (press) and the 1.25 million post [5][13][14].
- 15 Sep and 26 Sep 2026: 2 million and 3 million posts [6][7].
- No price change since launch was observed; the storefronts showed no discount on 2026-10-08 [1][2]. The 2026-10-30 snapshot (after Update 0.2.0) shows the same US and GB prices and platform flags; only store art changed, and the description text is unchanged [19].
- 9 Oct 2026: Season 02 Preview repeats the "3+ million" sales claim [20]. The 0.2.0 notes mention Steam Trading Cards and Point Shop items being added within Season 2, pending Valve's approval; they do not mention Linux, console or edition changes [20].

# Admin & Technical Notes

None found. Community Server hosting is covered in technical-servers-foundation.

# Risks & Caveats

- The store page says the price may be raised closer to full release and is higher at full release; current prices are Early Access prices [18].
- Prices are two dated snapshots (2026-10-08 and 2026-10-30, US and GB only) and Steam can alter regional prices or add sales without notice [1][2][3][19]. Non-US/GB rows were not re-fetched.
- Review counts move continuously; the 74.3% is the API all-language figure and is not comparable with English-only figures; the store page's all-language total (95,146) disagrees with the API total (109,396) for unexplained reasons [11][18].
- Console and Linux statements are press reports of developer statements, not found in the official Steam posts; treat as unconfirmed by official text.
- The cosmetic-only claim is a developer statement; pack contents may expand later [2].
- The press "18 days" and "over 1 million" sales figures conflict with the official posts and are not used [5][7].

# Open Questions

- Supporter Edition and DLC prices in regions other than US and UK.
- What the second DLC app id (4809930) is.
- Whether Xbox or PS5 will have a different edition structure or price: unpublished, and no official Steam post confirms the 2028 window.
- Whether Proton or Linux support will ship: unconfirmed (Steam Deck is officially Unsupported now [18]).
- Why the store page's all-language review total (95,146) differs from the API total (109,396) on the same day: unexplained; the review API could not be re-fetched on 2026-10-30 to test it.
- The "stair stepped pricing" steps: described in a video devlog, not in post text.
- Whether the Trading Cards and Point Shop items mentioned in the 0.2.0 notes shipped: pending Valve approval at 14 Oct 2026; not checked.
- Full-release price and 1.0 date: unpublished; only "around 1 to 2 years" and "higher price at full release" are stated [18].

# References

**Primary Sources**

- [1] **Valve / BULKHEAD** — *WARDOGS on Steam, store data for app 1867240, US and GB storefronts (snapshots/2026-10-08/store-app-us.json and store-app-gb.json)*. https://store.steampowered.com/app/1867240/WARDOGS/. Accessed 2026-10-08.
- [2] **Valve (Steam storefront)** — *Supporter Pack DLC, app 4809960, US and GB (snapshots/2026-10-08/store-dlc-supporter-pack-us.json and -gb.json)*. https://store.steampowered.com/api/appdetails?appids=4809960&cc=us. Accessed 2026-10-08.
- [3] **Valve (Steam storefront API)** — *Regional price field, country code varied per row (not part of the snapshot)*. https://store.steampowered.com/api/appdetails?appids=1867240&cc=de&filters=price_overview. Accessed 2026-10-08.
- [4] **BULKHEAD (Steam news)** — *PRE-ORDER NOW!* (11 Aug 2026). https://store.steampowered.com/news/app/1867240/view/1840310314354505. Accessed 2026-10-08.
- [5] **BULKHEAD (Steam news)** — *1.25 MILLION COPIES SOLD!* (11 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1843481262693807. Accessed 2026-10-08.
- [6] **BULKHEAD (Steam news)** — *2 MILLION COPIES SOLD* (15 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1843481262705755. Accessed 2026-10-08.
- [7] **BULKHEAD (Steam news)** — *3 Million Sales + Golden Joystick Awards [VOTE NOW!]* (26 Sep 2026). https://store.steampowered.com/news/app/1867240/view/1844751498227777. Accessed 2026-10-08.
- [8] **BULKHEAD (Steam news)** — *WARDOGS - Early Access & Beyond* (7 Apr 2026). https://store.steampowered.com/news/app/1867240/view/1828894815567544. Accessed 2026-10-08.
- [9] **BULKHEAD (Steam news)** — *WARDOGS - TOP QUESTIONS* (18 Feb 2026). https://store.steampowered.com/news/app/1867240/view/1825093633182385. Accessed 2026-10-08.
- [10] **BULKHEAD (Steam news)** — *WARDOGS - Answering Your Questions* (3 Mar 2026). https://store.steampowered.com/news/app/1867240/view/1825727806721330. Accessed 2026-10-08.
- [11] **Valve (Steam reviews API)** — *Review summary, all languages (snapshots/2026-10-08/reviews-summary.json)*. https://store.steampowered.com/appreviews/1867240?json=1&language=all. Accessed 2026-10-08.
- [12] **Team17 / BULKHEAD** — *WARDOGS is coming to Steam Early Access on 10 September* (press release). https://www.gamedeveloper.com/press-release/wardogs-is-coming-to-steam-early-access-on-10-september. Accessed 2026-10-08.

- [18] **Valve / BULKHEAD** — *WARDOGS on Steam, rendered live store page (live captures 2026-10-08 and 2026-10-30, snapshots/2026-10-08/store-page-live.txt and snapshots/2026-10-30/store-page-live.txt)*. https://store.steampowered.com/app/1867240/WARDOGS/. Accessed 2026-10-08 and 2026-10-30.
- [19] **Valve (Steam storefront)** — *WARDOGS and Supporter Pack store data, US and GB (snapshots/2026-10-30/store-app-us.json, store-app-gb.json, store-dlc-supporter-pack-us.json and -gb.json; price and platform fields compared with 2026-10-08)*. https://store.steampowered.com/app/1867240/WARDOGS/. Accessed 2026-10-30.
- [20] **BULKHEAD (Steam news)** — *WARDOGS | Season 02 Preview* (9 Oct 2026) and *Season 02 Patch Notes* (14 Oct 2026). https://store.steampowered.com/news/app/1867240/view/1846018067933823 and https://store.steampowered.com/news/app/1867240/view/1846651706674560. Accessed 2026-10-30.

**Press & Secondary**

- [13] **Pure Xbox** — *WARDOGS is coming to Xbox in 2028 and is available today with Steam Early Access*. https://www.purexbox.com/news/2026/09/wardogs-is-coming-to-xbox-in-2028-and-is-available-today-with-steam-early-access. Accessed 2026-10-08.
- [14] **Push Square** — *Multiplayer shooter WARDOGS confirmed for PS5 as Early Access launch goes nuclear*. https://www.pushsquare.com/news/2026/09/multiplayer-shooter-wardogs-confirmed-for-ps5-as-early-access-launch-goes-nuclear. Accessed 2026-10-08.
- [15] **GamingOnLinux** — *WARDOGS developers clarify Linux support via Proton may come later*. http://www.gamingonlinux.com/2026/09/wardogs-developers-clarify-linux-support-via-proton-may-come-later. Accessed 2026-10-08.
- [16] **SteamDeckHQ** — *WARDOGS devs are working on Proton support*. https://steamdeckhq.com/news/wardogs-devs-are-working-on-proton-support/. Accessed 2026-10-08.
- [17] **GosuGamers** — *WARDOGS sells 3 million copies in just over two weeks after Early Access launch* (peak concurrent figure only). https://www.gosugamers.net/entertainment/news/79260-wardogs-sells-3-million-copies-in-just-over-two-weeks-after-early-access-launch. Accessed 2026-10-08.

**Player-Reported Evidence**

None cited.

# Further Reading

- meta-release-foundation for the release timeline and patch table.

# Related Documents

- meta-release-foundation
- economy-foundation
- patch-history
- system-requirements-and-performance

# Revision History

| Version | Date | Author | Change | Approved By |
|---------|------|--------|--------|-------------|
| 0.1.0 | 2026-10-08 | Research Pipeline (virtual agent) | Initial draft. | — |
| 1.0.0 | 2026-10-08 | Orchestrator | Frozen after independent re-verification of validate, markdownlint and links (0 dead). | Standing mandate (auto-approve on green QA) |
| 1.1.0 | 2026-10-08 | Research Pipeline (revision worker) | Revised against official Steam posts and store snapshot; prices, packages and DLC contents now from snapshots, sales figures replaced with official posts (1.25M, 2M, 3M), all-language review counts, console and Linux labelled press-only, confidence re-rated. | Standing mandate (auto-approve on green QA) |
| 1.1.1 | 2026-10-08 | Research Pipeline (revision worker) | Corrected against live store-page capture; Steam Deck status now Unsupported (official), prices confirmed, official Early Access pricing policy and 1 to 2 year estimate added, store-page vs API review discrepancy recorded, interactive elements, 14 languages and Elytra anti-cheat added. | Standing mandate (auto-approve on green QA) |
| 1.2.0 | 2026-10-30 | Research Pipeline (virtual agent) | Store prices, platform flags and discount status re-checked against the 2026-10-30 storefront snapshot (US and GB, base game and Supporter Pack): unchanged after Update 0.2.0; Preview "3+ million sales" studio claim added; Trading Cards and Point Shop mention noted as pending; no Linux, console or edition statements in the 0.2.0 notes. Confidence stays Medium (console and Linux claims remain press-only). | — |
| 1.2.1 | 2026-10-30 | Research Pipeline (virtual agent) | Fresh browser capture of the live store page (2026-10-30): all Primary store-page claims unchanged since 2026-10-08 (Elytra, Steam Deck Unsupported, fighter jets, 1 to 2 years, gunplay quote, proximity and local voice chat, GBP prices); review figures recorded alongside the 2026-10-08 values; the review API could not be re-fetched. Prices (GBP 36.99, 45.99, 11.99) confirmed unchanged on the page. | — |
