import unittest
from pypanini.tinanta import TinantaDerivationEngine

class TestTinanta(unittest.TestCase):
    def setUp(self):
        self.engine = TinantaDerivationEngine()

    def test_bhu_lrt(self):
        t = self.engine.derive_all("BU", "lfw")
        self.assertEqual(t[("prathama", "eka")], "Bavizyati")
        self.assertEqual(t[("prathama", "dvi")], "BavizyataH")
        self.assertEqual(t[("prathama", "bahu")], "Bavizyanti")
        self.assertEqual(t[("madhyama", "eka")], "Bavizyasi")
        self.assertEqual(t[("uttama", "eka")], "BavizyAmi")
        self.assertEqual(t[("uttama", "bahu")], "BavizyAmaH")

    def test_bhu_lat(self):
        t = self.engine.derive_all("BU", "lw")
        self.assertEqual(t[("prathama", "eka")], "Bavati")

    def test_bhu_lan(self):
        t = self.engine.derive_all("BU", "laN")
        self.assertEqual(t[("prathama", "eka")], "aBavat")

    def test_bhu_lot(self):
        t = self.engine.derive_all("BU", "low")
        self.assertEqual(t[("prathama", "eka")], "Bavatu")

    def test_bhu_vidhilin(self):
        t = self.engine.derive_all("BU", "viDiliN")
        self.assertEqual(t[("prathama", "eka")], "Bavet")

if __name__ == '__main__':
    unittest.main()
