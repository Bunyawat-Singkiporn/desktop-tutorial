# ⚙️ Functions

---

## What is a function?

A function is a **named block of statements** you can run again and again.

---

## Why use functions?

Code without a function:
```python
print("Hello Alice")
print("Hello Bob")
print("Hello Charlie")
```

Code with a function:
```python
def greet():
    print("Hello!")

greet()
greet()
greet()
```

> Write once, use many times

---

## Defining a function

```python
def function_name():
    # statements inside
    print("Hello!")
```

- `def` = keyword that starts a function definition
- `function_name` = name of the function
- `:` = ends the `def` line
- statements inside **must be indented** 4 spaces

---

## Calling a function

```python
def greet():
    print("Hello!")
    print("Nice to meet you!")

greet()   # first call
greet()   # second call
```

**Output:**
```
Hello!
Nice to meet you!
Hello!
Nice to meet you!
```

---

## Order matters

```
1. Define (create) first
2. Call second
```

```python
# ❌ wrong — call before define
greet()
def greet():
    print("Hello!")

# ✅ correct — define then call
def greet():
    print("Hello!")
greet()
```
