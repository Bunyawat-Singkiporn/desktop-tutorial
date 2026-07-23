## Goal

Add a score that increases on a correct guess + display it on screen.

---

## Concept

The `score` variable stores the current score, starting at 0:

```python
score = 0      # int, starts at 0
score += 1     # add 1 each time
```

`score += 1` is short for `score = score + 1`
(the `+=` operator from Python basics)

**f-string** puts a variable's value inside a string:

```python
f"Score: {score}"    # if score = 2 → "Score: 2"
```

`{score}` inserts the variable's value directly into the text.

---

## Code Explained

| Line | Meaning |
|------|---------|
| `score = 0` | Set starting score |
| `score += 1` | Add 1 to the current score |
| `f"Score: {score}"` | Show the score number in the text |
| `screen.blit(score_text, (20, 20))` | Place score in the top-left corner |

---

## 📝 Add to game.py

**1.** Add **after** `secret_number = 3`:

```python
score = 0
```

**2.** Add inside `if guess == secret_number:`, **after** `message = "Correct!"`:

```python
                    score += 1
```

**3.** Add **before** `pygame.display.flip()`:

```python
    score_text = font.render(f"Score: {score}", True, "blue")
    screen.blit(score_text, (20, 20))
```

> Run it — guess correctly and the score goes up! 🎉

---

## Check Your Answer

Open `game.py` in this folder and compare with yours.
