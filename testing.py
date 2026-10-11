import unittest
from processing import kontak, PengelolaKontak
from validasi import KontakError, validasi_kontak

class TestKontakApp(unittest.TestCase):

    def test_1_kontak_init(self):
        k = kontak("K01", "Budi", "0877668825")
        self.assertEqual(k.nama, "Budi")

    def test_2_kwargs(self):
        k = kontak(
            "K02", "Sari", "0987654321",
            hubungan="Teman Kuliah"
        )
        self.assertEqual(k.kuwargs.get("hubungan"), "Teman Kuliah")

    def test_3_args_total_kontak(self):
        p = PengelolaKontak()
        self.assertEqual(
            p.hitung_TotalKontak("K1", "K2", "K3"), 3
        )

    def test_4_lambda_urutkan(self):
        p = PengelolaKontak([
            kontak("K1", "Zack", "0876786543"),
            kontak("K2", "Andi", "081234567890")
        ])
        self.assertEqual(p.urutkan_nama()[0].nama, "Andi")

    def test_5_raise_error(self):
        with self.assertRaises(KontakError):
            validasi_kontak("081234567890", "")

if __name__ == "__main__":
    unittest.main()
