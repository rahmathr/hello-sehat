def simpan_proses_rhr(
    nama_lengkap: str,
    jenis_kelamin: str,
    umur: int,
    tingkat_aktivitas: str,
    detak_jantung_maks: int,
    detak_jantung_istirahat: int,
    batas_bawah: float,
    batas_atas: float,
):
    file_path: str = "Kalkulator Detak Jantung/data/dataframes.csv"
    try:
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(
                f"{nama_lengkap},{jenis_kelamin},{umur},{tingkat_aktivitas},{detak_jantung_maks},{detak_jantung_istirahat},{batas_bawah},{batas_atas}\n"
            )
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan hasil BMI: {e}")
