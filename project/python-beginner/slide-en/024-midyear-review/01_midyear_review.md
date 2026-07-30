# 🏆 Mid-Year Review — Half-Year Review

---

## What You Learned Across 24 Weeks

### Months 1–3: Basics

| Week | Topic | Key Points |
|------|-------|------------|
| 1–4 | Python, Environment, Syntax, Comments | `print()`, read Errors |
| 5–8 | Variables, Naming, Data Types, Conversion | `int()`, `float()`, `str()` |
| 9–12 | Input, Formatting, Operators, Review | `input()`, f-string |

### Month 4: Conditions

| Week | Topic | Key Points |
|------|-------|------------|
| 13 | Even/Odd | `%` modulo |
| 14 | elif | multiple conditions |
| 15 | Logical Operators | `and`, `or`, `not` |
| 16 | for Loop | `range()` |

### Months 5–6: Loops

| Week | Topic | Key Points |
|------|-------|------------|
| 17–18 | for + Lists, while Loop | `for item in list`, `while` |
| 19–20 | Loop Safety, Nested | `break`, `continue`, nested |
| 21–22 | Loop Review, Debugging | all loops combined |

---

## Sample Program Combining Everything

```python
# Read name and 3 subject scores, then summarize
name = input()
scores = []

for i in range(3):
    score = int(input())
    scores.append(score)

total = 0
for s in scores:
    total = total + s

average = total / len(scores)

print(f"Name: {name}")
print(f"Average: {average:.1f}")

if average >= 80:
    print("Grade: A")
elif average >= 60:
    print("Grade: B")
else:
    print("Grade: C")
```

---

## Checklist Before Finishing Half-Year

- [ ] Comfortable with `print()` / `input()` / f-string
- [ ] Variable, Data Types, Type Conversion
- [ ] `if` / `elif` / `else` / logical operators
- [ ] `for` with range and list
- [ ] `while`, `break`, `continue`
- [ ] Nested loops
- [ ] Basic loop debugging
