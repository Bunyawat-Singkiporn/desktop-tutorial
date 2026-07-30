# 🧾 Practice: Loop Review — Question 7: Running Total

**Difficulty:** 🟡 Medium

---

## Problem

Cycle through the list of prices and show the cumulative total after each item is added.

```python
prices = [100, 50, 200, 75]
```

**Output:**
```
100 → total: 100
50 → total: 150
200 → total: 350
75 → total: 425
```

---

## 💡 Hint

- `total` starts at 0
- Each cycle: `total += p` and print immediately.

---

## Starter Code

```python
prices = [100, 50, 200, 75]
total = 0

for p in prices:
    # Add p to total
    # Print "p → total: total"
```
