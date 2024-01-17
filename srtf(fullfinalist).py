def srtf_formula(jobs, arrival_time, burst_time):
    sorted_AT = sorted(arrival_time)
    remaining_time = list(burst_time)
    n = len(jobs)
    current_time = 0
    finished = 0

    waiting_time = [0] * n
    turnaround_time = [0] * n
    gantt_chart = []
    indel = 1
    
    while finished != n:
        min_remaining_time = float('inf')
        next_job = None

        #This for loop selects the next job that will be processed
        for i in range(n):
            if arrival_time[i] <= current_time and remaining_time[i] <= min_remaining_time:
                #If it encounters jobs with same RBT and AT, it will choose the first job that arrived
                if arrival_time[i] == current_time and remaining_time[i] == min_remaining_time:
                    continue
                min_remaining_time = remaining_time[i]
                next_job = i
                
        #If there's no job was selected, this will add 1 to the current time
        if next_job is None:
            current_time += 1
            continue

        if (remaining_time[next_job] + current_time) > sorted_AT[1]:
            gantt_chart.append((jobs[next_job], sorted_AT[1] - current_time))
            current_time = sorted_AT[1]
            #update remaining time of [next job]
            remaining_time[next_job] = remaining_time[next_job] - (sorted_AT[1] - current_time)
            indel += 1
            print(f"this is indel: {indel}")
            continue
        else:
            gantt_chart.append((jobs[next_job], remaining_time[next_job]))
            current_time = current_time + remaining_time[next_job]
            turnaround_time[next_job] = current_time - arrival_time[next_job]
            waiting_time[next_job] = turnaround_time[next_job] - burst_time[next_job]
            remaining_time[next_job] = float('inf')
            finished += 1

        current_time += 1
    return arrival_time, burst_time, waiting_time, turnaround_time, gantt_chart

def main():
    jobs = ["A", "B", "C"]
    arrival_time = [0, 4, 7]
    burst_time = [7, 4, 1]

    print("======================================================")
    print("Welcome to the Shortest Remaining Time First Simulator")
    print("======================================================")
    '''
    for i in range(len(jobs)):
        arrival_time.append(int(input(f"Enter arrival time for the job {jobs[i]}: ")))
        burst_time.append(int(input(f"Enter burst time for the job {jobs[i]}: ")))
        print("")
    '''
    arrival_time, burst_time, waiting_time, turnaround_time, gantt_chart = srtf_formula(jobs, arrival_time, burst_time)

    print(f"the gantt chart: {gantt_chart}")
    
    print("------------------------------------------------------")
    print("   Job\t|   AT\t|   BT\t|  TAT\t|   WT")
    for i in range(len(jobs)):
        print(f"    {jobs[i]}\t|   {arrival_time[i]}\t|   {burst_time[i]}\t|   {turnaround_time[i]}\t|   {waiting_time[i]}")
    print("------------------------------------------------------")


main()