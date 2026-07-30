# 🔲 Nested Loops — Loops Inside Loops

---

## What is a Nested Loop?

A **nested loop** is a loop inside another loop.

```python
for i in range(3):        # Outer loop — runs 3 times
    for j in range(3):    # Inner loop — runs 3 times each time
        print(i, j)
```

Output:
```
0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2
```

> The inner loop **finishes all its iterations** before the outer loop moves to its next iteration.

---

## Total Number of Iterations

```
3 outer iterations × 4 inner iterations = 12 iterations in total
```

```python
for row in range(3):
    for col in range(4):
        print("*", end="")
    print()    # new line
```

Output:
```
****
****
****
```

---

## Example: Triangle Pattern

```python
for row in range(1, 6):
    for col in range(row):
        print("*", end="")
    print()
```

Output:
```
*
**
***
****
*****
```

> `range(row)` makes the inner loop run once for each value in the current row.

---

## Example: Multiplication Table

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end="\t")
    print()
```

Output:
```
1	2	3	
2	4	6	
3	6	9	
```

---

## Summary

| Topic | Example |
|-------|---------|
| Outer loop | Runs N times |
| Inner loop | Runs M times for each outer iteration |
| Total | N × M iterations |
| `end=""` | Prints on the same line |
| Empty `print()` | Starts a new line |
