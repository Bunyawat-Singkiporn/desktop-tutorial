# 📋 Lists — Data collections

---

## What is a list?

A list is a data structure used to **store many values in one variable**.

Instead of creating many variables:
```python
name1 = "Alice"
name2 = "Bob"
name3 = "Charlie"
```

You can use a list:
```python
names = ["Alice", "Bob", "Charlie"]
```

---

## Creating lists

```python
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
mixed = [10, "hello", True]
empty = []
```

---

## Accessing data (index)

Index always starts at **0**.

```python
fruits = ["apple", "banana", "mango"]

print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[2])   # mango
print(fruits[-1])  # mango  ← last item
print(fruits[-2])  # banana ← second-to-last
```

---

## len() — count members

```python
fruits = ["apple", "banana", "mango"]
print(len(fruits))  # 3
```

---

## Loop with for

```python
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)
```

**Output:**
```
apple
banana
mango
```

---

## Example program — sum scores

```python
scores = [85, 90, 78, 92, 88]
total = 0

for score in scores:
    total += score

print("Total:", total)
```

---

## Index example

| Index | -3 | -2 | -1 |
|-------|----|----|----|
| Value | `"apple"` | `"banana"` | `"mango"` |
| **Index** | **0** | **1** | **2** |
