# ⏭️ Practice: Loop Safety — Question 2: Skip Even Numbers

**Difficulty:** 🟡 Medium

---

## Problem

Loop 1–10, but skip all even numbers. Show only odd numbers

**Output:**
```
1
3
5
7
9
```

---

## 💡 Hint

- If `i % 2 == 0` (even number) then `continue`
- If not, it's normal `print`.

---

## Starter Code

```python
for i in range(1, 11):
    if i % 2 == 0:
        # Skip even numbers
    print(i)
```
