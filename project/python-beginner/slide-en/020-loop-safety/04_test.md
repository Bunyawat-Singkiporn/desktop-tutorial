# 🔍 Practice: Loop Safety — Question 3: Find First Match

**Difficulty:** 🟡 Medium

---

## Problem

Loop through the list and stop when you find the name you want.

```python
names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
```

Get name from user Then show how many places it was found (start counting at 1)

**Input:**
```
Charlie
```

**Output:**
```
Found Charlie at position 3
```

**Input:**
```
Zara
```

**Output:**
```
Zara not found
```

---

## 💡 Hint

- Use the variable `found = False`.
- If found: Show location, `found = True`, `break`
- After loop: if `not found` shows not found

---

## Starter Code

```python
names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
target = input()

for i in range(len(names)):
    if names[i] == target:
        # Print position (i+1) and stop searching

# If never found, print "target not found"
```
