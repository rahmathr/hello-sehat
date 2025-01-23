"""
Program Pengelolaan Denyut Jantung Istirahat
================================================

Program ini dirancang untuk membantu pengguna menghitung zona latihan denyut jantung
berdasarkan data pribadi seperti nama, jenis kelamin, umur, dan denyut jantung istirahat.

Fitur Utama:
1. Menghitung zona latihan denyut jantung berdasarkan intensitas rendah, sedang, dan tinggi.
2. Menyimpan hasil perhitungan zona latihan ke dalam database untuk referensi.
3. Menampilkan database hasil perhitungan sebelumnya.
4. Keluar dari program dengan aman.

Modul ini berfungsi sebagai pengontrol utama (main controller) dari program,
mengelola alur kerja dengan memanfaatkan berbagai fungsi dan modul pendukung.
"""

import os

from utils.display_headers import (
    tampilan_header_utama,
    tampilan_zona_latihan_detak_jantung,
)
from utils.user_inputs import (
    input_nama_lengkap,
    input_jenis_kelamin,
    input_umur,
    input_tingkat_aktivitas,
    input_detak_jantung_istirahat,
)
from utils.calculators import (
    hitung_denyut_jantung_maksimum,
    zona_intensitas_rendah,
    zona_intensitas_sedang,
    zona_intensitas_tinggi,
)

from data.reader import read_database
from data.saver import simpan_proses_rhr


def pilih_menu():
    """
    Menampilkan menu utama aplikasi dan meminta pengguna memilih opsi.

    Returns:
        int: Pilihan menu yang dipilih pengguna (1, 2, atau 3).
    """
    os.system("cls" if os.name == "nt" else "clear")
    tampilan_header_utama()
    print(f"  [1] Hitung Denyut Jantung Istirahat{7*'\t'}  ")
    print(f"  [2] Lihat Database{9*'\t'}  ")
    print(f"  [3] Exit{10*'\t'}  ")
    print(f" {88*' '} ")
    return int(input("Silahkan pilih menu (1/2/3): "))


def zona_denyut_jantung():
    """
    Menghitung dan menampilkan zona denyut jantung berdasarkan data pengguna.
    Data pengguna meliputi nama, jenis kelamin, umur, dan denyut jantung istirahat.

    Hasil perhitungan zona denyut jantung disimpan ke dalam database.
    """
    os.system("cls" if os.name == "nt" else "clear")
    tampilan_header_utama()
    try:
        # Meminta data pengguna
        nama_lengkap: str = input_nama_lengkap()
        jenis_kelamin: str = input_jenis_kelamin()
        umur: int = input_umur()
        denyut_jantung_istirahat: int = input_detak_jantung_istirahat()

        # Menghitung denyut jantung maksimum
        denyut_jantung_maks: int = hitung_denyut_jantung_maksimum(umur=umur)

        tampilan_zona_latihan_detak_jantung()
        zona_latihan: int = input_tingkat_aktivitas()

        # Menentukan zona latihan berdasarkan pilihan
        if zona_latihan == 1:
            rendah_bawah, rendah_atas = zona_intensitas_rendah(
                denyut_jantung_maks=denyut_jantung_maks,
                denyut_jantung_istirahat=denyut_jantung_istirahat,
            )   
            print(
                f"\nUntuk denyut_jantung_maks {denyut_jantung_maks} dan denyut_jantung_istirahat {denyut_jantung_istirahat}, intensitas rendah berada di antara {rendah_bawah} - {rendah_atas} bpm"
            )
            simpan_proses_rhr(
                nama_lengkap=nama_lengkap,
                jenis_kelamin=jenis_kelamin,
                umur=umur,
                tingkat_aktivitas="Intensitas Rendah",
                detak_jantung_maks=denyut_jantung_maks,
                detak_jantung_istirahat=denyut_jantung_istirahat,
                batas_bawah=rendah_bawah,
                batas_atas=rendah_atas,
            )
            input("\nTekan enter untuk melanjutkan...")
        elif zona_latihan == 2:
            rendah_bawah, rendah_atas = zona_intensitas_sedang(
                denyut_jantung_maks=denyut_jantung_maks,
                denyut_jantung_istirahat=denyut_jantung_istirahat,
            )
            print(
                f"\nUntuk denyut_jantung_maks {denyut_jantung_maks} dan denyut_jantung_istirahat {denyut_jantung_istirahat}, intensitas sedang berada di antara {rendah_bawah} - {rendah_atas} bpm"
            )
            simpan_proses_rhr(
                nama_lengkap=nama_lengkap,
                jenis_kelamin=jenis_kelamin,
                umur=umur,
                tingkat_aktivitas="Intensitas Sedang",
                detak_jantung_maks=denyut_jantung_maks,
                detak_jantung_istirahat=denyut_jantung_istirahat,
                batas_bawah=rendah_bawah,
                batas_atas=rendah_atas,
            )
            input("\nTekan enter untuk melanjutkan...")
        elif zona_latihan == 3:
            rendah_bawah, rendah_atas = zona_intensitas_tinggi(
                denyut_jantung_maks=denyut_jantung_maks,
                denyut_jantung_istirahat=denyut_jantung_istirahat,
            )
            print(
                f"\nUntuk denyut_jantung_maks {denyut_jantung_maks} dan denyut_jantung_istirahat {denyut_jantung_istirahat}, intensitas tinggi berada di antara {rendah_bawah} - {rendah_atas} bpm"
            )
            simpan_proses_rhr(
                nama_lengkap=nama_lengkap,
                jenis_kelamin=jenis_kelamin,
                umur=umur,
                tingkat_aktivitas="Intensitas Tinggi",
                detak_jantung_maks=denyut_jantung_maks,
                detak_jantung_istirahat=denyut_jantung_istirahat,
                batas_bawah=rendah_bawah,
                batas_atas=rendah_atas,
            )
            input("\nTekan enter untuk melanjutkan...")
        else:
            print("\nPilihan zona tidak valid.")
    except ValueError as ve:
        print(f"Terjadi kesalahan: {ve}")


def main_denyut_jantung_istirahat():
    """
    Fungsi utama untuk mengelola aplikasi penghitungan denyut jantung istirahat.
    Menampilkan menu, memproses pilihan pengguna, dan menjalankan fungsi terkait.
    """
    while True:
        try:
            pilihan: str = pilih_menu()
            if pilihan == 1:
                zona_denyut_jantung()
            elif pilihan == 2:
                read_database()
            elif pilihan == 3:
                print("\nTerima kasih! Sampai jumpa.")
                break
            else:
                print("\nPilihan Tidak Valid. Silakan pilih 1/2/3.")
                input("\nTekan enter untuk melanjutkan...")
        except ValueError as ve:
            print(f"Terjadi kesalahan: {ve}")


if __name__ == "__main__":
    main_denyut_jantung_istirahat()
