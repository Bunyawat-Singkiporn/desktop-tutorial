# 💰 Practice: Loop Review — Question 13: Collect Inputs

**Difficulty:** 🟡 Medium

---

## Problem

Use a while loop to get a number 5 times and display the average.

**Input:**
```
70
85
90
60
95
```

**Output:**
```
Average: 80.0
```

---

## 💡 Hint

- Use `while len(numbers) < 5:` until there are 5 numbers.
- `numbers.append(n)` stores the value
- `sum(numbers) / len(numbers)` average

---

## Starter Code

```python
numbers = []

while len(numbers) < 5:
    n = int(input())
    # Append n to numbers

print(f"Average: {sum(numbers)/len(numbers):.1f}")
```
