# 🔭 Scope — Where Variables Are Available

---

## What Is Scope?

Scope is the **area** in which a variable can be accessed.

---

## Local Variables

A variable created **inside a function** is available only within that function.

```python
def my_func():
    x = 10          # local variable
    print(x)        # ✅ Available here

my_func()
print(x)            # ❌ NameError — x does not exist outside the function
```

---

## Global Variables

A variable created **outside a function** is available throughout the program.

```python
name = "Alice"      # global variable

def show():
    print(name)     # ✅ Can be read here

show()              # Alice
print(name)         # Alice
```

---

## When Names Are the Same

```python
x = 100             # global

def test():
    x = 50          # local (a different variable!)
    print("Inside:", x)

test()
print("Outside:", x)
```

**Output:**
```
Inside: 50
Outside: 100
```

> Python uses the local variable first.

---

## Variable Lifetime

```python
def calc():
    result = 42     # Created when the function runs
    return result   # Returned before the variable disappears

value = calc()
print(value)        # 42
# result has now been deleted
```

---

## The `global` Keyword (Advanced)

```python
count = 0

def add_one():
    global count    # Use the global variable
    count += 1

add_one()
add_one()
print(count)        # 2
```
