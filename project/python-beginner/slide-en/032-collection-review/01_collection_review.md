# 🗂️ Collection Review

---

## All Three Types in One Place

```python
# List — ordered, mutable, allows duplicates
students = ["Alice", "Bob", "Charlie", "Alice"]

# Tuple — ordered and immutable
days = ("Mon", "Tue", "Wed", "Thu", "Fri")

# Set — unordered, mutable, unique values
unique_students = {"Alice", "Bob", "Charlie"}
```

---

## Accessing Items

```python
# Lists and tuples support indexing.
print(students[0])  # Alice
print(days[0])      # Mon

# Sets do not support indexing — use a loop.
for s in unique_students:
    print(s)
```

---

## Tuple Immutability

```python
days = ("Mon", "Tue", "Wed")

# ✅ Valid operations
print(days[0])       # Read an item
for d in days:       # Loop through the tuple
    print(d)

# ❌ Invalid operations
days[0] = "Sunday"   # TypeError!
days.append("Sat")   # AttributeError!
```

---

## Example Program Using All Three Types

```python
# Student data
all_students = ["Alice", "Bob", "Alice", "Charlie"]
unique = set(all_students)           # Remove duplicates
grade_info = ("Grade 9", "Room 3")  # Fixed data

print("Total entries:", len(all_students))
print("Unique students:", len(unique))
print("Class:", grade_info[0], grade_info[1])
```

---

## Comparison Summary

| | List | Tuple | Set |
|-|------|-------|-----|
| Create | `[1,2]` | `(1,2)` | `{1,2}` |
| Index | ✅ | ✅ | ❌ |
| Add | `.append()` | ❌ | `.add()` |
| Remove | `.remove()` | ❌ | `.remove()` |
| Duplicates | ✅ | ✅ | ❌ |
