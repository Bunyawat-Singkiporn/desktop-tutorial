# 🔥 Practice: while Loop — Question 4: Number Accumulator

**Difficulty:** 🔴 Hard

---

## Problem

Get repeated numbers Until the user types `0` and then the statistics are displayed.

**Input:**
```
5
12
3
8
0
```

**Output:**
```
Count: 4
Total: 28
Average: 7.00
Largest: 12
Smallest: 3
```

---

## 💡 Hint

- Use `while True:` + `break` when getting 0
- Store every number in the list.
- Use `max()`, `min()`, `sum()`, `len()` to calculate.

---

## Starter Code

```python
numbers = []

while True:
    n = int(input())
    if n == 0:
        break
    numbers.append(n)

# Calculate and print stats
```
