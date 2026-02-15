def Algo(processList, priorityList, burstList, arrivalList, n, choice):

    #Class 
    class Process:
        def __init__(self, processID, arrivalTime, priority, burstTime):
            self.processID = processID
            self.arrivalTime = arrivalTime
            self.priority = priority
            self.burstTime = burstTime
            self.tempburstTime = burstTime
            self.responsetime = -1
            self.outtime = 0
            self.intime = -1


    #Helper functions
    def insert(Heap, value, heapsize, currentTime):
        start = heapsize[0]
        Heap[start] = value

        if Heap[start].intime == -1:
            Heap[start].intime = currentTime

        heapsize[0] += 1

        # Min-heap based on priority
        while start != 0 and Heap[(start - 1) // 2].priority > Heap[start].priority:
            Heap[(start - 1) // 2], Heap[start] = Heap[start], Heap[(start - 1) // 2]
            start = (start - 1) // 2


    def order(Heap, heapsize, start):
        smallest = start
        left = 2 * start + 1
        right = 2 * start + 2

        if left < heapsize[0] and Heap[left].priority < Heap[smallest].priority:
            smallest = left

        if right < heapsize[0] and Heap[right].priority < Heap[smallest].priority:
            smallest = right

        if smallest != start:
            Heap[start], Heap[smallest] = Heap[smallest], Heap[start]
            order(Heap, heapsize, smallest)


    def extractminimum(Heap, heapsize, currentTime):
        min_process = Heap[0]

        if min_process.responsetime == -1:
            min_process.responsetime = currentTime - min_process.arrivalTime

        heapsize[0] -= 1

        if heapsize[0] >= 1:
            Heap[0] = Heap[heapsize[0]]
            order(Heap, heapsize, 0)

        return min_process


    def scheduling(Heap, array, heapsize, currentTime):
        if heapsize[0] == 0:
            return

        min_process = extractminimum(Heap, heapsize, currentTime)

        min_process.outtime = currentTime + 1
        min_process.burstTime -= 1

        print(f"process id = {min_process.processID} current time = {currentTime}")

        if min_process.burstTime > 0:
            insert(Heap, min_process, heapsize, currentTime)
            return


    #Input of processes
    processes = []
    for i in range(n):
        processes.append(
            Process(
                processList[i],
                arrivalList[i],
                priorityList[i],
                burstList[i]
            )
        )


    #Main function of program
    processes.sort(key=lambda x: x.arrivalTime)

    total_waiting_time = 0
    total_turnaround_time = 0
    total_response_time = 0

    inserted_process = 0
    heap_size = [0]
    current_time = processes[0].arrivalTime

    Heap = [None] * (4 * n)

    for i in range(n):
        processes[i].tempburstTime = processes[i].burstTime

    while True:

        # Insert processes that arrive at current_time
        if inserted_process != n:
            for i in range(n):
                if processes[i].arrivalTime == current_time:
                    inserted_process += 1
                    processes[i].intime = -1
                    processes[i].responsetime = -1
                    insert(Heap, processes[i], heap_size, current_time)

        scheduling(Heap, processes, heap_size, current_time)

        current_time += 1

        if heap_size[0] == 0 and inserted_process == n:
            break


    #Calculate and display of results
    print("\n{:<10}{:<8}{:<8}{:<10}{:<10}{:<10}".format(
        "Process", "AT", "BT", "Prio(P)", "TAT", "WT"
    ))

    print("-" * 56)

    for i in range(n):
        turnaround_time = processes[i].outtime - processes[i].arrivalTime
        waiting_time = turnaround_time - processes[i].tempburstTime

        total_response_time += processes[i].responsetime
        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time

        print("{:<10}{:<8}{:<8}{:<10}{:<10}{:<10}".format(
            processes[i].processID,
            processes[i].arrivalTime,
            processes[i].tempburstTime,
            processes[i].priority,
            turnaround_time,
            waiting_time
        ))

    print("-" * 56)
    print(f"Average waiting time      = {total_waiting_time / n:.2f}")
    print(f"Average response time     = {total_response_time / n:.2f}")
    print(f"Average turn around time  = {total_turnaround_time / n:.2f}")

