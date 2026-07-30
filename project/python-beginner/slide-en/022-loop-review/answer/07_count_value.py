# โจทย์: นับว่าค่าที่กำหนดปรากฏกี่ครั้งใน list

scores = [80, 60, 80, 90, 80, 70, 80]
target = 80
count = 0

for s in scores:
    if s == target:
        count += 1

print(f"{target} appears {count} times")
