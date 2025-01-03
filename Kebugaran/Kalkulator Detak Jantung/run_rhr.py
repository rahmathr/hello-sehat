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
    os.system("cls" if os.name == "nt" else "clear")
    tampilan_header_utama()
    print(f"| [1] Hitung Denyut Jantung Istirahat{7*"\t"} |")
    print(f"| [2] Lihat Database{9*"\t"} |")
    print(f"| [3] Exit{10*"\t"} |")
    print(f"+{88*"="}+")
    return int(input("Silahkan pilih menu (1/2/3): "))


def zona_denyut_jantung():
    os.system("cls" if os.name == "nt" else "clear")
    tampilan_header_utama()
    try:
        nama_lengkap: str = input_nama_lengkap()
        jenis_kelamin: str = input_jenis_kelamin()
        umur: int = input_umur()
        denyut_jantung_istirahat: int = input_detak_jantung_istirahat()

        denyut_jantung_maks: int = hitung_denyut_jantung_maksimum(umur=umur)

        tampilan_zona_latihan_detak_jantung()
        zona_latihan: int = input_tingkat_aktivitas()
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
        elif zona_latihan == 3:
            rendah_bawah, rendah_atas = zona_intensitas_tinggi(
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
        else:
            pass
    except:
        pass


def main_denyut_jantung_istirahat():
    while True:
        try:
            pilihan: str = pilih_menu()
            if pilihan == 1:
                zona_denyut_jantung()
            elif pilihan == 2:
                read_database()
            elif pilihan == 3:
                print("\nTerima kasih! Sampai jumpa. 👋\n")
                break
            else:
                print("\nPilihan Tidak Valid. Silakan pilih 1/2/3.")
                input("\nTekan enter untuk melanjutkan...")
        except:
            pass


if __name__ == "__main__":
    main_denyut_jantung_istirahat()
