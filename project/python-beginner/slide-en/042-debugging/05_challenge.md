# 🔥 Debugging — Question 4: Fix All Three

**Difficulty:** 🔴 Hard

---

## Problem

The code below has **three bugs**: one syntax error, one runtime error, and one logic error. Find and fix all of them.

```python
scores = [85, 72, 90, 68, 95]
total = 0

for score in scores
    total = score

average = total / 0    # ← Look carefully

if average >= 70:
    print("Class passed)   # ← Look carefully
else:
    print("Class failed")

print("Average:", average)
```

**Correct Output:**
```
Class passed
Average: 82.0
```

---

## 💡 Hint

Read the code one line at a time and ask yourself:
1. Which line breaks Python's grammar?
2. Which line will crash while the program runs?
3. Which line has incorrect logic?

---

## Starter Code

```python
scores = [85, 72, 90, 68, 95]
total = 0

for score in scores
    total = score

average = total / 0

if average >= 70:
    print("Class passed)
else:
    print("Class failed")

print("Average:", average)
```
