# 🧾 Practice: Type Conversion — Question 3: Fix the TypeError

**Difficulty:** 🟡 Medium

---

## Problem

The code below has a TypeError — **fix it so it runs** without changing the Output.

```python
student_name = input()
score = input()
passed_score = 50

print("Name: " + student_name)
print("Score: " + score)
print("Pass score: " + passed_score)
```

**Input:**
```
Emma
75
```

**Output:**
```
Name: Emma
Score: 75
Pass score: 50
```

---

## 💡 Hint

You cannot join `str` and `int` with `+` — convert the `int` to `str` first

---

## Starter Code

```python
student_name = input()
score = input()
passed_score = 50

print("Name: " + student_name)
print("Score: " + score)
print("Pass score: " + passed_score)  # ← Error is here!
```
