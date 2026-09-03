import unittest
from pypanini.tinanta import TinantaDerivationEngine

class TestTinanta(unittest.TestCase):
    def setUp(self):
        self.engine = TinantaDerivationEngine()

    def test_bhu_lrn(self):
        t = self.engine.derive_all("BU", "lfN")
        self.assertEqual(t[("prathama", "eka")], "aBavizyat")
        self.assertEqual(t[("prathama", "dvi")], "aBavizyatAm")
        self.assertEqual(t[("prathama", "bahu")], "aBavizyan")
        self.assertEqual(t[("madhyama", "eka")], "aBavizyaH")
        self.assertEqual(t[("madhyama", "dvi")], "aBavizyatam")
        self.assertEqual(t[("madhyama", "bahu")], "aBavizyata")
        self.assertEqual(t[("uttama", "eka")], "aBavizyam")
        self.assertEqual(t[("uttama", "dvi")], "aBavizyAva")
        self.assertEqual(t[("uttama", "bahu")], "aBavizyAma")

    def test_bhu_lrt(self):
        t = self.engine.derive_all("BU", "lfw")
        self.assertEqual(t[("prathama", "eka")], "Bavizyati")

    def test_bhu_lat(self):
        t = self.engine.derive_all("BU", "lw")
        self.assertEqual(t[("prathama", "eka")], "Bavati")

if __name__ == '__main__':
    unittest.main()
