# 📊 Practice Review — Question 2: Dict + Loop + Function

**Difficulty:** 🟡 Medium

---

## Problem

Create a function named `print_report(students)` that accepts a `{name: score}` dictionary and displays a report with grades.

| Score | Grade |
|-------|-------|
| >= 80 | A |
| >= 70 | B |
| >= 60 | C |
| < 60 | F |

**Output:**
```
=== Report ===
Alice: 88 → A
Bob: 72 → B
Charlie: 55 → F
```

---

## Starter Code

```python
def get_grade(score):
    # Write your code here

def print_report(students):
    print("=== Report ===")
    for name, score in students.items():
        # Write your code here

print_report({"Alice": 88, "Bob": 72, "Charlie": 55})
```
