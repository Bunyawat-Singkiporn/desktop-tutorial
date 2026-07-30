# 📐 Practice: Nested Loops — Question 2: Right Triangle

**Difficulty:** 🟡 Medium

---

## Problem

Get the number of rows and display a right triangle.

**Input:**
```
6
```

**Output:**
```
*
**
***
****
*****
******
```

---

## 💡 Hint

- Outside Loop: `for row in range(1, n+1)`
- Loop in: `for col in range(row)` — Loop through the current row.

---

## Starter Code

```python
n = int(input())

for row in range(1, n + 1):
    for col in range(row):
        # Print one * without newline
    # Move to next line
```
