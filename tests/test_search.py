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

    def test_upasarga_krdanta(self):
        # pra + kfta: prefixed participle splits and root-links
        res = krdanta_search("prakftaH")
        self.assertTrue(any(r.get("dhatu") == "kf" and r.get("pratyaya") == "kta"
                            and r.get("upasarga") == "pra" for r in res), res[:5])

    def test_natva_reversal(self):
        # praRamati: R hides dental n of root nam
        res = tinanta_search("praRamati")
        self.assertTrue(any(r.get("dhatu") == "nam" and r.get("upasarga") == "pra"
                            for r in res), res[:5])

    def test_unadi_boundary(self):
        # sTira is uNAdi (kira), outside the 14-krt engine: no krdanta reading,
        # even with prati- split + reverse sandhi. Subanta still analyses it.
        self.assertEqual(krdanta_search("pratizWira"), [])
        self.assertTrue(has_sub(subanta_search("pratizWireRa"), "pratizWira", 3, "eka"))

    def test_prefix_double_sandhi(self):
        # prati + sTita (kta of sTA): zatva + zwutva reversed, root linked
        from pypanini.search import _rev_prefix_sandhi
        self.assertEqual(_rev_prefix_sandhi("zWira"), ["zWira", "sWira", "sTira"])
        res = krdanta_search("pratizWitaH")
        self.assertTrue(any(r.get("dhatu") == "sTA" and r.get("pratyaya") == "kta"
                            and r.get("upasarga") == "prati" for r in res), res[:5])

    def test_global_ranking(self):
        # exact tinanta root reading outranks open-vocabulary noise
        res = analyze("Bavati")
        self.assertEqual(res[0]["kind"], "tinanta")
        self.assertEqual(res[0].get("dhatu"), "BU")

    def test_empty_unknown(self):
        self.assertEqual(analyze(""), [])
        self.assertEqual(subanta_search("xyz"), [])

    def test_dadan(self):
        # dadan: participle nominative (default num-paradigm) + dad/laN
        # with missing-augment note + honest Satf-unresolved tail
        res = analyze("dadan")
        self.assertTrue(has_sub(res, "dadat", 1, "eka", "puM"))
        _laN = [r for r in res if r["kind"] == "tinanta" and r.get("dhatu") == "dad"
                and r.get("lakara") == "laN"]
        self.assertTrue(_laN, res[:5])
        self.assertIn("augment", _laN[0].get("note", ""))
        self.assertEqual(_laN[0].get("pada"), "parasmaipada")
        self.assertEqual(_laN[0].get("dhAtu_pada"), "Atmanepadi")

    def test_dadat_abhyasta(self):
        # class-3 dadat bans num (7.1.78): bare form is the nominative
        from pypanini.subanta import SubantaEngine
        se = SubantaEngine()
        self.assertEqual(se.decline("dadat", "puM", extra={"abhyasta": True})[(1, "eka")],
                         ["dadat"])
        res = analyze("dadat")
        self.assertTrue(has_sub(res, "dadat", 1, "eka", "puM"))

    def test_satf_abhyasa_root(self):
        # dadan/dadat: abhyasa reversal links dA (now full: juhoti/biBar too)
        for _w in ("dadan", "dadat"):
            _res = analyze(_w)
            self.assertTrue(any(r["kind"] == "krdanta" and r.get("dhatu") == "dA"
                                and r.get("pratyaya") == "Satf" for r in _res), _w)

    def test_san_desiderative(self):
        # contracted (dA->dits, DA->Dits) vs full (vid->vividiz) types;
        # reduplicant aspiration picks dA over DA and vice versa
        for _w, _rt in (("ditsanti", "dA"), ("Ditsati", "DA"),
                        ("vividizati", "vid")):
            _res = [r for r in analyze(_w) if r["kind"] == "tinanta"
                    and r.get("dhatu")]
            self.assertTrue(_res and _res[0].get("dhatu") == _rt, (_w, _res[:3]))


if __name__ == "__main__":
    unittest.main()
