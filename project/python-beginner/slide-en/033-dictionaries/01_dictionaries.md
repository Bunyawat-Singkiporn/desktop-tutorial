# 📖 Dictionaries — Key-Value Data

---

## What is a Dictionary?

A dictionary stores data in **key-value pairs** (key → value), much like a real dictionary pairs words with definitions.

```python
student = {
    "name": "Alice",
    "age": 15,
    "score": 92
}
```

---

## Creating a Dictionary

```python
contact = {
    "name": "Bob",
    "phone": "081-234-5678",
    "city": "Bangkok"
}
```

---

## Accessing Values

```python
student = {"name": "Alice", "age": 15}

print(student["name"])  # Alice
print(student["age"])   # 15
```

---

## Adding a New Key

```python
student = {"name": "Alice", "age": 15}
student["score"] = 92
print(student)
# {'name': 'Alice', 'age': 15, 'score': 92}
```

---

## Checking Whether a Key Exists

```python
if "name" in student:
    print("Found:", student["name"])
```

---

## Loop

```python
student = {"name": "Alice", "age": 15, "score": 92}

for key in student:
    print(key, ":", student[key])
```

**Output:**
```
name : Alice
age : 15
score : 92
```

---

## Example Program — Contact Information

```python
contact = {
    "name": "Charlie",
    "phone": "089-111-2222"
}

print("Name:", contact["name"])
print("Phone:", contact["phone"])
```
