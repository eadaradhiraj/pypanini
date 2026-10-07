"""Krdanta -> Subanta pipeline: participle stems decline to krdanta M forms."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from pypanini import KrdantaEngine
from pypanini.subanta import SubantaEngine, stri_pratipadika


class TestKrdantaSubantaPipeline(unittest.TestCase):
    def test_BU_pipeline(self):
        ke = KrdantaEngine()
        e = SubantaEngine()
        d = ke.derive_all_krdantas("BU")
        # kta: stem BUta -> rAma-like
        self.assertIn(d["kta"]["M"], e.decline("BUta", "puM")[(1, "eka")])
        self.assertIn(d["kta"]["F"], e.decline("BUtA", "strI")[(1, "eka")])
        # ktavatu: stem BUtavat -> -vAn
        self.assertIn(d["ktavatu"]["M"], e.decline("BUtavat", "puM")[(1, "eka")])
        fem = stri_pratipadika("BUtavat", "RIp")
        self.assertEqual(fem, "BUtavatI")
        # krdanta F omits visarga (BUtavatI) vs subanta pada (BUtavatIH): accept either
        fem_nom = e.decline(fem, "strI")[(1, "eka")]
        self.assertTrue(d["ktavatu"]["F"] in fem_nom or d["ktavatu"]["F"] + "H" in fem_nom)
        # Satf BU: M Bavan via satf flag (ambiguous Bavat string)
        self.assertIn(d["Satf"]["M"], e.decline("Bavat", "puM", extra={"satf": True})[(1, "eka")])
        # Satf gacCat unambiguous short
        self.assertIn("gacCan", e.decline("gacCat", "puM")[(1, "eka")])
        # SAnac: a-stem
        self.assertIn(d["SAnac"]["M"], e.decline("BUyamAna", "puM")[(1, "eka")])
        # kvasu weak feminine via RIp: cakfvas -> cakfuzI declinable (pada cakfuzIH)
        fem2 = stri_pratipadika("cakfvas", "RIp")
        self.assertEqual(fem2, "cakfuzI")
        self.assertIn("cakfuzIH", e.decline(fem2, "strI")[(1, "eka")])

    def test_stri_forms_decline(self):
        e = SubantaEngine()
        # I-feminine Nom takes visarga (nadIH-pattern): kartrIH
        self.assertIn("kartrIH", e.decline(stri_pratipadika("kartf", "RIp"), "strI")[(1, "eka")])
        self.assertIn("rAjYIH", e.decline(stri_pratipadika("rAjan", "RIp"), "strI")[(1, "eka")])
        self.assertIn("gacCantIH", e.decline("gacCantI", "strI")[(1, "eka")])


if __name__ == "__main__":
    unittest.main()
