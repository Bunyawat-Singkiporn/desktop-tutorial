# 🔍 Practice: Loop Review — Question 6: Count Value

**Difficulty:** 🟢 Easy

---

## Problem

Counts how many times a given number appears in a list.

```python
scores = [80, 60, 80, 90, 80, 70, 80]
target = 80
```

**Output:**
```
80 appears 4 times
```

---

## 💡 Hint

- loop through list
- If `s == target` → `count += 1`

---

## Starter Code

```python
scores = [80, 60, 80, 90, 80, 70, 80]
target = 80
count = 0

for s in scores:
    # Check if s equals target
    # Count it

print(f"{target} appears {count} times")
```
