"""
Module untuk meminta input dari pengguna.

Fungsi-fungsi dalam module ini bertujuan untuk memvalidasi data yang dimasukkan oleh pengguna
sehingga sesuai dengan format atau rentang yang diharapkan. 
Fungsi ini dapat digunakan untuk mengumpulkan informasi seperti nama lengkap, umur, jenis kelamin,
tinggi badan, berat badan, dan tingkat intensitas aktivitas fisik.

Fungsi yang tersedia:
- input_nama_lengkap: Meminta input nama lengkap dengan validasi huruf dan spasi.
- input_umur: Meminta input umur dengan validasi rentang usia 0-120.
- input_jenis_kelamin: Meminta input jenis kelamin dengan validasi 'L' atau 'P'.
- input_tinggi_badan: Meminta input tinggi badan dengan validasi rentang 0-300 cm.
- input_berat_badan: Meminta input berat badan dengan validasi rentang 0-300 kg.
- input_intensitas_aktivitas: Meminta input tingkat aktivitas dengan validasi pilihan 1, 2, atau 3.
"""


def input_nama_lengkap() -> str:
    """
    Meminta pengguna untuk memasukkan nama lengkap mereka.

    Returns:
        str: Nama lengkap yang diinput oleh pengguna, diubah menjadi format judul (title case).
    """
    while True:
        nama_lengkap: str = (
            input("Nama Lengkap : ").strip().title()
        )  # Meminta input dan mengubah ke title case
        if all(
            x.isalpha() or x.isspace() for x in nama_lengkap
        ):  # Memastikan hanya huruf dan spasi yang diizinkan
            return nama_lengkap

        print(
            "\n>>> Input Harus Berupa Huruf dan Spasi!!\n"
        )  # Pesan kesalahan jika input tidak valid


def input_umur() -> int:
    """
    Meminta pengguna untuk memasukkan umur mereka.

    Returns:
        int: Umur pengguna jika valid (antara 0 dan 120).
    """
    while True:
        try:
            umur: int = int(
                input("Berapa umur Anda saat ini? : ")
            )  # Meminta input umur sebagai integer
            if 0 <= umur <= 120:  # Memastikan umur dalam rentang yang valid
                return umur
            print(
                "\n>>> Usia harus lebih dari 0 dan kurang dari atau sama dengan 120!!\n"
            )
        except ValueError:
            print(
                "\n>>> Input Harus Berupa Angka!!\n"
            )  # Pesan kesalahan jika input bukan angka


def input_jenis_kelamin() -> str:
    """
    Meminta pengguna untuk memasukkan jenis kelamin mereka.

    Returns:
        str: Jenis kelamin dalam format 'L' atau 'P'.
    """
    while True:
        jenis_kelamin: str = (
            input("Apa jenis kelamin Anda? (L/P) : ").strip().upper()
        )  # Meminta input dan mengubah ke huruf besar
        if jenis_kelamin in ["L", "P"]:  # Memastikan input valid ('L' atau 'P')
            return jenis_kelamin
        else:
            print(
                "\n>>> Input harus berupa 'L' atau 'P'!!\n"
            )  # Pesan kesalahan jika input tidak valid


def input_tinggi_badan() -> int:
    """
    Meminta pengguna untuk memasukkan tinggi badan mereka.

    Returns:
        int: Tinggi badan dalam satuan cm jika valid (antara 0 dan 300).
    """
    while True:
        try:
            tinggi_badan: int = int(
                input("Berapa tinggi Anda? (cm) : ")
            )  # Meminta input tinggi badan sebagai integer
            if (
                0 < tinggi_badan <= 300
            ):  # Memastikan tinggi badan dalam rentang yang valid
                return tinggi_badan
            else:
                print(
                    "\n>>> Tinggi badan harus lebih dari 0 dan kurang dari atau sama dengan 300!!\n"
                )
        except ValueError:
            print(
                "\n>>> Input Harus Berupa Angka!!\n"
            )  # Pesan kesalahan jika input bukan angka


def input_berat_badan() -> int:
    """
    Meminta pengguna untuk memasukkan berat badan mereka.

    Returns:
        int: Berat badan dalam satuan kg jika valid (antara 0 dan 300).
    """
    while True:
        try:
            berat_badan: int = int(
                input("Berapa berat badan Anda? (kg) : ")
            )  # Meminta input berat badan sebagai integer
            if (
                0 < berat_badan <= 300
            ):  # Memastikan berat badan dalam rentang yang valid
                return berat_badan
            else:
                print(
                    "\n>>> Berat badan harus lebih dari 0 dan kurang dari atau sama dengan 300!!\n"
                )
        except ValueError:
            print(
                "\n>>> Input Harus Berupa Angka!!\n"
            )  # Pesan kesalahan jika input bukan angka


def input_intensitas_aktivitas() -> int:
    """
    Meminta pengguna untuk memilih tingkat intensitas aktivitas fisik.

    Returns:
        int: Pilihan tingkat aktivitas (1, 2, atau 3).
    """
    while True:
        try:
            total_kalori: int = int(
                input("Pilih tingkat intensitas aktivitas fisik Anda : ")
            )  # Meminta input pilihan aktivitas
            if total_kalori in (1, 2, 3):  # Memastikan pilihan valid (1, 2, atau 3)
                return total_kalori
            print(
                "\n>>> Pilihan tidak valid. Harap pilih 1, 2, atau 3.\n"
            )  # Pesan kesalahan jika pilihan tidak valid
        except ValueError:
            print(
                "\n>>> Input Harus Berupa Angka!!\n"
            )  # Pesan kesalahan jika input bukan angka
