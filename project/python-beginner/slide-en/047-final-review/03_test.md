# 📚 Final Review — Question 2: Collections

**Difficulty:** 🟡 Medium

---

## Problem

The student data is provided as a list of `(name, score)` tuples.
Create a `{name: score}` dictionary from the data, then find the unique students and the average score.

```python
records = [("Alice", 85), ("Bob", 72), ("Alice", 90), ("Charlie", 68)]
```

**Output:**
```
Unique students: {'Alice', 'Bob', 'Charlie'}
Latest scores: {'Alice': 90, 'Bob': 72, 'Charlie': 68}
Average: 76.7
```

(If a name appears more than once, keep its latest score.)

---

## Starter Code

```python
records = [("Alice", 85), ("Bob", 72), ("Alice", 90), ("Charlie", 68)]

names = set()
scores = {}

# Build names set and scores dict
# Calculate average from scores.values()
```
