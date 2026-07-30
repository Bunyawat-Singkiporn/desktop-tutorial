# 🔥 Practice Review — Question 4: Mini Grade System

**Difficulty:** 🔴 Hard

---

## Problem

Create a grade management system using lists, dictionaries, and functions.

**Commands:** `add`, `show`, `average`, `top`, `exit`

| Function | Purpose |
|----------|---------|
| `add_student(db, name, score)` | Add a student |
| `show_all(db)` | Display every student with a grade |
| `get_average(db)` | Return the average score |
| `get_top(db)` | Return the name of the top student |

**Example Session:**
```
Command: add
Name: Alice
Score: 88
Command: add
Name: Bob
Score: 72
Command: show
Alice: 88 (A)
Bob: 72 (B)
Command: average
Average: 80.0
Command: top
Top: Alice (88)
Command: exit
```

---

## Starter Code

```python
def add_student(db, name, score):
    # Write your code here

def show_all(db):
    # Write your code here

def get_average(db):
    # Write your code here

def get_top(db):
    # Write your code here

db = {}
while True:
    command = input("Command: ")
    if command == "exit":
        break
    # Write your code here
```
