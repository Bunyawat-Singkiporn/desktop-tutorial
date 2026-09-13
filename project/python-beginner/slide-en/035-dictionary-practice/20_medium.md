# Practice Dictionary — Question 19: Count Fruit in Basket

**Difficulty:** 🟡 Medium

---

## Task

Count how many of each fruit.

```python
basket = ["apple", "banana", "apple", "apple", "banana", "mango"]
```

**Output:**
```
apple: 3
banana: 2
mango: 1
```

---

## 💡 Hint

Like Word Counter — if already in dict `+= 1`, else set to `1`

---

## Starter Code

```python
basket = ["apple", "banana", "apple", "apple", "banana", "mango"]
count = {}

for fruit in basket:
    # Write your code here

for fruit, n in count.items():
    print(f"{fruit}: {n}")
```
