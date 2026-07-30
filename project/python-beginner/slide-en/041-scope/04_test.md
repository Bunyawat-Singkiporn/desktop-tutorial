# 🌐 Practice Scope — Question 3: Local and Global

**Difficulty:** 🟡 Medium

---

## Problem

Create a program that uses both global and local variables correctly.

**Requirements:**
- `SCHOOL_NAME = "True Coding"` is global and can be used inside the function.
- The `introduce(name, score)` function uses local variables.
- Display each result with the global school name.

**Output:**
```
[True Coding] Alice scored 90
[True Coding] Bob scored 75
```

---

## Starter Code

```python
SCHOOL_NAME = "True Coding"

def introduce(name, score):
    # Use SCHOOL_NAME (global) and name and score (local parameters)
    # Write your code here

introduce("Alice", 90)
introduce("Bob", 75)
```
