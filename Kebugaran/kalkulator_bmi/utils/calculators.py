"""
Modul ini menyediakan fungsi untuk menghitung dan menampilkan BMI (Body Mass Index) 
serta kategori berat badan.

Fungsi:
- hitung_bmi: Menghitung BMI berdasarkan tinggi badan dan berat badan.
- tampilkan_hasil_bmi: Menampilkan hasil BMI beserta kategorinya.
- tampilkan_bmi_kurus: Menampilkan pesan jika BMI dalam kategori kurus.
- tampilkan_bmi_normal: Menampilkan pesan jika BMI dalam kategori normal.
- tampilkan_bmi_gemuk: Menampilkan pesan jika BMI dalam kategori gemuk.
- tampilkan_bmi_obesitas: Menampilkan pesan jika BMI dalam kategori obesitas.
"""

import os


def hitung_bmi(tinggi_cm: float, berat_kg: float) -> float:
    """
    Menghitung Body Mass Index (BMI).

    Args:
        tinggi_cm (float): Tinggi badan dalam satuan cm.
        berat_kg (float): Berat badan dalam satuan kg.

    Returns:
        float: Nilai BMI.

    Raises:
        ValueError: Jika tinggi_cm atau berat_kg bernilai kurang dari atau sama dengan nol.
    """
    if tinggi_cm <= 0 or berat_kg <= 0:
        raise ValueError("Tinggi badan dan berat badan harus lebih dari nol.")
    tinggi_meter = tinggi_cm / 100
    return berat_kg / (tinggi_meter**2)


def tampilkan_hasil_bmi(hasil_bmi: float, status_berat_badan: str) -> None:
    """
    Menampilkan hasil BMI beserta kategori berat badan.

    Args:
        hasil_bmi (float): Nilai BMI yang telah dihitung.
        status_berat_badan (str): Kategori berat badan (KURUS, NORMAL, GEMUK, atau OBESITAS).
    """
    emoji_map = {"KURUS": "🌱", "NORMAL": "✨", "GEMUK": "⚠️", "OBESITAS": "🚨"}
    bmi: str = f"{hasil_bmi:.2f}"
    hasil: str = (
        f"\nBMI anda sekitar {bmi}, yang termasuk dalam kategori {status_berat_badan} {emoji_map.get(status_berat_badan, '')}"
    )
    print(hasil)
    input("\nTekan Enter untuk melanjutkan...")
    os.system("cls" if os.name == "nt" else "clear")


def tampilkan_bmi_kurus(hasil_bmi: float) -> None:
    """
    Menampilkan pesan jika BMI termasuk dalam kategori kurus.

    Args:
        hasil_bmi (float): Nilai BMI yang telah dihitung.
    """
    tampilkan_hasil_bmi(hasil_bmi, "KURUS")


def tampilkan_bmi_normal(hasil_bmi: float) -> None:
    """
    Menampilkan pesan jika BMI termasuk dalam kategori normal.

    Args:
        hasil_bmi (float): Nilai BMI yang telah dihitung.
    """
    tampilkan_hasil_bmi(hasil_bmi, "NORMAL")


def tampilkan_bmi_gemuk(hasil_bmi: float) -> None:
    """
    Menampilkan pesan jika BMI termasuk dalam kategori gemuk.

    Args:
        hasil_bmi (float): Nilai BMI yang telah dihitung.
    """
    tampilkan_hasil_bmi(hasil_bmi, "GEMUK")


def tampilkan_bmi_obesitas(hasil_bmi: float) -> None:
    """
    Menampilkan pesan jika BMI termasuk dalam kategori obesitas.

    Args:
        hasil_bmi (float): Nilai BMI yang telah dihitung.
    """
    tampilkan_hasil_bmi(hasil_bmi, "OBESITAS")
