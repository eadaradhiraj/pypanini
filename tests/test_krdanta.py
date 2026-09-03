import unittest
from pypanini.krdanta import KrdantaEngine

class TestKrdanta(unittest.TestCase):
    def setUp(self):
        self.ke = KrdantaEngine()

    def test_primitive_genders(self):
        res = self.ke.derive_all_krdantas("BU")
        # kta: M, F, N
        self.assertEqual(res["kta"]["M"], "BUtaH")
        self.assertEqual(res["kta"]["F"], "BUtA")
        self.assertEqual(res["kta"]["N"], "BUtam")
        # Satf: M, F, N
        self.assertEqual(res["Satf"]["M"], "Bavan")
        self.assertEqual(res["Satf"]["F"], "BavantI")
        self.assertEqual(res["Satf"]["N"], "Bavat")

    def test_sannanta_paninian_overrides(self):
        res = self.ke.derive_all_krdantas("BU", sanadi="sannanta")
        # 3.2.168: Sannanta takes 'u', not Rvul
        self.assertEqual(res["Rvul"]["M"], "buBUzuH")
        self.assertEqual(res["Rvul"]["F"], "buBUzuH")
        self.assertEqual(res["Rvul"]["N"], "buBUzu")
        # 3.3.102: Sannanta takes 'a + wAp' -> feminine buBUzA, not GaY
        self.assertEqual(res["GaY"]["form"], "buBUzA")
        self.assertEqual(res["GaY"]["gender"], "Feminine")

if __name__ == '__main__':
    unittest.main()
