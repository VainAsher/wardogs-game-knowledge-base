#!/usr/bin/env python3
"""
Export the knowledge base's tables as versioned, machine-readable datasets.

Reads the Season 02 (Update 0.2.0) tables in the docs and writes JSON under
exports/datasets/ for downstream consumers (the community site). The KB stays
the single source of truth: every record carries its source document, section,
document version, confidence and a status, so a site can show provenance.

Strict by design: a table row that does not match a known shape raises an error
(exit 1) instead of being guessed at or dropped.

Datasets
  meta.json       game version, source docs (version, confidence, review_due), counts
  items.json      vendor prices from price-tables-season-1 (Season 02 sections)
  unlocks.json    role-track unlocks from progression-unlock-tables (0.2.0 sections)
  xp_curve.json   role-track XP curve, with the Season 1 source conflict flagged
  changes.json    before/after rows derived from the three datasets above

Usage
  python scripts/export_datasets.py [--docs docs] [--out exports/datasets]
  python scripts/export_datasets.py --check     # exit 1 if committed files are stale
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("ERROR: PyYAML is required (pip install pyyaml)", file=sys.stderr)
    sys.exit(2)

PRICE_DOC = "economy/price-tables-season-1.md"
UNLOCK_DOC = "gameplay-modes/progression-unlock-tables.md"
DATASET_VERSION = 1
ARROW = "→"
TRACKS = ("WARDOG", "Assault", "Medic", "Recon", "Support", "Driver", "Pilot")


class ParseError(ValueError):
    pass


# ── Markdown tables ──────────────────────────────────────────────────────────

def split_cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def read_tables(text: str) -> list[dict]:
    """Return every pipe table with its nearest heading, header and body rows."""
    lines = text.split("\n")
    tables, heading, i = [], "", 0
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("#"):
            heading = ln.lstrip("#").strip()
            i += 1
            continue
        if ln.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:|-]+\|?\s*$", lines[i + 1]):
            header, rows, j = split_cells(ln), [], i + 2
            while j < len(lines) and lines[j].startswith("|"):
                rows.append(split_cells(lines[j]))
                j += 1
            tables.append({"heading": heading, "header": header, "rows": rows})
            i = j
            continue
        i += 1
    return tables


def front_matter(text: str) -> dict:
    return yaml.safe_load(text.split("---")[1])


# ── Cell parsers ─────────────────────────────────────────────────────────────

MONEY_RE = re.compile(r"^\$(\d[\d,]*(?:\.\d+)?)(k)?$")


def parse_money(s: str) -> int:
    m = MONEY_RE.match(s.strip())
    if not m:
        raise ParseError(f"not a money value: {s!r}")
    val = float(m.group(1).replace(",", "")) * (1000 if m.group(2) else 1)
    return int(round(val))


def parse_int(s: str) -> int:
    t = s.strip().replace(",", "")
    if not re.fullmatch(r"\d+", t):
        raise ParseError(f"not an integer: {s!r}")
    return int(t)


def slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def _split_note(s: str) -> tuple[str, str | None]:
    m = re.match(r"^(.*?)\s*\((.+)\)$", s.strip())
    return (m.group(1).strip(), m.group(2).strip()) if m else (s.strip(), None)


def _level_side(x: str) -> tuple[int | None, bool]:
    x = re.sub(r"^previously\s+", "", x.strip())
    if x == "unlocked by default":
        return None, True
    return parse_int(x), False


def parse_level(raw: str) -> dict:
    s, note = _split_note(raw)
    base = {"level": None, "level_prev": None, "level_default": False, "level_prev_default": False, "note": note}
    if s == "n/c":
        return {**base, "level_status": "not_changed"}
    if "no per-tape values" in s or s.startswith('"reshuffled') or s.startswith("reshuffled"):
        return {**base, "level_status": "not_stated", "note": raw.strip()}
    if ARROW in s:
        a, b = (x.strip() for x in s.split(ARROW, 1))
        prev, prev_d = _level_side(a)
        now, now_d = _level_side(b)
        return {**base, "level": now, "level_prev": prev, "level_default": now_d, "level_prev_default": prev_d, "level_status": "stated"}
    now, now_d = _level_side(s)
    return {**base, "level": now, "level_default": now_d, "level_status": "stated"}


def parse_cost(raw: str) -> dict:
    s, note = _split_note(raw)
    base = {"cost": None, "cost_prev": None, "cost_status": "stated", "cost_note": note}
    if s == "n/c":
        return {**base, "cost_status": "not_changed"}
    if s == "not stated":
        return {**base, "cost_status": "not_stated"}
    if s == "none":
        return {**base, "cost_status": "none"}
    if s.startswith("previously "):
        return {**base, "cost_prev": parse_money(s[len("previously "):]), "cost_status": "now_none"}
    if ARROW in s:
        a, b = (x.strip() for x in s.split(ARROW, 1))
        prev = parse_money(a) if a else None
        if b == "free":
            return {**base, "cost": 0, "cost_prev": prev, "cost_status": "free"}
        return {**base, "cost": parse_money(b), "cost_prev": prev}
    return {**base, "cost": parse_money(s)}


# ── Extractors ───────────────────────────────────────────────────────────────

def prov(doc_id: str, fm: dict, section: str) -> dict:
    return {"source_doc": doc_id, "source_section": section, "doc_version": str(fm["version"]), "confidence": fm["confidence"]}


def extract_items(text: str, fm: dict) -> list[dict]:
    kinds = {
        "New items (no previous price)": "new",
        "Price increases": "increase",
        "Price decreases": "decrease",
        "Attachment price decreases": "decrease",
    }
    out = []
    for t in read_tables(text):
        kind = kinds.get(t["heading"])
        if not kind:
            continue
        for row in t["rows"]:
            if kind == "new":
                if len(row) != 3:
                    raise ParseError(f"{t['heading']}: expected 3 cells, got {row}")
                name, typ, price = row
                rec = {"type": typ, "price": parse_money(price), "price_prev": None}
            else:
                if len(row) != 3:
                    raise ParseError(f"{t['heading']}: expected 3 cells, got {row}")
                name, prev, now = row
                rec = {"type": "Attachment" if t["heading"].startswith("Attachment") else None,
                       "price": parse_money(now), "price_prev": parse_money(prev)}
                if kind == "increase" and not rec["price"] > rec["price_prev"]:
                    raise ParseError(f"{name}: listed as an increase but {rec['price_prev']} -> {rec['price']}")
                if kind == "decrease" and not rec["price"] < rec["price_prev"]:
                    raise ParseError(f"{name}: listed as a decrease but {rec['price_prev']} -> {rec['price']}")
            out.append({"item_id": slug(name), "name": name, **rec, "change": kind, "status": "verified",
                        **prov("price-tables-season-1", fm, t["heading"])})
    if not out:
        raise ParseError("no Season 02 price rows found")
    return out


UNLOCK_HEADING = re.compile(r"^(WARDOG|Assault|Medic|Recon|Support|Driver):\s+(additional unlocks|moved into the track|track changes)$")
UNLOCK_KIND = {"additional unlocks": "additional", "moved into the track": "moved", "track changes": "changed"}
MOVED_RE = re.compile(r"^(WARDOG|Assault|Medic|Recon|Support|Driver) level (\d+)$")


def extract_unlocks(text: str, fm: dict) -> list[dict]:
    out = []
    for t in read_tables(text):
        m = UNLOCK_HEADING.match(t["heading"])
        if m:
            track, kind = m.group(1), UNLOCK_KIND[m.group(2)]
        elif t["heading"] == "Pilot track":
            track, kind = "Pilot", "changed"
        else:
            continue
        hdr = t["header"]
        if not hdr or hdr[0] != "Item" or "Level" not in hdr:
            raise ParseError(f"{t['heading']}: unexpected header {hdr}")
        ix = {h: k for k, h in enumerate(hdr)}
        for row in t["rows"]:
            if len(row) != len(hdr):
                raise ParseError(f"{t['heading']}: row has {len(row)} cells, header has {len(hdr)}: {row}")
            name = row[ix["Item"]]
            rec = {"unlock_id": f"{slug(track)}:{slug(name)}", "item_id": slug(name), "name": name, "track": track, "kind": kind}
            rec.update(parse_level(row[ix["Level"]]))
            rec.update(parse_cost(row[ix["Cost"]]) if "Cost" in ix else
                       {"cost": None, "cost_prev": None, "cost_status": "not_stated", "cost_note": None})
            rec["moved_from_track"] = rec["moved_from_level"] = None
            if "Moved from" in ix:
                mm = MOVED_RE.match(row[ix["Moved from"]])
                if not mm:
                    raise ParseError(f"{t['heading']}: unrecognised 'Moved from' cell {row[ix['Moved from']]!r}")
                rec["moved_from_track"], rec["moved_from_level"] = mm.group(1), int(mm.group(2))
            if "Note" in ix and row[ix["Note"]]:
                rec["note"] = "; ".join(x for x in (rec["note"], row[ix["Note"]]) if x)
            out.append({**rec, "status": "verified", **prov("progression-unlock-tables", fm, t["heading"])})
    if not out:
        raise ParseError("no 0.2.0 unlock rows found")
    ids = [r["unlock_id"] for r in out]
    dups = sorted({i for i in ids if ids.count(i) > 1})
    if dups:
        raise ParseError(f"duplicate unlock ids: {dups}")
    return out


def extract_xp(text: str, fm: dict) -> list[dict]:
    out = []
    for t in read_tables(text):
        if not t["heading"].startswith("Season 02 role-track XP curve"):
            continue
        for row in t["rows"]:
            if len(row) != 5:
                raise ParseError(f"XP curve: expected 5 cells, got {row}")
            lvl, before, now, change, s1 = row
            before_i, now_i, s1_i = parse_int(before), parse_int(now), parse_int(s1)
            pct = re.match(r"^(\d+)% quicker$", change)
            out.append({"level": parse_int(lvl), "xp_season02": now_i, "xp_before_per_notes": before_i,
                        "xp_season1_changelog": s1_i, "before_values_conflict": before_i != s1_i,
                        "change_stated_pct_quicker": int(pct.group(1)) if pct else None,
                        "status": "conflict" if before_i != s1_i else "verified",
                        **prov("progression-unlock-tables", fm, t["heading"])})
    if not out:
        raise ParseError("no XP curve rows found")
    levels = [r["level"] for r in out]
    if levels != sorted(levels) or len(set(levels)) != len(levels):
        raise ParseError(f"XP curve levels not strictly ascending: {levels}")
    return out


def build_changes(items: list[dict], unlocks: list[dict], xp: list[dict]) -> list[dict]:
    out = []
    for r in items:
        if r["change"] == "new":
            out.append({"category": "Prices", "subject": r["name"], "field": "price", "before": None, "after": r["price"],
                        "unit": "usd_in_game", "direction": "new"})
        else:
            out.append({"category": "Prices", "subject": r["name"], "field": "price", "before": r["price_prev"], "after": r["price"],
                        "unit": "usd_in_game", "direction": "up" if r["change"] == "increase" else "down"})
        out[-1].update({k: r[k] for k in ("source_doc", "source_section", "doc_version", "confidence", "status")})
    for r in xp:
        out.append({"category": "Progression", "subject": f"Level {r['level']} total XP", "field": "xp",
                    "before": r["xp_before_per_notes"], "after": r["xp_season02"], "unit": "xp",
                    "direction": "up" if r["xp_season02"] > r["xp_before_per_notes"] else "down",
                    # When the 0.2.0 notes and the Season 1 changelog disagree on the old value, keep both.
                    "before_alt": r["xp_season1_changelog"] if r["before_values_conflict"] else None,
                    "before_alt_source": "Season 1 changelog (9 Sep 2026)" if r["before_values_conflict"] else None,
                    **{k: r[k] for k in ("source_doc", "source_section", "doc_version", "confidence", "status")}})
    for r in unlocks:
        if r["kind"] != "changed":
            continue
        if r["level_status"] == "stated" and r["level_prev"] is not None and r["level"] is not None and r["level_prev"] != r["level"]:
            out.append({"category": "Progression", "subject": f"{r['name']} ({r['track']} unlock level)", "field": "unlock_level",
                        "before": r["level_prev"], "after": r["level"], "unit": "level",
                        "direction": "up" if r["level"] > r["level_prev"] else "down",
                        **{k: r[k] for k in ("source_doc", "source_section", "doc_version", "confidence", "status")}})
        if r["cost_prev"] is not None and r["cost"] is not None and r["cost_prev"] != r["cost"]:
            out.append({"category": "Progression", "subject": f"{r['name']} ({r['track']} unlock cost)", "field": "unlock_cost",
                        "before": r["cost_prev"], "after": r["cost"], "unit": "usd_in_game",
                        "direction": "up" if r["cost"] > r["cost_prev"] else "down",
                        **{k: r[k] for k in ("source_doc", "source_section", "doc_version", "confidence", "status")}})
    for n, r in enumerate(out, 1):
        r["change_id"] = f"c{n:04d}"
    return out


# ── Driver ───────────────────────────────────────────────────────────────────

def build(docs_dir: Path) -> dict[str, object]:
    ptext = (docs_dir / PRICE_DOC).read_text(encoding="utf-8")
    utext = (docs_dir / UNLOCK_DOC).read_text(encoding="utf-8")
    pfm, ufm = front_matter(ptext), front_matter(utext)
    items = extract_items(ptext, pfm)
    unlocks = extract_unlocks(utext, ufm)
    xp = extract_xp(utext, ufm)
    changes = build_changes(items, unlocks, xp)
    item_ids = {r["item_id"] for r in items}
    meta = {
        "dataset_version": DATASET_VERSION,
        "game_version": str(pfm["game_version"]),
        "sources_verified": max(str(pfm["sources_verified"]), str(ufm["sources_verified"])),
        "docs": [{"id": fm["id"], "version": str(fm["version"]), "confidence": fm["confidence"], "status": fm["status"],
                  "review_due": str(fm["review_due"])} for fm in (pfm, ufm)],
        "counts": {"items": len(items), "unlocks": len(unlocks), "xp_curve": len(xp), "changes": len(changes)},
        "notes": [
            "Generated by scripts/export_datasets.py from the KB docs; do not edit by hand.",
            "Statuses: verified (official notes), conflict (sources disagree, both values kept). A null price, level or cost means the notes do not give it; see the *_status fields.",
            "unlocks.item_id matches items.item_id only when the two docs use the same item name (join is partial).",
            f"{sum(1 for r in unlocks if r['item_id'] in item_ids)} of {len(unlocks)} unlock rows share an item_id with a price row.",
            "Combat, building and economy changes are prose in the docs and are not in changes.json yet.",
        ],
    }
    return {"meta": meta, "items": items, "unlocks": unlocks, "xp_curve": xp, "changes": changes}


def render(obj: object) -> bytes:
    return (json.dumps(obj, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--docs", default="docs")
    ap.add_argument("--out", default="exports/datasets")
    ap.add_argument("--check", action="store_true", help="exit 1 if the committed files differ from a fresh export")
    a = ap.parse_args()
    try:
        data = build(Path(a.docs))
    except ParseError as e:
        print(f"EXPORT FAILED: {e}", file=sys.stderr)
        return 1
    out = Path(a.out)
    stale = []
    for name, obj in data.items():
        path, new = out / f"{name}.json", render(obj)
        if a.check:
            if not path.exists() or path.read_bytes().replace(b"\r\n", b"\n") != new:
                stale.append(path.as_posix())
        else:
            out.mkdir(parents=True, exist_ok=True)
            path.write_bytes(new)
    if a.check:
        if stale:
            print("STALE datasets (run python scripts/export_datasets.py and commit): " + ", ".join(stale), file=sys.stderr)
            return 1
        print("datasets up to date")
        return 0
    c = data["meta"]["counts"]  # type: ignore[index]
    print(f"Wrote {out.as_posix()}/: items {c['items']}, unlocks {c['unlocks']}, xp_curve {c['xp_curve']}, changes {c['changes']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
