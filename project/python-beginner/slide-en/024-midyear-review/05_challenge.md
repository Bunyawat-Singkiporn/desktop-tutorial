# 🔥 Practice: Mid-Year Review — Question 4: Full Student Report

**Difficulty:** 🔴 Hard

---

## Problem

Get the names and 3 subject scores of n students and display a summary report.

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

> Grade: A = 80+, B = 60–79, C = below 60

---

## 💡 Hint

- Get 3 subject scores in one line with `input().split()` and convert to int
- Collect the average of each person in the list and find the max.

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
