def input_nama_lengkap() -> str:
    while True:
        nama_lengkap: str = input("Nama Lengkap: ").strip().title()
        if all(huruf.isalpha() or huruf.isspace() for huruf in nama_lengkap):
            return nama_lengkap
        else:
            print("\n>>> Input Harus Berupa Huruf dan Spasi!!\n")


def input_jenis_kelamin() -> str:
    while True:
        jenis_kelamin: str = input("Apa jenis kelamin anda? (L/P) : ").strip().upper()
        if jenis_kelamin in ["L", "P"]:
            return jenis_kelamin
        else:
            print("\n>>> Input harus berupa 'L' atau 'P'!!\n")


def input_umur() -> int:
    while True:
        try:
            umur: int = int(input("Berapa umur anda saat ini? : "))
            if 0 < umur <= 120:
                return umur
            else:
                print(
                    "\n>>> Umur harus lebih dari 0 dan kurang dari atau sama dengan 120!!\n"
                )
        except ValueError:
            print("\n>>> Input Harus Berupa Angka!!\n")


def input_tingkat_aktivitas():
    while True:
        try:
            tingkat_aktivitas: int = int(
                input("Seberapa aktif Anda sehari-hari? (1-3) : ")
            )
            if tingkat_aktivitas in [1, 2, 3]:
                return tingkat_aktivitas
            else:
                print("\n>>> Pilihan harus diantara (1/2/3)\n")
        except ValueError:
            print("\n>>> Input Harus Berupa Angka!!\n")


def input_detak_jantung_istirahat():
    while True:
        try:
            detak_jantung: int = int(
                input("Berapa detak jantung istirahat Anda (bpm) : ")
            )
            if 20 <= detak_jantung <= 120:
                return detak_jantung
            else:
                print("\n>>> Detak jantung istirahat harus antara 30 dan 120 bpm!!\n\n")
        except ValueError:
            print("\n>>> Input Harus Berupa Angka!!\n")
