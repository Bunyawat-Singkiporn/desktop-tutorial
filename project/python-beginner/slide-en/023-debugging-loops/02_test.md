# 🐛 Practice: Debugging Loops — Question 1: Fix Off-by-One

**Difficulty:** 🟢 Easy

---

## Problem

The code below wants to display 1–10 but only 1–9 — correct that.

```python
for i in range(1, 10):
    print(i)
```

**Required Output:**
```
1
2
3
4
5
6
7
8
9
10
```

---

## 💡 Hint

`range(1, 10)` stops before 10 — What needs to be changed?

---

## Starter Code

```python
for i in range(1, 10):   # ← Fix this line
    print(i)
```
