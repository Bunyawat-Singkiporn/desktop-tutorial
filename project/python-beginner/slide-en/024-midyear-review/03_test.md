# 🏆 Practice: Mid-Year Review — Question 2: Class Average

**Difficulty:** 🟡 Medium

---

## Problem

Get n people's scores and display class summary results.

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

- Get n first, then loop `range(n)` takes the points one by one.
- Store in a list and calculate after the loop.

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
