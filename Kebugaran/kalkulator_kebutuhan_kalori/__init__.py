"""
Package-level imports untuk aplikasi kalkulator kebutuhan kalori.

Modul yang diimpor:
- data:
    - reader: Untuk membaca data dari file CSV atau sumber lainnya.
    - saver: Untuk menyimpan data hasil perhitungan ke file atau database.
- utils:
    - calculators: Berisi fungsi-fungsi untuk perhitungan kebutuhan kalori dan BMR.
    - display_headers: Untuk menampilkan header di berbagai bagian aplikasi.
    - user_inputs: Untuk mengelola input pengguna seperti nama, umur, dan aktivitas fisik.

Fungsi utama:
Memfasilitasi pengelompokan dan pengelolaan modul-modul yang digunakan dalam aplikasi ini.
"""

from .data import reader, saver
from .utils import calculators, display_headers, user_inputs
