# Practice Function — Question 7: Who Passed the Test?

**Difficulty:** 🟡 Medium

---

## Task

A teacher checks test scores. Score >= 50 means pass.

Create `get_passed(scores)` that returns only passing scores.

---

## Example Session

```
How many scores? 5
Score: 40
Score: 70
Score: 55
Score: 30
Score: 90
Passed scores: [70, 55, 90]
```

---

## Starter Code

```python
def get_passed(scores):
    # Write your code here

n = int(input("How many scores? "))
scores = []
for i in range(n):
    scores.append(int(input("Score: ")))

print(f"Passed scores: {get_passed(scores)}")
```
