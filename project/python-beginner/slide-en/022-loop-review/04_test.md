# ✅ Practice: Loop Review — Question 3: Grade List

**Difficulty:** 🟡 Medium

---

## Problem

Get points 5 times and show each person's grade. with a summary of the number of passes/fails

**Input:**
```
85
55
92
45
70
```

**Output:**
```
Score 85: Pass
Score 55: Fail
Score 92: Pass
Score 45: Fail
Score 70: Pass
---
Pass: 3
Fail: 2
```

---

## 💡 Hint

- Use `for i in range(5):` to receive input 5 times.
- If score >= 60: Pass, count pass
- If not: Fail, count fail.

---

## Starter Code

```python
pass_count = 0
fail_count = 0

for i in range(5):
    score = int(input())
    # Check pass/fail and print result
    # Count each

print("---")
# Print pass and fail counts
```
