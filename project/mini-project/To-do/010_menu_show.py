tasks = []

while True:

    print("\n===== TODO APP =====")
    print("1. Show")
    print("2. Add")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":

        # เดิมเราใช้
        # print(tasks)

        # ตอนนี้จะแสดงแบบสวยขึ้น

        if len(tasks) == 0: # ถ้าไม่มีงานเลย ให้แสดงว่า No Tasks

            print("No Tasks")

        else: # ถ้ามีงาน ให้แสดงงานทั้งหมด

            for i in range(len(tasks)):
                print(i + 1, tasks[i])

    elif choice == "2":

        task = input("Task: ")

        tasks.append(task)

    elif choice == "3":

        break