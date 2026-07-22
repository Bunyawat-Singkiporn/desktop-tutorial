# โจทย์: รายงานเกรดของนักเรียน n คน (3 วิชา) พร้อมสรุปชั้นเรียน

n = int(input())
names = []
averages = []

for i in range(n):
    name = input()
    # รับคะแนน 3 วิชาในบรรทัดเดียว: "80 90 70" → [80, 90, 70]
    scores = list(map(int, input().split()))
    avg = sum(scores) / len(scores)
    names.append(name)
    averages.append(avg)

    # ตรวจเกรด
    if avg >= 80:
        grade = "A"
    elif avg >= 60:
        grade = "B"
    else:
        grade = "C"

    print(f"{name:<6}| Avg: {avg:.1f} | Grade: {grade}")

print("---")
class_avg = sum(averages) / len(averages)
print(f"Class Average: {class_avg:.1f}")
# หาชื่อนักเรียนที่มีเฉลี่ยสูงสุด
top_index = averages.index(max(averages))
print(f"Top Student: {names[top_index]}")
