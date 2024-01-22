def srtf_formula(jobs, arrival_time, burst_time):
    sorted_AT = sorted(arrival_time)
    remaining_time = list(burst_time)
    n = len(jobs)
    current_time = 0
    finished = 0

    waiting_time = [0] * n
    turnaround_time = [0] * n
    f_jobs = [0] * n
    gantt_chart = []
    indel = 1
    
    while sum(f_jobs) != n:
        min_remaining_time = float('inf')
        next_job = None

        #This for loop selects the next job that will be processed
        for i in range(n):
            if arrival_time[i] <= current_time and remaining_time[i] <= min_remaining_time and f_jobs[i] == 0:
                #If it encounters jobs with same RBT and AT, it will choose the first job that arrived
                if arrival_time[i] == current_time and remaining_time[i] == min_remaining_time:
                    continue
                min_remaining_time = remaining_time[i]
                next_job = i
                
        #If there's no job was selected, this will add 1 to the current time
        if next_job is None:
            current_time += 1
            continue
        print("...........................................................")
        print(f'initialremaining {remaining_time[next_job]}\ntime {current_time}\nindel {indel}')
        if len(sorted_AT) > indel:
            #
            if remaining_time[next_job] <= sorted_AT[indel] - current_time:
                gantt_chart.append((jobs[next_job], remaining_time[next_job]))
                #update remaining time of [next job]
                f_jobs[next_job] = 1
                current_time = remaining_time[next_job] + current_time
                turnaround_time[next_job] = current_time - arrival_time[next_job]
                waiting_time[next_job] = turnaround_time[next_job] - burst_time[next_job]
                print(f'three+++++++++++++++++\nremaining{remaining_time[next_job]}\ntime {current_time}\nindel {indel}')
                print(turnaround_time, waiting_time, 00000000)
            else:
                gantt_chart.append((jobs[next_job], sorted_AT[indel] - current_time))
                #update remaining time of [next job]
                remaining_time[next_job] = remaining_time[next_job] - (sorted_AT[indel] - current_time)
                current_time = sorted_AT[indel]
                indel += 1
                print(f'two=============\nremaining{remaining_time[next_job]}\ntime {current_time}\nindel {indel}')

        elif len(sorted_AT) == indel or current_time == sorted_AT.pop():
            print('fuck')
            gantt_chart.append((jobs[next_job], remaining_time[next_job]))
            current_time = current_time + remaining_time[next_job]
            turnaround_time[next_job] = current_time - arrival_time[next_job]
            waiting_time[next_job] = turnaround_time[next_job] - burst_time[next_job]
            f_jobs[next_job] = 1
            print(f'one------------\nremaining{remaining_time[next_job]}\ntime {current_time}\nindel {indel}')
            print(turnaround_time, waiting_time, 0000)                    
        
        print(gantt_chart)
        
    return arrival_time, burst_time, waiting_time, turnaround_time, gantt_chart

def main(): 
    
    jobs = ["A", "B", "C"]
    arrival_time = [0, 4, 7]
    burst_time = [7, 4, 1]
    '''
    jobs = ["A", "B", "C", "D", "E", "F", "G", "H"]
    arrival_time = [7, 4, 16, 0, 18, 12, 24, 4]
    burst_time = [5, 6, 8, 12, 2, 7, 3, 8]
    
    jobs = ["A", "B", "C", "D", "E"]
    arrival_time = [3, 5, 8, 0 , 12]
    burst_time = [4, 9, 4, 7, 6]
    '''
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