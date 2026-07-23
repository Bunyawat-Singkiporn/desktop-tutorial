## Goal

Create the game window.

---

## Concept

Every pygame game has the same structure:

```text
import pygame        ← load pygame
pygame.init()        ← start the system
screen = ...         ← create the window
while running:       ← game runs forever
```

`while running:` = **while loop** — repeats as long as `running` is `True`.

---

## Code Explained

| Line | Meaning |
|------|---------|
| `set_mode((800, 600))` | Window width 800, height 600 |
| `set_caption("Guess The Number")` | Title shown at the top |
| `running = True` | **Variable** — game is still running |
| `while running:` | Loop until the game closes |
| `event.get()` | Check what the player is doing |
| `pygame.QUIT` | Player clicked the close button → `running = False` |
| `screen.fill("white")` | Paint the background white |
| `display.flip()` | Update the screen (required every frame!) |

---

## Result

A white window titled "Guess The Number".

---

## 📝 Type in game.py (whole file)

```python
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Guess The Number")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    pygame.display.flip()

pygame.quit()
```

> Run it — you should see a white window titled "Guess The Number".
