import unittest
from pypanini.tinanta import TinantaDerivationEngine

class TestTinanta(unittest.TestCase):
    def setUp(self):
        self.engine = TinantaDerivationEngine()

    def test_bhu_lut(self):
        t = self.engine.derive_all("BU", "luw")
        self.assertEqual(t[("prathama", "eka")], "BavitA")
        self.assertEqual(t[("prathama", "dvi")], "BavitArO")
        self.assertEqual(t[("prathama", "bahu")], "BavitAraH")
        self.assertEqual(t[("madhyama", "eka")], "BavitAsi")
        self.assertEqual(t[("madhyama", "dvi")], "BavitAsTaH")
        self.assertEqual(t[("madhyama", "bahu")], "BavitAsTa")
        self.assertEqual(t[("uttama", "eka")], "BavitAsmi")
        self.assertEqual(t[("uttama", "dvi")], "BavitAsvaH")
        self.assertEqual(t[("uttama", "bahu")], "BavitAsmaH")

    def test_bhu_lrt(self):
        t = self.engine.derive_all("BU", "lfw")
        self.assertEqual(t[("prathama", "eka")], "Bavizyati")

    def test_bhu_lat(self):
        t = self.engine.derive_all("BU", "lw")
        self.assertEqual(t[("prathama", "eka")], "Bavati")

if __name__ == '__main__':
    unittest.main()
