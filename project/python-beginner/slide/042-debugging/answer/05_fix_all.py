scores = [85, 72, 90, 68, 95]
total = 0

# Syntax fix: เพิ่ม : หลัง for
for score in scores:
    total += score     # Logic fix: += แทน =

# Runtime fix: หารด้วย len(scores) ไม่ใช่ 0
average = total / len(scores)

# Syntax fix: ปิด " ใน print
if average >= 70:
    print("Class passed")
else:
    print("Class failed")

print("Average:", average)
