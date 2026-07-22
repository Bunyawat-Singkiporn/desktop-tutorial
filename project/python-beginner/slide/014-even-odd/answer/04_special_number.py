# โจทย์: รับตัวเลข แล้วตัดสินว่าเป็น Special หรือ Normal
# - เป็น Special เมื่อ: เป็นเลขคู่ AND มากกว่า 20
# - อื่น ๆ: Normal

number = int(input())  # รับตัวเลขจากผู้ใช้

# ใช้ and เพื่อรวม 2 เงื่อนไขเข้าด้วยกัน
# ต้องเป็นจริงทั้งคู่ถึงจะเป็น Special
if number % 2 == 0 and number > 20:
    print("Special")
else:
    print("Normal")
