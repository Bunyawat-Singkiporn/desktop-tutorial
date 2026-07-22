# โจทย์: รับตัวเลขจากผู้ใช้ แล้วนับถอยหลังถึง 1

count = int(input())

# วนจนกว่า count จะเป็น 0
while count > 0:
    print(count)
    count = count - 1  # ลดค่าลง 1 ทุกรอบ

print("Blast off!")
