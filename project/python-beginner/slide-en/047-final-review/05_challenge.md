# 🔥 Final Review — Question 4: Mini Project Assessment

**Difficulty:** 🔴 Hard

---

## Problem

Create a **Student Management System** using everything you have learned.

**Features:**
- `add` — Add a student (name and score)
- `show` — Display all students (name, score, and grade)
- `search` — Search by name
- `stats` — Display the average, top score, and bottom score
- `exit` — End the program

**Requirements:**
- Organize the program into functions.
- Store the data in a dictionary.
- Use these grades: A ≥ 80, B ≥ 70, C ≥ 60, F < 60.

**Example Session:**
```
Command: add
Name: Alice
Score: 88
Command: add
Name: Bob
Score: 65
Command: show
Alice: 88 (A)
Bob: 65 (C)
Command: stats
Average: 76.5
Top: Alice (88)
Bottom: Bob (65)
Command: search
Name: Alice
Found: Alice - 88 (A)
Command: exit
```

---

## Starter Code

```python
# Create the required functions
# Write the main loop

students = {}

while True:
    command = input("Command: ")
    if command == "exit":
        break
    # Write your code here
```
