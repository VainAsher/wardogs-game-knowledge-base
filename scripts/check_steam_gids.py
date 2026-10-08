#!/usr/bin/env python3
"""Verify every cited Steam news post id exists in the newest snapshot index.

The link checker cannot prove these links (store.steampowered.com returns 200 for
any id), so this offline gate checks ids against snapshots/<date>/steam-news/index.json.
Usage: python scripts/check_steam_gids.py [--docs docs] [--snapshots snapshots]
Exit 0 = all cited ids known; 1 = unknown id(s).
"""
import argparse, json, re, sys
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--docs", default="docs")
ap.add_argument("--snapshots", default="snapshots")
a = ap.parse_args()
idx = sorted(Path(a.snapshots).glob("*/steam-news/index.json"))
if not idx:
    print("no snapshot index found", file=sys.stderr); sys.exit(2)
known = {i["gid"]: i for f in idx for i in json.loads(f.read_text(encoding="utf-8"))}
pat = re.compile(r"(?:news/app/\d+/view|announcements/detail)/(\d{10,})")
bad, cited = [], set()
for f in sorted(Path(a.docs).rglob("*.md")):
    for gid in pat.findall(f.read_text(encoding="utf-8")):
        cited.add(gid)
        if gid not in known:
            bad.append((f.as_posix(), gid))
for f, g in bad:
    print(f"UNKNOWN  {g}  in {f}")
print(f"{len(cited)} distinct Steam post ids cited; {len(bad)} unknown")
sys.exit(1 if bad else 0)
