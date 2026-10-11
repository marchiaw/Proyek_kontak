class kontak:
    # Untuk menyimpan data entitas satu kontak

    # Penggunaan **kwargs
    def __init__(self, id_kontak, nama, nomor_hp, hubungan=None, **kwargs):
        self.id_kontak = id_kontak
        self.nama = nama
        self.nomor_hp = nomor_hp
        self.hubungan = hubungan

    def format_baris(self):
        return f"{self.id_kontak};{self.nama};{self.nomor_hp};{self.hubungan}\n"

class PengelolaKontak:
    # Untuk mengolah kumpulan kontak

    def __init__(self, daftar_kontak=None):
        self.daftar_kontak = daftar_kontak if daftar_kontak else []

    def tambah_kontak(self, kontak):
        self.daftar_kontak.append(kontak)

    # Penggunaan *args
    def hitung_TotalKontak(self, *daftar_item):
        return len(daftar_item)

    # Penggunaan Lambda untuk mengurutkan kontak dari A-Z
    def urutkan_nama(self):
        return sorted(
            self.daftar_kontak,
            key=lambda k: k.nama.lower()
        )
