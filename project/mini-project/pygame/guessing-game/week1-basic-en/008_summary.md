# Summary — Guessing Game Week 1

---

## What the Game Can Do

✅ Game window
✅ Display text on screen
✅ Accept key presses 1-5
✅ Check the answer (Correct / Too Low / Too High)
✅ Keep score

---

## Flowchart → Code

| Flowchart | Code |
|-----------|------|
| ▭ `secret_number = 3` | `secret_number = 3` |
| ▭ `score = 0` | `score = 0` |
| ▭ Player presses a key | `if event.type == KEYDOWN` |
| ◇ `guess == secret?` | `if guess == secret_number:` |
| ▭ `"Correct!" + score += 1` | `message = "Correct!"` / `score += 1` |
| ◇ `guess < secret?` | `elif guess < secret_number:` |
| ▭ `"Too Low!"` | `message = "Too Low!"` |
| ▭ `"Too High!"` | `else: message = "Too High!"` |

---

## Python Used in This Game

| Python (from Python basics) | Used in the game |
|-----------------------------|-----------------|
| `variable = value` | `secret_number = 3`, `score = 0` |
| `if / elif / else` | Check the guess |
| `==` `<` (comparison operators) | Compare numbers |
| `+=` (assignment operator) | `score += 1` |
| `f"Score: {score}"` (f-string) | Display the score |

---

## Steps We Followed (How to Build Any Game)

```text
1. Draw a Flowchart first
2. Create the window
3. Display text
4. Accept input (key press)
5. Process (if / elif / else)
6. Output (score, message)
```

---

> Every new game → start with a Flowchart.
