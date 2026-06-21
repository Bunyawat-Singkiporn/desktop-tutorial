# โจทย์: รับรหัสผ่านซ้ำจนกว่าจะถูก

# รหัสที่ถูกต้อง
correct = "python123"

# รับรหัสครั้งแรก
password = input()

# วนจนกว่าจะพิมพ์ถูก
while password != correct:
    print("Wrong password! Try again.")
    password = input()

print("Access granted!")
