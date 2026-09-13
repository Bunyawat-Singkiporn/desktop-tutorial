# 🧩 Function Practice

---

## Review of Functions

| Skill | Example |
|-------|---------|
| Define a function | `def greet():` |
| Use a parameter | `def greet(name):` |
| Return a value | `return result` |
| Call a function | `greet("Alice")` |

---

## Combining a Function with a List

```python
def get_total(scores):
    total = 0
    for score in scores:
        total += score
    return total

my_scores = [80, 75, 90, 65, 88]
print("Total:", get_total(my_scores))
```

---

## Combining a Function with a Dictionary

```python
def show_student(student):
    for key, value in student.items():
        print(f"{key}: {value}")

alice = {"name": "Alice", "score": 92}
show_student(alice)
```

---

## Combining Multiple Functions

```python
def get_average(scores):
    return sum(scores) / len(scores)

def get_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    else:
        return "C"

scores = [85, 90, 78]
avg = get_average(scores)
grade = get_grade(avg)
print(f"Average: {avg:.1f}, Grade: {grade}")
```

---

## What Makes a Good Function?

- It does one thing (single responsibility).
- It has a meaningful name.
- It is no longer than 10–15 lines.

---

## Combining Functions with Input

```python
def get_grade(score):
    if score >= 80:
        return "A"
    elif score >= 60:
        return "B"
    else:
        return "F"

score = int(input("Enter score: "))
print("Grade:", get_grade(score))
```

Read from the user → pass into a function → get a result back.

Also combine with what you already know: `input`, `if`, `for`, `list`, `dict`.
