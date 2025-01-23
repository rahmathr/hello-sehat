"""
Module ini berisi fungsi-fungsi untuk meminta input dari pengguna.

Fungsi-fungsi ini digunakan untuk memastikan validitas data yang dimasukkan oleh pengguna
seperti nama lengkap, jenis kelamin, berat badan, umur, dan tinggi badan.
"""


def input_nama_lengkap() -> str:
    """
    Meminta pengguna untuk memasukkan nama lengkap. Nama hanya boleh terdiri dari huruf
    dan spasi.

    Returns:
        str: Nama lengkap pengguna yang telah divalidasi.
    """
    while True:
        nama_lengkap: str = input("Nama Lengkap: ").strip().title()
        if all(x.isalpha() or x.isspace() for x in nama_lengkap):
            return nama_lengkap
        print("\n>>> Input Harus Berupa Huruf dan Spasi!!\n")


def input_jenis_kelamin() -> str:
    """
    Meminta pengguna untuk memasukkan jenis kelamin dengan pilihan 'L' (Laki-laki)
    atau 'P' (Perempuan).

    Returns:
        str: Jenis kelamin pengguna ('L' atau 'P').
    """
    while True:
        jenis_kelamin: str = input("Apa jenis kelamin Anda? (L/P) : ").strip().upper()
        if jenis_kelamin in ["L", "P"]:
            return jenis_kelamin
        print("\n>>> Input harus berupa 'L' atau 'P'!!\n")


def input_berat_badan() -> int:
    """
    Meminta pengguna untuk memasukkan berat badan dalam kilogram. Nilai harus lebih dari 0
    dan kurang dari atau sama dengan 300.

    Returns:
        int: Berat badan pengguna yang telah divalidasi.
    """
    while True:
        try:
            berat_badan: int = int(input("Berapa berat badan Anda? (kg) : "))
            if 0 < berat_badan <= 300:
                return berat_badan
            print(
                "\n>>> Berat badan harus lebih dari 0 dan kurang dari atau sama dengan 300!!\n"
            )
        except ValueError:
            print("\n>>> Input Harus Berupa Angka!!\n")


def input_umur() -> int:
    """
    Meminta pengguna untuk memasukkan umur. Nilai harus lebih dari 0 dan kurang dari
    atau sama dengan 120.

    Returns:
        int: Umur pengguna yang telah divalidasi.
    """
    while True:
        try:
            umur: int = int(input("Berapa umur Anda saat ini? : "))
            if 0 < umur <= 120:
                return umur
            print(
                "\n>>> Umur harus lebih dari 0 dan kurang dari atau sama dengan 120!!\n"
            )
        except ValueError:
            print("\n>>> Input Harus Berupa Angka!!\n")


def input_tinggi_badan() -> int:
    """
    Meminta pengguna untuk memasukkan tinggi badan dalam sentimeter. Nilai harus lebih dari 0
    dan kurang dari atau sama dengan 300.

    Returns:
        int: Tinggi badan pengguna yang telah divalidasi.
    """
    while True:
        try:
            tinggi_badan: int = int(input("Berapa tinggi Anda? (cm) : "))
            if 0 < tinggi_badan <= 300:
                return tinggi_badan
            print(
                "\n>>> Tinggi badan harus lebih dari 0 dan kurang dari atau sama dengan 300!!\n"
            )
        except ValueError:
            print("\n>>> Input Harus Berupa Angka!!\n")
