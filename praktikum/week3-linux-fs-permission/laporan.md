
# Laporan Praktikum Minggu 3
Topik: linux fs permission

---

## Identitas
- **Nama**  : Muhamad Juhan
- **NIM**   : 250202953
- **Kelas** : 1ikrb

---

## Tujuan
Tujuan dari praktikum ini adalah untuk memberikan pemahaman dan keterampilan kepada mahasiswa dalam mengelola file serta direktori menggunakan perintah dasar Linux. Melalui kegiatan ini, mahasiswa diharapkan mampu melakukan navigasi sistem file, mengatur hak akses (permission), dan mengubah kepemilikan (ownership) file dengan benar

---

## Dasar Teori
-Struktur Sistem File Linux

 Linux memiliki struktur sistem file yang berbentuk hierarki, dimulai dari direktori root. Semua file dan folder tersusun secara berurutan di bawahnya, sehingga pengguna perlu memahami cara navigasi untuk mengelola file dengan benar.

-Perintah Dasar Linux

 Beberapa perintah penting seperti ls, pwd, cd, dan cat digunakan untuk melihat daftar file, mengetahui posisi direktori saat ini, berpindah direktori, dan menampilkan isi file. Penguasaan perintah dasar ini merupakan langkah awal dalam penggunaan sistem Linux.

-Hak Akses (Permission)

 Setiap file dan direktori di Linux memiliki hak akses yang mengatur siapa yang boleh membaca, menulis, atau mengeksekusi file tersebut. Pengaturan dilakukan dengan perintah chmod untuk menjaga keamanan dan pengelolaan data.

-Kepemilikan File (Ownership)

 File di Linux memiliki pemilik (user) dan grup (group). Perintah chown digunakan untuk mengubah kepemilikan tersebut agar pengelolaan file sesuai dengan hak pengguna yang berwenang.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
pwd
ls -l
cd /tmp
ls -a
cat /etc/passwd | head -n 5
echo "Hello <NAME><NIM>" > percobaan.txt
ls -l percobaan.txt
chmod 600 percobaan.txt
ls -l percobaan.txt

```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

![Screenshot hasil](screenshots/screenshoot_week_3[1].png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. Fungsi dari perintah chmod
   
Perintah chmod berfungsi untuk mengatur atau mengubah hak akses pada file maupun direktori di sistem Linux. Dengan perintah ini, kita bisa menentukan siapa yang diperbolehkan untuk membaca, menulis, atau menjalankan suatu file. Tujuan utamanya adalah untuk menjaga keamanan data agar hanya pengguna yang berhak saja yang bisa melakukan tindakan tertentu terhadap file tersebut.

2. Arti dari kode permission rwxr-xr--

Kode rwxr-xr-- menunjukkan pembagian hak akses file menjadi tiga bagian utama:

rwx : untuk pemilik (user), artinya pemilik file dapat membaca, mengedit, dan menjalankan file tersebut.

r-x : untuk grup (group), artinya anggota grup hanya bisa membaca dan menjalankan file, tetapi tidak dapat mengubah isinya.

r-- : untuk pengguna lain (others), artinya mereka hanya dapat melihat atau membaca file tanpa bisa mengedit ataupun menjalankannya.

3. Perbedaan antara chown dan chmod

Perintah chown digunakan untuk mengganti kepemilikan suatu file atau direktori, baik dari sisi pengguna (user) maupun grupnya. Sedangkan chmod digunakan untuk mengubah hak akses terhadap file, seperti siapa yang boleh membaca, menulis, atau menjalankannya. Jadi, chown mengatur siapa pemilik file, sedangkan chmod mengatur apa yang bisa dilakukan terhadap file tersebut.
 

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
