# 📦 Variables — Boxes That Store Data

---

## What is a Variable?

A **Variable** is a "data storage place" in computer memory.

Imagine a **box with a name tag** 📦:

```
┌─────────────┐
│     12      │  ← stored data (value)
└─────────────┘
     age        ← box name (variable name)
```

---

## How to Create a Variable

```python
age = 12
name = "Alex"
price = 99.5
```

> The `=` sign means **"store this value"**
> (not "equals" like in math)

---

## How to Use a Variable

```python
name = "Alex"
print(name)              # show the value in the variable
print("Hello,", name)    # use it together with text
```

Output:
```
Alex
Hello, Alex
```

---

## You Can Change a Variable's Value

```python
score = 0
print(score)   # 0

score = 100
print(score)   # 100
```

> Same box, but you can always put something new inside

---

## Variables Can Be Added Together

```python
price = 100
tax = 7
total = price + tax

print("Price:", price)
print("Tax:", tax)
print("Total:", total)
```

Output:
```
Price: 100
Tax: 7
Total: 107
```

---

## Program Example

```python
name = "Sarah"
age = 13
city = "Bangkok"

print("Name:", name)
print("Age:", age)
print("City:", city)
```

Output:
```
Name: Sarah
Age: 13
City: Bangkok
```

---

## Things to Remember

| Allowed ✅ | Not allowed ❌ |
|------------|----------------|
| `name = "Alex"` | `"Alex" = name` |
| `score = 100` | `100 = score` |
| You can change the value anytime | The left side must be a variable name |
