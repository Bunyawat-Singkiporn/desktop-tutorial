# โจทย์: รับคะแนน 2 วิชา แล้ว:
# 1. ถ้าผลรวมเป็นเลขคู่ → บวก Bonus 10 คะแนน
# 2. ถ้าผลรวมเป็นเลขคี่ → ไม่ได้ Bonus
# 3. ถ้าผลรวม (ก่อนบวก bonus) >= 100 → Pass ไม่เช่นนั้น → Fail

a = int(input())  # รับคะแนนวิชาที่ 1
b = int(input())  # รับคะแนนวิชาที่ 2

total = a + b  # คำนวณผลรวมก่อน

# บล็อคที่ 1: ตรวจว่าผลรวมเป็นเลขคู่หรือเลขคี่
if total % 2 == 0:
    # เลขคู่: แสดงผลรวมพร้อม bonus +10
    print("Bonus! Total: " + str(total + 10))
else:
    # เลขคี่: ไม่ได้ bonus แสดงผลรวมเดิม
    print("No Bonus. Total: " + str(total))

# บล็อคที่ 2: ตรวจ pass/fail จากผลรวมก่อนบวก bonus
# สังเกต: ใช้ total (ไม่ใช้ตัวเลขหลังบวก bonus)
if total >= 100:
    print("Pass")
else:
    print("Fail")
