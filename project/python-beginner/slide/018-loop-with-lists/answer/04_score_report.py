# โจทย์: แสดงคะแนนแต่ละคนพร้อมเลขลำดับ และหาเฉลี่ย

scores = [88, 95, 72, 100, 65]
total = 0

# วนด้วย index เพื่อแสดง "Student X: score"
for i in range(len(scores)):
    print(f"Student {i + 1}: {scores[i]}")
    total = total + scores[i]

# คำนวณเฉลี่ยแล้วแสดง
average = total / len(scores)
print(f"Average: {average:.1f}")
