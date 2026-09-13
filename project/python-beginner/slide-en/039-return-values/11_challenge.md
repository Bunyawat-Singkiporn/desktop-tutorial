# 🔥 Practice Return — Challenge: Game Username Signup

**Difficulty:** 🔴 Hard

---

## Task

Game signup: username must be at least 8 characters.

Create:
1. `name_length(text)` — return length
2. `can_register(text)` — return `True` if length >= 8 (use `name_length`)

---

## Example

**Input:**
```
dragon123
```

**Output:**
```
Username: dragon123
Length: 9
Status: OK to register
```

---

## Starter Code

```python
def name_length(text):
    # Write your code here

def can_register(text):
    # Write your code here

username = input()
print(f"Username: {username}")
print(f"Length: {name_length(username)}")
if can_register(username):
    print("Status: OK to register")
else:
    print("Status: Too short")
```
