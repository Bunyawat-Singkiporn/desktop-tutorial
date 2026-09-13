# Practice Dictionary — Question 23: Highest Score

**Difficulty:** 🟡 Medium

---

## Task

Find who has the highest score in class.

```python
scores = {"Alice": 85, "Bob": 92, "Cara": 78}
```

**Output:**
```
Top: Bob (92)
```

---

## 💡 Hint

Loop and keep the top name and top score in variables.

---

## Starter Code

```python
scores = {"Alice": 85, "Bob": 92, "Cara": 78}

top_name = ""
top_score = -1

for name, score in scores.items():
    # Write your code here

print(f"Top: {top_name} ({top_score})")
```
