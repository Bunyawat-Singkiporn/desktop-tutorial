# 🧩 Debugging — Question 3: Fix a Logic Error

**Difficulty:** 🟡 Medium

---

## Problem

The code runs, but the result is **incorrect**. Find and fix the logic error.

```python
# Program to find the sum from 1 through 5
total = 0
for i in range(1, 5):
    total = i        # ← Logic error!

print("Sum:", total)
# Expected: Sum: 15
# Got: Sum: 4
```

---

## 💡 Hint

You need to **accumulate** each value, not **replace** the previous value.

---

## Starter Code

```python
total = 0
for i in range(1, 5):
    total = i   # Fix this line

# Fix the range as well
print("Sum:", total)
```
