# Practice Dictionary — Question 22: Buy Two Items

**Difficulty:** 🟡 Medium

---

## Task

Read 2 item names from the shop and calculate the total.

```python
prices = {"pen": 10, "book": 40, "eraser": 5, "ruler": 15}
```

**Example Session:**
```
Item 1: pen
Item 2: book
Total: 50 baht
```

If an item is missing → skip it (do not add its price).

---

## Starter Code

```python
prices = {"pen": 10, "book": 40, "eraser": 5, "ruler": 15}
total = 0

for i in range(2):
    item = input(f"Item {i+1}: ")
    # Write your code here

print(f"Total: {total} baht")
```
