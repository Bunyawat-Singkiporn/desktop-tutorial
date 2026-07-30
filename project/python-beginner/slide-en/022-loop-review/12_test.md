# 📏 Practice: Loop Review — Question 11: Longest Word

**Difficulty:** 🟡 Medium

---

## Problem

Find the longest word in the list.

```python
words = ["cat", "elephant", "dog", "butterfly", "ox"]
```

**Output:**
```
Longest: butterfly (9)
```

---

## 💡 Hint

- Starting from `longest = ""`
- If `len(w) > len(longest)` → Update `longest = w`

---

## Starter Code

```python
words = ["cat", "elephant", "dog", "butterfly", "ox"]
longest = ""

for w in words:
    # If w is longer than longest, update longest

print(f"Longest: {longest} ({len(longest)})")
```
