def tampilan_header_utama():
    judul_utama: str = "Kalkulator Detak Jantung (RHR)".center(88)
    print(f"+{88*"="}+")
    print(f"|{judul_utama}|")
    print(f"+{88*"="}+")

    deskripsi_utama_satu: str = (
        "Cari tahu berapa detak jantung istirahat (RHR) maksimum untuk usia Anda ".center(
            88
        )
    )
    print(f"|{deskripsi_utama_satu}|")

    deskripsi_utama_dua: str = (
        "dan bagaimana Zona intensitas olahraga dan faktor lain memengaruhi detak jantung".center(
            88
        )
    )
    print(f"|{deskripsi_utama_dua}|")
    print(f"+{88*"="}+")


def tampilan_header_database():
    judul_database: str = "Kalkulator Detak Jantung (RHR) | Database".center(102)
    print(f"+{102*"="}+")
    print(f"|{judul_database}|")
    print(f"+{102*"="}+")


def tampilan_zona_latihan_detak_jantung():
    judul_zona_latihan: str = "Zona Latihan Detak Jantung".center(31)
    print(f"\n+{31*"="}+")
    print(f"|{judul_zona_latihan}|")
    print(f"+{31*"="}+")

    zona_pilihan: str = [
        "| [1] Zona Intensitas Rendah\t|",
        "| [2] Zona Intensitas Sedang\t|",
        "| [3] Zona Intensitas Tinggi\t|",
    ]
    for tampil in zona_pilihan:
        print(tampil)
    print(f"+{31*"="}+")
