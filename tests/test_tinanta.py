import unittest
from pypanini.tinanta import TinantaDerivationEngine

class TestTinanta(unittest.TestCase):
    def setUp(self):
        self.engine = TinantaDerivationEngine()

    def test_sannanta_desiderative(self):
        # Present: buBUzati
        t_lat = self.engine.derive_all("BU", "lw", sanadi="sannanta")
        self.assertEqual(t_lat[("prathama", "eka")], "buBUzati")
        self.assertEqual(t_lat[("uttama", "eka")], "buBUzAmi")

        # Past: abuBUzat
        t_lan = self.engine.derive_all("BU", "laN", sanadi="sannanta")
        self.assertEqual(t_lan[("prathama", "eka")], "abuBUzat")

        # Future: buBUzizyati
        t_lrt = self.engine.derive_all("BU", "lfw", sanadi="sannanta")
        self.assertEqual(t_lrt[("prathama", "eka")], "buBUzizyati")

    def test_nijanta_causative(self):
        # Present: BAvayati
        t_lat = self.engine.derive_all("BU", "lw", sanadi="nijanta")
        self.assertEqual(t_lat[("prathama", "eka")], "BAvayati")

        # Past: aBAvayat
        t_lan = self.engine.derive_all("BU", "laN", sanadi="nijanta")
        self.assertEqual(t_lan[("prathama", "eka")], "aBAvayat")

    def test_karmani_passive(self):
        # Present: BUyate
        t_lat = self.engine.derive_all("BU", "lw", prayoga="karmani")
        self.assertEqual(t_lat[("prathama", "eka")], "BUyate")

        # Past: aBUyata
        t_lan = self.engine.derive_all("BU", "laN", prayoga="karmani")
        self.assertEqual(t_lan[("prathama", "eka")], "aBUyata")

    def test_primitive_lat(self):
        t = self.engine.derive_all("BU", "lw")
        self.assertEqual(t[("prathama", "eka")], "Bavati")

if __name__ == '__main__':
    unittest.main()
