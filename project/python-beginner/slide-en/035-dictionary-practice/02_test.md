# 📊 Practice Dictionary — Question 1: Word Counter

**Difficulty:** 🟢 Easy

---

## Problem

Count how many times each word appears in the list.

```python
words = ["cat", "dog", "cat", "bird", "dog", "cat"]
```

**Output:**
```
cat: 3
dog: 2
bird: 1
```

---

## 💡 Hint

If `word` is already in the dict → add 1
If not yet → set it to 1

---

## Starter Code

```python
words = ["cat", "dog", "cat", "bird", "dog", "cat"]
count = {}

for word in words:
    # Write your code here

for word, n in count.items():
    print(f"{word}: {n}")
```
