def Algo(processList, priorityList, burstList, arrivalList, process):

    completed = 0
    current_time = 0
    visited = [False] * process
    waitingTime = [0] * process
    turnaroundTime = [0] * process
    completionTime = [0] * process

    print("\nNon-Preemptive Priority Scheduling\n")

    while completed != process:

        idx = -1
        best_priority = float('inf')

        for i in range(process):
            if arrivalList[i] <= current_time and not visited[i]:
                if priorityList[i] < best_priority:
                    best_priority = priorityList[i]
                    idx = i
                elif priorityList[i] == best_priority:
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

    print("Process\tPriority\tAT\tBT\tET\tTAT\tWT")
    for i in range(process):
        print(f"{processList[i]}\t{priorityList[i]}\t\t{arrivalList[i]}\t{burstList[i]}"
              f"\t{completionTime[i]}\t{turnaroundTime[i]}\t{waitingTime[i]}")

    print("\nAverage Waiting Time:", round(totalWT / process, 2))
    print("Average Turnaround Time:", round(totalTAT / process, 2))
