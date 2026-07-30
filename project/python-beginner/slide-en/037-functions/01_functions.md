# ⚙️ Functions

---

## What Is a Function?

A function is a **named set of instructions** that you can reuse.

---

## Why Use Functions?

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

> Write it once and use it many times.

---

## Defining a Function

```python
def function_name():
    # Instructions inside the function
    print("Hello!")
```

- `def` is a keyword that begins a function definition.
- `function_name` is the name of the function.
- `:` ends the `def` line.
- The instructions inside the function **must be indented** by four spaces.

---

## Calling a Function

```python
def greet():
    print("Hello!")
    print("Nice to meet you!")

greet()   # First call
greet()   # Second call
```

**Output:**
```
Hello!
Nice to meet you!
Hello!
Nice to meet you!
```

---

## Order Matters

```
1. Define the function first.
2. Call the function afterward.
```

```python
# ❌ Incorrect — called before it is defined
greet()
def greet():
    print("Hello!")

# ✅ Correct — defined before it is called
def greet():
    print("Hello!")
greet()
```
