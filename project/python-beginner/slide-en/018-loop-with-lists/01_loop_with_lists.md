# 📋 Loop with Lists — Looping Over Multiple Items

---

## What is a List?

**List** is a collection of multiple pieces of information in a single variable.

```python
fruits = ["Apple", "Banana", "Mango"]
```

| Index |fee|
|-------|-----|
| `[0]` | `"Apple"` |
| `[1]` | `"Banana"` |
| `[2]` | `"Mango"` |

> Index always starts at **0**.

---

## Loop through a List with for

```python
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
```

Output:
```
Apple
Banana
Mango
```

> `fruit` is a temporary variable that holds a value each cycle — name it whatever you want.

---

## Combine numbers in a List

```python
scores = [85, 92, 78, 95, 88]
total = 0

for score in scores:
    total = total + score

print("Total:", total)
print("Count:", len(scores))
print(f"Average: {total / len(scores):.1f}")
```

Output:
```
Total: 438
Count: 5
Average: 87.6
```

---

## for vs range

```python
# range — know the number of turns
for i in range(3):
    print(i)      # 0, 1, 2

# list — cycle through each value
colors = ["Red", "Green", "Blue"]
for color in colors:
    print(color)  # Red, Green, Blue
```

---

## len() — Counts the number of members.

```python
names = ["Alice", "Bob", "Charlie"]
print(len(names))   # 3

numbers = [10, 20, 30, 40, 50]
print(len(numbers)) # 5
```

---

## Summary

|subject|example|
|-------|---------|
|Create a list| `items = ["a", "b", "c"]` |
|Member access| `items[0]` → `"a"` |
|loop list| `for item in items:` |
|Count the number| `len(items)` → `3` |
