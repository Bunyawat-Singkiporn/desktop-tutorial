# 🔄 Dictionary Review

---

## Common Dictionary Operations

```python
# Create
student = {"name": "Alice", "age": 15, "score": 90}

# Access a value
print(student["name"])        # Alice

# Add or edit
student["grade"] = "A"        # Add a new key
student["age"] = 16           # Change an existing value

# Update multiple values
student.update({"score": 95, "age": 17})

# Delete
del student["grade"]

# Loop through all key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")
```

---

## Check before accessing

```python
# Recommended: always check first
if "score" in student:
    print(student["score"])
else:
    print("No score yet")
```

---

## Combining a Dictionary with a Loop

```python
scores = {"Alice": 88, "Bob": 72, "Charlie": 95}
highest = ""
max_score = 0

for name, score in scores.items():
    if score > max_score:
        max_score = score
        highest = name

print(f"Top: {highest} ({max_score})")
```

---

## Review Checklist

- [ ] Create a dictionary
- [ ] Access a value by its key
- [ ] Add, edit, and delete keys
- [ ] Use `.update()`
- [ ] Loop through key-value pairs with `.items()`
- [ ] Check for a key with `in`
