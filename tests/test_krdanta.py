import unittest
from pypanini.krdanta import KrdantaEngine

class TestKrdanta(unittest.TestCase):
    def setUp(self):
        self.ke = KrdantaEngine()

    def test_primitive_krdanta(self):
        res = self.ke.derive_all_krdantas("BU")
        self.assertEqual(res["kta"], "BUta")
        self.assertEqual(res["ktavatu"], "BUtavat")
        self.assertEqual(res["Satf"], "Bavat")
        self.assertEqual(res["SAnac"], "BUyamAna")
        self.assertEqual(res["tavya"], "Bavitavya")
        self.assertEqual(res["anIyar"], "BavanIya")
        self.assertEqual(res["tumun"], "Bavitum")
        self.assertEqual(res["ktvA"], "BUtvA")
        self.assertEqual(res["lyap"], "saMBUya")

    def test_nijanta_krdanta(self):
        res = self.ke.derive_all_krdantas("BU", sanadi="nijanta")
        self.assertEqual(res["kta"], "BAvita")
        self.assertEqual(res["ktavatu"], "BAvitavat")
        self.assertEqual(res["Satf"], "BAvayat")
        self.assertEqual(res["SAnac"], "BAvyamAna")
        self.assertEqual(res["tavya"], "BAvayitavya")
        self.assertEqual(res["anIyar"], "BAvanIya")
        self.assertEqual(res["tumun"], "BAvayitum")
        self.assertEqual(res["ktvA"], "BAvayitvA")
        self.assertEqual(res["lyap"], "saMBAvya")

    def test_sannanta_krdanta(self):
        res = self.ke.derive_all_krdantas("BU", sanadi="sannanta")
        self.assertEqual(res["kta"], "buBUzita")
        self.assertEqual(res["ktavatu"], "buBUzitavat")
        self.assertEqual(res["Satf"], "buBUzat")
        self.assertEqual(res["SAnac"], "buBUzamARa")
        self.assertEqual(res["tavya"], "buBUzitavya")
        self.assertEqual(res["anIyar"], "buBUzanIya")
        self.assertEqual(res["tumun"], "buBUzitum")
        self.assertEqual(res["ktvA"], "buBUzitvA")
        self.assertEqual(res["lyap"], "saMbuBUzya")

if __name__ == '__main__':
    unittest.main()
