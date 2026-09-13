# Practice Return Values — Medium: Grade from Input

**Difficulty:** 🟡 Medium

---

## Task

Create `get_grade(score)` that **returns** a grade:

| Score | Grade |
|-------|-------|
| >= 80 | `A` |
| >= 70 | `B` |
| >= 60 | `C` |
| < 60  | `F` |

Main program reads a score from `input` and prints the grade.

> Combines: return + input + int() + elif

---

## Example

**Input:**
```
73
```

**Output:**
```
Grade: B
```

---

## Starter Code

```python
def get_grade(score):
    # Write your code here

score = int(input())
grade = get_grade(score)
print(f"Grade: {grade}")
```
