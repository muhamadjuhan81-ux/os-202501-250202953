```bash
import os
import time

# PROYEK SIMULASI OS - TEMA: MULTITASKING RAM LAPTOP
# Modul: Page Replacement Algorithm (FIFO)

class LaptopMultitasking:
    def __init__(self):
        # Dataset: Urutan aplikasi yang dibuka pengguna laptop
        self.app_requests = [
            "Chrome", "Spotify", "Word", "Chrome", 
            "VS Code", "Spotify", "Zoom", "Word"
        ]
        self.ram_slots = 3  
        self.delay_transisi = 1.5

    def clear(self):
        """Membersihkan layar terminal agar simulasi terlihat rapi"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def gambar_tabel(self, history):
        self.clear()
        # Header Utama
        print("="*85)
        print(f"{'SIMULASI MULTITASKING LAPTOP (MANAJEMEN RAM)':^85}")
        print("="*85)
        
        print(f"{'Step':<6} | {'Aplikasi':<15} | {'Isi RAM (Slot)':<30} | {'Status'}")
        print("-" * 85)

        faults = 0
        for i, h in enumerate(history):
            status = "FAULT" if h['fault'] else "HIT"
            if h['fault']: faults += 1
            
            ram_display = " | ".join(h['ram'])
            
            print(f"{i+1:<6} | {h['app']:<15} | [ {ram_display:^26} ] | {status}")
        
        print("-" * 85)
        return faults

    def jalankan_simulasi(self):
        while True:
            ram = []
            history = []
            page_faults = 0
            
            for app_name in self.app_requests:
                is_fault = False
                
                # Logika: Apakah aplikasi sudah ada di RAM?
                if app_name not in ram:
                    is_fault = True
                    page_faults += 1
                    
                    if len(ram) >= self.ram_slots:
                        ram.pop(0)
                    ram.append(app_name)
                
                history.append({
                    'app': app_name,
                    'ram': list(ram),
                    'fault': is_fault
                })

                self.gambar_tabel(history)
                
                if len(history) < len(self.app_requests):
                    print(f"\n⏳ Membuka aplikasi: {app_name}...")
                    time.sleep(self.delay_transisi)
            # Hitung dan tampilkan statistik akhir
            total_req = len(self.app_requests)
            hit_ratio = ((total_req - page_faults) / total_req) * 100

            print(f"\n[KETERANGAN]")
            print(f"1. Total FAULT : {page_faults}")
            print(f"2. HIT Ratio   : {hit_ratio:.2f}%")
            
            
            print("\nMematikan sistem laptop...")
            break

if __name__ == "__main__":
    LaptopMultitasking().jalankan_simulasi()

```

---
