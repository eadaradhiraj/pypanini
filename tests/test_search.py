"""Tests for pypanini.search (subanta/krdanta/tinanta/global). SLP1 only.

Grouped output: one entry per dhatu/stem with a readings list.
Helpers below walk groups -> readings.
"""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from pypanini.search import (analyze, best, krdanta_search, subanta_search,
                             tinanta_search)


def has_sub(res, stem, vib, vac, linga=None):
    for g in res:
        if g.get("kind") != "subanta" or g.get("stem") != stem:
            continue
        for r in g.get("readings", []):
            if (r.get("vibhakti") == vib and r.get("vacana") == vac
                    and (linga is None or r.get("linga") == linga)):
                return True
    return False


def tin_has(res, dhatu=None, lakara=None, purusha=None, vacana=None,
            upasarga=None, pada=None):
    for g in res:
        if g.get("kind") != "tinanta":
            continue
        if dhatu is not None and g.get("dhatu") != dhatu:
            continue
        if upasarga is not None and g.get("upasarga") != upasarga:
            continue
        for r in g.get("readings", []):
            if lakara is not None and r.get("lakara") != lakara:
                continue
            if purusha is not None and r.get("purusha") != purusha:
                continue
            if vacana is not None and r.get("vacana") != vacana:
                continue
            if pada is not None and r.get("pada") != pada:
                continue
            return True
    return False


def krd_has(res, dhatu=None, pratyaya=None, upasarga=None):
    for g in res:
        if g.get("kind") != "krdanta":
            continue
        if dhatu is not None and g.get("dhatu") != dhatu:
            continue
        if upasarga is not None and g.get("upasarga") != upasarga:
            continue
        for r in g.get("readings", []):
            if pratyaya is not None and r.get("pratyaya") != pratyaya:
                continue
            return True
    return False


def _tin_group(res, dhatu):
    return [g for g in res if g.get("kind") == "tinanta"
            and g.get("dhatu") == dhatu]


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
        bad = [g for g in res if g.get("kind") == "subanta"
               and g.get("stem") == "wrampa"
               for r in g.get("readings", [])
               if (r.get("vibhakti"), r.get("vacana")) == (3, "eka")]
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
        self.assertTrue(krd_has(res, "kf", "kta"), res[:5])
        res2 = krdanta_search("kartavyaH")
        self.assertTrue(krd_has(res2, "kf", "tavya"), res2[:5])

    def test_tinanta_search_only(self):
        res = tinanta_search("Bavati")
        self.assertTrue(all(r["kind"] == "tinanta" for r in res))
        self.assertTrue(tin_has(res, "BU", "lw", "prathama", "eka"), res[:5])

    def test_tinanta_unresolved_root(self):
        # gacCati: ending slot identified even though gam- stem is irregular
        res = tinanta_search("gacCati")
        self.assertTrue(tin_has(res, None, "lw", "prathama", "eka")
                        or any(r.get("lakara") == "lw"
                               and r.get("purusha") == "prathama"
                               and r.get("vacana") == "eka"
                               for g in res for r in g.get("readings", [])))

    def test_upasarga(self):
        res = tinanta_search("praBavati")
        self.assertTrue(tin_has(res, "BU", upasarga="pra"), res[:5])

    def test_upasarga_krdanta(self):
        # pra + kfta: prefixed participle splits and root-links
        res = krdanta_search("prakftaH")
        self.assertTrue(krd_has(res, "kf", "kta", "pra"), res[:5])

    def test_natva_reversal(self):
        # praRamati: R hides dental n of root nam
        res = tinanta_search("praRamati")
        self.assertTrue(tin_has(res, "nam", upasarga="pra"), res[:5])

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
        self.assertTrue(krd_has(res, "sTA", "kta", "prati"), res[:5])

    def test_global_ranking(self):
        # exact tinanta root reading outranks open-vocabulary noise
        res = analyze("Bavati")
        self.assertEqual(res[0]["kind"], "tinanta")
        self.assertEqual(res[0].get("dhatu"), "BU")

    def test_empty_unknown(self):
        self.assertEqual(analyze(""), [])
        self.assertEqual(subanta_search("xyz"), [])
        self.assertIsNone(best(""))
        self.assertEqual(best("wrampeRa")["stem"], "wrampa")

    def test_dadan(self):
        # dadan: participle nominative (default num-paradigm) + dad/laN
        # with missing-augment note + honest Satf-unresolved tail
        res = analyze("dadan")
        self.assertTrue(has_sub(res, "dadat", 1, "eka", "puM"))
        _laN = [r for g in res if g["kind"] == "tinanta"
                and g.get("dhatu") == "dad"
                for r in g.get("readings", []) if r.get("lakara") == "laN"]
        self.assertTrue(_laN, res[:5])
        self.assertIn("augment", _laN[0].get("note", ""))
        self.assertEqual(_laN[0].get("pada"), "parasmaipada")
        _dad = [g for g in res if g.get("kind") == "tinanta"
                and g.get("dhatu") == "dad"][0]
        self.assertEqual(_dad.get("dhAtu_pada"), "Atmanepadi")

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
            self.assertTrue(krd_has(_res, "dA", "Satf"), _w)

    def test_san_desiderative(self):
        # contracted (dA->dits, DA->Dits) vs full (vid->vividiz) types;
        # reduplicant aspiration picks dA over DA and vice versa.
        # Attested homonyms coexist (Ditsati is data-true for Dew 01.1050
        # san too), so assert presence in top-3, not top-1.
        for _w, _rt in (("ditsanti", "dA"), ("Ditsati", "DA"),
                        ("vividizati", "vid")):
            _tins = [g for g in analyze(_w) if g["kind"] == "tinanta"
                     and g.get("dhatu")]
            self.assertTrue(any(g.get("dhatu") == _rt for g in _tins[:3]),
                            (_w, _tins[:3]))

    def test_ditsanti_grounded_011079(self):
        # ditsanti must be the attested sannanta-kartari-laW of 01.1079 (dAR):
        # analysis triple + dhAtu ID + JSON attestation all agree
        _res = _tin_group(analyze("ditsanti"), "dA")
        self.assertTrue(_res, "no dA reading")
        _top = _res[0]
        self.assertTrue(any(r.get("lakara") == "lw" and r.get("purusha") == "prathama"
                            and r.get("vacana") == "bahu" for r in _top["readings"]),
                        _top)
        self.assertIn("01.1079", _top.get("ids", []), _top)
        import json as _json
        from pathlib import Path as _Path
        _jf = _Path("skt-morph-data/01/01.1079.json")
        if not _jf.exists():
            _jf = _Path("/home/edhiraj/Documents/projs/skt-morph-data/data/01/01.1079.json")
        with open(_jf, encoding="utf-8") as _fh:
            _data = _json.load(_fh)

        def _toks(_o):
            _s = set()
            if isinstance(_o, str):
                for _p in _o.split("/"):
                    _p = _p.strip()
                    if _p:
                        _s.add(_p)
            elif isinstance(_o, list):
                for _i in _o:
                    _s |= _toks(_i)
            elif isinstance(_o, dict):
                for _v in _o.values():
                    _s |= _toks(_v)
            return _s
        self.assertIn("ditsanti", _toks(_data.get("conjugations", {}).get("san", {})))


if __name__ == "__main__":
    unittest.main()
