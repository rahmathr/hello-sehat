"""
Modul ini menyediakan fungsi untuk menampilkan header pada aplikasi Kalkulator BMI.

Fungsi:
- tampilkan_header_utama: Menampilkan header utama dengan judul dan deskripsi aplikasi.
- tampilkan_header_database: Menampilkan header untuk halaman database aplikasi.
"""


def tampilkan_header_utama():
    """
    Menampilkan header utama untuk aplikasi Kalkulator BMI.

    Header ini mencakup judul utama dan deskripsi singkat tentang fungsi kalkulator.
    """
    judul_utama: str = "Kalkulator BMI".center(
        71
    )  # Menampilkan judul di tengah dengan lebar 71 karakter
    print(f" {71*" "} ")  # Baris kosong untuk estetika
    print(f" {judul_utama} ")
    deskripsi_utama = "Apakah berat badan Anda sudah ideal?".center(
        71
    )  # Menampilkan deskripsi di tengah
    print(f" {71*" "} ")  # Baris kosong untuk estetika
    print(f" {deskripsi_utama} ")
    print(f" {71*" "} ")  # Baris kosong untuk estetika


def tampilkan_header_database():
    """
    Menampilkan header untuk halaman database Kalkulator BMI.

    Header ini mencakup judul database untuk memberikan konteks kepada pengguna.
    """
    judul_database: str = "Kalkulator BMI   Database".center(
        85
    )  # Menampilkan judul database di tengah dengan lebar 85 karakter
    print(f" {85*" "} ")  # Baris kosong untuk estetika
    print(f" {judul_database} ")
    print(f" {85*" "} ")  # Baris kosong untuk estetika
