import os
from time import sleep

from utils import display_headers
from utils import calculators
from data import reader


def pilih_menu() -> str:
    os.system("cls" if os.name == "nt" else "clear")
    display_headers.tampilan_header_utama()
    print(f"| [1] Hitung BMR{4*"\t"}|")
    print(f"| [2] Lihat Database{4*"\t"}|")
    print(f"| [3] Exit{5*"\t"}|")
    print(f"+{47*"="}+")
    return int(input("Silakan pilih menu (1/2/3): "))


def main_bmr():
    while True:
        try:
            pilihan: int = pilih_menu()
            if pilihan == 1:
                calculators.hitung_kebutuhan_kalori()
            elif pilihan == 2:
                reader.read_database()
                sleep(2)
            elif pilihan == 3:
                print("\nTerima kasih! Sampai jumpa. 👋")
                break
            else:
                print("\nPilihan Tidak Valid. Silakan pilih 1/2/3.")
                input("\nTekan enter untuk melanjutkan...")
        except KeyboardInterrupt:
            print("\n\nProgram dihentikan oleh pengguna.")
            break
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            sleep(2)


if __name__ == "__main__":
    main_bmr()