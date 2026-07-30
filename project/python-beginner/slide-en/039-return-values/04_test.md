# 🎓 Practice Return Values — Question 3: Get Grade

**Difficulty:** 🟡 Medium

---

## Problem

Create a `get_grade(score)` function that returns a grade, then display the result with an f-string.

| Score | Grade |
|-------|-------|
| >= 80 | `A` |
| >= 70 | `B` |
| >= 60 | `C` |
| < 60 | `F` |

**Output:**
```
Score 85 → Grade A
Score 72 → Grade B
Score 55 → Grade F
```

---

## Starter Code

```python
def get_grade(score):
    # Write your code here

scores = [85, 72, 55]
for s in scores:
    grade = get_grade(s)
    print(f"Score {s} → Grade {grade}")
```
