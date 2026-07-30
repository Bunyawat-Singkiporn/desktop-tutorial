# 📋 Lists — Collections of Data

---

## What is a List?

A list is a data structure that lets you **store multiple values in one variable**.

Instead of creating multiple variables:
```python
name1 = "Alice"
name2 = "Bob"
name3 = "Charlie"
```

We can use a list instead:
```python
names = ["Alice", "Bob", "Charlie"]
```

---

## Creating a List

```python
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
mixed = [10, "hello", True]
empty = []
```

---

## Accessing Items by Index

Indexes always start at **0**.

```python
fruits = ["apple", "banana", "mango"]

print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[2])   # mango
print(fruits[-1])  # mango  ← last item
print(fruits[-2])  # banana ← second-to-last item
```

---

## len() — Count the Items

```python
fruits = ["apple", "banana", "mango"]
print(len(fruits))  # 3
```

---

## Looping with a for Loop

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

## Example Program — Adding Scores

```python
scores = [85, 90, 78, 92, 88]
total = 0

for score in scores:
    total += score

print("Total:", total)
```

---

## Index Example

| Index | -3 | -2 | -1 |
|-------|----|----|----|
| Value | `"apple"` | `"banana"` | `"mango"` |
| **Index** | **0** | **1** | **2** |
