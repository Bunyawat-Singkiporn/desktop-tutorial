# ⌨️ Input — Getting Data from the User

---

## What is input()?

`input()` is a command that makes the program **pause and wait** for text from the user.

```python
name = input()
print("Hello,", name)
```

```
→ program waits... user types: Alex
Hello, Alex
```

---

## input() Always Returns a String

No matter what the user types — the result is always `str`.

```python
age = input()
print(type(age))    # <class 'str'>
```

> If you want to calculate with it, convert with `int()` or `float()` first

---

## Getting Multiple Inputs

Each `input()` reads **1 line** from the user:

```python
first_name = input()
last_name = input()
print("Full name:", first_name, last_name)
```

Input:
```
Alice
Smith
```

Output:
```
Full name: Alice Smith
```

---

## Getting Numbers and Calculating

```python
age = int(input())         # convert to int right away
next_year = age + 1
print("Next year:", next_year)
```

Input: `14`
Output: `Next year: 15`

---

## Complete Program Example

```python
name = input()
age = int(input())

print("Name:", name)
print("Age:", age)
print("Next year:", age + 1)
```

Input:
```
Bob
14
```

Output:
```
Name: Bob
Age: 14
Next year: 15
```

---

## Summary

| Command | Result |
|---------|--------|
| `x = input()` | Get a string from the user |
| `x = int(input())` | Get a string, then convert to int |
| `x = float(input())` | Get a string, then convert to float |

> **Remember:** `input()` always gives a string — always convert before calculating
