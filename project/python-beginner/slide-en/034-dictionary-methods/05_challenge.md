# 🔥 Practice Dictionary Methods — Question 4: Contact Editor

**Difficulty:** 🔴 Hard

---

## Problem

Build a contact editor that supports 3 commands: `show`, `update`, `delete`

```python
contact = {
    "name": "Alice",
    "phone": "081-111-1111",
    "city": "Bangkok"
}
```

| Command | Effect |
|---------|--------|
| `show` | Show every key-value |
| `update` | Read a key and new value, then update |
| `delete` | Read a key and delete it |
| `exit` | Quit the program |

**Sample Session:**
```
Command: show
name: Alice
phone: 081-111-1111
city: Bangkok
Command: update
Key: city
Value: Chiang Mai
Command: delete
Key: phone
Command: show
name: Alice
city: Chiang Mai
Command: exit
```

---

## Starter Code

```python
contact = {
    "name": "Alice",
    "phone": "081-111-1111",
    "city": "Bangkok"
}

while True:
    command = input("Command: ")
    if command == "exit":
        break
    # Write your code here
```
