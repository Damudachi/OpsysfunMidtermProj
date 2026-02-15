import RoundRobin
import NonPreempPrio
import PreempPrio
import ShortestJob


def menu():
    while True:
        print("Please input what Algorithm You want to use: \n [1] Round-Robin Algorithm \n [2] Non-Preemptive Priority Algorithm \n [3] Preemptive Priority Algorithm \n [4] Shortest Job First Algorithm \n [0] Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            print("You have selected Round-Robin Algorithm")
            process = int(input("Enter the number of processes: "))
            quantum = int(input("Enter the time quantum: "))
            processList = [0] * process
            priorityList = [0] * process
            burstList = [0] * process
            arrivalList = [0] * process
            takingInput(processList, priorityList, burstList, arrivalList, process, choice)
            RoundRobin.Algo(processList, priorityList, burstList, arrivalList, process, choice, quantum)
            break
        elif choice == '2':
            print("You have selected Non-Preemptive Priority Algorithm")
            process = int(input("Enter the number of processes: "))
            processList = [0] * process
            priorityList = [0] * process
            burstList = [0] * process
            arrivalList = [0] * process
            takingInput(processList, priorityList, burstList, arrivalList, process, choice)
            NonPreempPrio.Algo(processList, priorityList, burstList, arrivalList, process, choice)
            break
        elif choice == '3':
            print("You have selected Preemptive Priority Algorithm")
            process = int(input("Enter the number of processes: "))
            processList = [0] * process
            priorityList = [0] * process
            burstList = [0] * process
            arrivalList = [0] * process
            takingInput(processList, priorityList, burstList, arrivalList, process, choice)
            PreempPrio.Algo(processList, priorityList, burstList, arrivalList, process, choice)
            break
        elif choice == '4':
            print("You have selected Shortest Job First Algorithm")
            process = int(input("Enter the number of processes: "))
            processList = [0] * process
            priorityList = [0] * process
            burstList = [0] * process
            arrivalList = [0] * process
            takingInput(processList, priorityList, burstList, arrivalList, process, choice)
            ShortestJob.Algo(processList, priorityList, burstList, arrivalList, process, choice)
            break
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")



def takingInput(processList, priorityList, burstList, arrivalList, process, choice):
    if choice == '1' or choice == '4':
        for i in range(process):
            processList[i] = f"P{i+1}"
            arrivalList[i]  = int(input(f"Arrival time for {processList[i]}: "))
            burstList[i]    = int(input(f"Burst time for {processList[i]}: "))
    else:
        print("Enter details for each process (Lower number = higher priority):")
        for i in range(process):
            processList[i] = f"P{i+1}"
            priorityList[i] = int(input(f"Priority for {processList[i]}: "))
            arrivalList[i]  = int(input(f"Arrival time for {processList[i]}: "))
            burstList[i]    = int(input(f"Burst time for {processList[i]}: "))





if __name__ == "__main__":
        menu()
    










