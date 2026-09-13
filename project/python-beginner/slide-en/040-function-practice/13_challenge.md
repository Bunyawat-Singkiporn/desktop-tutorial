# 🔥 Practice Function — Challenge: Student Grade System

**Difficulty:** 🔴 Hard

---

## Task

Build a grade system from input:

| Function | Job |
|----------|-----|
| `read_scores(n)` | read n scores, return list |
| `average(scores)` | return average |
| `grade(avg)` | return A/B/C/F |
| `report(name, avg, g)` | print one report line |

Grade rules: >=80 A, >=70 B, >=60 C, else F

> Combines: many functions + input + list + for + elif + f-string

---

## Example Session

```
Name: Alice
Subjects: 3
Score: 80
Score: 90
Score: 70
Alice | avg=80.0 | grade=A
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
