# ⬇️ Practice: Loop Review — Question 5: Countdown

**Difficulty:** 🟢 Easy

---

## Problem

Get the number n, count down from n down to 1, then type "Go!"

**Input:**
```
5
```

**Output:**
```
5
4
3
2
1
Go!
```

---

## 💡 Hint

- Use `range(n, 0, -1)` — range 3 numbers: start, stop, step
- step `-1` = decrease by 1

---

## Starter Code

```python
n = int(input())

for i in range(n, 0, -1):
    # Print i

print("Go!")
```
