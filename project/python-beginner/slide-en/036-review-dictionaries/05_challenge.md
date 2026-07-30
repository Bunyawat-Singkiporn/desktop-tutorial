# 🔥 Practice Review Dictionaries — Question 4: Grade Book

**Difficulty:** 🔴 Hard

---

## Problem

Create a gradebook that can add students, update scores, display all records, and find the student with the highest score.

Accept these commands: `add`, `update`, `show`, `top`, and `exit`.

**Example Session:**
```
Command: add
Name: Alice
Score: 85
Command: add
Name: Bob
Score: 92
Command: top
Top: Bob (92)
Command: update
Name: Alice
Score: 95
Command: top
Top: Alice (95)
Command: show
Alice: 95
Bob: 92
Command: exit
```

---

## Starter Code

```python
gradebook = {}

while True:
    command = input("Command: ")
    if command == "exit":
        break
    # Write your code here
```
