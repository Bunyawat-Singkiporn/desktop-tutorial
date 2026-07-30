records = [("Alice", 85), ("Bob", 72), ("Alice", 90), ("Charlie", 68)]

names = set()
scores = {}

for name, score in records:
    names.add(name)
    scores[name] = score   # ค่าล่าสุดทับค่าเดิม

total = 0
for score in scores.values():
    total += score
average = total / len(scores)

print("Unique students:", names)
print("Latest scores:", scores)
print(f"Average: {average:.1f}")
