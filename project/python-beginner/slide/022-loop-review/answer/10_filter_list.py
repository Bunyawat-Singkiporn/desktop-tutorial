# โจทย์: เก็บเฉพาะคะแนนที่ >= 60 ใน list ใหม่

scores = [88, 45, 72, 30, 95, 58, 66]
passed = []

for s in scores:
    if s >= 60:
        passed.append(s)

print("Passed:", passed)
print("Count:", len(passed))
