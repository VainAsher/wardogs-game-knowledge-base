#!/usr/bin/env python3
"""Snapshot official Steam news for the app into snapshots/<date>/steam-news/.

Writes one .md per official (steam_community_announcements) post plus index.json,
so later runs can be diffed for staleness checks. Network required.
Usage: python scripts/snapshot_steam_news.py [--appid 1867240] [--out snapshots]
"""
import argparse, datetime, hashlib, json, re, urllib.request
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--appid", default="1867240")
ap.add_argument("--out", default="snapshots")
a = ap.parse_args()
url = (f"https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid={a.appid}"
       "&count=100&maxlength=0&format=json")
data = json.load(urllib.request.urlopen(url, timeout=60))
items = data["appnews"]["newsitems"]
day = datetime.date.today().isoformat()
out = Path(a.out) / day / "steam-news"
out.mkdir(parents=True, exist_ok=True)
index = []
for it in items:
    official = it.get("feedname") == "steam_community_announcements"
    ts = datetime.datetime.fromtimestamp(it["date"], datetime.timezone.utc)
    slug = re.sub(r"[^a-z0-9]+", "-", it["title"].lower()).strip("-")[:60]
    name = f"{ts:%Y-%m-%d}-{it['gid']}-{slug}.md" if official else None
    body = it["contents"]
    index.append({"gid": it["gid"], "date_utc": ts.isoformat(), "title": it["title"],
                  "feed": it.get("feedname"), "official": official, "url": it.get("url"),
                  "sha256": hashlib.sha256(body.encode()).hexdigest(), "file": name})
    if official:
        (out / name).write_text(
            f"# {it['title']}\n\n- Posted (UTC): {ts.isoformat()}\n- Feed: {it.get('feedname')}\n"
            f"- URL: {it.get('url')}\n- Snapshot taken: {day}\n\n---\n\n{body}\n", encoding="utf-8")
(out / "index.json").write_text(json.dumps(index, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"{len(items)} items, {sum(i['official'] for i in index)} official -> {out}")

# Store page data (description, price, requirements, DLC, review counts).
for label, aid in (("app", a.appid), ("dlc-supporter-pack", "4809960")):
    for cc in ("us", "gb"):
        u = f"https://store.steampowered.com/api/appdetails?appids={aid}&cc={cc}&l=english"
        try:
            d = json.load(urllib.request.urlopen(u, timeout=60))
            (out.parent / f"store-{label}-{cc}.json").write_text(
                json.dumps(d, indent=2, ensure_ascii=False), encoding="utf-8")
        except Exception as e:  # network/rate-limit: record and continue
            print("store fetch failed", label, cc, e)
try:
    u = f"https://store.steampowered.com/appreviews/{a.appid}?json=1&language=all&purchase_type=all&num_per_page=0"
    (out.parent / "reviews-summary.json").write_text(
        json.dumps(json.load(urllib.request.urlopen(u, timeout=60)), indent=2), encoding="utf-8")
except Exception as e:
    print("reviews fetch failed", e)
