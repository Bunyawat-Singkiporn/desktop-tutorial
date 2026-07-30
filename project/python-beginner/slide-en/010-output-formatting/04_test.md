# 📊 Practice: Output Formatting — Question 3: Score Report

**Difficulty:** 🟡 Medium

---

## Problem

Get a name and 3 subject scores, then display a grade report with the average.

**Input:**
```
Sam
80
90
70
```

**Output:**
```
=== Score Report ===
Name: Sam
Math: 80
English: 90
Science: 70
Average: 80.00
```

---

## 💡 Hint

- Average = (total scores) / 3
- Use `{average:.2f}` to show 2 decimal places

---

## Starter Code

```python
name = input()
math = int(input())
english = int(input())
science = int(input())

average = (math + english + science) / 3

# Print report using f-string
```
