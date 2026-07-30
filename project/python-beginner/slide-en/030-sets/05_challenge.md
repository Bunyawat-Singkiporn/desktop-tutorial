# 🔥 Practice Sets — Question 4: Class Roster

**Difficulty:** 🔴 Hard

---

## Problem

You are given student names from two classrooms, with some students appearing in both. Display:
1. The total number of unique students
2. The names that appear in both classrooms
3. The names that appear in only one classroom (union minus intersection)

```python
room_a = ["Alice", "Bob", "Charlie", "Diana"]
room_b = ["Bob", "Eve", "Charlie", "Frank"]
```

**Output** (order may vary):
```
Total unique students: 6
In both rooms: {'Bob', 'Charlie'}
Only in one room: {'Alice', 'Diana', 'Eve', 'Frank'}
```

---

## 💡 Hint

- Convert list to set first.
- Use `|` and `&` and `-` (difference)

---

## Starter Code

```python
room_a = ["Alice", "Bob", "Charlie", "Diana"]
room_b = ["Bob", "Eve", "Charlie", "Frank"]

set_a = set(room_a)
set_b = set(room_b)

# Write your code here
```
