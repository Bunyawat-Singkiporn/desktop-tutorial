# ⭐ Practice: Loop Review — Question 14: Star Rows with Count

**Difficulty:** 🔴 Hard

---

## Problem

Take n and display a star triangle with the number of stars in each row.

**Input:**
```
4
```

**Output:**
```
Row 1: * (1 star)
Row 2: ** (2 stars)
Row 3: *** (3 stars)
Row 4: **** (4 stars)
```

---

## 💡 Hint

- Outside Loop: Rows 1 to n
- Loop in: create star string `stars = ""` then `stars += "*"`
- Show `f"Row {row}: {stars} ({row} stars)"`

---

## Starter Code

```python
n = int(input())

for row in range(1, n + 1):
    stars = ""
    for j in range(row):
        # Add one star to stars
    # Print "Row row: stars (row stars)"
```
