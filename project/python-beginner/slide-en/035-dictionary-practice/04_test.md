# 🛒 Practice Dictionary — Question 3: Shopping Total

**Difficulty:** 🟡 Medium

---

## Problem

Given product prices, read 3 item names from the user and calculate the total.

```python
prices = {"apple": 15, "banana": 8, "mango": 25, "orange": 20, "kiwi": 35}
```

**Sample Session:**
```
Item 1: apple
Item 2: mango
Item 3: banana
apple: 15
mango: 25
banana: 8
Total: 48 baht
```

If an item is not in the system, show `"Not found: [name]"` and do not add a price.

---

## Starter Code

```python
prices = {"apple": 15, "banana": 8, "mango": 25, "orange": 20, "kiwi": 35}
total = 0

for i in range(3):
    item = input(f"Item {i+1}: ")
    # Write your code here

print(f"Total: {total} baht")
```
