# 🤝 Practice Review Dictionaries — Question 3: Merge Dicts

**Difficulty:** 🟡 Medium

---

## Problem

Merge two dictionaries. If a key appears in both, use the value from `extra`.

```python
base = {"name": "Alice", "age": 15}
extra = {"score": 90, "age": 16}
```

**Output:**
```
{'name': 'Alice', 'age': 16, 'score': 90}
```

---

## 💡 Hint

Use `.update(extra)` to merge them. A value from `extra` replaces the existing value when a key appears in both dictionaries.

---

## Starter Code

```python
base = {"name": "Alice", "age": 15}
extra = {"score": 90, "age": 16}

# Merge extra into base

print(base)
```
