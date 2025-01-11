"""
Modul Input dan Validasi Data Pengguna
====================================

Modul ini digunakan untuk mengelola input data dari pengguna dan memastikan validasi 
terhadap data yang dimasukkan. Input meliputi nama lengkap, jenis kelamin, umur, tingkat aktivitas, 
dan detak jantung istirahat. Semua input diverifikasi agar sesuai dengan 
aturan yang telah ditentukan.

Fungsi yang tersedia:
1. input_nama_lengkap: Memvalidasi nama lengkap hanya berisi huruf dan spasi.
2. input_jenis_kelamin: Memvalidasi input jenis kelamin sebagai 'L' atau 'P'.
3. input_umur: Memvalidasi input umur dalam rentang 1 hingga 120 tahun.
4. input_tingkat_aktivitas: Memvalidasi tingkat aktivitas dalam rentang 1 hingga 3.
5. input_detak_jantung_istirahat: Memvalidasi detak jantung istirahat dalam 
    rentang 20 hingga 120 bpm.
"""


def input_nama_lengkap() -> str:
    """
    Meminta input nama lengkap dari pengguna. Nama hanya boleh berisi huruf dan spasi.

    Returns:
        str: Nama lengkap yang telah divalidasi.
    """
    while True:
        nama_lengkap: str = input("Nama Lengkap: ").strip().title()
        # Validasi nama hanya berisi huruf dan spasi
        if all(huruf.isalpha() or huruf.isspace() for huruf in nama_lengkap):
            return nama_lengkap
        print("\n>>> Input Harus Berupa Huruf dan Spasi!!\n")


def input_jenis_kelamin() -> str:
    """
    Meminta input jenis kelamin dari pengguna (L/P).

    Returns:
        str: Jenis kelamin yang telah divalidasi ('L' atau 'P').
    """
    while True:
        jenis_kelamin: str = input("Apa jenis kelamin anda? (L/P) : ").strip().upper()
        # Validasi input hanya menerima 'L' atau 'P'
        if jenis_kelamin in ["L", "P"]:
            return jenis_kelamin
        print("\n>>> Input harus berupa 'L' atau 'P'!!\n")


def input_umur() -> int:
    """
    Meminta input umur pengguna. Umur harus berupa angka antara 1 hingga 120.

    Returns:
        int: Umur yang telah divalidasi.
    """
    while True:
        try:
            umur: int = int(input("Berapa umur anda saat ini? : "))
            # Validasi umur dalam rentang 1 hingga 120
            if 0 < umur <= 120:
                return umur
            print(
                "\n>>> Umur harus lebih dari 0 dan kurang dari atau sama dengan 120!!\n"
            )
        except ValueError:
            print("\n>>> Input Harus Berupa Angka!!\n")


def input_tingkat_aktivitas():
    """
    Meminta input tingkat aktivitas dari pengguna.
    Tingkat aktivitas harus berupa angka antara 1 hingga 3.

    Returns:
        int: Tingkat aktivitas yang telah divalidasi (1, 2, atau 3).
    """
    while True:
        try:
            tingkat_aktivitas: int = int(
                input("Seberapa aktif Anda sehari-hari? (1-3) : ")
            )
            # Validasi tingkat aktivitas hanya menerima 1, 2, atau 3
            if tingkat_aktivitas in [1, 2, 3]:
                return tingkat_aktivitas
            print("\n>>> Pilihan harus diantara (1/2/3)\n")
        except ValueError:
            print("\n>>> Input Harus Berupa Angka!!\n")


def input_detak_jantung_istirahat():
    """
    Meminta input detak jantung istirahat pengguna dalam bpm. Nilai harus antara 20 hingga 120.

    Returns:
        int: Detak jantung istirahat yang telah divalidasi.
    """
    while True:
        try:
            detak_jantung: int = int(
                input("Berapa detak jantung istirahat Anda (bpm) : ")
            )
            # Validasi detak jantung dalam rentang 20 hingga 120 bpm
            if 20 <= detak_jantung <= 120:
                return detak_jantung
            print("\n>>> Detak jantung istirahat harus antara 20 dan 120 bpm!!\n\n")
        except ValueError:
            print("\n>>> Input Harus Berupa Angka!!\n")
