"""
Fungsi untuk menyimpan hasil perhitungan BMR ke dalam file CSV.

Fungsi:
- simpan_proses_bmr: Menyimpan data pengguna dan hasil kalkulasi BMR serta kebutuhan kalori total.

Detail:
File yang digunakan untuk penyimpanan adalah 'dataframes.csv', yang berlokasi di folder
'Kalkulator Kebutuhan Kalori/data/'. Jika file belum ada, file baru akan dibuat secara otomatis.
"""

def simpan_proses_bmr(
    nama_lengkap: str,
    jenis_kelamin: str,
    berat_badan: int,
    umur: int,
    tinggi_badan: int,
    bmr: int,
    total_kalori: int,
):
    """
    Menyimpan data hasil perhitungan BMR ke dalam file CSV.

    Parameter:
    - nama_lengkap (str): Nama lengkap pengguna.
    - jenis_kelamin (str): Jenis kelamin pengguna ('L' untuk laki-laki, 'P' untuk perempuan).
    - berat_badan (int): Berat badan pengguna dalam kilogram.
    - umur (int): umur pengguna dalam tahun.
    - tinggi_badan (int): Tinggi badan pengguna dalam sentimeter.
    - bmr (int): Nilai Basal Metabolic Rate pengguna.
    - total_kalori (int): Total kebutuhan kalori berdasarkan tingkat aktivitas.

    File yang digunakan untuk menyimpan data:
    'dataframes.csv' di folder 'Kalkulator Kebutuhan Kalori/data/'.
    Jika file tidak ada, data akan ditambahkan ke file yang baru.
    """
    file_path: str = (
        "Kebugaran/kalkulator_kebutuhan_kalori/data/dataframes.csv"  # Lokasi file penyimpanan
    )

    try:
        # Membuka file CSV dalam mode append ('a') untuk menambahkan data baru
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(
                f"{nama_lengkap},{jenis_kelamin},{berat_badan},{umur},{tinggi_badan},{int(bmr)},{int(total_kalori)}\n"
            )
            # Menulis data dalam format CSV, dipisahkan oleh koma
    except ValueError as ve:
        # Menangkap dan mencetak pesan kesalahan jika terjadi error saat menyimpan data
        print(f"Terjadi kesalahan saat menyimpan hasil BMR: {ve}")
