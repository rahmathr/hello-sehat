def hitung_denyut_jantung_maksimum(umur: int) -> int:
    denyut_jantung_maks: int = 220 - umur
    return denyut_jantung_maks


def zona_intensitas_rendah(
    denyut_jantung_maks: int, denyut_jantung_istirahat: int
) -> float:
    batas_bawah: float = denyut_jantung_maks * (50 / 100) + denyut_jantung_istirahat
    batas_atas: float = denyut_jantung_maks * (60 / 100) + denyut_jantung_istirahat
    # print(f"\nUntuk denyut_jantung_maks {denyut_jantung_maks} dan denyut_jantung_istirahat {denyut_jantung_istirahat}, intensitas rendah berada di antara {batas_bawah} - {batas_atas} bpm")
    # input("\nTekan enter untuk melanjutkan...")
    return batas_bawah, batas_atas


def zona_intensitas_sedang(
    denyut_jantung_maks: int, denyut_jantung_istirahat: int
) -> float:
    batas_bawah: float = denyut_jantung_maks * (60 / 100) + denyut_jantung_istirahat
    batas_atas: float = denyut_jantung_maks * (70 / 100) + denyut_jantung_istirahat
    # print(f"\nUntuk denyut_jantung_maks {denyut_jantung_maks} dan denyut_jantung_istirahat {denyut_jantung_istirahat}, intensitas sedang berada di antara {batas_bawah} - {batas_atas} bpm")
    # input("\nTekan enter untuk melanjutkan...")
    return batas_bawah, batas_atas


def zona_intensitas_tinggi(
    denyut_jantung_maks: int, denyut_jantung_istirahat: int
) -> float:
    batas_bawah: float = denyut_jantung_maks * (70 / 100) + denyut_jantung_istirahat
    batas_atas: float = denyut_jantung_maks * (85 / 100) + denyut_jantung_istirahat
    # print(f"\nUntuk denyut_jantung_maks {denyut_jantung_maks} dan denyut_jantung_istirahat {denyut_jantung_istirahat}, intensitas tinggi berada di antara {batas_bawah} - {batas_atas} bpm")
    # input("\nTekan enter untuk melanjutkan...")
    return batas_bawah, batas_atas
