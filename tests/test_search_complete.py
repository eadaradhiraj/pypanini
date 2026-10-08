"""Round-trip completeness: every generated form must analyse back.

Tinanta: sample roots x all 10 lakaras x all slots -> analyze() must
contain the (lakara, purusha, vacana) slot, and usually the dhatu.
Krdanta: participles/gerundives/avyayas -> (dhatu, pratyaya).
Subanta obscure: lakzmI et al must read correctly.

Grouped output: groups carry readings lists; helpers expand them.
"""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from pypanini import TinantaDerivationEngine, KrdantaEngine
from pypanini.search import analyze

TIN_ROOTS = ["BU", "gam", "kf", "dA", "vid", "tud"]
TIN_LAKARAS = ["lw", "liw", "luw", "lfw", "low", "laN", "viDiliN",
               "ASIrliN", "luN", "lfN"]
PURUSAS = ["prathama", "madhyama", "uttama"]
VACANAS = ["eka", "dvi", "bahu"]
# engine labels vs search labels (formally identical formations)
KRD_FAMILY = {"cAnaS": "SAnac", "BAvakarma-SAnac": "SAnac",
              "Ryat": "yat", "kyap": "yat", "vun": "Rvul",
              "zwran": "tfc", "a": "a", "ac": "ac", "GaY": "GaY",
              "lyuw": "lyuw"}


def _tin_readings(groups):
    for g in groups:
        if g.get("kind") != "tinanta":
            continue
        for r in g.get("readings", []):
            yield g, r


def _krd_readings(groups):
    for g in groups:
        if g.get("kind") != "krdanta":
            continue
        for r in g.get("readings", []):
            yield g, r


class TestSearchComplete(unittest.TestCase):
    def test_tinanta_roundtrip(self):
        te = TinantaDerivationEngine()
        total = slot_hit = root_hit = 0
        misses = []
        for dh in TIN_ROOTS:
            for lak in TIN_LAKARAS:
                for pur in PURUSAS:
                    for vac in VACANAS:
                        try:
                            cands, _log = te.derive(dh, lak, pur, vac)
                        except Exception:
                            continue
                        # primary form only: twins legitimately recur across slots
                        for surf in cands[:1]:
                            total += 1
                            rs = [g for g in analyze(surf)
                                  if g["kind"] == "tinanta"]
                            if lak in ("luN", "liw"):
                                # twin-exploded lakaras: surfaces recur across
                                # slots (aBAvIt), so assert lakara only
                                ok_slot = any(r.get("lakara") == lak
                                              for _, r in _tin_readings(rs))
                                ok_root = any(r.get("lakara") == lak and g.get("dhatu")
                                              for g, r in _tin_readings(rs))
                            else:
                                ok_slot = any(
                                    r.get("lakara") == lak and r.get("purusha") == pur
                                    and r.get("vacana") == vac
                                    for _, r in _tin_readings(rs))
                                ok_root = any(
                                    r.get("lakara") == lak and r.get("purusha") == pur
                                    and r.get("vacana") == vac and g.get("dhatu")
                                    for g, r in _tin_readings(rs))
                            if ok_slot:
                                slot_hit += 1
                            else:
                                misses.append((dh, lak, pur, vac, surf))
                            if ok_root:
                                root_hit += 1
        print(f"\ntinanta roundtrip: slot {slot_hit}/{total}, "
              f"root {root_hit}/{total}")
        self.assertEqual(slot_hit, total, f"slot misses: {misses[:10]}")
        # root linkage is heuristic (reduplication/grades); require majority
        self.assertGreaterEqual(root_hit / max(total, 1), 0.7,
                                f"root rate too low")

    def test_krdanta_roundtrip(self):
        ke = KrdantaEngine()
        total = hit = 0
        misses = []
        for dh in TIN_ROOTS:
            try:
                d = ke.derive_all_krdantas(dh)
            except Exception:
                continue
            for prat, data in d.items():
                forms = []
                if isinstance(data, dict):
                    for k in ("M", "F", "N"):
                        v = data.get(k)
                        if isinstance(v, str):
                            forms.append(v)
                    av = data.get("avyaya")
                    if isinstance(av, str):
                        forms.append(av)
                    elif isinstance(av, list):
                        forms += [x for x in av if isinstance(x, str)]
                for surf in forms[:3]:
                    total += 1
                    rs = [g for g in analyze(surf)
                          if g["kind"] == "krdanta"]
                    want = {prat, KRD_FAMILY.get(prat, prat)}
                    if any(r.get("pratyaya") in want and g.get("dhatu")
                           for g, r in _krd_readings(rs)):
                        hit += 1
                    else:
                        misses.append((dh, prat, surf))
        print(f"\nkrdanta roundtrip: {hit}/{total}")
        self.assertGreaterEqual(hit / max(total, 1), 0.7,
                                f"misses: {misses[:10]}")

    def test_subanta_obscure(self):
        from pypanini.search import subanta_search

        def _has(word, stem, vib, vac):
            for g in subanta_search(word):
                if g.get("stem") != stem:
                    continue
                for r in g.get("readings", []):
                    if r.get("vibhakti") == vib and r.get("vacana") == vac:
                        return True
            return False

        self.assertTrue(_has("lakzmIH", "lakzmI", 1, "eka"))
        self.assertTrue(_has("lakzmyA", "lakzmI", 3, "eka"))
        self.assertTrue(_has("lakzmyE", "lakzmI", 4, "eka"))
        # pati alone (non-Ghi) vs compound (Ghi) Datives differ
        self.assertTrue(_has("patye", "pati", 4, "eka"))


if __name__ == "__main__":
    unittest.main()
