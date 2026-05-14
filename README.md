
# Website Katalog Sederhana dengan Django

## Deskripsi
Website ini merupakan aplikasi katalog produk sederhana yang dikembangkan menggunakan framework Django. Website ini bertujuan untuk menampilkan daftar produk berupa buku manga, detail setiap produk, serta menyediakan halaman informasi dasar seperti homepage dan kontak. Semua data produk disimpan secara hardcoded di kode program, sehingga tidak memerlukan database.

## Fitur Utama
- **Homepage**: Menampilkan pesan selamat datang dan deskripsi singkat mengenai website katalog.
- **Daftar Produk**: Menampilkan daftar buku manga populer (lebih dari 3 judul), lengkap dengan nama dan harga. Pengguna dapat mengklik judul manga untuk melihat detailnya.
- **Detail Produk**: Menampilkan informasi detail dari satu buku manga berdasarkan ID, seperti nama, deskripsi, dan harga.
- **Halaman Kontak**: Menampilkan informasi kontak sederhana agar pengunjung dapat menghubungi pengelola website.

## Teknologi yang Digunakan
- Python 
- Django 
- HTML (template bawaan Django)

## Alur Penggunaan
1. Pengguna membuka website pada alamat utama (homepage).
2. Pengguna dapat memilih menu "Lihat Daftar Produk" untuk melihat seluruh katalog manga.
3. Pada halaman daftar produk, pengguna dapat mengklik judul manga untuk melihat detail lengkap.
4. Pengguna juga dapat mengunjungi halaman kontak untuk mendapatkan informasi kontak pengelola.

## Cara Menjalankan Website
1. Pastikan sudah menginstall Python 3 dan pip.
2. Aktifkan virtual environment: `venv\Scripts\activate` (Windows)
3. Jalankan server Django dengan perintah: `python manage.py runserver`
4. Buka browser dan akses `http://127.0.0.1:8000/`

## Struktur URL
- `/` : Homepage
- `/produk/` : Daftar produk manga
- `/produk/<id>/` : Detail produk manga berdasarkan ID
- `/kontak/` : Halaman kontak

