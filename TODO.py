

tasks = []

while True:

    print("\n========== TODO MENU ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Completed")
    print("4. Remove Task")
    print("5. Search Task")
    print("6. Total Tasks")
    print("7. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":

        task_name = input("Enter Task Name : ")
        priority = input("Enter Priority (High/Medium/Low) : ")

        task = [task_name, priority, "Pending"]

        tasks.append(task)

        print("Task Added Successfully")


    elif choice == "2":

        if len(tasks) == 0:
            print("No Tasks Available")

        else:

            print("\n========== TASK LIST ==========")

            for i in range(len(tasks)):

                print(
                    f"{i+1}. "
                    f"Task : {tasks[i][0]} | "
                    f"Priority : {tasks[i][1]} | "
                    f"Status : {tasks[i][2]}"
                )


    elif choice == "3":

        if len(tasks) == 0:
            print("No Tasks Available")

        else:

            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i][0]}")

            complete = int(input("Enter Task Number : "))

            if complete > 0 and complete <= len(tasks):

                tasks[complete - 1][2] = "Completed"

                print("Task Marked Completed")

            else:
                print("Invalid Task Number")


    elif choice == "4":

        if len(tasks) == 0:
            print("No Tasks To Remove")

        else:

            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i][0]}")

            remove = int(input("Enter Task Number : "))

            if remove > 0 and remove <= len(tasks):

                removed = tasks.pop(remove - 1)

                print(f"{removed[0]} Removed Successfully")

            else:
                print("Invalid Task Number")


    elif choice == "5":

        search = input("Enter Task To Search : ").lower()

        found = False

        for task in tasks:

            if search in task[0].lower():

                print(
                    f"\nTask : {task[0]} | "
                    f"Priority : {task[1]} | "
                    f"Status : {task[2]}"
                )

                found = True

        if found == False:
            print("Task Not Found")
   elif choice == "6":

        total = len(tasks)

        completed = 0
        pending = 0

        for task in tasks:

            if task[2] == "Completed":
                completed += 1
            else:
                pending += 1

        print("\n========== TASK REPORT ==========")
        print(f"Total Tasks      : {total}")
        print(f"Completed Tasks  : {completed}")
        print(f"Pending Tasks    : {pending}")


    
    elif choice == "7":

        print("Program Closed")
        break

    else:
        print("Invalid Choice")
