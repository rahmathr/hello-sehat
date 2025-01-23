"""
Module untuk menampilkan header pada aplikasi kalkulator kebutuhan kalori.

Fungsi-fungsi dalam module ini bertujuan untuk memberikan struktur visual yang rapi dan informatif
kepada pengguna pada berbagai bagian aplikasi, seperti header utama, header database, dan header
aktivitas fisik.

Fungsi yang tersedia:
- tampilan_header_utama: Menampilkan header utama aplikasi dengan judul dan deskripsi singkat.
- tampilan_header_database: Menampilkan header untuk bagian database aplikasi.
- tampilan_header_aktivitas_fisik: Menampilkan header untuk bagian tingkat aktivitas fisik.
"""


def tampilan_header_utama() -> str:
    """
    Menampilkan header utama aplikasi.

    Header ini mencakup judul "Kalkulator Kebutuhan Kalori" dan deskripsi singkat
    "Apakah berat badan Anda sudah ideal?" yang diformat ke tengah.
    """
    judul_utama: str = "Kalkulator Kebutuhan Kalori".center(
        55
    )  # Mengatur judul utama di tengah dengan lebar 55 karakter
    print(f" {55*' '} ")  # Garis horizontal atas
    print(f" {judul_utama} ")  # Baris judul utama
    print(f" {55*' '} ")  # Garis horizontal bawah

    deskripsi_utama = "Berapa jumlah kalori yang Anda butuhkan setiap hari?".center(
        55
    )  # Mengatur deskripsi di tengah
    print(f" {deskripsi_utama} ")  # Baris deskripsi utama
    print(f" {55*' '} ")  # Garis horizontal bawah


def tampilan_header_database() -> str:
    """
    Menampilkan header untuk bagian database.

    Header ini mencakup judul "Kalkulator Kebutuhan Kalori   Database" yang diformat ke tengah
    dengan lebar 84 karakter.
    """
    judul_database: str = "Kalkulator Kebutuhan Kalori   Database".center(
        85
    )  # Mengatur judul database di tengah
    print(f" {85*' '} ")  # Garis horizontal atas
    print(f" {judul_database} ")  # Baris judul database
    print(f" {85*' '} ")  # Garis horizontal bawah


def tampilan_header_aktivitas_fisik() -> str:
    """
    Menampilkan header untuk bagian tingkat aktivitas fisik.

    Header ini mencakup judul "TINGKAT AKTIVITAS FISIK" yang diformat ke tengah
    dengan lebar 63 karakter, diikuti dengan daftar pilihan tingkat aktivitas.
    """
    judul_aktivitas_fisik: str = "TINGKAT AKTIVITAS FISIK".center(
        63
    )  # Mengatur judul aktivitas fisik di tengah
    print(f"\n {63*' '} ")  # Garis horizontal atas
    print(f" {judul_aktivitas_fisik} ")  # Baris judul aktivitas fisik
    print(f" {63*' '} ")  # Garis horizontal bawah

    aktivitas_pilihan: list = [
        "  [1] Hampir tidak pernah berolahraga\t\t\t\t ",
        "  [2] Jarang berolahraga\t\t\t\t\t ",
        "  [3] Sering berolahraga atau beraktivitas fisik berat\t\t ",
    ]
    for pilihan in aktivitas_pilihan:
        print(pilihan)  # Menampilkan setiap pilihan aktivitas fisik

    print(f" {63*' '} ")  # Garis horizontal bawah
