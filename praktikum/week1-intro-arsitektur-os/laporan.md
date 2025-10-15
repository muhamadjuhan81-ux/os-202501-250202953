
# Laporan Praktikum Minggu [X]
Arsitektur Sistem Operasi dan Kernel

---

## Identitas
- **Nama**  : Muhamad Juhan
- **NIM**   : 250202953
- **Kelas** : 1ikrb

---

## Tujuan
Fungsi Utama Sistem Operasi
Sistem operasi (Operating System/OS) adalah program utama yang mengatur semua aktivitas komputer. Bisa dibilang OS adalah “jembatan” antara hardware komputer dengan aplikasi atau program yang kita gunakan. Fungsi utamanya antara lain:
1. Manajemen Proses
 Sistem operasi mengatur jalannya program atau proses di CPU. Dengan OS, komputer bisa menjalankan beberapa program sekaligus (multitasking), menentukan program mana yang dijalankan terlebih dahulu, dan memastikan tidak ada proses yang saling mengganggu.
2. Manajemen Memori
 Setiap program membutuhkan memori untuk berjalan. OS mengatur alokasi memori, memastikan tiap program mendapatkan ruang yang cukup, dan mencegah program satu “mengacak-acak” memori program lain.
3.Manajemen Perangkat Keras (I/O)
 OS mengatur komunikasi antara komputer dan perangkat keras, seperti keyboard, mouse, printer, hard disk, atau layar. Jadi, program tidak perlu tahu detail teknis perangkat keras, cukup “meminta” OS untuk mengaksesnya.
4. Manajemen File
 OS mengatur penyimpanan, pengambilan, dan penghapusan data di media penyimpanan. Sistem file yang rapi membuat kita bisa menyimpan dokumen, gambar, atau program dengan aman dan mudah diakses.
5. Keamanan dan Proteksi
 OS menjaga agar program dan pengguna tidak saling mengganggu. Contohnya, mencegah program jahat mengakses data orang lain, atau membatasi hak akses pengguna tertentu ke file penting.

Peran Kernel
Kernel adalah inti dari sistem operasi. Bisa dibilang kernel adalah “otak” OS yang bertugas mengatur komunikasi langsung dengan hardware dan menjalankan perintah-perintah penting. Beberapa perannya:
1. Manajemen Proses: Kernel yang membuat, menghentikan, dan mengatur jalannya semua proses.
2. Manajemen Memori: Kernel mengalokasikan memori fisik atau virtual sesuai kebutuhan program.
3. Manajemen Perangkat: Kernel mengatur semua akses ke perangkat keras melalui driver, sehingga program bisa menggunakan hardware tanpa harus “mengerti” cara kerjanya.
4. Menyediakan System Call: Kernel menjadi perantara resmi antara aplikasi dan hardware.
Kernel biasanya berjalan di mode khusus (mode kernel) dengan akses penuh ke semua perangkat keras, sehingga bisa bekerja lebih efisien dan aman.

Peran System Call
System call adalah jembatan resmi antara program aplikasi dengan kernel. Karena aplikasi tidak boleh langsung mengakses hardware, system call menyediakan “pintu” bagi program untuk meminta layanan OS. Contohnya:
1. Membuka atau menulis file open, write
2. Mengatur memori atau mengalokasikan ruang baru malloc pada level aplikasi, mmap di level kernel
3. Membuat atau menghentikan proses fork, exec
4. Mengakses perangkat keras seperti printer atau keyboard
Singkatnya, system call adalah cara aplikasi “berbicara” dengan OS agar komputer bisa melakukan tugas yang diminta dengan aman dan terkontrol.
 
---

## Dasar Teori
1. Peran Sistem Operasi sebagai Pengelola Sumber Daya
Sistem operasi bertindak sebagai pengatur utama sumber daya komputer — CPU, memori, perangkat I/O, dan penyimpanan. Dalam percobaan, pengamatan terhadap pembuatan proses, akses memori, dan operasi file menunjukkan bagaimana OS membagi, menjadwalkan, dan melindungi sumber daya agar sistem tetap stabil dan efisien.
2. Kernel sebagai Inti yang Menghubungkan Aplikasi dengan Hardware
Kernel adalah bagian inti OS yang berjalan dengan hak akses penuh dan bertanggung jawab atas kontrol perangkat keras, manajemen proses, dan manajemen memori. Saat aplikasi meminta layanan (mis. menjalankan program baru atau mengakses disk), kernel yang mengeksekusi permintaan tersebut secara terkontrol sehingga aplikasi tidak berinteraksi langsung dengan hardware.
3. System Call sebagai Antarmuka Resmi Aplikasi–Kernel
Aplikasi tidak boleh mengakses sumber daya sistem secara langsung; mereka menggunakan system call untuk meminta layanan kernel (contoh: fork, exec, open, read, write). Percobaan yang memantau pemanggilan system call membantu menunjukkan batasan keamanan, overhead kontekstual, dan mekanisme komunikasi antar-lapisan perangkat lunak.
4. Manajemen Proses dan Sinkronisasi
Sistem operasi mengelola siklus hidup proses (pembuatan, penjadwalan, komunikas i, terminasi). Percobaan yang melibatkan fork/exec atau multiple threads akan menyorot bagaimana OS mengalokasikan CPU, bagaimana proses saling berkomunikasi, dan perlunya mekanisme sinkronisasi untuk menghindari kondisi balapan (race condition).
5. Manajemen Memori dan Proteksi
Untuk menjamin kestabilan, OS menyediakan memori virtual, proteksi ruang alamat, dan mekanisme paging/segmentation. Dalam praktik, pengamatan pada penggunaan memori dan kesalahan akses (mis. segfault) menjelaskan bagaimana OS mencegah bentrokan antar-proses dan bagaimana alokasi memori memengaruhi performa aplikasi.

---

## Langkah Praktikum
Langkah-langkah praktikum minggu pertama:
1. Melakukan fork terhadap repositori yang telah disediakan.
2. Mengganti nama repositori hasil fork sesuai identitas masing-masing.
3. Menyalin clone repositori  ke komputer/laptop.
4. Membuat struktur folder baru di dalam repositori lokal untuk menyimpan hasil praktikum.
5. Di dalam folder tersebut, membuat file laporan.md serta menambahkan folder screenshot/ untuk bukti hasil kerja.
6. Menuliskan ringkasan mengenai system operasi, peran kernel dan system call
7. Menjawab kuis
8.  melakukan commit dengan pesan week1-intro-arsitektur-os, lalu push ke GitHub.


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
-Makna Hasil Percobaan
Dari percobaan ini terlihat kalau OS benar-benar penting buat ngatur jalannya program dan penggunaan sumber daya. Waktu beberapa proses dijalankan bareng, kalau manajemen CPU atau memori nggak bagus, sistem bisa lambat atau proses saling ganggu. Pemanggilan I/O juga kelihatan ada delay karena harus lewat OS dulu.

-Hubungan dengan Teori (Kernel, System Call, Arsitektur OS)
Hasil ini sesuai teori: kernel itu inti OS yang nge-handle semua operasi. Semua layanan program bikin proses, akses file, komunikasi antar proses,dijalankan kernel lewat system call. Jadi wajar kalau ada delay atau overhead pas banyak system call. Arsitektur OS juga memengaruhi performa dan cara sistem ngatur permintaan.
-Perbedaan di Linux vs Windows
Konsep dasarnya sama, tapi implementasi beda
Penjadwalan CPU bisa beda, jadi responsivitas proses nggak sama.
System call dan API berbeda, Linux pakai POSIX, Windows pakai WinAPI.
Manajemen memori dan proteksi beda, terlihat pas banyak proses jalan.
Tools buat ngeliat penggunaan resource di Linux lebih gampang daripada Windows.

---

## Kesimpulan
1. Dari percobaan ini, saya lihat kalau sistem operasi itu memang penting banget buat ngatur semua sumber daya komputer. Kalau nggak ada manajemen proses dan memori, program bisa saling ganggu dan sistem bisa lemot atau errorr
2. Waktu nyoba system call, kelihatan jelas kalau aplikasi nggak bisa langsung akses hardware, harus lewat kernel dulu. Jadi OS itu bikin semuanya aman dan terkontrol.
3. Percobaan sama beberapa proses nunjukin pentingnya sinkronisasi dan proteksi memori. Tanpa itu, bisa terjadi benturan data atau crash, jadi penting buat aplikasi ngerti cara berbagi sumber daya dengan benar.


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
Karna sekarang masih semseter 1 dan masih dalam proses adaptasi, saya masi kesusahan memahami materi dan mengerjakan tugas.
Cara mengatasinya saya meminta bantuan ke teman yang sudah bisa dan minta diajarin kating juga.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
