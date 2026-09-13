# Practice Function — Medium: Temperature Mode Convert

**Difficulty:** 🟡 Medium

---

## Task

Create `to_f(c)` and `to_c(f)`.
Read mode (`C` or `F`) and a value, then convert.

> Combines: return + input + if/elif + float

---

## Example

**Input:**
```
F
100
```

**Output:**
```
37.78 C
```

---

## Starter Code

```python
def to_f(c):
    # Write your code here

def to_c(f):
    # Write your code here

mode = input()
value = float(input())

if mode == "C":
    print(f"{to_f(value):.2f} F")
elif mode == "F":
    print(f"{to_c(value):.2f} C")
else:
    print("Unknown mode")
```
