from kontak_app.fileio import (
    baca_kontak_file,
    inisialisasi_file,
    tambah_kontak_file,
    tulis_laporan,
)

from kontak_app.processing import kontak, PengelolaKontak

fileData = "data_kontak.txt"
file_laporan = "laporan_kontak.txt"

def main():
    print("<<< Program Pengelola Buku Kontak >>>\n")

    # Memanggil mode "x" dengan keyword argument
    inisialisasi_file(file_path=fileData)

    # Mode A menyimpan data kontak baru dengan kwargs
    tambah_kontak_file(
        fileData,
        kontak("K01", "Budi Santoso", "0997654454",
               hubungan="teman")
    )

    tambah_kontak_file(
        fileData,
        kontak("K02", "Ucup", "089876543210",
               hubungan="Teman")
    )
    
    tambah_kontak_file(
        fileData,
        kontak("K03", "Mar", "0898788883210",
               hubungan="Sahabat")
    )

    # Untuk apabila data rusak saat uji error
    with open(fileData, "a") as file:
        file.write("K03;Kontak Rusak;123\n")

    # Mode "r" untuk membaca data dan melewati baris yang rusak
    data_terbaca = baca_kontak_file(fileData)

    pengelola = PengelolaKontak()

    for d in data_terbaca:
        pengelola.tambah_kontak(
            kontak(d["ID"], d["Nama"], d["No_hp"], hubungan=d["Hubungan"])
        )

    # Pengolahan data (*args & lambda)
    list_item = [
        k.id_kontak for k in pengelola.daftar_kontak
    ]

    total_kontak = pengelola.hitung_TotalKontak(*list_item)
    kontak_terurut = pengelola.urutkan_nama()

    # Mode "w" untuk menyusun dan menulis laporan
    isi_laporan = (
        f"Total Kontak Tersimpan: {total_kontak} Kontak\n\n"
        "Daftar Kontak (A-Z):\n"
    )

    for k in kontak_terurut:
        teks_hubungan = f" ({k.hubungan})" if k.hubungan else ""
        isi_laporan += f"- {k.nama} {k.nomor_hp}{teks_hubungan}\n"

    tulis_laporan(file_laporan, isi_laporan)

    print("<<< Laporan Berhasil Dibuat >>>")
    print(isi_laporan)

if __name__ == "__main__":
    main()
