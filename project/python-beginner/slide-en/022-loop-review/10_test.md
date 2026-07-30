# 🔽 Practice: Loop Review — Question 9: Filter List

**Difficulty:** 🟡 Medium

---

## Problem

Cycle through the list and store only scores >= 60 into the new list.

```python
scores = [88, 45, 72, 30, 95, 58, 66]
```

**Output:**
```
Passed: [88, 72, 95, 66]
Count: 4
```

---

## 💡 Hint

- Create `passed = []` first.
- If `s >= 60` → `passed.append(s)`
- Use `len(passed)` to count the numbers.

---

## Starter Code

```python
scores = [88, 45, 72, 30, 95, 58, 66]
passed = []

for s in scores:
    # If s >= 60, add to passed

print("Passed:", passed)
print("Count:", len(passed))
```
