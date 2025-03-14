"""
Modul untuk menghitung kebutuhan kalori berdasarkan tingkat aktivitas fisik.

Fungsi utama dalam modul ini mencakup:
- Menghitung BMR (Basal Metabolic Rate) untuk pria dan wanita.
- Menghitung kebutuhan kalori harian berdasarkan faktor aktivitas fisik.
- Menyimpan hasil perhitungan ke dalam database.

Fungsi yang tersedia:
- hitung_kebutuhan_kalori: Fungsi utama untuk menerima input pengguna 
  dan menghitung kebutuhan kalori.
- hitung_bmr_pria: Menghitung BMR untuk pria.
- hitung_bmr_wanita: Menghitung BMR untuk wanita.
- proses_kalori: Menghitung dan menampilkan kebutuhan kalori berdasarkan BMR dan aktivitas.
- aktivitas_ringan_pria: Proses kalori pria dengan aktivitas ringan.
- aktivitas_sedang_pria: Proses kalori pria dengan aktivitas sedang.
- aktivitas_berat_pria: Proses kalori pria dengan aktivitas berat.
- aktivitas_ringan_wanita: Proses kalori wanita dengan aktivitas ringan.
- aktivitas_sedang_wanita: Proses kalori wanita dengan aktivitas sedang.
- aktivitas_berat_wanita: Proses kalori wanita dengan aktivitas berat.

Dependencies:
- os: Untuk membersihkan layar terminal.
- time: Untuk menambahkan jeda visual.
- utils: Modul internal untuk input pengguna dan header tampilan.
- data.saver: Untuk menyimpan hasil ke dalam database.
"""

import os

from utils import user_inputs
from utils.display_headers import tampilan_header_utama, tampilan_header_aktivitas_fisik
from data.saver import simpan_proses_bmr


def hitung_kebutuhan_kalori():
    """
    Menghitung kebutuhan kalori berdasarkan input pengguna dan aktivitas fisik.

    Fungsi ini meminta pengguna untuk memasukkan data seperti nama, umur,
    jenis kelamin, tinggi badan, dan berat badan. Berdasarkan jenis kelamin,
    akan dihitung BMR (Basal Metabolic Rate) menggunakan rumus yang sesuai,
    dan kebutuhan kalori ditentukan berdasarkan tingkat aktivitas fisik.

    Hasil perhitungan disimpan dalam database melalui fungsi `simpan_proses_bmr`.
    """
    os.system("cls" if os.name == "nt" else "clear")
    tampilan_header_utama()

    global nama_lengkap, umur, jenis_kelamin, tinggi_badan, berat_badan

    try:
        # Meminta input dari pengguna
        nama_lengkap = user_inputs.input_nama_lengkap()
        umur = user_inputs.input_umur()
        jenis_kelamin = user_inputs.input_jenis_kelamin()
        tinggi_badan = user_inputs.input_tinggi_badan()
        berat_badan = user_inputs.input_berat_badan()

        # Menghitung BMR berdasarkan jenis kelamin
        if jenis_kelamin.upper() == "L":
            bmr_pria: float = hitung_bmr_pria(berat_badan, tinggi_badan, umur)
            tampilan_header_aktivitas_fisik()
            total_kalori: int = user_inputs.input_intensitas_aktivitas()

            aktivitas_fungsi_pria = {
                1: aktivitas_ringan_pria,
                2: aktivitas_sedang_pria,
                3: aktivitas_berat_pria,
            }

            aktivitas_fungsi_pria.get(total_kalori)(bmr_pria)

        elif jenis_kelamin.upper() == "P":
            bmr_wanita: float = hitung_bmr_wanita(berat_badan, tinggi_badan, umur)
            tampilan_header_aktivitas_fisik()
            total_kalori: int = user_inputs.input_intensitas_aktivitas()

            aktivitas_fungsi_wanita = {
                1: aktivitas_ringan_wanita,
                2: aktivitas_sedang_wanita,
                3: aktivitas_berat_wanita,
            }

            aktivitas_fungsi_wanita.get(total_kalori)(bmr_wanita)

        else:
            print("Jenis kelamin tidak valid!")

    except ValueError as ve:
        print(f"\nKesalahan input: {str(ve)}")
    except RuntimeError as re:
        print(f"\nTerjadi kesalahan tidak terduga: {re}")


def hitung_bmr_pria(
    berat_badan_pria: float, tinggi_badan_pria: float, umur_pria: int
) -> float:
    """
    Menghitung BMR untuk pria berdasarkan berat badan, tinggi badan, dan umur.

    Args:
        berat_badan (float): Berat badan dalam kilogram.
        tinggi_badan (float): Tinggi badan dalam sentimeter.
        umur (int): Umur dalam tahun.

    Returns:
        float: Nilai BMR yang dihitung.
    """
    try:
        bmr: float = (
            66.5
            + (13.7 * berat_badan_pria)
            + (5 * tinggi_badan_pria)
            - (6.8 * umur_pria)
        )
        return max(bmr, 0)  # Mengembalikan BMR minimal 0 jika hasil negatif
    except ValueError as ve:
        print(f"Kesalahan perhitungan BMR pria: {ve}")
        return 0


def hitung_bmr_wanita(
    berat_badan_wanita: float, tinggi_badan_wanita: float, umur_wanita: int
) -> float:
    """
    Menghitung BMR untuk wanita berdasarkan berat badan, tinggi badan, dan umur.

    Args:
        berat_badan (float): Berat badan dalam kilogram.
        tinggi_badan (float): Tinggi badan dalam sentimeter.
        umur (int): Umur dalam tahun.

    Returns:
        float: Nilai BMR yang dihitung.
    """
    try:
        bmr: float = (
            655
            + (9.6 * berat_badan_wanita)
            + (1.8 * tinggi_badan_wanita)
            - (4.7 * umur_wanita)
        )
        return max(bmr, 0)  # Mengembalikan BMR minimal 0 jika hasil negatif
    except ValueError as ve:
        print(f"Kesalahan perhitungan BMR wanita: {ve}")
        return 0


def proses_kalori(bmr: float, faktor_aktivitas: float, *jenis_aktivitas: str):
    """
    Menghitung kebutuhan kalori berdasarkan BMR dan faktor aktivitas.

    Args:
        bmr (float): Nilai BMR yang dihitung.
        faktor_aktivitas (float): Faktor pengali berdasarkan tingkat aktivitas fisik.
        jenis_aktivitas (str): Deskripsi tingkat aktivitas fisik.

    Hasil dihitung akan ditampilkan kepada pengguna dan disimpan dalam database.
    """
    kalori_kebutuhan: float = bmr * faktor_aktivitas
    print(
        f"\nBMR-nya sebesar {bmr:.0f} kkal, sedangkan kebutuhan kalorinya sebesar {kalori_kebutuhan:.0f} kkal"
    )

    input("\nTekan Enter untuk melanjutkan...")

    simpan_proses_bmr(
        nama_lengkap=nama_lengkap,
        umur=umur,
        jenis_kelamin=jenis_kelamin,
        tinggi_badan=tinggi_badan,
        berat_badan=berat_badan,
        bmr=bmr,
        total_kalori=kalori_kebutuhan,
    )

    os.system("cls")


def aktivitas_ringan_pria(bmr_pria: float):
    """Memproses kebutuhan kalori pria dengan aktivitas ringan."""
    proses_kalori(bmr_pria, 1.2, "Aktivitas Ringan")


def aktivitas_sedang_pria(bmr_pria: float):
    """Memproses kebutuhan kalori pria dengan aktivitas sedang."""
    proses_kalori(bmr_pria, 1.3, "Aktivitas Sedang")


def aktivitas_berat_pria(bmr_pria: float):
    """Memproses kebutuhan kalori pria dengan aktivitas berat."""
    proses_kalori(bmr_pria, 1.4, "Aktivitas Berat")


def aktivitas_ringan_wanita(bmr_wanita: float):
    """Memproses kebutuhan kalori wanita dengan aktivitas ringan."""
    proses_kalori(bmr_wanita, 1.2, "Aktivitas Ringan")


def aktivitas_sedang_wanita(bmr_wanita: float):
    """Memproses kebutuhan kalori wanita dengan aktivitas sedang."""
    proses_kalori(bmr_wanita, 1.3, "Aktivitas Sedang")


def aktivitas_berat_wanita(bmr_wanita: float):
    """Memproses kebutuhan kalori wanita dengan aktivitas berat."""
    proses_kalori(bmr_wanita, 1.4, "Aktivitas Berat")
