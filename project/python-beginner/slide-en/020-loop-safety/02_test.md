# 🛑 Practice: Loop Safety — Question 1: Use break

**Difficulty:** 🟢 Easy

---

## Problem

Loops 1–10, but stops when a 6 is found.

**Output:**
```
1
2
3
4
5
Stopped at 6
```

---

## 💡 Hint

- Use `for i in range(1, 11):`
- IF `i == 6` GIVES MESSAGE `print` THEN `break`

---

## Starter Code

```python
for i in range(1, 11):
    if i == 6:
        print("Stopped at 6")
        # Stop the loop
    # Print i (only reached if i != 6)
```
