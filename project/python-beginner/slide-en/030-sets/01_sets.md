# 🎯 Sets — Unique data sets.

---

## What is Set?

Set is a data structure. **Values ​​are unique** and **No exact order**

---

## Creating a Set

```python
fruits = {"apple", "banana", "mango"}
numbers = {1, 2, 3, 4, 5}
```

> If you enter duplicate values ​​— Set will automatically delete them.

```python
nums = {1, 2, 2, 3, 3, 3}
print(nums)  # {1, 2, 3}
```

---

## Delete duplicate values ​​from List

```python
data = [1, 2, 2, 3, 4, 4, 5]
unique = set(data)
print(unique)  # {1, 2, 3, 4, 5}
```

---

## .add() and .remove()

```python
fruits = {"apple", "banana"}
fruits.add("mango")       # increase
fruits.remove("banana")   # delete
print(fruits)             # {'apple', 'mango'}
```

---

## Check the value

```python
fruits = {"apple", "banana", "mango"}
print("apple" in fruits)   # True
print("grape" in fruits)   # False
```

---

## Union and Intersection

**Union `|` — Total (unique):**
```python
a = {"A", "B", "C"}
b = {"B", "C", "D"}
print(a | b)  # {'A', 'B', 'C', 'D'}
```

**Intersection `&` — duplicate values:**
```python
print(a & b)  # {'B', 'C'}
```

---

## Summary of Set Methods

| Method | Purpose |
|--------|---------|
| `set(list)` |Convert list to set (delete duplicates)|
| `.add(x)` |increase value|
| `.remove(x)` |Delete value|
| `x in set` |examine|
| `a \| b` | Union |
| `a & b` | Intersection |
