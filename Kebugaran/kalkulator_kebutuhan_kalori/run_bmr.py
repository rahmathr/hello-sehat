"""
Program Kalkulator BMR (Basal Metabolic Rate)
================================================

Program ini dirancang untuk membantu pengguna menghitung kebutuhan kalori harian
dengan mempertimbangkan berat badan, tinggi badan, usia, jenis kelamin, dan tingkat aktivitas.
Selain itu, program ini memungkinkan pengguna untuk melihat data yang telah disimpan sebelumnya.

Fitur Utama:
1. Menghitung BMR berdasarkan input pengguna.
2. Menampilkan database hasil perhitungan sebelumnya.
3. Keluar dari program dengan aman.

Modul ini berfungsi sebagai pengontrol utama (main controller) dari program,
menghubungkan berbagai fungsi dan modul pendukung lainnya.
"""

import os
from time import sleep

from utils.display_headers import tampilan_header_utama
from utils.calculators import hitung_kebutuhan_kalori
from data.reader import read_database


def pilih_menu():
    """
    Menampilpkan menu utama program dan meminta input dari pengguna.

    Returns:
        str: Pilihan menu yang dimasukkan oleh pengguna.
    """
    os.system("cls" if os.name == "nt" else "clear")  # Membersihkan terminal sesuai OS
    tampilan_header_utama()  # Menampilkan header utama
    print(f"| [1] Hitung BMR{5*"\t"}|")  # Opsi menu untuk menghitung BMR
    print(f"| [2] Lihat Database{5*"\t"}|")  # Opsi menu untuk melihat database
    print(f"| [3] Exit{6*"\t"}|")  # Opsi menu untuk keluar dari program
    print(f"+{55*"="}+")
    return int(input("Silakan pilih menu (1/2/3): "))  # Mengembalikan pilihan pengguna


def main_bmr():
    """
    Fungsi utama untuk menjalankan logika program BMR.

    Program akan terus berjalan hingga pengguna memilih opsi untuk keluar atau
    program dihentikan secara manual.
    """
    while True:
        try:
            pilihan: int = (
                pilih_menu()
            )  # Memanggil fungsi pilih_menu untuk mendapatkan input pengguna
            if pilihan == 1:
                hitung_kebutuhan_kalori()  # Memanggil fungsi untuk menghitung kalori
            elif pilihan == 2:
                read_database()  # Memanggil fungsi untuk membaca database
                sleep(2)  # Menunggu 2 detik sebelum kembali ke menu utama
            elif pilihan == 3:
                print("\nTerima kasih! Sampai jumpa.")  # Pesan saat keluar dari program
                break  # Keluar dari loop utama
            else:
                print(
                    "\nPilihan Tidak Valid. Silakan pilih 1/2/3."
                )  # Pesan jika input tidak valid
                input(
                    "\nTekan enter untuk melanjutkan..."
                )  # Menunggu pengguna sebelum melanjutkan
        except KeyboardInterrupt:
            print(
                "\n\nProgram dihentikan oleh pengguna."
            )  # Pesan jika program dihentikan dengan Ctrl+C
            break  # Keluar dari loop utama
        except ValueError as ve:
            print(f"Terjadi kesalahan: {ve}")  # Menampilkan pesan jika ada error
            sleep(2)  # Menunggu 2 detik sebelum kembali ke menu utama


if __name__ == "__main__":
    main_bmr()
