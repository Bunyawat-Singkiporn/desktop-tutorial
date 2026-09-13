# 🔥 Practice Function — Challenge: Mini Quiz

**Difficulty:** 🔴 Hard

---

## Task

Build a short quiz with functions:

| Function | Job |
|----------|-----|
| `ask(question, answer)` | ask question, read `input` — return `True` if correct else `False` |
| `show_result(score, total)` | print score and a message |

`show_result` rules:
- full score → `Perfect!`
- >= half → `Good job!`
- otherwise → `Keep practicing!`

Ask **3 questions** and track score.

> Combines: function + return + input + if + score += 1

---

## Example Session

```
What is 2 + 2? 4
Correct!
Capital of Thailand? Bangkok
Correct!
Color of the sky? green
Wrong!
Score: 2/3
Good job!
```

---

## Starter Code

```python
def ask(question, answer):
    # Write your code here

def show_result(score, total):
    # Write your code here

score = 0
total = 3

if ask("What is 2 + 2? ", "4"):
    print("Correct!")
    score += 1
else:
    print("Wrong!")

if ask("Capital of Thailand? ", "Bangkok"):
    print("Correct!")
    score += 1
else:
    print("Wrong!")

if ask("Color of the sky? ", "blue"):
    print("Correct!")
    score += 1
else:
    print("Wrong!")

show_result(score, total)
```
