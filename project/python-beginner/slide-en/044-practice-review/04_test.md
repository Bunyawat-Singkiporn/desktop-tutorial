# 🔄 Practice Review — Question 3: Input → Store → Display

**Difficulty:** 🟡 Medium

---

## Problem

Create a program that reads the names and scores of three students, stores them in a list, and displays a summary.

**Example Session:**
```
Name: Alice
Score: 85
Name: Bob
Score: 72
Name: Charlie
Score: 90
=== Results ===
Alice: 85
Bob: 72
Charlie: 90
Average: 82.3
```

---

## Starter Code

```python
records = []

for i in range(3):
    name = input("Name: ")
    score = int(input("Score: "))
    records.append((name, score))

print("=== Results ===")
# Display every student
# Calculate and display the average
```
