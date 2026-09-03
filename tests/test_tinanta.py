import unittest
from pypanini.tinanta import TinantaDerivationEngine

class TestTinanta(unittest.TestCase):
    def setUp(self):
        self.engine = TinantaDerivationEngine()

    def test_lot_tatan_vikalpa(self):
        # 7.1.35 tātaṅ: 3rd and 2nd singular have 2 forms
        forms_3s, _ = self.engine.derive("BU", "low", "prathama", "eka")
        self.assertIn("Bavatu", forms_3s)
        self.assertIn("BavatAt", forms_3s)

        forms_2s, _ = self.engine.derive("BU", "low", "madhyama", "eka")
        self.assertIn("Bava", forms_2s)
        self.assertIn("BavatAt", forms_2s)

    def test_yanluganta_vikalpa(self):
        # 7.3.94 yaṅo vā: 3rd, 2nd, 1st singular have 2 forms
        forms_3s, _ = self.engine.derive("BU", "lw", "prathama", "eka", sanadi="yanluganta")
        self.assertIn("boBavIti", forms_3s)
        self.assertIn("boBoti", forms_3s)

    def test_primitive_lat(self):
        forms, _ = self.engine.derive("BU", "lw", "prathama", "eka")
        self.assertEqual(forms, ["Bavati"])

if __name__ == '__main__':
    unittest.main()
