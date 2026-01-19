import time
import sys


# Fungsi Simulasi 
def simulasi_fcfs(daftar_musik):
    # Urutkan berdasarkan Waktu Datang
    daftar_musik.sort(key=lambda x: x['waktu datang'])

    waktu_sekarang = 0
    for proses in daftar_musik:
         # Jika CPU menganggur, lompat ke waktu kedatangan proses
        if waktu_sekarang < proses['waktu datang']:
            waktu_sekarang = proses['waktu datang']

        # Hitung Waktu Selesai 
        proses['waktu selesai'] = waktu_sekarang + proses ['durasi musik']

        # Hitung Turnaround Time
        proses['tat'] = proses ['waktu selesai'] - proses ['waktu datang']

        # Hitung Waktu Tunggu
        proses['waktu tunggu'] = proses ['tat'] - proses ['durasi musik']

        # Update waktu sekarang ke waktu selesai proses ini
        waktu_sekarang = proses ['waktu selesai']

# Daftar Musik
daftar_musik=[
    {'nama musik' : 'Blue - Yung Kai ', 'waktu datang' : 0, 'durasi musik' : 3},
    {'nama musik' : 'Untitled - Rex Orange ', 'waktu datang' : 1, 'durasi musik' : 3},
    {'nama musik' : 'Peradaban - Feast.', 'waktu datang' : 2, 'durasi musik' : 5},
    {'nama musik' : 'Sial - Mahalini', 'waktu datang' : 3, 'durasi musik' : 4},
    {'nama musik' : 'Double Take - Dhruv', 'waktu datang' : 4, 'durasi musik' : 3}
]

# Memanggil Fungsi Simulasi
simulasi_fcfs(daftar_musik)

# Bagian Perhitungan Rata-rata
total_tat = 0
total_wt = 0
jumlah_proses = len(daftar_musik)

for p in daftar_musik:
    total_tat += p['tat']
    total_wt += p['waktu tunggu']

rata_rata_tat = total_tat / jumlah_proses
rata_rata_wt = total_wt / jumlah_proses

print("-" * 90)
print(f"{'SIMULATOR MUSIK':^90}")
print("-" * 90)
time.sleep(1)

# Tampilkan Tabel Hasil
print(f"{'Nama Musik':<23} | {'Waktu Datang':<3} | {'Durasi Musik':<3} | {'Waktu Selesai':<3} | {'TAT':<3} | {'Waktu Tunggu':<3}")
print("-" * 90)


for p in daftar_musik:
    time.sleep(0.8)
    sys.stdout.write(f"\rMemutar: {p['nama musik']} ......⏳")
    sys.stdout.flush()
    time.sleep(1.0)

    sys.stdout.write("\r" + " " * 50 + "\r")
    sys.stdout.flush()

    print(f"{p['nama musik']:<23} | {p['waktu datang']:<12} | {p['durasi musik']:<12} | {p['waktu selesai']:<13} | {p['tat']:<3} | {p['waktu tunggu']:<10}")

# Tampilkan Rata-rata
print("-" * 90)
print(f"Rata-rata Turnaround Time (TAT): {rata_rata_tat:.2f}")
print(f"Rata-rata Waiting Time (Waktu Tunggu)   : {rata_rata_wt:.2f}")
