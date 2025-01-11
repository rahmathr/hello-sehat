"""
Modul ini digunakan untuk melakukan perhitungan terkait denyut jantung 
maksimum dan zona intensitas latihan.
Zona latihan ini dihitung berdasarkan persentase denyut jantung maksimum 
(Denyut Jantung Maksimum - DJM) yang diperoleh dari usia pengguna. 

Fitur Utama:
1. Menghitung denyut jantung maksimum berdasarkan usia.
2. Menentukan batas bawah dan batas atas zona intensitas rendah.
3. Menentukan batas bawah dan batas atas zona intensitas sedang.
4. Menentukan batas bawah dan batas atas zona intensitas tinggi.
"""


def hitung_denyut_jantung_maksimum(umur: int) -> int:
    """
    Menghitung denyut jantung maksimum berdasarkan usia pengguna.

    Args:
        umur (int): Usia pengguna dalam tahun.

    Returns:
        int: Denyut jantung maksimum (DJM) yang dihitung sebagai 220 - usia.
    """
    denyut_jantung_maks: int = 220 - umur
    return denyut_jantung_maks


def zona_intensitas_rendah(
    denyut_jantung_maks: int, denyut_jantung_istirahat: int
) -> tuple:
    """
    Menghitung zona intensitas rendah berdasarkan DJM dan denyut jantung istirahat.

    Args:
        denyut_jantung_maks (int): Denyut jantung maksimum pengguna.
        denyut_jantung_istirahat (int): Denyut jantung istirahat pengguna.

    Returns:
        tuple: Batas bawah dan batas atas zona intensitas rendah dalam bpm.
    """
    batas_bawah: float = denyut_jantung_maks * (50 / 100) + denyut_jantung_istirahat
    batas_atas: float = denyut_jantung_maks * (60 / 100) + denyut_jantung_istirahat
    return batas_bawah, batas_atas


def zona_intensitas_sedang(
    denyut_jantung_maks: int, denyut_jantung_istirahat: int
) -> tuple:
    """
    Menghitung zona intensitas sedang berdasarkan DJM dan denyut jantung istirahat.

    Args:
        denyut_jantung_maks (int): Denyut jantung maksimum pengguna.
        denyut_jantung_istirahat (int): Denyut jantung istirahat pengguna.

    Returns:
        tuple: Batas bawah dan batas atas zona intensitas sedang dalam bpm.
    """
    batas_bawah: float = denyut_jantung_maks * (60 / 100) + denyut_jantung_istirahat
    batas_atas: float = denyut_jantung_maks * (70 / 100) + denyut_jantung_istirahat
    return batas_bawah, batas_atas


def zona_intensitas_tinggi(
    denyut_jantung_maks: int, denyut_jantung_istirahat: int
) -> tuple:
    """
    Menghitung zona intensitas tinggi berdasarkan DJM dan denyut jantung istirahat.

    Args:
        denyut_jantung_maks (int): Denyut jantung maksimum pengguna.
        denyut_jantung_istirahat (int): Denyut jantung istirahat pengguna.

    Returns:
        tuple: Batas bawah dan batas atas zona intensitas tinggi dalam bpm.
    """
    batas_bawah: float = denyut_jantung_maks * (70 / 100) + denyut_jantung_istirahat
    batas_atas: float = denyut_jantung_maks * (85 / 100) + denyut_jantung_istirahat
    return batas_bawah, batas_atas
