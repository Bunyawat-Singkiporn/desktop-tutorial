# 🔥 Practice Return Values — Question 4: Chain Functions

**Difficulty:** 🔴 Hard

---

## Problem

Create two functions that work together:
1. `get_average(scores)` — returns the average
2. `classify(average)` — returns the performance level

| Average | Level |
|---------|-------|
| >= 80 | `Excellent` |
| >= 60 | `Satisfactory` |
| < 60 | `Needs Improvement` |

Then use both functions with a dictionary of students.

**Output:**
```
Alice: 85.0 → Excellent
Bob: 62.0 → Satisfactory
Charlie: 50.0 → Needs Improvement
```

---

## Starter Code

```python
def get_average(scores):
    # Write your code here

def classify(average):
    # Write your code here

students = {
    "Alice": [90, 85, 80],
    "Bob": [70, 55, 61],
    "Charlie": [45, 55, 50]
}

for name, scores in students.items():
    avg = get_average(scores)
    level = classify(avg)
    print(f"{name}: {avg:.1f} → {level}")
```
