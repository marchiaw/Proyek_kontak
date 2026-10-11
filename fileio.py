from kontak_app.validasi import KontakError, validasi_kontak

# Mode "x" untuk pertama kali file dibuat
def inisialisasi_file(file_path):
    try:
        with open(file_path, "x") as file:
            file.write("ID;Nama;Nomor_HP\n")
    except FileExistsError:
        pass


# Mode "a" menambah kontak pada baris baru
def tambah_kontak_file(file_path, kontak):
    with open(file_path, "a") as file:
        file.write(kontak.format_baris())


# Mode "r" untuk membaca dan menangani ValueError
def baca_kontak_file(file_path):
    hasil = []
    try:
        with open(file_path, "r") as file:
            next(file)
            for baris in file:
                teks = baris.strip()
                if not teks:
                    continue
                try:
                    id_k, nama, no_hp = teks.split(";")
                    # Uji validasi tipe data & ukuran
                    validasi_kontak(no_hp, nama)
                    hasil.append({
                        "ID": id_k,
                        "Nama": nama,
                        "No_hp": no_hp
                    })
                except (ValueError, KontakError, AssertionError):
                    # Continue apabila ada baris yang rusak maka dilewati
                    continue
    except FileNotFoundError:
        print(f"Error: file '{file_path}' tidak ditemukan!")
    return hasil


# Mode "w" untuk menulis file ringkasan
def tulis_laporan(file_laporan, isi):
    with open(file_laporan, "w") as file:
        file.write(isi)
