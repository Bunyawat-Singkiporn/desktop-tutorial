# 💥 Debugging — Question 2: Fix Runtime Errors

**Difficulty:** 🟢 Easy

---

## Problem

The code below has **two runtime errors**. Find and fix both of them.

```python
scores = [85, 92, 78]

# Bug 1: index out of range
print(scores[5])

# Bug 2: wrong data type
age = input("Age: ")
next_year = age + 1
print(next_year)
```

**Correct Output** (if the user enters `15`):
```
78
16
```

---

## 💡 Hint

- Bug 1: The last index is `len(scores) - 1`.
- Bug 2: `input()` always returns a `str`, so convert it to an `int` first.

---

## Starter Code

```python
scores = [85, 92, 78]

# Fix Bug 1
print(scores[5])

# Fix Bug 2
age = input("Age: ")
next_year = age + 1
print(next_year)
```
