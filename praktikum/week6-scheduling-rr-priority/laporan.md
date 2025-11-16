
# Laporan Praktikum Minggu [X]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : Muhamad Juhan
- **NIM**   : 250202953
- **Kelas** : 1 IKRB

---

## Tujuan

Tujuan dari praktikum ini adalah untuk memahami bagaimana algoritma Round Robin dan Priority Scheduling bekerja dalam mengatur proses pada CPU. Melalui percobaan ini, saya menghitung waiting time dan turnaround time dari setiap proses, kemudian membandingkan hasil keduanya. Saya juga menganalisis bagaimana ukuran time quantum dan tingkat prioritas dapat memengaruhi keadilan eksekusi proses dan kinerja sistem. Pada akhirnya, praktikum ini membantu saya melihat algoritma mana yang lebih efisien dan kapan masing-masing algoritma lebih tepat digunakan.

---

## Dasar Teori

1. Penjadwalan CPU adalah mekanisme sistem operasi untuk menentukan proses mana yang mendapatkan giliran menggunakan CPU. Tujuannya adalah menjaga efisiensi penggunaan CPU, mengurangi waktu tunggu proses, dan memastikan setiap proses mendapat eksekusi secara adil.

2. Round Robin (RR) merupakan algoritma penjadwalan yang menggunakan time quantum sebagai batas waktu bagi setiap proses. Semua proses dieksekusi secara bergiliran, sehingga algoritma ini dianggap adil. Namun, performanya sangat dipengaruhi oleh besar kecilnya quantum.

3. Priority Scheduling menentukan urutan eksekusi proses berdasarkan tingkat prioritas. Proses dengan prioritas lebih tinggi dijalankan lebih dulu. Algoritma ini efisien untuk proses penting, tetapi dapat menimbulkan starvation bagi proses dengan prioritas rendah.

4. Perbedaan utama kedua algoritma terletak pada fokusnya: Round Robin menekankan pemerataan waktu eksekusi untuk semua proses, sedangkan Priority Scheduling memprioritaskan proses tertentu berdasarkan tingkat kepentingannya.


---

## Langkah Praktikum

1. Menyiapkan data proses yang berisi burst time, arrival time, dan priority sebagai dasar perhitungan kedua algoritma.

2. Melakukan simulasi Round Robin dengan menentukan nilai time quantum, menyusun Gantt Chart, serta menghitung waiting time dan turnaround time menggunakan Excel.

3. Melakukan simulasi Priority Scheduling dengan mengurutkan proses berdasarkan prioritas dan menghitung waiting time serta turnaround time melalui tabel di Excel.

4. Menyusun seluruh hasil perhitungan, tabel, dan Gantt Chart ke dalam file laporan.md, kemudian menyimpan hasil screenshot ke dalam folder screenshots.

5. Mengunggah seluruh hasil praktikum ke GitHub


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
![Screenshot hasil](2.png)


<img width="844" height="211" alt="image" src="https://github.com/user-attachments/assets/3468d0e4-8b60-4d02-a010-ea9294ef84d7" />



---

## Analisis

Hasil percobaan menunjukkan bahwa algoritma Round Robin membuat semua proses mendapatkan giliran secara lebih merata. Setiap proses diputar berdasarkan time quantum, sehingga waktu tunggu tiap proses tidak terlalu jauh berbeda. Hal ini sesuai dengan teori bahwa Round Robin menekankan keadilan dalam pembagian waktu CPU.

Untuk Priority Scheduling, proses dengan prioritas tertinggi selalu dijalankan lebih dulu. Dari hasil perhitungan, proses dengan prioritas rendah cenderung menunggu lebih lama. Ini sesuai dengan teori bahwa algoritma ini bisa menyebabkan proses tertentu tertunda karena kalah prioritas.

Secara umum, hasil percobaan memperlihatkan bahwa Round Robin lebih adil, sedangkan Priority Scheduling lebih mengutamakan proses penting. Perbedaan ini menunjukkan bahwa setiap algoritma memiliki tujuan dan karakteristik masing-masing sesuai kebutuhan sistem.


---

## Kesimpulan

1. Algoritma Round Robin memberikan pembagian waktu eksekusi yang lebih adil karena semua proses mendapatkan giliran secara bergantian sesuai time quantum.

2. Priority Scheduling lebih memprioritaskan proses penting, tetapi dapat menyebabkan proses berprioritas rendah menunggu lebih lama.

3. Perbedaan nilai waiting time dan turnaround time pada kedua algoritma menunjukkan bahwa pemilihan metode penjadwalan harus disesuaikan dengan tujuan sistem, apakah ingin menekankan keadilan atau prioritas proses.

---

## Quiz
1. Apa perbedaan utama antara Round Robin dan Priority Scheduling?

Round Robin mengeksekusi semua proses secara bergiliran dengan waktu terbatas, tanpa memperhatikan prioritas. Sedangkan Priority Scheduling mengeksekusi proses berdasarkan tingkat prioritas, proses dengan prioritas lebih tinggi dijalankan lebih dulu.

2. Apa pengaruh besar/kecilnya time quantum terhadap performa sistem?

Time quantum yang terlalu kecil membuat CPU sering berpindah antarproses, sehingga sistem terasa lambat. Kalau terlalu besar, proses harus menunggu lebih lama dan Round Robin jadi mirip FCFS.

3. Mengapa algoritma Priority dapat menyebabkan starvation?

Karena proses dengan prioritas rendah bisa terus menunggu jika selalu ada proses prioritas tinggi, sehingga ada kemungkinan tidak pernah dijalankan

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
