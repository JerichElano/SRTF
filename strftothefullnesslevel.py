def srtf_formula(pid, AT, BT):
    n = len(pid)
    WT = [0] * n
    TAT = [0] * n
    ET = [0] * n
    sequence = []  # Sequence of processes
    t_sequence = [0]  # Sequence of time
    gantt_chart = []

    remaining_time = list(BT)
    CT = 0  # Current time

    while True:
        min_bt = float('inf')  # Minimum remaining burst time
        min_at = float('inf')  # Minimum arrival time for tie-break
        NJ = None  # Next job

        for i in range(n):
            if AT[i] <= CT and remaining_time[i] > 0:
                if remaining_time[i] < min_bt or (remaining_time[i] == min_bt and AT[i] < min_at):
                    min_bt = remaining_time[i]
                    min_at = AT[i]
                    NJ = i

        if NJ is None:
            break

        remaining_time[NJ] -= 1
        CT += 1

        sequence.append(pid[NJ])

        #if there is job that will arrive or will be finished it will be appended into the list
        if CT in AT:
            t_sequence.append(CT)
        elif remaining_time[NJ] == 0:
            t_sequence.append(CT)

        if remaining_time[NJ] == 0:
            WT[NJ] = CT - AT[NJ] - BT[NJ]
            ET[NJ] = CT
            TAT[NJ] = ET[NJ] - AT[NJ]

    time_sequence = t_sequence

    while len(t_sequence) >= 2:
        number = t_sequence[1] - t_sequence[0]
        gantt_chart.append((sequence[0], number))
        sequence = sequence[number:]
        t_sequence = t_sequence[1:]

    return AT, BT, ET, TAT, WT, gantt_chart, time_sequence

def main():    
    pid, AT, BT = [], [], []

    print("\n-----------------------------------------------------")
    print("CPU SCHEDULING | Shortest Remaining Time First (SRTF)")
    print("-----------------------------------------------------\n")
    n = 8

    for i in range(n):
        job = chr(ord('A') + i)
        pid.append(job)
        arrival = int(input(f"Arrival Time (AT) of JOB {job}: "))
        AT.append(arrival)
        burst = int(input(f"Burst Time (BT) of JOB {job}: "))
        BT.append(burst)
        print("\n")

    AT, BT, ET, TAT, WT, gantt_chart, time_sequence = srtf_formula(pid, AT, BT)

    print("\nG A N T T   C H A R T:")
    print("  ----- " * len(gantt_chart), end='\n')
    for process, duration in gantt_chart:
        print(f"| {process}{duration} \t", end='')
    print("|")
    print("  ----- " * len(gantt_chart), end='\n')
    for time in time_sequence:
        print(f"{time}\t", end='')

    print("\n\n\nR  E  S  U  L  T:")
    print("--------------------------------------------")
    print("JOBS\tAT\tBT\tET\tTAT\tWT")
    print("--------------------------------------------")
    for i in range(len(pid)):
        print(f"{pid[i]}\t{AT[i]}\t{BT[i]}\t{ET[i]}\t{TAT[i]}\t{WT[i]}")
    print("")

main()
