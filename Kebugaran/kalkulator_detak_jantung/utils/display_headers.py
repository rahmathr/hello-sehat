"""
Module untuk menampilkan header pada aplikasi kalkulator detak jantung.

Fungsi-fungsi dalam module ini bertujuan untuk memberikan struktur visual yang rapi dan informatif
kepada pengguna pada berbagai bagian aplikasi, seperti header utama, header database, dan header
zona latihan.

Fungsi yang tersedia:
- tampilan_header_utama: Menampilkan header utama aplikasi dengan judul dan deskripsi singkat.
- tampilan_header_database: Menampilkan header untuk bagian database aplikasi.
- tampilan_zona_latihan_detak_jantung: Menampilkan header untuk zona latihan detak jantung.
"""


def tampilan_header_utama() -> str:
    """
    Menampilkan header utama aplikasi dengan deskripsi singkat
    tentang fungsi kalkulator detak jantung istirahat (RHR).
    """
    judul_utama: str = "Kalkulator Detak Jantung (RHR)".center(88)
    print(f" {88*' '} ")
    print(f" {judul_utama} ")
    print(f" {88*' '} ")

    # Deskripsi singkat tentang aplikasi
    deskripsi_utama_satu: str = (
        "Cari tahu berapa detak jantung istirahat (RHR) maksimum untuk usia Anda ".center(
            88
        )
    )
    print(f" {deskripsi_utama_satu} ")

    deskripsi_utama_dua: str = (
        "dan bagaimana Zona intensitas olahraga dan faktor lain memengaruhi detak jantung".center(
            88
        )
    )
    print(f" {deskripsi_utama_dua} ")
    print(f" {88*' '} ")


def tampilan_header_database() -> str:
    """
    Menampilkan header untuk bagian database yang menyimpan
    riwayat perhitungan detak jantung.
    """
    judul_database: str = "Kalkulator Detak Jantung (RHR)   Database".center(102)
    print(f" {102*' '} ")
    print(f" {judul_database} ")
    print(f" {102*' '} ")


def tampilan_zona_latihan_detak_jantung() -> str:
    """
    Menampilkan menu untuk memilih zona latihan detak jantung
    berdasarkan intensitas rendah, sedang, atau tinggi.
    """
    judul_zona_latihan: str = "Zona Latihan Detak Jantung".center(31)
    print(f"\n {31*' '} ")
    print(f" {judul_zona_latihan} ")
    print(f" {31*' '} ")

    # Menu pilihan zona latihan
    zona_pilihan: list[str] = [
        "  [1] Zona Intensitas Rendah\t ",
        "  [2] Zona Intensitas Sedang\t ",
        "  [3] Zona Intensitas Tinggi\t ",
    ]
    for tampil in zona_pilihan:
        print(tampil)
    print(f" {31*' '} ")
