# 🔗 Logic Integration — Bringing All Skills Together

---

## Algorithmic Thinking

Before writing code, ask yourself:
```
1. What is the input?
2. What should the output look like?
3. What steps transform the input into the output?
4. Which tools do I need?
```

---

## Choose the Right Tool

| Situation | Use |
|-----------|-----|
| Store multiple values that can be added or removed | List |
| Store key-value pairs | Dictionary |
| Store fixed data | Tuple |
| Store unique values | Set |
| Repeat a set number of times | `for` loop |
| Repeat until a condition changes | `while` loop |
| Reuse code | Function |

---

## Problem-Solving Example

**Problem:** Read the names of five students and display the names that begin with `"A"`.

```
Input:  Five names
Output: Names that begin with A

Steps:
1. Create an empty list.
2. Use a loop to read five names.
3. Loop through the list.
4. If a name begins with "A", print it.
```

```python
names = []
for i in range(5):
    name = input(f"Enter name {i+1}: ")
    names.append(name)

for name in names:
    if name.startswith("A"):
        print(name)
```

---

## Key Principles

- Solve the problem one step at a time.
- Test the output at every step.
- Split complex code into functions.
