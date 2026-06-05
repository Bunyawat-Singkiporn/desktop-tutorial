# Todo List App

tasks = []

while True:

    print("\n===== TODO APP =====")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose: ")

    # ==========================
    # SHOW TASKS
    # ==========================
    if choice == "1":

        if len(tasks) == 0:
            print("No tasks")

        else:
            for i in range(len(tasks)):
                print(i + 1, tasks[i])

    # ==========================
    # ADD TASK
    # ==========================
    elif choice == "2":

        task = input("New Task: ")

        tasks.append(task)

        print("Task Added!")

    # ==========================
    # REMOVE TASK
    # ==========================
    elif choice == "3":

        if len(tasks) == 0:
            print("No tasks")

        else:

            for i in range(len(tasks)):
                print(i + 1, tasks[i])

            index = int(input("Remove Number: "))

            # List เริ่มนับจาก 0
            tasks.pop(index - 1)

            print("Task Removed!")

    # ==========================
    # EXIT
    # ==========================
    elif choice == "4":

        print("Goodbye")

        break

    # ==========================
    # INVALID CHOICE
    # ==========================
    else:

        print("Invalid Choice")