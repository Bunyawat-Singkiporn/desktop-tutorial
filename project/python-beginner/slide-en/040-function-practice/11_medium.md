# Practice Function — Question 9: Camp Attendance List

**Difficulty:** 🟡 Medium

---

## Task

A teacher collects names for camp.

Create:
- `add_name(names, name)`
- `show_names(names)`

---

## Example Session

```
How many campers? 3
Name: Alice
Name: Bob
Name: Cara
=== Camp List ===
Alice
Bob
Cara
```

---

## Starter Code

```python
def add_name(names, name):
    # Write your code here

def show_names(names):
    # Write your code here

names = []
n = int(input("How many campers? "))
for i in range(n):
    add_name(names, input("Name: "))

print("=== Camp List ===")
show_names(names)
```
