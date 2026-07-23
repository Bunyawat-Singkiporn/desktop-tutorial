## Goal

Check if the player's guess is correct.

---

## Concept

The **secret number** is stored in a variable — the player has to guess it:

```python
secret_number = 3    # int variable holding the secret
```

Compare `guess` with `secret_number` using `if / elif / else`:

```python
if guess == secret_number:     # correct guess
    message = "Correct!"
elif guess < secret_number:    # too small
    message = "Too Low!"
else:                          # too big
    message = "Too High!"
```

`==` means **compare** (different from `=` which assigns a value!):

```text
secret_number = 3    ← assign  (=)
guess == 3           ← compare (==) → True or False
```

---

## Code Explained

| Line | Meaning |
|------|---------|
| `secret_number = 3` | The hidden number |
| `guess = None` | No guess yet (None = no value) |
| `guess == secret_number` | Is the guess equal to the secret? |
| `guess < secret_number` | Is the guess less than the secret? |
| `else` | Otherwise → must be greater |
| `if guess is not None` | A key was actually pressed |

---

## 📝 Update game.py

**1.** Add **after** `message = "Guess Number 1-5"`:

```python
secret_number = 3
```

**2.** **Replace** the entire `if event.type == pygame.KEYDOWN:` block with:

```python
        if event.type == pygame.KEYDOWN:
            guess = None

            if event.key == pygame.K_1:
                guess = 1
            elif event.key == pygame.K_2:
                guess = 2
            elif event.key == pygame.K_3:
                guess = 3
            elif event.key == pygame.K_4:
                guess = 4
            elif event.key == pygame.K_5:
                guess = 5

            if guess is not None:
                if guess == secret_number:
                    message = "Correct!"
                elif guess < secret_number:
                    message = "Too Low!"
                else:
                    message = "Too High!"
```

> Run it — press 3 → "Correct!", press 1 → "Too Low!", press 5 → "Too High!"

---

## Bonus — Random Secret Number

Right now the secret number is always `3`. You can make it random:

**1.** Add at the very top of the file (next to `import pygame`):

```python
import random
```

**2.** Change `secret_number = 3` to:

```python
secret_number = random.randint(1, 5)
```

`random.randint(1, 5)` picks a random whole number between 1 and 5 — different every time you run the game!
