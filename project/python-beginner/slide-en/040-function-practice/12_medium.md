# Practice Function — Question 10: Travel Temperature Helper

**Difficulty:** 🟡 Medium

---

## Task

Travel app: user chooses mode then converts temperature.

- `C` → convert to °F
- `F` → convert to °C

Create `to_f(c)` and `to_c(f)`.

---

## Example

**Input:**
```
C
0
```

**Output:**
```
Travel Helper
0.0 C = 32.00 F
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
print("Travel Helper")
if mode == "C":
    print(f"{value} C = {to_f(value):.2f} F")
elif mode == "F":
    print(f"{value} F = {to_c(value):.2f} C")
else:
    print("Unknown mode")
```
