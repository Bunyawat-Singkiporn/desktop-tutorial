# 🔥 Practice: Loop Safety — Question 4: Number Filter

**Difficulty:** 🔴 Hard

---

## Problem

Receive repeated numbers until typing `0` showing only numbers **divided by 3** and counting them.

**Input:**
```
3
7
9
2
12
5
6
0
```

**Output:**
```
3
9
12
6
Count of multiples of 3: 4
```

---

## 💡 Hint

- `while True:` + `break` when receiving 0
- If `n % 3 != 0` then `continue` (skip)
- If `n % 3 == 0` print and add count

---

## Starter Code

```python
count = 0

while True:
    n = int(input())
    if n == 0:
        break
    if n % 3 != 0:
        continue   # Skip non-multiples
    # Print and count multiples of 3

print(f"Count of multiples of 3: {count}")
```
