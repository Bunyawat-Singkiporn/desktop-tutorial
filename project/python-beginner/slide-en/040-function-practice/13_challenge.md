# 🔥 Practice Function — Challenge: Student Report Card

**Difficulty:** 🔴 Hard

---

## Task

Build one student's report card.

| Function | Job |
|----------|-----|
| `read_scores(n)` | read n subject scores |
| `average(scores)` | return average |
| `grade(avg)` | return A/B/C/F |
| `report(name, avg, g)` | print report card |

---

## Example Session

```
Name: Alice
Subjects: 3
Score: 80
Score: 90
Score: 70
=== Report Card ===
Student: Alice
Average: 80.0
Grade: A
```

---

## Starter Code

```python
def read_scores(n):
    # Write your code here

def average(scores):
    # Write your code here

def grade(avg):
    # Write your code here

def report(name, avg, g):
    # Write your code here

name = input("Name: ")
n = int(input("Subjects: "))
scores = read_scores(n)
avg = average(scores)
g = grade(avg)
report(name, avg, g)
```
