# Practice Function — Medium: Menu Calculator

**Difficulty:** 🟡 Medium

---

## Task

Create `add(a, b)` and `mul(a, b)` that return results.

Read `a`, `b`, then choice `1` (add) or `2` (multiply).

> Combines: return + input + if/elif + operators

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
Result: 10
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

if choice == "1":
    print(f"Result: {add(a, b)}")
elif choice == "2":
    print(f"Result: {mul(a, b)}")
else:
    print("Invalid")
```
