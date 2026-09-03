import unittest
from pypanini.tinanta import TinantaDerivationEngine

class TestTinanta(unittest.TestCase):
    def setUp(self):
        self.engine = TinantaDerivationEngine()

    def test_yananta(self):
        t = self.engine.derive_all("BU", "lw", sanadi="yananta")
        self.assertEqual(t[("prathama", "eka")], "boBUyate")
        self.assertEqual(t[("prathama", "dvi")], "boBUyete")
        self.assertEqual(t[("prathama", "bahu")], "boBUyante")

    def test_yanluganta(self):
        t = self.engine.derive_all("BU", "lw", sanadi="yanluganta")
        self.assertEqual(t[("prathama", "eka")], "boBavIti")
        self.assertEqual(t[("prathama", "dvi")], "boBUtaH")
        self.assertEqual(t[("prathama", "bahu")], "boBuvati")
        self.assertEqual(t[("madhyama", "eka")], "boBavIzi")

    def test_sannanta_karmani(self):
        t = self.engine.derive_all("BU", "lw", prayoga="karmani", sanadi="sannanta")
        self.assertEqual(t[("prathama", "eka")], "buBUzyate")
        self.assertEqual(t[("prathama", "bahu")], "buBUzyante")

    def test_nijanta_karmani(self):
        t = self.engine.derive_all("BU", "lw", prayoga="karmani", sanadi="nijanta")
        self.assertEqual(t[("prathama", "eka")], "BAvyate")

if __name__ == '__main__':
    unittest.main()
