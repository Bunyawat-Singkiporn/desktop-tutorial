# 🔥 Practice List — Question 4: To-Do Manager

**Difficulty:** 🔴 Hard

---

## Problem

Create a user-selectable to-do program:

| Command | Effect |
|--------|-----|
| `add` |Add a new to-do|
| `remove` |Delete the specified to-do.|
| `show` |Show all to-do|
| `exit` |End of program|

---

## Example Session

```
Command: add
Item: Buy milk
Command: add
Item: Do laundry
Command: show
1. Buy milk
2. Do laundry
Command: remove
Item: Buy milk
Command: show
1. Do laundry
Command: exit
Done!
```

---

## 💡 Hint

- Use `while True:` and `break` to exit the loop.
- Use `if command == "add":` for each command.

---

## Starter Code

```python
todos = []

while True:
    command = input("Command: ")
    
    if command == "exit":
        print("Done!")
        break
    # Write your code here
```
