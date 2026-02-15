from collections import deque

def Algo(processList, priorityList, burstList, arrivalList, process, quantum):

    print("\nRound Robin Scheduling\n")

    remainingBurst = burstList.copy()
    completionTime = [0] * process
    waitingTime = [0] * process
    turnaroundTime = [0] * process

    # Sort process indices by arrival time (tie-break by index)
    order = sorted(range(process), key=lambda i: (arrivalList[i], i))

    time = 0
    complete = 0
    queue = deque()
    inQueue = [False] * process
    ptr = 0  # pointer into sorted order

    # Add processes arriving at time 0
    while ptr < process and arrivalList[order[ptr]] <= time:
        queue.append(order[ptr])
        inQueue[order[ptr]] = True
        ptr += 1

    while complete != process:
        if queue:
            i = queue.popleft()

            exec_time = min(quantum, remainingBurst[i])
            time += exec_time
            remainingBurst[i] -= exec_time

            # Add newly arrived processes before putting current back
            while ptr < process and arrivalList[order[ptr]] <= time:
                queue.append(order[ptr])
                inQueue[order[ptr]] = True
                ptr += 1

            if remainingBurst[i] == 0:
                completionTime[i] = time
                turnaroundTime[i] = completionTime[i] - arrivalList[i]
                waitingTime[i] = turnaroundTime[i] - burstList[i]
                complete += 1
            else:
                queue.append(i)
        else:
            # No process ready — jump to next arrival
            time = arrivalList[order[ptr]]
            while ptr < process and arrivalList[order[ptr]] <= time:
                queue.append(order[ptr])
                inQueue[order[ptr]] = True
                ptr += 1

    totalWT = sum(waitingTime)
    totalTAT = sum(turnaroundTime)

    print("Process\tAT\tBT\tET\tTAT\tWT")
    for i in range(process):
        print(f"{processList[i]}\t{arrivalList[i]}\t{burstList[i]}\t"
              f"{completionTime[i]}\t{turnaroundTime[i]}\t{waitingTime[i]}")

    print(f"\nAverage Waiting Time: {round(totalWT / process, 2)}")
    print(f"Average Turnaround Time: {round(totalTAT / process, 2)}")