# 🐛 Practice: Debugging Loops — Question 3: Fix Three Bugs

**Difficulty:** 🟡 Medium

---

## Problem

The code below has **3 bugs** that need to be fixed to display correctly.

```python
names = ["Alice", "Bob", "Charlie"]

for name in names:
    print(names)

total = 0
for i in range(1, 5):
    total = total + i
print("Total 1-5:", total)
```

**Required Output:**
```
Alice
Bob
Charlie
Total 1-5: 15
```

---

## 💡 Hint

Bug 1: Use `names` instead of `name`.
Bug 2: `range(1, 5)` only gets 1–4
Bug 3: `print` is outside the loop but the total value is wrong.

---

## Starter Code

```python
names = ["Alice", "Bob", "Charlie"]

for name in names:
    print(names)   # Bug 1

total = 0
for i in range(1, 5):   # Bug 2
    total = total + i
print("Total 1-5:", total)
```
