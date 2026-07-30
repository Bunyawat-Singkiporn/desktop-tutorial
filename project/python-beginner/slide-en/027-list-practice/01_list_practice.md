# 📝 List Practice — Practice using Lists.

---

## Review the list you learned.

|Skills|example|
|-------|---------|
|Create a list| `items = ["a", "b", "c"]` |
|Access with index| `items[0]`, `items[-1]` |
|Loop| `for item in items:` |
|Add information| `items.append("d")` |
|Delete data| `items.remove("b")` |
|Sort data| `items.sort()` |

---

## Common patterns

**Filter (Filter) — Select only those that meet the conditions:**
```python
numbers = [3, 15, 7, 22, 8, 30]
big = []

for n in numbers:
    if n > 10:
        big.append(n)

print(big)  # [15, 22, 30]
```

**Count (Count) — Count the numbers that meet the conditions:**
```python
scores = [85, 45, 92, 38, 77, 61]
passed = 0

for score in scores:
    if score >= 50:
        passed += 1

print("Passed:", passed)
```

---

## Example program — To-Do list

```python
todos = ["Buy food", "Do homework", "Clean room"]

print("=== My To-Do List ===")
for i in range(len(todos)):
    print(i + 1, ".", todos[i])
```

**Output:**
```
=== My To-Do List ===
1 . Buy food
2 . Do homework
3 . Clean room
```

---

## Order of working with Lists

```
1. Create a list
2. Add/edit information
3. Process with loop
4. Show results
```
