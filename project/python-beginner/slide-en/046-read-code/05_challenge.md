# 🔥 Read Code — Question 4: Find and Fix Bug

**Difficulty:** 🔴 Hard

---

## Problem

Read the code below **without running it**. Find the bugs, explain them, and fix them.

```python
def find_average(scores):
    total = 0
    for score in scores:
        total = total + score
    return total / 10    # ← Look carefully

def classify(avg):
    if avg > 80:         # ← Look carefully
        return "Excellent"
    if avg > 60:
        return "Good"
    else:
        return "Needs Work"

data = [70, 80, 90, 85, 75]
avg = find_average(data)
print(f"Average: {avg}")
print(f"Level: {classify(avg)}")
```

**Output:**
```
Average: 80.0
Level: Excellent
```

---

## Questions

1. Where are the bugs? Find them without running the code.
2. What type of bugs are they?
3. How should they be fixed?

---

## Starter Code

```python
# Explain the bugs you found:
# Bug 1: Line __ because __
# Bug 2: Line __ because __

# Fix the code:
```
