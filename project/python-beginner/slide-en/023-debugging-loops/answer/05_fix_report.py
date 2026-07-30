# โจทย์: แก้ 4 bugs ในโค้ด report
# Bug 1: total = total + score ไม่มี indent (ต้องอยู่ใน loop)
# Bug 2: count = count + 1 ไม่มี indent
# Bug 3:   print(f"Count: ...") มี indent เกิน
# Bug 4: max(score) → max(scores) — ใช้ชื่อ list ไม่ใช่ตัวแปรวน

scores = [80, 95, 60, 45, 75]
total = 0
count = 0

for score in scores:
    total = total + score   # ✅ Bug 1 แก้: เพิ่ม indent
    count = count + 1       # ✅ Bug 2 แก้: เพิ่ม indent

average = total / count
print(f"Total: {total}")
print(f"Count: {count}")        # ✅ Bug 3 แก้: ลด indent
print(f"Average: {average:.1f}")
print(f"Max: {max(scores)}")    # ✅ Bug 4 แก้: scores ไม่ใช่ score
