# Week 20 - เช็คพอยต์ 1 : อ่านไฟล์ครั้งแรก
import os

FILE = "scores.txt"

# สร้างไฟล์ทดสอบก่อน
with open(FILE, "w", encoding="utf-8") as f:
    f.write("5\n")
    f.write("12\n")
    f.write("3\n")

# อ่านกลับมา
if os.path.exists(FILE):
    with open(FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    total = 0
    for line in lines:
        number = int(line.strip())
        print("อ่านได้:", number)
        total = total + number

    print("รวม:", total)
    print("เฉลี่ย:", total / len(lines))
else:
    print("ยังไม่มีไฟล์")
