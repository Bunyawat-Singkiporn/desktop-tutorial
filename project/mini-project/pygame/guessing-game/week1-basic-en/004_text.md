## Goal

Display text on the screen.

---

## Concept

A **variable** stores the message to display:

```python
message = "Guess Number 1-5"   # str = text
```

When `message` changes, the text on screen updates automatically.

Displaying text in pygame takes 3 steps:

```text
1. Create a font   →  pygame.font.Font(None, 48)
2. Render text     →  font.render(message, True, "black")
3. Place on screen →  screen.blit(text, (x, y))
```

---

## Code Explained

| Line | Meaning |
|------|---------|
| `pygame.font.Font(None, 48)` | Create a font, size 48 |
| `font.render(message, True, "black")` | Turn text into an image, black color |
| `screen.blit(text, (180, 250))` | Place it at position x=180, y=250 |

Position (x, y) on screen:

```text
(0,0) ──────────────→ x
  │
  │    (180, 250) ← text goes here
  ↓
  y
```

---

## 📝 Add to game.py

**1.** Add **after** `pygame.display.set_caption(...)`:

```python
font = pygame.font.Font(None, 48)
message = "Guess Number 1-5"
```

**2.** Add **before** `pygame.display.flip()` inside the game loop:

```python
    text = font.render(message, True, "black")
    screen.blit(text, (180, 250))
```

> Run it — you should see "Guess Number 1-5" in the middle of the screen.
