"""
Modul ini menyediakan fungsi untuk menyimpan hasil perhitungan BMI ke dalam file CSV.

Fungsi:
- simpan_hasil_bmi: Menyimpan data BMI pengguna beserta informasi pribadi ke file CSV.
"""


def simpan_hasil_bmi(
    nama: str,
    jenis_kelamin: str,
    berat_badan: int,
    usia: int,
    tinggi_badan: int,
    bmi: int,
    status_berat_badan: str,
):
    """
    Menyimpan hasil perhitungan BMI pengguna ke dalam file CSV.

    Args:
        nama (str): Nama lengkap pengguna.
        jenis_kelamin (str): Jenis kelamin pengguna ('L' untuk laki-laki, 'P' untuk perempuan).
        berat_badan (int): Berat badan pengguna dalam kilogram.
        usia (int): Usia pengguna dalam tahun.
        tinggi_badan (int): Tinggi badan pengguna dalam sentimeter.
        bmi (int): Nilai BMI yang telah dihitung.
        status_berat_badan (str): Kategori berat badan berdasarkan BMI.

    File:
        data/dataframe.csv: File tempat data disimpan. Jika file tidak ada, 
        data akan ditambahkan ke file baru.

    Raises:
        ValueError: Jika terjadi kesalahan saat menyimpan data ke file.
    """
    file_path: str = (
        "Kebugaran/kalkulator_bmi/data/dataframe.csv"  # Lokasi file tempat data disimpan
    )
    try:
        with open(
            file_path, "a", encoding="utf-8"
        ) as file:  # Membuka file dalam mode append
            file.write(
                f"{nama},{jenis_kelamin},{berat_badan},{usia},{tinggi_badan},{int(bmi)},{status_berat_badan}\n"
            )  # Menulis data pengguna ke file CSV
    except ValueError as ve:
        print(
            f"Terjadi kesalahan saat menyimpan hasil BMI: {ve}"
        )  # Menampilkan pesan jika ada kesalahan
