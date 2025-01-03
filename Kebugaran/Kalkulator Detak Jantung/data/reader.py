import os
import pandas as pd
from utils.display_headers import tampilan_header_database


def read_database():
    os.system("cls" if os.name == "nt" else "clear")
    tampilan_header_database()
    file_path: str = "Kalkulator Detak Jantung/data/dataframes.csv"

    try:
        content = pd.read_csv(file_path)
        print(content)
        print(f"+{102*'='}+")
    except FileNotFoundError:
        print(f"File tidak ditemukan: {file_path}")
    except pd.errors.EmptyDataError:
        print(f"File kosong: {file_path}")
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file: {e}")

    input("\nTekan Enter untuk melanjutkan...")
