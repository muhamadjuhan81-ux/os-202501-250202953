
# Laporan Praktikum Minggu [X]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : Muhamad Juhan
- **NIM**   : 250202953
- **Kelas** : 1 ikrb

---

## Tujuan
Tujuan dari praktikum ini adalah untuk memahami bagaimana sistem operasi bekerja dalam mengatur proses yang berjalan di komputer. Melalui percobaan ini, mahasiswa diharapkan bisa menjelaskan fungsi utama sistem operasi, mengenal peran kernel sebagai bagian inti yang mengatur jalannya sistem, serta memahami bagaimana system call digunakan sebagai penghubung antara program pengguna dengan layanan yang ada di dalam sistem operasi. Dengan memahami hal tersebut, mahasiswa dapat mengetahui bagaimana komunikasi antara user mode dan kernel mode berlangsung saat sebuah program dijalankan.

---

## Dasar Teori
1. Fungsi utama sistem operasi adalah mengelola seluruh sumber daya komputer agar dapat digunakan secara efisien oleh pengguna maupun program. Sistem operasi bertanggung jawab terhadap pengaturan proses, memori, berkas, serta perangkat input/output.
2. Kernel merupakan inti dari sistem operasi yang berperan langsung dalam mengontrol perangkat keras dan menjalankan instruksi penting. Kernel mengatur komunikasi antara perangkat keras dan perangkat lunak agar setiap proses dapat berjalan dengan aman dan stabil.
3. System call berfungsi sebagai jembatan antara program pengguna (user mode) dengan layanan yang disediakan oleh kernel (kernel mode). Melalui system call, program dapat meminta layanan sistem seperti membaca file, membuat proses baru, atau mengatur memori tanpa harus berinteraksi langsung dengan perangkat keras.
4. Pemisahan antara user mode dan kernel mode dibuat untuk menjaga keamanan sistem. Dengan cara ini, program pengguna tidak bisa langsung mengakses bagian sensitif dari sistem operasi, sehingga risiko kesalahan atau kerusakan dapat diminimalkan.


---

## Langkah Praktikum
1. Membuka terminal pada sistem operasi yang digunakan misalnya Linux
2. Membuat file program baru menggunakan teks editor
3. Menulis kode program sederhana yang menggunakan system call, misalnya untuk menampilkan teks atau membaca file.
4. Menyimpan file, kemudian melakukan kompilasi program menggunakan perintah gcc atau perintah lain yang sesuai.
5. Menjalankan hasil kompilasi untuk melihat bagaimana program berinteraksi dengan sistem operasi melalui system call.
6. Melakukan pengujian beberapa kali untuk memastikan hasil yang ditampilkan sesuai dengan fungsi yang diharapkan.
7. Menyimpan perubahan ke dalam repositori Git dengan pesan (commit message) yang menjelaskan kegiatan yang dilakukan.


---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

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
1. [Pertanyaan 1]  
   **Jawaban:**  
2. [Pertanyaan 2]  
   **Jawaban:**  
3. [Pertanyaan 3]  
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
