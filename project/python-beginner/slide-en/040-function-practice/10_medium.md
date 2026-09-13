# Practice Function — Question 8: Phone Calculator App

**Difficulty:** 🟡 Medium

---

## Task

Make a tiny phone calculator.

- `add(a, b)` returns sum
- `mul(a, b)` returns product

User enters two numbers, then presses `1` (add) or `2` (multiply).

---

## Example

**Input:**
```
7
3
1
```

**Output:**
```
Calculator
7 + 3 = 10
```

---

## Starter Code

```python
def add(a, b):
    # Write your code here

def mul(a, b):
    # Write your code here

a = int(input())
b = int(input())
choice = input()
print("Calculator")
if choice == "1":
    print(f"{a} + {b} = {add(a, b)}")
elif choice == "2":
    print(f"{a} * {b} = {mul(a, b)}")
else:
    print("Unknown button")
```
