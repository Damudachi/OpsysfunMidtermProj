def Algo(processList, priorityList, burstList, arrivalList, process, choice, quantum=None):

    completed = 0
    current_time = 0
    visited = [False] * process

    waitingTime = [0] * process
    turnaroundTime = [0] * process
    completionTime = [0] * process

    print("\nShortest Job First Scheduling\n")

    while completed != process:

        idx = -1
        min_burst = float('inf')

        for i in range(process):
            if arrivalList[i] <= current_time and not visited[i]:
                if burstList[i] < min_burst:
                    min_burst = burstList[i]
                    idx = i
                elif burstList[i] == min_burst:
                    if arrivalList[i] < arrivalList[idx]:
                        idx = i

        if idx != -1:
            current_time += burstList[idx]
            completionTime[idx] = current_time
            turnaroundTime[idx] = completionTime[idx] - arrivalList[idx]
            waitingTime[idx] = turnaroundTime[idx] - burstList[idx]

            visited[idx] = True
            completed += 1
        else:
            current_time += 1  

    totalWT = sum(waitingTime)
    totalTAT = sum(turnaroundTime)

    print("Process\tAT\tBT\tET\tTAT\tWT")
    for i in range(process):
        print(f"{processList[i]}\t{arrivalList[i]}\t{burstList[i]}"
              f"\t{completionTime[i]}\t{turnaroundTime[i]}\t{waitingTime[i]}")

    print("\nAverage Waiting Time:", round(totalWT / process, 2))
    print("Average Turnaround Time:", round(totalTAT / process, 2))
