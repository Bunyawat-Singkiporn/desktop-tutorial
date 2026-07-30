# 🔥 Practice: Nested Loops — Question 4: Number Pattern

**Difficulty:** 🔴 Hard

---

## Problem

Get n and display the pattern numbers according to this format.

**Input:**
```
4
```

**Output:**
```
1
1 2
1 2 3
1 2 3 4
```

**Input:**
```
5
```

**Output:**
```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

---

## 💡 Hint

- Outside Loop: Rows 1–n
- Loop in: numbers 1 to current row
- `print(j, end=" ")` then `print()` starts a new line.

---

## Starter Code

```python
n = int(input())

for row in range(1, n + 1):
    for j in range(1, row + 1):
        print(j, end=" ")
    print()
```
