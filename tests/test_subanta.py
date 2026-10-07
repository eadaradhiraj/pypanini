"""Generative validation for subanta — SLP1 only, no Devanagari.

Usage:
  python3 -m unittest tests.test_subanta -v
  python3 tests/test_subanta.py
"""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from pypanini.subanta import SubantaEngine


def has(forms, exp):
    return exp in forms


class TestSubantaGenerative(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.e = SubantaEngine()

    def assertForm(self, stem, linga, key, exp):
        got = self.e.decline(stem, linga).get(key, [])
        self.assertIn(exp, got, f"{stem}/{linga} {key}: got {got} want {exp}")

    def test_a_masc_rAma(self):
        self.assertForm("rAma", "puM", (1, "eka"), "rAmaH")
        self.assertForm("rAma", "puM", (1, "dvi"), "rAmO")
        self.assertForm("rAma", "puM", (1, "bahu"), "rAmAH")
        self.assertForm("rAma", "puM", (2, "bahu"), "rAmAn")
        self.assertForm("rAma", "puM", (3, "eka"), "rAmeRa")
        self.assertForm("rAma", "puM", (6, "bahu"), "rAmARAm")
        self.assertForm("rAma", "puM", (7, "bahu"), "rAmezu")
        self.assertForm("rAma", "puM", (8, "eka"), "rAma")

    def test_Trump_natva(self):
        # declension_discussion: wramPa Instr sg must be wramPeRa (Natva), not dental
        self.assertForm("wramPa", "puM", (3, "eka"), "wramPeRa")

    def test_a_neut_Pala(self):
        self.assertForm("Pala", "napuMsaka", (1, "eka"), "Palam")
        self.assertForm("Pala", "napuMsaka", (1, "bahu"), "PalAni")
        self.assertForm("Pala", "napuMsaka", (3, "eka"), "PaleRa")

    def test_A_fem(self):
        self.assertForm("sItA", "strI", (1, "eka"), "sItA")
        self.assertForm("sItA", "strI", (3, "eka"), "sItayA")
        self.assertForm("sItA", "strI", (8, "eka"), "sIte")

    def test_i_gI_nadI(self):
        self.assertForm("hari", "puM", (3, "eka"), "haryA")
        self.assertForm("hari", "puM", (8, "eka"), "hare")
        self.assertForm("hari", "puM", (6, "bahu"), "harIRAm")
        self.assertForm("nadI", "strI", (4, "eka"), "nadyE")
        self.assertForm("nadI", "strI", (8, "eka"), "nadi")
        # short fem optionality mati: mataye / matyE
        got = self.e.decline("mati", "strI")[(4, "eka")]
        self.assertIn("mataye", got)
        self.assertIn("matyE", got)

    def test_u(self):
        self.assertForm("guru", "puM", (3, "eka"), "gurvA")
        self.assertForm("guru", "puM", (8, "eka"), "guro")
        self.assertForm("vaDU", "strI", (4, "eka"), "vaDvE")
        got = self.e.decline("Denu", "strI")[(4, "eka")]
        self.assertIn("Denave", got)
        self.assertIn("DenvE", got)

    def test_neuter_liquid_shield(self):
        self.assertForm("vAri", "napuMsaka", (3, "eka"), "vAriRA")
        self.assertForm("vAri", "napuMsaka", (1, "bahu"), "vArIRi")
        self.assertForm("madhu", "napuMsaka", (4, "eka"), "madhune")

    def test_f_agent_kin_svasf(self):
        self.assertForm("kartf", "puM", (1, "bahu"), "kartAraH")
        self.assertForm("kartf", "puM", (6, "bahu"), "kartrARAm")
        self.assertForm("pitf", "puM", (1, "bahu"), "pitaraH")
        self.assertForm("pitf", "puM", (6, "bahu"), "pitFRAm")
        self.assertForm("svasf", "strI", (1, "dvi"), "svasArO")

    def test_an(self):
        self.assertForm("rAjan", "puM", (1, "eka"), "rAjA")
        self.assertForm("rAjan", "puM", (3, "eka"), "rAjYA")
        self.assertForm("Atman", "puM", (3, "eka"), "AtmanA")
        self.assertForm("karman", "napuMsaka", (3, "eka"), "karmanA")
        self.assertForm("nAman", "napuMsaka", (1, "eka"), "nAma")

    def test_as_neut(self):
        self.assertForm("manas", "napuMsaka", (1, "bahu"), "manAMsi")
        self.assertForm("havis", "napuMsaka", (1, "bahu"), "havIMsi")
        self.assertForm("cakzus", "napuMsaka", (1, "bahu"), "cakzUMsi")

    def test_at_participles_bhavat_mahat(self):
        self.assertForm("gacCat", "puM", (1, "eka"), "gacCan")
        self.assertForm("Bavat", "puM", (1, "eka"), "BavAn")
        self.assertForm("mahat", "puM", (1, "eka"), "mahAn")
        self.assertForm("jagat", "napuMsaka", (1, "bahu"), "jaganti")
        # feminine Satf declines like nadI
        self.assertForm("gacCantI", "strI", (4, "eka"), "gacCantyE")
        # ktavatu
        self.assertForm("kftavat", "puM", (1, "eka"), "kftavAn")
        self.assertForm("kftavat", "puM", (2, "bahu"), "kftavataH")
        # kvasu three stems
        self.assertForm("cakfvas", "puM", (1, "eka"), "cakfvAn")
        self.assertForm("cakfvas", "puM", (2, "bahu"), "cakfuzaH")
        # SAnac normalizes to a-stem
        self.assertForm("laBamAna", "puM", (1, "eka"), "laBamAnaH")
        # kta normalizes
        self.assertForm("kfta", "puM", (1, "eka"), "kftaH")

    def test_c_h(self):
        self.assertForm("vAc", "strI", (1, "eka"), "vAk")
        self.assertForm("vAc", "strI", (3, "bahu"), "vAgBiH")
        self.assertForm("vAc", "strI", (7, "bahu"), "vAkzu")
        self.assertForm("upAnah", "puM", (3, "bahu"), "upAnadBiH")

    def test_go_rE_nO(self):
        self.assertForm("go", "puM", (1, "eka"), "gOH")
        self.assertForm("go", "puM", (2, "eka"), "gAm")
        self.assertForm("go", "puM", (2, "bahu"), "gAH")
        self.assertForm("rE", "puM", (1, "eka"), "rAH")
        self.assertForm("nO", "strI", (2, "eka"), "nAvam")

    def test_saKi_pati_krozwu_asTi(self):
        self.assertForm("saKi", "puM", (2, "eka"), "saKAyam")
        self.assertForm("saKi", "puM", (6, "eka"), "saKyuH")
        self.assertForm("pati", "puM", (3, "eka"), "patyA")
        self.assertForm("krozwu", "puM", (1, "eka"), "krozwA")
        self.assertForm("krozwu", "puM", (2, "eka"), "krozwAram")
        self.assertForm("asTi", "napuMsaka", (3, "eka"), "asTnA")
        self.assertForm("akzi", "napuMsaka", (3, "eka"), "akznA")

    def test_pronouns(self):
        self.assertForm("tad", "puM", (4, "eka"), "tasmE")
        self.assertForm("tad", "puM", (1, "eka"), "saH")
        self.assertForm("tad", "puM", (3, "eka"), "tena")
        self.assertForm("kim", "puM", (1, "eka"), "kaH")
        self.assertForm("kim", "napuMsaka", (1, "eka"), "kim")
        self.assertForm("idam", "puM", (1, "eka"), "ayam")
        self.assertForm("adas", "puM", (1, "eka"), "asO")
        self.assertForm("adas", "puM", (1, "bahu"), "amI")
        self.assertForm("asmad", "puM", (1, "eka"), "aham")
        self.assertForm("yuzmad", "puM", (4, "eka"), "tuByam")
        self.assertForm("sarva", "puM", (4, "eka"), "sarvasmE")
        # semi-pronoun optionality pUrva: pUrvAt / pUrvasmAt
        got = self.e.decline("pUrva", "puM")[(5, "eka")]
        self.assertIn("pUrvAt", got)
        self.assertIn("pUrvasmAt", got)

    def test_numerals_zaw(self):
        self.assertForm("dvi", "puM", (1, "dvi"), "dvO")
        self.assertForm("tri", "strI", (1, "bahu"), "tisraH")
        self.assertForm("tri", "puM", (1, "bahu"), "trayaH")
        self.assertForm("catur", "strI", (1, "bahu"), "catasraH")
        self.assertForm("catur", "puM", (1, "bahu"), "catvAraH")
        self.assertForm("paYcan", "puM", (1, "bahu"), "paYca")
        self.assertForm("zaz", "puM", (1, "bahu"), "zaw")
        got = self.e.decline("azwan", "puM")[(1, "bahu")]
        self.assertIn("azwO", got)
        self.assertIn("azwa", got)

    def test_misc_edge(self):
        self.assertForm("SrI", "strI", (2, "eka"), "Sriyam")
        self.assertForm("SrI", "strI", (8, "eka"), "SrI")
        self.assertForm("pratyaYc", "puM", (3, "eka"), "pratIcA")
        self.assertForm("pratyaYc", "puM", (1, "eka"), "pratyaN")
        self.assertForm("Sreyas", "puM", (1, "eka"), "SreyAn")
        self.assertForm("puMs", "puM", (1, "eka"), "pumAn")
        self.assertForm("div", "strI", (1, "eka"), "dyOH")
        self.assertForm("ahan", "napuMsaka", (1, "eka"), "ahaH")
        self.assertForm("paTin", "puM", (1, "eka"), "panTAH")
        self.assertForm("paTin", "puM", (3, "eka"), "paTA")
        self.assertForm("Svan", "puM", (2, "bahu"), "SunAH")
        self.assertForm("ap", "strI", (1, "bahu"), "ApaH")
        self.assertForm("anaQuh", "puM", (1, "eka"), "anaQvAn")
        # jarA optionality
        got = self.e.decline("jarA", "strI")[(3, "eka")]
        self.assertIn("jarayA", got)
        self.assertIn("jarasA", got)

    def test_all_v2(self):
        # parivrAj exception 8.2.36
        self.assertForm("parivrAj", "puM", (1, "eka"), "parivrAw")
        self.assertForm("parivrAj", "puM", (7, "bahu"), "parivrAwzu")
        # h-class auto (no extra needed)
        self.assertForm("duh", "puM", (3, "bahu"), "dugBiH")
        self.assertForm("lih", "puM", (3, "bahu"), "liqBiH")
        self.assertForm("upAnah", "puM", (3, "bahu"), "upAnadBiH")
        # mahat neut
        self.assertForm("mahat", "napuMsaka", (1, "bahu"), "mahAnti")
        # prathama-class: Nom pl both, Dat sg noun-only
        got = self.e.decline("praTama", "puM")[(1, "bahu")]
        self.assertIn("praTamAH", got)
        self.assertIn("praTame", got)
        self.assertForm("praTama", "puM", (4, "eka"), "praTamAya")
        # uBa dual-only
        self.assertEqual(self.e.decline("uBa", "puM")[(1, "eka")], [])
        self.assertForm("uBa", "puM", (1, "dvi"), "uBO")
        # eka is sarvanAman (eke)
        self.assertForm("eka", "puM", (1, "bahu"), "eke")
        # supplementary ops
        from pypanini.subanta import (ekaSeza, pumvatBAva, avyaya_pada,
                                       saH_sulopa, satf_feminine, stri_pratipadika)
        self.assertEqual(ekaSeza(["mAtf", "pitf"]), "pitf")
        self.assertEqual(ekaSeza(["rAma", "rAma"]), "rAma")
        self.assertEqual(pumvatBAva("kalyARI"), "kalyARa")
        self.assertEqual(avyaya_pada("ca"), "ca")
        self.assertEqual(saH_sulopa("p"), "sa")
        self.assertEqual(saH_sulopa("a"), "saH")
        self.assertIn("gacCantI", satf_feminine("gacCat", "BvAdi"))
        self.assertIn("tudatI", satf_feminine("tudat", "tudAdi"))
        self.assertEqual(satf_feminine("dadat", "adAdi"), ["dadatI"])
        self.assertEqual(stri_pratipadika("aja"), "ajA")
        self.assertEqual(stri_pratipadika("kartf", "RIp"), "kartrI")
        self.assertEqual(stri_pratipadika("Bavat", "RIp"), "BavatI")
        self.assertEqual(stri_pratipadika("sUrya", "RIp"), "sUrI")
        self.assertEqual(stri_pratipadika("matsya", "RIp"), "matsI")
        self.assertEqual(stri_pratipadika("manuzya", "RIp"), "manuzI")
        self.assertEqual(stri_pratipadika("rAjan", "RIp"), "rAjYI")
        self.assertEqual(stri_pratipadika("Danin", "RIp"), "DaninI")
        self.assertIn("DaninIH", self.e.decline("DaninI", "strI")[(1, "eka")])
        # pati in compounds is Ghi (pataye), alone it is not (patye)
        self.assertForm("pati", "puM", (4, "eka"), "patye")
        self.assertEqual(
            self.e.decline("pati", "puM", extra={"compound": True})[(4, "eka")], ["pataye"])
        # second fractional + uBaya spot checks
        for exp in ("caramAH", "carame"):
            self.assertIn(exp, self.e.decline("carama", "puM")[(1, "bahu")])
        self.assertForm("uBaya", "puM", (4, "eka"), "uBayasmE")


if __name__ == "__main__":
    unittest.main()
