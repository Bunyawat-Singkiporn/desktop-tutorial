# 🔥 Practice: Mid-Year Review — Question 4: Full Student Report

**Difficulty:** 🔴 Hard

---

## โจทย์

รับชื่อและคะแนน 3 วิชาของนักเรียน n คน แล้วแสดงรายงานสรุป

**Input:**
```
2
Alice
80 90 70
Bob
60 55 75
```

**Output:**
```
=== Class Report ===
Alice | Avg: 80.0 | Grade: A
Bob   | Avg: 63.3 | Grade: B
---
Class Average: 71.7
Top Student: Alice
```

> เกรด: A = 80+, B = 60–79, C = ต่ำกว่า 60

---

## 💡 Hint

- รับคะแนน 3 วิชาในบรรทัดเดียวด้วย `input().split()` แล้วแปลงเป็น int
- เก็บ average ของแต่ละคนใน list แล้วหา max

---

## Starter Code

```python
n = int(input())
names = []
averages = []

for i in range(n):
    name = input()
    scores = list(map(int, input().split()))
    avg = sum(scores) / len(scores)
    names.append(name)
    averages.append(avg)

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
top_index = averages.index(max(averages))
print(f"Top Student: {names[top_index]}")
```
