import os

def fifo_algorithm(pages, capacity):
    memory = []
    page_faults = 0
    
    print("\n--- Simulasi FIFO ---")
    for page in pages:
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            page_faults += 1
            print(f"Page {page} -> [FAULT] Memori: {memory}")
        else:
            print(f"Page {page} -> [HIT]   Memori: {memory}")
    return page_faults

def lru_algorithm(pages, capacity):
    memory = []
    page_faults = 0
    
    print("\n--- Simulasi LRU ---")
    for page in pages:
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            page_faults += 1
            print(f"Page {page} -> [FAULT] Memori: {memory}")
        else:
            memory.remove(page)
            memory.append(page)
            print(f"Page {page} -> [HIT]   Memori: {memory}")
    return page_faults

def main():
    file_path = os.path.join(os.path.dirname(__file__), 'reference_string.txt')
    
    try:
        with open(file_path, 'r') as f:
            data = f.read()
            pages = [int(x.strip()) for x in data.replace(',', ' ').split()]
    except FileNotFoundError:
        print(f"Error: File {file_path} tidak ditemukan!")
        return

    frames = 3
    
    fifo_faults = fifo_algorithm(pages, frames)
    lru_faults = lru_algorithm(pages, frames)

    print("\n" + "="*30)
    print(f"HASIL AKHIR (Frames: {frames})")
    print(f"Total Page Fault FIFO: {fifo_faults}")
    print(f"Total Page Fault LRU : {lru_faults}")
    print("="*30)

if __name__ == "__main__":
    main()