# เริ่มสร้างเมนู

tasks = []

while True: # คือวนลูปไปเรื่อย ๆ จนกว่าจะเจอคำสั่ง break

    print("1. Show")
    print("2. Add")
    print("3. Exit")

    choice = input("Choose: ")

    print("You choose:", choice)

    if choice == "3":
        break

# while True
# คือวนไปเรื่อย ๆ

# break
# คือหยุดลูป