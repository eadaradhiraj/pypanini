import unittest
from pypanini.tinanta import TinantaDerivationEngine

class TestTinanta(unittest.TestCase):
    def setUp(self):
        self.engine = TinantaDerivationEngine()

    def test_bhu_lat(self):
        t = self.engine.derive_all("BU", "lw")
        self.assertEqual(t[("prathama", "eka")], "Bavati")
        self.assertEqual(t[("uttama", "eka")], "BavAmi")

    def test_bhu_lan(self):
        t = self.engine.derive_all("BU", "laN")
        self.assertEqual(t[("prathama", "eka")], "aBavat")
        self.assertEqual(t[("uttama", "bahu")], "aBavAma")

    def test_bhu_lot(self):
        t = self.engine.derive_all("BU", "low")
        self.assertEqual(t[("prathama", "eka")], "Bavatu")
        self.assertEqual(t[("madhyama", "eka")], "Bava")
        self.assertEqual(t[("uttama", "eka")], "BavAni")

    def test_bhu_vidhilin(self):
        t = self.engine.derive_all("BU", "viDiliN")
        self.assertEqual(t[("prathama", "eka")], "Bavet")
        self.assertEqual(t[("prathama", "dvi")], "BavetAm")
        self.assertEqual(t[("prathama", "bahu")], "BaveyuH")
        self.assertEqual(t[("madhyama", "eka")], "BaveH")
        self.assertEqual(t[("uttama", "eka")], "Baveyam")
        self.assertEqual(t[("uttama", "dvi")], "Baveva")
        self.assertEqual(t[("uttama", "bahu")], "Bavema")

if __name__ == '__main__':
    unittest.main()
