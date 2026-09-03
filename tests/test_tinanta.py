import unittest
from pypanini.tinanta import TinantaDerivationEngine

class TestTinanta(unittest.TestCase):
    def setUp(self):
        self.engine = TinantaDerivationEngine()

    def test_bhu_lat(self):
        t = self.engine.derive_all("BU", "lw")
        self.assertEqual(t[("prathama", "eka")], "Bavati")
        self.assertEqual(t[("prathama", "bahu")], "Bavanti")
        self.assertEqual(t[("uttama", "eka")], "BavAmi")
        self.assertEqual(t[("uttama", "bahu")], "BavAmaH")

    def test_bhu_lan(self):
        t = self.engine.derive_all("BU", "laN")
        self.assertEqual(t[("prathama", "eka")], "aBavat")
        self.assertEqual(t[("prathama", "dvi")], "aBavatAm")
        self.assertEqual(t[("prathama", "bahu")], "aBavan")
        self.assertEqual(t[("madhyama", "eka")], "aBavaH")
        self.assertEqual(t[("uttama", "eka")], "aBavam")

    def test_bhu_lot(self):
        t = self.engine.derive_all("BU", "low")
        self.assertEqual(t[("prathama", "eka")], "Bavatu")
        self.assertEqual(t[("prathama", "dvi")], "BavatAm")
        self.assertEqual(t[("prathama", "bahu")], "Bavantu")
        self.assertEqual(t[("madhyama", "eka")], "Bava")
        self.assertEqual(t[("madhyama", "dvi")], "Bavatam")
        self.assertEqual(t[("madhyama", "bahu")], "Bavata")
        self.assertEqual(t[("uttama", "eka")], "BavAni")
        self.assertEqual(t[("uttama", "dvi")], "BavAva")
        self.assertEqual(t[("uttama", "bahu")], "BavAma")

if __name__ == '__main__':
    unittest.main()
