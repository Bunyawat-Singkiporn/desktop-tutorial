# 🐛 Debugging — Finding and Fixing Errors

---

## Three Types of Errors

---

## 1. Syntax Error — Breaking the Language Rules

Python cannot understand the code, so it **cannot run at all**.

```python
# ❌ Missing :
if x > 5
    print(x)

# ✅ Fixed
if x > 5:
    print(x)
```

> Python reports: `SyntaxError: invalid syntax`

---

## 2. Runtime Error — Crashing While Running

The syntax is valid, but a problem occurs while the program runs.

```python
# ❌ Division by zero
x = 10 / 0          # ZeroDivisionError

# ❌ Index out of range
nums = [1, 2, 3]
print(nums[5])       # IndexError

# ❌ Wrong data type
print("5" + 3)       # TypeError
```

---

## 3. Logic Error — Incorrect Result

The code runs, but **produces the wrong result**.

```python
# ❌ Logic error
total = 0
for i in range(1, 5):
    total = i       # Wrong! Replaces the value each time

print(total)        # 4 (not 10)

# ✅ Correct
total = 0
for i in range(1, 5):
    total += i

print(total)        # 10
```

---

## Debugging with `print`

```python
def calc(x, y):
    print("x =", x, "y =", y)   # Check the input values
    result = x * y
    print("result =", result)    # Check the result
    return result
```

---

## Summary

| Type | When It Occurs | How to Fix It |
|------|----------------|---------------|
| Syntax | The code breaks Python's rules | Read the error message |
| Runtime | The program crashes while running | Check data types and valid ranges |
| Logic | The result is incorrect | Use `print` to trace variable values |
