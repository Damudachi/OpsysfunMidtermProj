def Algo(processList, priorityList, burstList, arrivalList, process):

    print("\nPreemptive Priority Scheduling\n")

    remainingBurst = burstList.copy()
    completionTime = [0] * process
    waitingTime = [0] * process
    turnaroundTime = [0] * process

    completed = 0
    current_time = 0

    while completed != process:

        idx = -1
        best_priority = float('inf')

        for i in range(process):
            if arrivalList[i] <= current_time and remainingBurst[i] > 0:
                if priorityList[i] < best_priority:
                    best_priority = priorityList[i]
                    idx = i
                elif priorityList[i] == best_priority:
                    if arrivalList[i] < arrivalList[idx]:
                        idx = i

        if idx != -1:
            remainingBurst[idx] -= 1
            current_time += 1

            if remainingBurst[idx] == 0:
                completionTime[idx] = current_time
                turnaroundTime[idx] = completionTime[idx] - arrivalList[idx]
                waitingTime[idx] = turnaroundTime[idx] - burstList[idx]
                completed += 1
        else:
            current_time += 1

    totalWT = sum(waitingTime)
    totalTAT = sum(turnaroundTime)

    print("Process\tPriority\tAT\tBT\tET\tTAT\tWT")
    for i in range(process):
        print(f"{processList[i]}\t{priorityList[i]}\t\t{arrivalList[i]}\t{burstList[i]}"
              f"\t{completionTime[i]}\t{turnaroundTime[i]}\t{waitingTime[i]}")

    print(f"\nAverage Waiting Time: {round(totalWT / process, 2)}")
    print(f"Average Turnaround Time: {round(totalTAT / process, 2)}")

