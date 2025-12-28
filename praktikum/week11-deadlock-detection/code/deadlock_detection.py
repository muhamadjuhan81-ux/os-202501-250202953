import csv

def detect_deadlock():
    processes = []
    allocation = {}
    request = {}
    
    with open('dataset_deadlock.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            p = row['Proses']
            processes.append(p)
            allocation[p] = [int(row['Allocation_R1']), int(row['Allocation_R2'])]
            request[p] = [int(row['Request_R1']), int(row['Request_R2'])]

    work = [0, 0]
    finish = {p: False for p in processes}
    
    changed = True
    while changed:
        changed = False
        for p in processes:
            if not finish[p]:
                if all(request[p][i] <= work[i] for i in range(len(work))):
                    for i in range(len(work)):
                        work[i] += allocation[p][i]
                    finish[p] = True
                    changed = True

    deadlocked = [p for p in processes if not finish[p]]
    
    print("=== HASIL DETEKSI DEADLOCK ===")
    if not deadlocked:
        print("Status: Sistem Aman")
    else:
        print(f"Status: Deadlock Terdeteksi")
        print(f"Proses Terlibat: {', '.join(deadlocked)}")

if __name__ == "__main__":
    detect_deadlock()