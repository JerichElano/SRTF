def ordinal_suffixes(j): # For ordinal suffixes 
    ordinal_suffixes = ['st', 'nd', 'rd'] + ['th'] * j
    ordinality = []
    for i in range(j+1): # It starts with "0th" so we need to add 1 to j
        if i % 10 in (1, 2, 3) and not i in (11, 12, 13):
            ordinality.append(f"{i}{ordinal_suffixes[i % 10 - 1]}")
        elif i in (11, 12, 13):
            ordinality.append(f"{i}{ordinal_suffixes[3]}")
        else:
            ordinality.append(f"{i}{ordinal_suffixes[3]}")

    return ordinality

def srtf(jobs, arrival_time, burst_time):
    # Copy the burst time into remaining_time list
    remaining_time = burst_time.copy()

    # Initialize completion_time, waiting_time, and turnaround_time lists with zeros
    completion_time = [0] * len(jobs)
    waiting_time = [0] * len(jobs)
    turnaround_time = [0] * len(jobs)

    # Initialize time and completed variables
    time = 0
    completed = 0

    # Initialize variables used in the main loop
    prev = -1
    min_burst = float('inf')
    shortest = 0
    check = False

    # Main loop runs until all jobs are completed
    while completed != len(jobs):
        # Find the job with the shortest remaining time that has arrived by the current time
        for i in range(len(jobs)):
            if arrival_time[i] <= time and remaining_time[i] < min_burst and remaining_time[i] > 0:
                min_burst = remaining_time[i]
                shortest = i
                check = True

        # If no job is found, increment the current time and continue to the next iteration
        if check == False:
            time += 1
            continue

        # Process the job for one unit of time
        remaining_time[shortest] -= 1
        min_burst = remaining_time[shortest]
        if min_burst == 0:
            min_burst = float('inf')

        # If the job is completed, update its completion time and waiting time
        if remaining_time[shortest] == 0:
            completed += 1
            check = False
            end_time = time + 1
            completion_time[shortest] = end_time
            waiting_time[shortest] = end_time - arrival_time[shortest] - burst_time[shortest]
            if waiting_time[shortest] < 0:
                waiting_time[shortest] = 0

        # Increment the current time
        time += 1

    # After all jobs are completed, calculate the turnaround time for each job
    for i in range(len(jobs)):
        turnaround_time[i] = burst_time[i] + waiting_time[i]

    # Return the waiting time and turnaround time for each job
    return waiting_time, turnaround_time

def main():
    jobs = []
    arrival_time = []
    burst_time = []

    print("=====================================================")
    print("   Welcome to the SRTF Process Scheduling Simulator")
    print("=====================================================")

    print("")
    valid = False
    while valid == False:
        no_of_processes = int(input("Enter number of processes: "))
        if no_of_processes > 0:
            valid = True
        else:
            print("Invalid input, please try again.")
    print("")
    
    ordinal = ordinal_suffixes(no_of_processes)
    for i in range(no_of_processes):
        print("")
        jobs.append(input(f"Enter {ordinal[i+1]} job name: "))
        arrival_time.append(int(input(f"Enter arrival time for the job {jobs[i]}: ")))
        burst_time.append(int(input(f"Enter burst time for {jobs[i]}: ")))

    print("")
    print("")

    waiting_time, turnaround_time = srtf(jobs, arrival_time, burst_time)

    print("-----------------------------------------")
    print("            R  E  S  U  L  T             ")
    print("-----------------------------------------")

    print("   Job\t|   AT\t|   BT\t|  TAT\t|   WT")
    for i in range(no_of_processes):
        print(f"    {jobs[i]}\t|   {arrival_time[i]}\t|   {burst_time[i]}\t|   {turnaround_time[i]}\t|   {waiting_time[i]}")
    
    print("-----------------------------------------")


main()