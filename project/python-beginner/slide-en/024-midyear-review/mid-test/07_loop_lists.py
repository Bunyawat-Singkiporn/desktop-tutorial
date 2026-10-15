# ข้อ 7 : loop with lists
# โจทย์: วนซ้ำ list คะแนน แสดงหมายเลขและคะแนน แล้วแสดงค่าเฉลี่ย

scores = [88, 95, 72, 100, 65]

total = 0

for i in range(len(scores)):
    print("Student", i + 1, ":", scores[i])
    total = total + scores[i]

average = total / len(scores)

print("Average:", average)
