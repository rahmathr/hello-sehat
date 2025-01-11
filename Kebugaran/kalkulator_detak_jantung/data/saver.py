"""
Fungsi untuk menyimpan hasil perhitungan detak jantung ke dalam file CSV.

Fungsi:
- simpan_proses_rhr: Menyimpan data pengguna dan hasil kalkulasi zona detak jantung.

Detail:
File yang digunakan untuk penyimpanan adalah 'dataframes.csv', yang berlokasi di folder
'Kebugaran/kalkulator_detak_jantung/data/'. 
Jika file belum ada, file baru akan dibuat secara otomatis.
"""


def simpan_proses_rhr(
    nama_lengkap: str,
    jenis_kelamin: str,
    umur: int,
    tingkat_aktivitas: str,
    detak_jantung_maks: int,
    detak_jantung_istirahat: int,
    batas_bawah: float,
    batas_atas: float,
):
    """
    Menyimpan data kalkulasi detak jantung ke dalam file CSV.

    Args:
        nama_lengkap (str): Nama lengkap individu.
        jenis_kelamin (str): Jenis kelamin individu ("Laki-laki"/"Perempuan").
        umur (int): Umur individu.
        tingkat_aktivitas (str): Tingkat aktivitas individu (contoh: "Sedentary", "Aktif").
        detak_jantung_maks (int): Detak jantung maksimal individu.
        detak_jantung_istirahat (int): Detak jantung saat istirahat.
        batas_bawah (float): Batas bawah zona detak jantung (dalam persen).
        batas_atas (float): Batas atas zona detak jantung (dalam persen).

    Raises:
        ValueError: Jika terjadi kesalahan dalam proses penulisan ke file.

    """
    # Lokasi file tempat data akan disimpan
    file_path: str = "Kebugaran/kalkulator_detak_jantung/data/dataframes.csv"

    try:
        # Membuka file dalam mode append ("a") untuk menambahkan data baru
        with open(file_path, "a", encoding="utf-8") as file:
            # Menulis data ke file dalam format CSV
            file.write(
                f"{nama_lengkap},{jenis_kelamin},{umur},{tingkat_aktivitas},{detak_jantung_maks},{detak_jantung_istirahat},{batas_bawah},{batas_atas}\n"
            )
    except ValueError as ve:
        # Menangani kesalahan jika terjadi error saat menyimpan data
        print(f"Terjadi kesalahan saat menyimpan hasil detak jantung: {ve}")
