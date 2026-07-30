# 🤔 Choosing the Right Data Type

---

## Comparison Table

| Feature | List `[]` | Tuple `()` | Set `{}` |
|----------|-----------|------------|----------|
| Mutable | ✅ | ❌ | ✅ |
| Ordered | ✅ | ✅ | ❌ |
| Allows duplicates | ✅ | ✅ | ❌ |
| Supports indexing | ✅ | ✅ | ❌ |

---

## Questions to help you decide

```
1. Do you need to add or remove items?
   ❌ No → Tuple
   ✅ Yes → Go to question 2

2. Do you want unique values?
   ✅ Yes → Set
   ❌ No → List
```

---

## Selection Examples

| Situation | Use | Reason |
|----------|-----|--------|
| Student roster (items can be added or removed) | `list` | Mutable and ordered |
| Days of the week (fixed) | `tuple` | Immutable, preventing accidental changes |
| Unique names | `set` | Stores unique values |
| Coordinates (x, y) | `tuple` | Fixed and ordered |

---

## Code example

```python
# List — mutable
shopping = ["milk", "eggs", "bread"]
shopping.append("butter")

# Tuple — fixed
weekdays = ("Mon", "Tue", "Wed", "Thu", "Fri")

# Set — unique values
visitors = {"Alice", "Bob", "Alice"}  # → {'Alice', 'Bob'}
```

---

## Key Points

- If you are unsure, start with a **list**.
- If the data must not change, use a **tuple**.
- If every value must be unique, use a **set**.
