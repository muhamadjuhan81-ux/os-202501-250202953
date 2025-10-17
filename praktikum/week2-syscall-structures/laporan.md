
# Laporan Praktikum Minggu [X]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : Muhamad Juhan
- **NIM**   : 250202953
- **Kelas** : 1 ikrb

---

## Tujuan
Tujuan dari praktikum ini adalah untuk memahami bagaimana system call bekerja di dalam sistem operasi. Melalui percobaan ini, mahasiswa diharapkan dapat menjelaskan konsep dan fungsi system call, mengenali jenis-jenisnya beserta fungsinya, serta mengamati bagaimana proses perpindahan dari user mode ke kernel mode terjadi saat sebuah system call dipanggil. Selain itu, mahasiswa juga belajar menggunakan beberapa perintah di Linux untuk menampilkan dan menganalisis aktivitas system call yang dijalankan oleh suatu program.

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
- Makna Hasil Percobaan

Dari hasil percobaan yang dilakukan, dapat dipahami bahwa sistem operasi memiliki peran penting sebagai pengelola seluruh aktivitas komputer. Percobaan menunjukkan bagaimana program pengguna tidak dapat berinteraksi langsung dengan perangkat keras, melainkan harus melalui sistem operasi. Hal ini terjadi karena setiap instruksi dari program akan diteruskan ke kernel melalui mekanisme system call. Proses tersebut membuktikan bahwa sistem operasi berfungsi sebagai penghubung utama antara pengguna dan sumber daya komputer. Ketika program menjalankan perintah seperti membaca file atau mencetak teks ke layar, kernel yang mengatur jalannya operasi tersebut agar berjalan dengan aman dan sesuai aturan. Dengan demikian, percobaan ini membantu mahasiswa memahami bagaimana sistem operasi bekerja di balik layar untuk menjalankan perintah yang tampak sederhana di sisi pengguna.Selain itu, percobaan juga menunjukkan pentingnya lapisan keamanan antara user mode dan kernel mode. Pembatasan ini memastikan bahwa program tidak dapat merusak sistem atau mengakses bagian sensitif dari perangkat keras secara langsung. Hal ini menjadi bukti bahwa sistem operasi tidak hanya mengatur sumber daya, tetapi juga menjaga kestabilan dan keamanan komputer secara keseluruhan.

- Hubungkan hasil dengan teori

Hasil percobaan yang diperoleh selaras dengan teori dasar mengenai fungsi utama sistem operasi. Secara teori, sistem operasi bertugas mengatur penggunaan sumber daya komputer dan menyediakan antarmuka bagi program untuk berinteraksi dengan perangkat keras. Dalam praktiknya, hal ini terlihat jelas melalui mekanisme system call, di mana kernel menjadi perantara antara program pengguna dan perangkat keras.Percobaan ini juga membuktikan teori bahwa kernel bekerja dalam mode istimewa (kernel mode), sementara program berjalan di mode pengguna (user mode). Ketika program membutuhkan layanan tertentu, sistem akan berpindah dari user mode ke kernel mode untuk menjalankan instruksi, kemudian kembali lagi setelah selesai. Mekanisme ini sesuai dengan konsep keamanan dan efisiensi yang dijelaskan dalam teori sistem operasi. Dengan demikian, hasil praktikum ini memperkuat pemahaman bahwa fungsi utama sistem operasi, peran kernel, dan mekanisme system call saling berkaitan erat. Tanpa system call, program pengguna tidak akan dapat memanfaatkan layanan yang disediakan oleh sistem operasi secara aman dan terkontrol.

- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)

Secara umum, percobaan system call di Linux dan Windows menghasilkan fungsi yang sama, yaitu sebagai sarana bagi program untuk berinteraksi dengan sistem operasi. Namun, cara kerja dan implementasinya memiliki beberapa perbedaan yang cukup jelas. 
Pada sistem Linux, system call bersifat lebih terbuka dan terdokumentasi dengan baik, sehingga pengguna atau pengembang dapat dengan mudah melihat daftar system call yang tersedia beserta cara kerjanya. Linux juga memberikan akses yang lebih langsung ke level kernel, sehingga hasil percobaan biasanya dapat diamati secara lebih detail, misalnya melalui penggunaan terminal atau perintah sistem seperti strace untuk menelusuri aktivitas system call yang terjadi. Sementara pada sistem Windows, mekanisme system call cenderung lebih tertutup dan kompleks. Akses langsung ke level kernel dibatasi, dan sebagian besar interaksi dilakukan melalui API (Application Programming Interface) milik Windows. Akibatnya, saat percobaan dilakukan di Windows, hasil yang terlihat tidak sejelas di Linux karena banyak proses berlangsung di latar belakang tanpa dapat diamati secara langsung.
Dengan demikian, perbedaan utama antara keduanya terletak pada tingkat keterbukaan, cara pemanggilan system call, serta kemudahan observasi hasilnya. Linux lebih transparan dan mudah dipelajari untuk keperluan praktikum sistem operasi, sedangkan Windows lebih fokus pada keamanan dan kestabilan dengan membatasi akses langsung ke kernel.


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
