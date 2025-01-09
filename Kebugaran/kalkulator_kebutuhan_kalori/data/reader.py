"""
Module untuk membaca dan menampilkan isi database kalkulator kebutuhan kalori.

Fungsi utama:
- read_database: Membaca file CSV yang berisi data perhitungan BMR dan menampilkannya.

Ketika file tidak ditemukan, kosong, atau terjadi kesalahan saat membaca file, 
modul ini akan memberikan pesan kesalahan yang sesuai.

Dependencies:
- os: Untuk membersihkan layar terminal sebelum menampilkan informasi.
- pandas: Untuk membaca dan menampilkan isi file CSV.
- display_headers: Modul internal untuk menampilkan header pada bagian database.
"""

import os
import pandas as pd

from utils import display_headers


def read_database():
    """
    Membaca dan menampilkan isi database dari file CSV yang berisi data perhitungan BMR.

    File yang digunakan: 'dataframes.csv' di folder 'Kalkulator Kebutuhan Kalori/data/'.
    Jika file tidak ditemukan, kosong,
    atau terjadi kesalahan lainnya, pesan yang sesuai akan ditampilkan.

    Tidak ada parameter yang diterima atau nilai yang dikembalikan.
    """
    # Membersihkan layar terminal sesuai dengan sistem operasi
    os.system("cls" if os.name == "nt" else "clear")

    # Menampilkan header database menggunakan fungsi yang tersedia di modul display_headers
    display_headers.tampilan_header_database()

    # Path file database CSV
    file_path: str = "Kebugaran/kalkulator_kebutuhan_kalori/data/dataframes.csv"

    try:
        # Membaca isi file CSV menggunakan pandas dan menampilkannya
        content = pd.read_csv(file_path)
        print(content)
        print(f"+{85*'='}+")
    except FileNotFoundError:
        # Pesan jika file CSV tidak ditemukan
        print(f"File tidak ditemukan: {file_path}")
    except pd.errors.EmptyDataError:
        # Pesan jika file CSV kosong
        print(f"File kosong: {file_path}")
    except ValueError as ve:
        # Pesan jika terjadi kesalahan lainnya saat membaca file
        print(f"Terjadi kesalahan saat membaca file: {ve}")

    # Menunggu pengguna menekan tombol Enter sebelum melanjutkan
    input("\nTekan Enter untuk melanjutkan...")
