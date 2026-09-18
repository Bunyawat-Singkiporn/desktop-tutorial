# Week 19 - เช็คพอยต์ 1 : เขียนไฟล์ครั้งแรก
name = "Mint"
score = 14

with open("test.txt", "w", encoding="utf-8") as f:
    f.write("ชื่อ: " + name + "\n")
    f.write("คะแนน: " + str(score) + "\n")

print("เขียนไฟล์เสร็จแล้ว")
print("ลองเปิดไฟล์ test.txt ดู")
