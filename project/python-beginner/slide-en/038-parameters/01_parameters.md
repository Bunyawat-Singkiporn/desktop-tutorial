# 📥 Parameters — Passing Values into Functions

---

## What Are Parameters?

A parameter is a **variable that receives a value from outside** a function.

```python
def greet(name):        # name = parameter
    print("Hello", name)

greet("Alice")          # "Alice" = argument
greet("Bob")
```

**Output:**
```
Hello Alice
Hello Bob
```

---

## Multiple Parameters

```python
def describe(name, age):
    print(f"{name} is {age} years old.")

describe("Alice", 15)
describe("Bob", 14)
```

**Output:**
```
Alice is 15 years old.
Bob is 14 years old.
```

---

## Example — Calculation

```python
def add(a, b):
    print(a + b)

add(3, 5)   # 8
add(10, 20) # 30
```

---

## Parameter vs. Argument

| Term | Meaning | Example |
|------|---------|---------|
| Parameter | A variable name in the `def` statement | `def greet(name):` |
| Argument | A value passed when calling the function | `greet("Alice")` |

---

## Common Mistakes

```python
def add(a, b):
    print(a + b)

add(3)        # ❌ Missing an argument
add(3, 5, 7)  # ❌ Too many arguments
add(3, 5)     # ✅ Correct
```

---

## Program Example — BMI Calculator

```python
def show_bmi(weight, height):
    bmi = weight / (height ** 2)
    print(f"BMI: {bmi:.1f}")

show_bmi(60, 1.70)
show_bmi(75, 1.75)
```
