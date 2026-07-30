# 📊 Practice Collection Review — Question 3: List + Set Mixed

**Difficulty:** 🟡 Medium

---

## Problem

Build an attendance system. Use a list to store all check-ins, including duplicates, and a set to track the students who attended.

```python
checkins = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]
```

**Output:**
```
Total check-ins: 6
Unique students: 3
Most check-ins: Alice (3 times)
```

---

## 💡 Hint

- Use `set(checkins)` to find unique names.
- Use `.count(name)` to count the number of check-ins.

---

## Starter Code

```python
checkins = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]

total = len(checkins)
unique = set(checkins)

# Find the student with the most check-ins
```
