# 🔥 Practice Function — Challenge: Classroom Quiz Game

**Difficulty:** 🔴 Hard

---

## Task

Make a short classroom quiz game.

| Function | Job |
|----------|-----|
| `ask(question, answer)` | ask and return True if correct |
| `show_result(score, total)` | print score + message |

Messages: Perfect! / Good job! / Keep practicing!

Ask 3 questions and keep score.

---

## Example Session

```
What is 2 + 2? 4
Correct!
Capital of Thailand? Bangkok
Correct!
Color of the sky? green
Wrong!
=== Result ===
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

print("=== Result ===")
show_result(score, total)
```
