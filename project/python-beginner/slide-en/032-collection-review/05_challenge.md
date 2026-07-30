# 🔥 Practice Collection Review — Question 4: Student Tracker

**Difficulty:** 🔴 Hard

---

## Problem

Create a student tracking system using all three collection types:

- **list** — store all scores, including duplicates
- **set** — store the unique letter grades that appear
- **tuple** — store fixed class information (class name and academic year)

```python
all_scores = [85, 72, 91, 85, 60, 72, 95, 88]
class_info = ("Grade 9/1", "2025")
```

**Output:**
```
Class: Grade 9/1 (2025)
Scores: [85, 72, 91, 85, 60, 72, 95, 88]
Average: 81.0
Grades given: {'A', 'B', 'C'}
Top score: 95
```

Use these grade thresholds: A >= 80, B >= 70, C >= 60, and F < 60.

---

## Starter Code

```python
all_scores = [85, 72, 91, 85, 60, 72, 95, 88]
class_info = ("Grade 9/1", "2025")
grades_given = set()

# Write your code here
```
