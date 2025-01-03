def tampilan_header_utama():
    judul_utama: str = "Kalkulator BMI".center(47)
    print(f"+{47*'='}+")
    print(f"|{judul_utama}|")
    print(f"+{47*'='}+")

    deskripsi_utama = "Apakah berat badan Anda sudah ideal?".center(47)
    print(f"|{deskripsi_utama}|")
    print(f"+{47*'='}+")


def tampilan_header_database():
    judul_database: str = "Kalkulator BMI | Database".center(103)
    print(f"+{103*'='}+")
    print(f"|{judul_database}|")
    print(f"+{103*'='}+")


def tampilan_header_aktivitas_fisik():
    judul_aktivitas_fisik: str = "TINGKAT AKTIVITAS FISIK".center(63)
    print(f"+{63*'='}+")
    print(f"|{judul_aktivitas_fisik}|")
    print(f"+{63*'='}+")
    aktivitas_pilihan: str = [
        "| [1] Hampir tidak pernah berolahraga\t\t\t\t|",
        "| [2] Jarang berolahraga\t\t\t\t\t|",
        "| [3] Sering berolahraga atau beraktivitas fisik berat\t\t|",
    ]
    for pilihan in aktivitas_pilihan:
        print(pilihan)
    print(f"+{63*'='}+")
