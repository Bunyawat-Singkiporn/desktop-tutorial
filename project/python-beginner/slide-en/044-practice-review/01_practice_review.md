# 🏋️ Practice Review — Comprehensive Review

---

## What You Have Learned (Lessons 025–043)

| Topic | Key Concepts |
|-------|--------------|
| Lists | Storing multiple values, indexes, loops, methods |
| Tuples | Fixed, immutable data |
| Sets | Unique values, union, intersection |
| Dictionaries | Key-value pairs, methods |
| Functions | `def`, parameters, `return` |
| Scope | Local vs. global |
| Debugging | Syntax, runtime, and logic errors |
| Readability | Clean code, naming, comments |

---

## Example Combining All Topics

```python
def get_average(scores):
    """Calculate the average of a list of scores."""
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

def get_grade(average):
    """Convert an average score to a grade."""
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "F"

# Main program
student_scores = {"Alice": [85, 90, 78],
                  "Bob": [72, 68, 75]}

for name, scores in student_scores.items():
    avg = get_average(scores)
    grade = get_grade(avg)
    print(f"{name}: {avg:.1f} → {grade}")
```

---

## Review Tips

1. Read the code one line at a time.
2. Trace variable values by hand.
3. If you find a bug, use `print()` to investigate it.
4. If the code runs but gives the wrong result, check its logic.
