"""Tests for pypanini.search (subanta/krdanta/tinanta/global). SLP1 only."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from pypanini.search import (analyze, best, krdanta_search, subanta_search,
                             tinanta_search)


def has_sub(res, stem, vib, vac, linga=None):
    return any(r["kind"] == "subanta" and r["stem"] == stem
               and r["vibhakti"] == vib and r["vacana"] == vac
               and (linga is None or r["linga"] == linga) for r in res)


class TestSearch(unittest.TestCase):
    def test_trump_instrumental(self):
        # wrampeRa (Trump, instrumental) -> base wrampa, trtIyA eka
        # (SLP1 p = unaspirated p, as in English "Trump")
        res = analyze("wrampeRa")
        self.assertTrue(has_sub(res, "wrampa", 3, "eka", "puM"), res[:5])

    def test_trump_dental_rejected(self):
        # dental *wrampena is ungrammatical (Natva obligatory after r):
        # no instrumental reading of wrampa may appear
        res = analyze("wrampena")
        bad = [r for r in res if r["kind"] == "subanta"
               and r["stem"] == "wrampa" and (r["vibhakti"], r["vacana"]) == (3, "eka")]
        self.assertEqual(bad, [])

    def test_bare_stem_vocative(self):
        # bare foreign stem reads as sambodhana (su-lopa)
        res = analyze("wrampa")
        self.assertTrue(has_sub(res, "wrampa", 8, "eka", "puM"))

    def test_subanta_search_only(self):
        res = subanta_search("rAmaH")
        self.assertTrue(all(r["kind"] == "subanta" for r in res))
        self.assertTrue(has_sub(res, "rAma", 1, "eka", "puM"))

    def test_krdanta_search_only(self):
        res = krdanta_search("kftaH")
        self.assertTrue(all(r["kind"] == "krdanta" for r in res))
        top = [r for r in res if r.get("dhatu") == "kf" and r.get("pratyaya") == "kta"]
        self.assertTrue(top, res[:5])
        res2 = krdanta_search("kartavyaH")
        self.assertTrue(any(r.get("dhatu") == "kf" and r.get("pratyaya") == "tavya"
                            for r in res2), res2[:5])

    def test_tinanta_search_only(self):
        res = tinanta_search("Bavati")
        self.assertTrue(all(r["kind"] == "tinanta" for r in res))
        top = [r for r in res if r.get("dhatu") == "BU" and r.get("lakara") == "lw"
               and r.get("purusha") == "prathama" and r.get("vacana") == "eka"]
        self.assertTrue(top, res[:5])

    def test_tinanta_unresolved_root(self):
        # gacCati: ending slot identified even though gam- stem is irregular
        res = tinanta_search("gacCati")
        self.assertTrue(any(r.get("lakara") == "lw" and r.get("purusha") == "prathama"
                            and r.get("vacana") == "eka" for r in res))

    def test_upasarga(self):
        res = tinanta_search("praBavati")
        self.assertTrue(any(r.get("dhatu") == "BU" and r.get("upasarga") == "pra"
                            for r in res), res[:5])

    def test_global_ranking(self):
        # exact tinanta root reading outranks open-vocabulary noise
        res = analyze("Bavati")
        self.assertEqual(res[0]["kind"], "tinanta")
        self.assertEqual(res[0].get("dhatu"), "BU")

    def test_empty_unknown(self):
        self.assertEqual(analyze(""), [])
        self.assertEqual(subanta_search("xyz"), [])


if __name__ == "__main__":
    unittest.main()
