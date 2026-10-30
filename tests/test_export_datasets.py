"""Tests for scripts/export_datasets.py. Run: python -m unittest discover -s tests"""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import export_datasets as ex  # noqa: E402

A = ex.ARROW


class CellParsers(unittest.TestCase):
    def test_money(self):
        self.assertEqual(ex.parse_money("$1,000"), 1000)
        self.assertEqual(ex.parse_money("$12.5k"), 12500)
        self.assertEqual(ex.parse_money("$350k"), 350000)
        with self.assertRaises(ex.ParseError):
            ex.parse_money("about $5")

    def test_level_plain_and_change(self):
        self.assertEqual(ex.parse_level("13")["level"], 13)
        r = ex.parse_level(f"15 {A} 4")
        self.assertEqual((r["level_prev"], r["level"]), (15, 4))

    def test_level_default_forms(self):
        r = ex.parse_level(f"unlocked by default {A} 5")
        self.assertTrue(r["level_prev_default"])
        self.assertEqual(r["level"], 5)
        r = ex.parse_level(f"previously 3 {A} unlocked by default")
        self.assertEqual(r["level_prev"], 3)
        self.assertTrue(r["level_default"])
        self.assertTrue(ex.parse_level(f"previously unlocked by default {A} 7")["level_prev_default"])

    def test_level_not_changed_and_not_stated(self):
        self.assertEqual(ex.parse_level("n/c")["level_status"], "not_changed")
        self.assertEqual(ex.parse_level("reshuffled between Driver and Pilot; no per-tape values stated")["level_status"], "not_stated")

    def test_level_annotation_kept(self):
        r = ex.parse_level(f"20 {A} 28 (the TCX-SPR takes its place)")
        self.assertEqual((r["level_prev"], r["level"], r["note"]), (20, 28, "the TCX-SPR takes its place"))

    def test_level_rejects_unknown(self):
        with self.assertRaises(ex.ParseError):
            ex.parse_level("sometime later")

    def test_cost_forms(self):
        self.assertEqual(ex.parse_cost("$25k")["cost"], 25000)
        r = ex.parse_cost(f"$75k {A} $25k")
        self.assertEqual((r["cost_prev"], r["cost"]), (75000, 25000))
        self.assertEqual(ex.parse_cost("n/c")["cost_status"], "not_changed")
        self.assertEqual(ex.parse_cost("not stated")["cost_status"], "not_stated")
        self.assertEqual(ex.parse_cost("none")["cost_status"], "none")
        r = ex.parse_cost("previously $10k")
        self.assertEqual((r["cost_prev"], r["cost_status"]), (10000, "now_none"))
        r = ex.parse_cost(f"$10k {A} free (comes with the T-21)")
        self.assertEqual((r["cost"], r["cost_status"], r["cost_note"]), (0, "free", "comes with the T-21"))
        self.assertIsNone(ex.parse_cost(f"{A} $10k")["cost_prev"])

    def test_slug(self):
        self.assertEqual(ex.slug("Wolf-110 [M2 Browning]"), "wolf-110-m2-browning")


class TableReader(unittest.TestCase):
    def test_reads_heading_header_rows(self):
        t = ex.read_tables("## Sec\n\n| A | B |\n|---|---|\n| 1 | 2 |\n| 3 | 4 |\n")
        self.assertEqual(t[0]["heading"], "Sec")
        self.assertEqual(t[0]["header"], ["A", "B"])
        self.assertEqual(t[0]["rows"], [["1", "2"], ["3", "4"]])


class StrictExtraction(unittest.TestCase):
    FM = {"version": "1.0.0", "confidence": "High", "id": "x"}

    def test_price_direction_is_checked(self):
        text = "### Price increases\n\n| Item | Season 1 (0.1.2) | Season 02 (0.2.0) |\n|---|---|---|\n| Thing | $500 | $100 |\n"
        with self.assertRaises(ex.ParseError):
            ex.extract_items(text, self.FM)

    def test_unknown_unlock_cell_fails_loudly(self):
        text = "### Assault: additional unlocks\n\n| Item | Level | Cost |\n|---|---|---|\n| Thing | 4 | lots |\n"
        with self.assertRaises(ex.ParseError):
            ex.extract_unlocks(text, self.FM)

    def test_xp_levels_must_ascend(self):
        text = ("## Season 02 role-track XP curve (Update 0.2.0)\n\n| Level | Old | New | Change | S1 |\n|---|---|---|---|---|\n"
                "| 20 | 250,000 | 111,500 | 55% quicker | 250,000 |\n| 10 | 35,000 | 25,000 | 29% quicker | 35,000 |\n")
        with self.assertRaises(ex.ParseError):
            ex.extract_xp(text, self.FM)


class RealDocs(unittest.TestCase):
    """Known 0.2.0 values from the official notes, via the real docs."""

    @classmethod
    def setUpClass(cls):
        cls.d = ex.build(ROOT / "docs")

    def item(self, i):
        return next(r for r in self.d["items"] if r["item_id"] == i)

    def unlock(self, track, i):
        return next(r for r in self.d["unlocks"] if r["unlock_id"] == f"{track}:{i}")

    def test_prices(self):
        r = self.item("tcx-spr")
        self.assertEqual((r["price"], r["price_prev"], r["change"]), (3200, None, "new"))
        r = self.item("ak74")
        self.assertEqual((r["price"], r["price_prev"]), (800, 1600))
        r = self.item("l2a6")
        self.assertEqual((r["price"], r["price_prev"]), (22000, 14000))

    def test_unlocks(self):
        r = self.unlock("assault", "molotov-cocktail")
        self.assertEqual((r["level"], r["cost"]), (13, 25000))
        r = self.unlock("medic", "medical-bag")
        self.assertEqual((r["level_prev"], r["level"], r["cost_prev"], r["cost"]), (24, 14, 75000, 50000))
        r = self.unlock("driver", "sph-2")
        self.assertEqual((r["moved_from_track"], r["moved_from_level"], r["level"]), ("WARDOG", 90, 31))

    def test_xp_curve_and_conflict(self):
        by = {r["level"]: r for r in self.d["xp_curve"]}
        self.assertEqual(by[20]["xp_season02"], 111500)
        self.assertFalse(by[20]["before_values_conflict"])
        self.assertTrue(by[25]["before_values_conflict"])
        self.assertEqual((by[25]["xp_before_per_notes"], by[25]["xp_season1_changelog"]), (365000, 325000))

    def test_conflict_rows_keep_both_values_in_changes(self):
        c = next(r for r in self.d["changes"] if r["subject"] == "Level 25 total XP")
        self.assertEqual((c["before"], c["before_alt"], c["status"]), (365000, 325000, "conflict"))

    def test_ids_unique_and_counts_match(self):
        ids = [r["change_id"] for r in self.d["changes"]]
        self.assertEqual(len(ids), len(set(ids)))
        for k, n in self.d["meta"]["counts"].items():
            self.assertEqual(len(self.d[k]), n)


if __name__ == "__main__":
    unittest.main()
