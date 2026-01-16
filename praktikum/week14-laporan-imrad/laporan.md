
# Laporan Praktikum Minggu 14
Topik: Penyusunan Laporan Praktikum Format IMRAD

---

## Identitas
- **Nama**  : Muhamad Juhan  
- **NIM**   : 250202953  
- **Kelas** : 1 IKRB

---

### Judul

#### Analisis Perbandingan Performa Algoritma Penjadwalan First-Come, First-Served (FCFS) dan Shortest Job First (SJF)

---

## 1. Pendahuluan
### 1.1 Latar Belakang

Sistem operasi modern dituntut untuk mampu menjalankan berbagai proses secara bersamaan (multitasking). Dalam kondisi ini, CPU sebagai unit pemrosesan utama menjadi sumber daya yang diperebutkan oleh banyak proses. Oleh karena itu, diperlukan sebuah mekanisme penjadwalan CPU untuk menentukan urutan eksekusi proses yang berada di dalam antrean (ready queue). Efisiensi dari algoritma penjadwalan sangat berpengaruh pada pengalaman pengguna dan performa sistem secara keseluruhan.

Dua algoritma klasik yang sering digunakan dalam studi sistem operasi adalah First-Come, First-Served (FCFS) dan Shortest Job First (SJF). FCFS bekerja dengan prinsip antrean sederhana di mana proses yang tiba lebih dulu akan dilayani lebih dulu. Namun, FCFS sering kali menghadapi masalah "convoy effect" di mana proses-proses pendek harus menunggu proses panjang selesai. Sebagai alternatif, SJF hadir dengan memprioritaskan proses dengan durasi (burst time) terpendek guna meminimalkan rata-rata waktu tunggu (Average Waiting Time).

Tujuan dari praktikum ini adalah untuk melakukan simulasi koding menggunakan bahasa Python guna membandingkan performa FCFS dan SJF secara langsung. Analisis difokuskan pada dua parameter utama, yaitu Average Waiting Time (AWT) dan Average Turnaround Time (ATT), untuk membuktikan algoritma mana yang lebih efisien dalam berbagai skenario beban kerja proses.

---

## 1.2 Rumusan Masalah

1. Bagaimana perbedaan urutan eksekusi antara algoritma FCFS dan SJF ketika dihadapkan pada skenario proses yang sama di Uji Coba 1 dan Uji Coba 2?

2. Apakah algoritma SJF selalu menghasilkan Average Waiting Time yang lebih rendah dibandingkan FCFS pada kedua skenario uji coba tersebut?

3. Seberapa besar pengaruh perubahan durasi proses (burst time) pada Uji Coba 2 terhadap efisiensi waktu tunggu di masing-masing algoritma?

## 1.3 Tujuan

Mensimulasikan algoritma FCFS dan SJF menggunakan Python melalui dua skenario pengujian yang berbeda.

Membandingkan metrik Average Waiting Time (AWT) dan Average Turnaround Time (ATT) antara FCFS dan SJF berdasarkan output terminal.

Menganalisis fenomena pergeseran antrean pada SJF di Uji Coba 2 yang bertujuan untuk mengoptimalkan efisiensi waktu tunggu sistem.

---

## 2. Metods

## 2.1 Lingkungan Pengujian

 Pengujian dilakukan pada perangkat keras yang sama untuk memastikan konsistensi hasil. Spesifikasi perangkat keras dan perangkat lunak yang digunakan adalah sebagai berikut:

 A. Perangkat Keras (Host Machine)

Model Laptop: Axioo Hype 5 X3

Processor (CPU): AMD Ryzen 5 3500U

RAM: 8 GB 

Sistem Operasi: Windows 11 64-bit

B. Perangkat Lunak (Software)

IDE: Visual Studio Code

Bahasa Pemrograman: Python 3.14.2

File Eksekusi: scheduling.py

---

## 3. Results (hasil)

| PID | Arrival | Burst | start | Finish | Waiting | Turnaround |
| --- | ------- | ----- | ----- | ------ | ------- | ---------- |
| P1  |         |       |       |        |         |            |
| P2  |         |       |       |        |         |            |
| P3  |         |       |       |        |         |            |
| P4  |         |       |       |        |         |            |
| P5  |         |       |       |        |         |            |




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
