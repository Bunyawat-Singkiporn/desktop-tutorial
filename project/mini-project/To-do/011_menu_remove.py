# Todo App เพิ่มความสามารถลบงาน

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

        # ถ้ายังไม่มีงาน
        if len(tasks) == 0:

            print("No tasks")

        else:

            # แสดงรายการงานก่อนลบ
            for i in range(len(tasks)):
                print(i + 1, tasks[i])

            # รับหมายเลขงานที่ต้องการลบ
            index = int(input("Remove Number: "))

            # ตัวอย่าง
            #
            # 1 Homework
            # 2 Study
            # 3 Exercise
            #
            # ถ้าผู้ใช้พิมพ์ 2
            #
            # index = 2
            #
            # แต่ใน List จริง ๆ
            #
            # tasks[0] = Homework
            # tasks[1] = Study
            # tasks[2] = Exercise
            #
            # จึงต้องลบ 1 ออกก่อน

            tasks.pop(index - 1)

            print("Task Removed!")

    # ==========================
    # EXIT
    # ==========================
    elif choice == "4":

        print("Goodbye")

        break

    else:

        print("Invalid Choice")