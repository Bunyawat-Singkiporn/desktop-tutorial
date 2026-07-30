# ✏️ Dictionary Methods — Working with Dictionaries

---

## Change a Value

```python
student = {"name": "Alice", "age": 15}
student["age"] = 16           # change an existing value
print(student["age"])         # 16
```

---

## .update() — Update Several Values at Once

```python
student = {"name": "Alice", "age": 15}
student.update({"age": 16, "score": 90})
print(student)
# {'name': 'Alice', 'age': 16, 'score': 90}
```

---

## del — Delete a Key

```python
student = {"name": "Alice", "age": 15, "score": 90}
del student["score"]
print(student)
# {'name': 'Alice', 'age': 15}
```

---

## .values() — Get All Values

```python
student = {"name": "Alice", "age": 15, "score": 90}

for value in student.values():
    print(value)
```

**Output:**
```
Alice
15
90
```

---

## .items() — Get Keys and Values Together

```python
student = {"name": "Alice", "age": 15}

for key, value in student.items():
    print(f"{key}: {value}")
```

**Output:**
```
name: Alice
age: 15
```

---

## Methods Summary

| Method | Purpose |
|--------|---------|
| `dict["key"] = x` | Change / add |
| `.update({...})` | Update several values |
| `del dict["key"]` | Delete a key |
| `.values()` | Get all values |
| `.items()` | Get key-value pairs |
