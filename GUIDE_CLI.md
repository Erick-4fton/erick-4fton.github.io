# Panduan Pengelolaan Website via CLI 🖥️

Dokumen ini adalah referensi cepat untuk mengelola dan memperbarui materi di **Dev Archive** menggunakan Terminal.

---

## 1. Perintah Cepat (Cheat Sheet)

Jika Anda hanya ingin melakukan update rutin, gunakan urutan perintah ini:

```bash
# 1. Konversi materi Markdown ke HTML
python3 tools/convert.py

# 2. Upload ke GitHub (Ganti pesan commit sesuai kebutuhan)
git add .
git commit -m "Update materi baru: [Nama Materi]"
git push origin main
```

---

## 2. Alur Tambah Materi Baru
Untuk menambahkan materi pembelajaran baru (misal: "Belajar CSS"):

1.  **Buat File**: Buat file `belajar-css.md` di dalam folder `content/`.
2.  **Gunakan Template**: Pastikan bagian atas file (Frontmatter) terisi:
    ```markdown
    ---
    title: "Belajar CSS Dasar"
    date: 2026-02-18
    category: "Design"
    author: "Admin"
    ---
    ```
3.  **Tulis Materi**: Gunakan format Markdown standar.
4.  **Jalankan Convert**: Ketik `python3 tools/convert.py`.
5.  **Cek Hasil**: File HTML otomatis tersedia di `pages/materials/belajar-css.html`.

---

## 3. Fitur Otomatis `convert.py`
Skrip konversi kita kini bekerja lebih cerdas:

-   **Auto-Sync**: Menghapus file HTML lama di `pages/materials/` sebelum melakukan konversi baru agar tidak ada duplikat atau file sampah.
-   **Dynamic Sidebar**: Otomatis membuat daftar menu navigasi di bar samping artikel berdasarkan semua file materi yang ada di folder `content/`.
-   **Smart Pathing**: Menyesuaikan link CSS dan JS secara otomatis meskipun file berada di dalam sub-folder yang dalam.
-   **HTML Protecting**: Memastikan tag contoh (seperti `<h1>`) tampil sebagai teks instruksi dan tidak merusak layout web.

---

## 4. Contoh Skenario Penggunaan

### **Skenario A: Mengubah Isi Materi yang Sudah Ada**
Jika Anda typo di materi HTML:
1.  Buka `content/HTML-post.md` -> Perbaiki teksnya.
2.  Jalankan `python3 tools/convert.py`.
3.  Perubahan langsung diterapkan ke file HTML terkait.

### **Skenario B: Menghapus Materi**
Jika sebuah materi ingin ditiadakan:
1.  Hapus file `.md` nya di folder `content/`.
2.  Jalankan `python3 tools/convert.py`.
3.  File HTML lamanya akan **otomatis terhapus** dari folder `pages/materials/` dan hilang dari menu navigasi sidebar.

---

## 5. Tips Pro
-   **Preview Lokal**: Sebelum push ke GitHub, Anda bisa mengecek hasil konversi dengan membuka langsung file di folder `pages/materials/` menggunakan browser (Klik kanan -> Open with Browser).
-   **Batch Update**: Anda bisa memasukkan 10 file Markdown sekaligus ke folder `content/`, dan cukup menjalankan `convert.py` satu kali untuk memproses semuanya.

---
*Engineering Excellence - Dev Archive 2026*
