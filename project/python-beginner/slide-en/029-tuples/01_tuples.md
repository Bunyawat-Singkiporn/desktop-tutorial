# 🔒 Tuples — data that does not change

---

## What is a Tuple?

Tuple is a data structure similar to List but **cannot be edited** after creation (Immutable).

---

## Creating a Tuple

Use parentheses `()` instead of `[]`.

```python
days = ("Mon", "Tue", "Wed", "Thu", "Fri")
point = (10, 20)
student = ("Alice", 15, "Grade 9")
```

---

## Accessing data (like a List)

```python
days = ("Mon", "Tue", "Wed")

print(days[0])   # Mon
print(days[-1])  # Wed
print(len(days)) # 3
```

---

## Loop with a for loop

```python
days = ("Mon", "Tue", "Wed", "Thu", "Fri")

for day in days:
    print(day)
```

---

## Immutable — Do not edit.

```python
days = ("Mon", "Tue", "Wed")
days[0] = "Sunday"  # ❌ TypeError!
```

> Tuples are designed to provide data that **Shouldn't change**

---

## When should I use Tuple?

|Use **List** when|Use **Tuple** when|
|------------------|-------------------|
|Want to add/delete information|The data is constant and does not need to be changed.|
|Information can be changed|Want to prevent editing|
|Product list|Day of the week, coordinates, student information|

---

## ExampleProgram

```python
student = ("Bob", 14, "Grade 8")

print("Name:", student[0])
print("Age:", student[1])
print("Grade:", student[2])
```

**Output:**
```
Name: Bob
Age: 14
Grade: Grade 8
```
