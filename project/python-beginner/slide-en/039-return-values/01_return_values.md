# 📤 Return Values

---

## What Is `return`?

`return` sends a value **back out of a function** so it can be used elsewhere.

---

## `print` vs. `return`

```python
# print displays a value, but does not make it available for later use
def add_print(a, b):
    print(a + b)

result = add_print(3, 5)
print(result)    # None  ← No value was returned!
```

```python
# return provides a value that can be used later
def add_return(a, b):
    return a + b

result = add_return(3, 5)
print(result)    # 8  ✅
```

---

## Using `return`

```python
def square(n):
    return n * n

result = square(5)
print(result)      # 25
print(square(4))   # 16
```

---

## `return` with `if`/`else`

```python
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

print(is_even(4))   # True
print(is_even(7))   # False
```

---

## `return` with Grades

```python
def get_grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"

grade = get_grade(85)
print(f"Grade: {grade}")  # Grade: A
```

---

## Important Points

- `return` immediately stops the function.
- A function without a `return` statement returns `None`.
- You can store a returned value: `result = func()`.
