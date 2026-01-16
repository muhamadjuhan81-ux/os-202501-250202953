processes = [
    {"pid": "P1", "arrival": 0, "burst": 5},
    {"pid": "P2", "arrival": 1, "burst": 3},
    {"pid": "P3", "arrival": 2, "burst": 8},
    {"pid": "P4", "arrival": 3, "burst": 6},
]

def fcfs(processes):
    time = 0
    result = []
    for p in processes:
        start = max(time, p["arrival"])
        finish = start + p["burst"]
        waiting = start - p["arrival"]
        turnaround = finish - p["arrival"]
        time = finish
        result.append({
            "pid": p["pid"],
            "arrival": p["arrival"],
            "burst": p["burst"],
            "start": start,
            "finish": finish,
            "waiting": waiting,
            "turnaround": turnaround
        })
    return result

def sjf(processes):
    time = 0
    processes = sorted(processes, key=lambda x: x["arrival"])
    ready = []
    result = []

    while processes or ready:
        while processes and processes[0]["arrival"] <= time:
            ready.append(processes.pop(0))
        if ready:
            ready.sort(key=lambda x: x["burst"])
            p = ready.pop(0)
            start = time
            finish = start + p["burst"]
            waiting = start - p["arrival"]
            turnaround = finish - p["arrival"]
            time = finish
            result.append({
                "pid": p["pid"],
                "arrival": p["arrival"],
                "burst": p["burst"],
                "start": start,
                "finish": finish,
                "waiting": waiting,
                "turnaround": turnaround
            })
        else:
            time += 1
    return result

def print_table(title, data):
    print(f"\n{title}")
    print("PID | Arrival | Burst | Start | Finish | Waiting | Turnaround")
    total_wait = total_turn = 0
    for p in data:
        print(f"{p['pid']:>3} | {p['arrival']:>7} | {p['burst']:>5} | "
              f"{p['start']:>5} | {p['finish']:>6} | {p['waiting']:>7} | {p['turnaround']:>10}")
        total_wait += p["waiting"]
        total_turn += p["turnaround"]
    n = len(data)
    print(f"Average Waiting Time    : {total_wait / n:.2f}")
    print(f"Average Turnaround Time : {total_turn / n:.2f}")



# =========================
# UJI COBA 1
# =========================
processes = [
    {"pid": "P1", "arrival": 0, "burst": 5},
    {"pid": "P2", "arrival": 1, "burst": 3},
    {"pid": "P3", "arrival": 2, "burst": 8},
    {"pid": "P4", "arrival": 3, "burst": 6},
]

print("\n=== UJI COBA 1 ===")
print_table("FCFS Scheduling Result", fcfs(processes))
print_table("SJF Scheduling Result", sjf(processes))


# =========================
# UJI COBA 2
# =========================
processes = [
    {"pid": "P1", "arrival": 0, "burst": 7},
    {"pid": "P2", "arrival": 2, "burst": 4},
    {"pid": "P3", "arrival": 4, "burst": 1},
    {"pid": "P4", "arrival": 5, "burst": 4},
]

print("\n=== UJI COBA 2 ===")
print_table("FCFS Scheduling Result", fcfs(processes))
print_table("SJF Scheduling Result", sjf(processes))
