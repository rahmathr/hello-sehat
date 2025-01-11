"""
Module untuk membaca dan menampilkan isi database kalkulator detak jantung.

Fungsi utama:
- read_database: Membaca file CSV yang berisi data detak jantung dan menampilkannya.

Ketika file tidak ditemukan, kosong, atau terjadi kesalahan saat membaca file, 
modul ini akan memberikan pesan kesalahan yang sesuai.

Dependencies:
- os: Untuk membersihkan layar terminal sebelum menampilkan informasi.
- pandas: Untuk membaca dan menampilkan isi file CSV.
- display_headers: Modul internal untuk menampilkan header pada bagian database.
"""

import os
import pandas as pd
from utils.display_headers import tampilan_header_database


def read_database():
    """
    Membaca dan menampilkan isi file database dalam format tabel.

    Raises:
        FileNotFoundError: Jika file database tidak ditemukan.
        pd.errors.EmptyDataError: Jika file database kosong.
        Exception: Untuk semua jenis kesalahan lainnya selama pembacaan file.
    """
    # Membersihkan layar konsol
    os.system("cls" if os.name == "nt" else "clear")

    # Menampilkan header khusus untuk database
    tampilan_header_database()

    # Lokasi file database
    file_path: str = "Kebugaran/kalkulator_detak_jantung/data/dataframes.csv"

    try:
        # Membaca isi file CSV menggunakan pandas
        content = pd.read_csv(file_path)
        # Menampilkan isi file ke konsol
        print(content)
        print(f"+{102*'='}+")
    except FileNotFoundError:
        # Menangani kesalahan jika file tidak ditemukan
        print(f"File tidak ditemukan: {file_path}")
    except pd.errors.EmptyDataError:
        # Menangani kesalahan jika file kosong
        print(f"File kosong: {file_path}")
    except ValueError as ve:
        # Menangani kesalahan lainnya
        print(f"Terjadi kesalahan saat membaca file: {ve}")

    # Menunggu input dari pengguna untuk melanjutkan
    input("\nTekan Enter untuk melanjutkan...")
