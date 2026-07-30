# ❓ Practice Dictionary — Question 2: Quiz Checker

**Difficulty:** 🟡 Medium

---

## Problem

Given answer keys for 3 questions, read the user's answers and show the score.

```python
answers = {"q1": "A", "q2": "C", "q3": "B"}
```

**Sample Session:**
```
q1: A
q2: B
q3: B
Score: 2/3
```

---

## 💡 Hint

Loop through `answers.items()`, read input for each question, and count matches

---

## Starter Code

```python
answers = {"q1": "A", "q2": "C", "q3": "B"}
score = 0

for question, correct in answers.items():
    user = input(f"{question}: ")
    # Write your code here

print(f"Score: {score}/3")
```
