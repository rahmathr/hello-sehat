import os
from time import sleep

from data.saver import simpan_hasil_bmi
from data.reader import tampilkan_database_bmi

from utils.calculators import (
    tampilkan_bmi_kurus,
    tampilkan_bmi_normal,
    tampilkan_bmi_gemuk,
    tampilkan_bmi_obesitas,
)
from utils.calculators import hitung_bmi

from utils.user_inputs import (
    input_nama_lengkap,
    input_jenis_kelamin,
    input_berat_badan,
    input_umur,
    input_tinggi_badan,
)
from utils.display_headers import tampilkan_header_utama


def pilih_menu() -> str:
    os.system("cls" if os.name == "nt" else "clear")
    tampilkan_header_utama()
    print(f"| [1] Hitung BMI{7*"\t"}|")
    print(f"| [2] Lihat Database{7*"\t"}|")
    print(f"| [3] Exit{8*"\t"}|")
    print(f"+{71*"="}+")
    return int(input("Silakan pilih menu (1/2/3): "))


def hitung_dan_simpan_bmi():
    os.system("cls" if os.name == "nt" else "clear")
    tampilkan_header_utama()
    try:
        nama_lengkap: str = input_nama_lengkap()
        jenis_kelamin: str = input_jenis_kelamin()
        berat_badan: int = input_berat_badan()
        usia: int = input_umur()
        tinggi_badan: int = input_tinggi_badan()
        hasil_bmi: float = hitung_bmi(tinggi_badan, berat_badan)
        if hasil_bmi < 18.5:
            tampilkan_bmi_kurus(hasil_bmi)
            simpan_hasil_bmi(
                nama_lengkap,
                jenis_kelamin,
                berat_badan,
                usia,
                tinggi_badan,
                hasil_bmi,
                "Kurus",
            )
        elif hasil_bmi <= 25:
            tampilkan_bmi_normal(hasil_bmi)
            simpan_hasil_bmi(
                nama_lengkap,
                jenis_kelamin,
                berat_badan,
                usia,
                tinggi_badan,
                hasil_bmi,
                "Normal",
            )
        elif 25 < hasil_bmi <= 30:
            tampilkan_bmi_gemuk(hasil_bmi)
            simpan_hasil_bmi(
                nama_lengkap,
                jenis_kelamin,
                berat_badan,
                usia,
                tinggi_badan,
                hasil_bmi,
                "Gemuk",
            )
        else:
            tampilkan_bmi_obesitas(hasil_bmi)
            simpan_hasil_bmi(
                nama_lengkap,
                jenis_kelamin,
                berat_badan,
                usia,
                tinggi_badan,
                hasil_bmi,
                "Obesitas",
            )
    except ValueError as e:
        print(f"Input tidak valid: {e}")
        sleep(2)
        hitung_dan_simpan_bmi()
    except Exception as e:
        print(f"Terjadi kesalahan dalam perhitungan BMI: {e}")
        sleep(3)


def main_bmi():
    while True:
        try:
            pilihan: int = pilih_menu()
            if pilihan == 1:
                hitung_dan_simpan_bmi()
            elif pilihan == 2:
                tampilkan_database_bmi()
                sleep(2)
            elif pilihan == 3:
                print("\nTerima kasih! Sampai jumpa. 👋\n")
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
    main_bmi()
