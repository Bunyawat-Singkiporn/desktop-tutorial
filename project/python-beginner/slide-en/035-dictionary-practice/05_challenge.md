# 🔥 Practice Dictionary — Question 4: Inventory System

**Difficulty:** 🔴 Hard

---

## Problem

Build an inventory system that supports: `add`, `update`, `remove`, `show`, `exit`

| Command | Effect |
|---------|--------|
| `add` | Add a product (name + price) |
| `update` | Update the price |
| `remove` | Remove a product |
| `show` | Show all products |
| `exit` | Quit |

**Sample Session:**
```
Command: add
Name: Pen
Price: 15
Command: add
Name: Book
Price: 120
Command: show
Pen: 15 baht
Book: 120 baht
Command: update
Name: Pen
New price: 18
Command: show
Pen: 18 baht
Book: 120 baht
Command: exit
```

---

## Starter Code

```python
inventory = {}

while True:
    command = input("Command: ")
    if command == "exit":
        break
    # Write your code here
```
