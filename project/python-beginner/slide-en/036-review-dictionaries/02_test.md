# 🐛 Practice Review Dictionaries — Question 1: Fix Access Bug

**Difficulty:** 🟢 Easy

---

## Problem

The code below contains bugs. Fix it so that it produces the correct output.

```python
# Code with bugs
student = {"name": "Alice", "age": 15}
print(student["score"])   # KeyError!
print(student[name])      # NameError!
```

**Correct Output:**
```
Name: Alice
Age: 15
```

---

## 💡 Hint

Check whether a key exists before accessing it, and use the string `"name"` rather than the variable `name`.

---

## Starter Code

```python
student = {"name": "Alice", "age": 15}

# Fix the code
```
