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
            RoundRobin.Algo()
            break
        elif choice == '2':
            print("You have selected Non-Preemptive Priority Algorithm")
            NonPreempPrio.Algo()
            break
        elif choice == '3':
            print("You have selected Preemptive Priority Algorithm")
            PreempPrio.Algo()
            break
        elif choice == '4':
            print("You have selected Shortest Job First Algorithm")
            ShortestJob.Algo()
            break
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")



def takingInput(processList, priorityList, burstList, arrivalList, process):
    print("Enter details for each process (Lower number = higher priority):")
    for i in range(process):
        processList[i] = f"P{i+1}"
        priorityList[i] = int(input(f"Priority for {processList[i]}: "))
        arrivalList[i]  = int(input(f"Arrival time for {processList[i]}: "))
        burstList[i]    = int(input(f"Burst time for {processList[i]}: "))





if __name__ == "__main__":
    menu()
    process = int(input("Enter the number of processes: "))
    processList = [0] * process
    priorityList = [0] * process
    burstList = [0] * process
    arrivalList = [0] * process

    takingInput(processList, priorityList, burstList, arrivalList, process)











