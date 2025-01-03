import os


def hitung_bmi(tinggi_cm: float, berat_kg: float) -> float:
    if tinggi_cm <= 0 or berat_kg <= 0:
        raise ValueError("Tinggi badan dan berat badan harus lebih dari nol.")
    tinggi_meter = tinggi_cm / 100
    return berat_kg / (tinggi_meter**2)


def tampilkan_hasil_bmi(hasil_bmi: float, status_berat_badan: str) -> None:
    emoji_map = {"KURUS": "🌱", "NORMAL": "✨", "GEMUK": "⚠️", "OBESITAS": "🚨"}
    bmi: str = f"{hasil_bmi:.2f}"
    hasil: str = (
        f"\nBMI anda sekitar {bmi}, yang termasuk dalam kategori {status_berat_badan} {emoji_map.get(status_berat_badan, '')}"
    )
    print(hasil)
    input("\nTekan Enter untuk melanjutkan...")
    os.system("cls" if os.name == "nt" else "clear")


def tampilkan_bmi_kurus(hasil_bmi: float) -> None:
    tampilkan_hasil_bmi(hasil_bmi, "KURUS")


def tampilkan_bmi_normal(hasil_bmi: float) -> None:
    tampilkan_hasil_bmi(hasil_bmi, "NORMAL")


def tampilkan_bmi_gemuk(hasil_bmi: float) -> None:
    tampilkan_hasil_bmi(hasil_bmi, "GEMUK")


def tampilkan_bmi_obesitas(hasil_bmi: float) -> None:
    tampilkan_hasil_bmi(hasil_bmi, "OBESITAS")
