# 🏆 Practice: Mid-Year Review — Question 2: Class Average

**Difficulty:** 🟡 Medium

---

## โจทย์

รับคะแนน n คน แล้วแสดงผลสรุปชั้นเรียน

**Input:**
```
4
90
55
75
80
```

**Output:**
```
Student 1: 90 → Pass
Student 2: 55 → Fail
Student 3: 75 → Pass
Student 4: 80 → Pass
---
Average: 75.0
Pass: 3 | Fail: 1
```

---

## 💡 Hint

- รับ n ก่อน แล้ว loop `range(n)` รับคะแนนทีละคน
- เก็บใน list แล้วคำนวณหลัง loop

---

## Starter Code

```python
n = int(input())
scores = []
pass_count = 0
fail_count = 0

for i in range(n):
    score = int(input())
    scores.append(score)
    # Print "Student X: score → Pass/Fail"
    # Count pass/fail

print("---")
# Print average
# Print pass/fail counts
```
