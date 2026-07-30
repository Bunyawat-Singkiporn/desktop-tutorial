# ✖️ Practice: Nested Loops — Question 3: Multiplication Table

**Difficulty:** 🟡 Medium

---

## Problem

Get the number n and display the n×n multiplication table.

**Input:**
```
4
```

**Output:**
```
1  2  3  4  
2  4  6  8  
3  6  9  12  
4  8  12  16  
```

---

## 💡 Hint

- Outside Loop: Rows 1–n
- Loop in: Columns 1–n
- `print(i * j, end="  ")` print numbers and space

---

## Starter Code

```python
n = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        # Print i * j with spaces
    # Move to next line
```
