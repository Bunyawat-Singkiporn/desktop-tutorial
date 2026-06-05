tasks = []

while True:

    print("\n===== TODO APP =====")
    print("1. Show")
    print("2. Add")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        print(tasks)

    elif choice == "2":

        task = input("Task: ") # รับชื่องาน

        tasks.append(task) # เพิ่มงานเข้าไปใน list

    elif choice == "3":
        break

# ตอนนี้โปรแกรม
# เพิ่มงานได้แล้ว