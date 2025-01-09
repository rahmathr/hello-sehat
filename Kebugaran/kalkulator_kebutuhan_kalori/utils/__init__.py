"""
Imports berbagai fungsi dari modul kalkulator kebutuhan kalori.

Imports:

1. calculators:
    - hitung_kebutuhan_kalori: Menghitung total kebutuhan kalori harian.
    - hitung_bmr_pria: Menghitung Basal Metabolic Rate (BMR) untuk pria.
    - hitung_bmr_wanita: Menghitung Basal Metabolic Rate (BMR) untuk wanita.
    - proses_kalori: Memproses hasil perhitungan kalori berdasarkan masukan pengguna.
    - aktivitas_*: Fungsi untuk menghitung kalori berdasarkan tingkat aktivitas.

2. display_headers:
    - tampilan_header_utama: Menampilkan header utama aplikasi.
    - tampilan_header_database: Menampilkan header untuk bagian database.
    - tampilan_header_aktivitas_fisik: Menampilkan header untuk bagian aktivitas fisik.

3. user_inputs:
    - input_nama_lengkap: Meminta input nama lengkap pengguna.
    - input_umur: Meminta input umur pengguna.
    - input_jenis_kelamin: Meminta input jenis kelamin pengguna.
    - input_tinggi_badan: Meminta input tinggi badan pengguna.
    - input_berat_badan: Meminta input berat badan pengguna.
    - input_intensitas_aktivitas: Meminta input tingkat intensitas aktivitas pengguna.

Fungsi-fungsi ini digunakan untuk membangun logika aplikasi secara modular dan terstruktur.
"""

from .calculators import (
    hitung_kebutuhan_kalori,
    hitung_bmr_pria,
    hitung_bmr_wanita,
    proses_kalori,
    aktivitas_ringan_pria,
    aktivitas_sedang_pria,
    aktivitas_berat_pria,
    aktivitas_ringan_wanita,
    aktivitas_sedang_wanita,
    aktivitas_berat_wanita,
)

from .display_headers import (
    tampilan_header_utama,
    tampilan_header_database,
    tampilan_header_aktivitas_fisik,
)

from .user_inputs import (
    input_nama_lengkap,
    input_umur,
    input_jenis_kelamin,
    input_tinggi_badan,
    input_berat_badan,
    input_intensitas_aktivitas,
)
