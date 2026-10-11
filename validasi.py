class KontakError(Exception):
    pass

def validasi_kontak(nomor_hp, nama):
    # Penggunaan Assert
    assert len(str(nomor_hp)) >= 10, "Nomor HP minimal 10 digit!"
    
    # Penggunaan Raise
    if not nama.strip():
        raise KontakError("Nama kontak tidak boleh kosong!")