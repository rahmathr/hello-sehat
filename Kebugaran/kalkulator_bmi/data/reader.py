"""
Modul ini menyediakan fungsi untuk menampilkan isi database BMI dalam format tabel.

Fungsi:
- tampilkan_database_bmi: Membaca dan menampilkan isi file CSV yang menyimpan data BMI pengguna.
"""

import os
from utils.display_headers import tampilkan_header_database

import pandas as pd


def tampilkan_database_bmi():
    """
    Menampilkan isi database BMI dari file CSV dalam format tabel.

    File yang digunakan:
        Kalkulator BMI/data/dataframe.csv: File CSV tempat data BMI disimpan.

    Proses:
    - Membersihkan layar sebelum menampilkan data.
    - Menampilkan header database.
    - Membaca file CSV menggunakan pandas dan mencetak isinya.

    Error Handling:
    - FileNotFoundError: Ditampilkan jika file tidak ditemukan.
    - pd.errors.EmptyDataError: Ditampilkan jika file kosong.
    - Exception: Menangkap kesalahan lainnya saat membaca file.

    Interaksi Pengguna:
        Pengguna diminta menekan Enter untuk melanjutkan setelah data ditampilkan.
    """
    os.system("cls" if os.name == "nt" else "clear")  # Membersihkan layar
    tampilkan_header_database()  # Menampilkan header
    file_path: str = "Kebugaran/kalkulator_bmi/data/dataframe.csv"  # Lokasi file CSV

    try:
        content = pd.read_csv(file_path)  # Membaca file CSV
        print(content)  # Menampilkan isi file
        print(f" {85*" "} ")  # Garis estetika
    except FileNotFoundError:
        print(f"File tidak ditemukan: {file_path}")  # Pesan jika file tidak ditemukan
    except pd.errors.EmptyDataError:
        print(f"File kosong: {file_path}")  # Pesan jika file kosong
    except ValueError as ve:
        print(
            f"Terjadi kesalahan saat membaca file: {ve}"
        )  # Pesan jika ada kesalahan lain

    input(
        "\nTekan Enter untuk melanjutkan..."
    )  # Menunggu input pengguna sebelum melanjutkan
