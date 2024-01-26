def srtf_formula(jobs, AT, BT):
    n = len(jobs)
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

        for i in range(n):  # Selects the next job that will be processed
            if AT[i] <= CT and remaining_time[i] > 0:
                if remaining_time[i] < min_bt or (remaining_time[i] == min_bt and AT[i] < min_at):
                    min_bt = remaining_time[i]
                    min_at = AT[i]
                    NJ = i

        if NJ is None:
            break

        remaining_time[NJ] -= 1
        CT += 1

        sequence.append(jobs[NJ])

        if CT in AT:  # Appends arriving and finished jobs to the list t_sequence
            t_sequence.append(CT)
        elif remaining_time[NJ] == 0:
            t_sequence.append(CT)

        if remaining_time[NJ] == 0:
            WT[NJ] = CT - AT[NJ] - BT[NJ]
            ET[NJ] = CT
            TAT[NJ] = ET[NJ] - AT[NJ]

    time_sequence = t_sequence  # To have a copy of data from t_sequence list

    while len(t_sequence) >= 2:  # Organizes the Gantt chart
        gantt_chart.append((sequence[0], t_sequence[1] - t_sequence[0]))  # Job, Duration of execution
        sequence = sequence[t_sequence[1] - t_sequence[0]:]  # Removes the first elements of sequence
        t_sequence = t_sequence[1:]  # Removes the first element of t_sequence

    return AT, BT, ET, TAT, WT, gantt_chart, time_sequence

def main():    
    # AT, BT = [], []

    # print("\n-----------------------------------------------------")
    # print("CPU SCHEDULING | Shortest Remaining Time First (SRTF)")
    # print("-----------------------------------------------------\n")

    # n = int(input(f"Enter number of process: "))
    # jobs = [chr(ord('A') + i) for i in range(n)]

    # for i in range(n):
    #     AT.append(int(input(f"\nArrival Time (AT) of JOB {jobs[i]}: ")))
    #     BT.append(int(input(f"Burst Time (BT) of JOB {jobs[i]}: ")))

    jobs = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    AT = [0, 0, 12, 22, 7, 27, 17, 3, 32]
    BT = [8, 6, 7, 6, 4, 3, 7, 6, 4]
    PR = [5, 5, 3, 1, 1, 3, 2, 4, 1]

    AT, BT, ET, TAT, WT, gantt_chart, time_sequence = srtf_formula(jobs, AT, BT)

    print("\n\nG A N T T   C H A R T:")
    print("+-------" * len(gantt_chart), end='+\n')
    for process, duration in gantt_chart:
        print(f"|  {process}{duration} \t", end='')
    print("|")
    print("+-------" * len(gantt_chart), end='+\n')
    for time in time_sequence:
        print(f"{time}\t", end='')

    print("\n\n\nR  E  S  U  L  T:")
    print("+-------" * 6, end='+\n')
    print("| JOBS\t|   AT\t|   BT\t|   ET\t|  TAT\t|  WT\t", end="|\n")
    print("+-------" * 6, end='+\n')
    for i in range(len(jobs)):
        print(f"|   {jobs[i]}\t|   {AT[i]}\t|   {BT[i]}\t|   {ET[i]}\t|   {TAT[i]}\t|   {WT[i]}\t", end="|\n")
    print("+-------" * 6, end='+\n')


main()