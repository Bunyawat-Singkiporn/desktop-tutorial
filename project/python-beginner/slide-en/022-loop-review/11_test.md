# 🏆 Practice: Loop Review — Question 10: All Pass Check

**Difficulty:** 🟡 Medium

---

## Problem

Check whether everyone in the class passed with a score of at least 60.

```python
scores = [80, 90, 75, 65, 88]   # Everyone passed
```

**Output:**
```
All passed!
```

```python
scores = [80, 55, 75, 65, 88]   # Someone didn't pass.
```

**Output:**
```
Someone failed.
```

---

## 💡 Hint

- Set `all_pass = True` first.
- If found a score < 60 → `all_pass = False` then `break`

---

## Starter Code

```python
scores = [80, 90, 75, 65, 88]
all_pass = True

for s in scores:
    # If s < 60, set all_pass to False and break

if all_pass:
    print("All passed!")
else:
    print("Someone failed.")
```
