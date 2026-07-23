## Goal

Detect which key the player pressed (1-5).

---

## Concept

Use `if` to check conditions — same as in Python basics:

```python
if event.type == pygame.KEYDOWN:    # a key was pressed
    if event.key == pygame.K_1:     # was it the 1 key?
        message = "You pressed 1"   # update the message
```

Use `elif` to check each key one by one:

```python
if event.key == pygame.K_1:
    ...
elif event.key == pygame.K_2:
    ...
```

---

## Input → Process → Output

```text
Input:   player presses 1
              ↓
Process: if event.key == pygame.K_1
              ↓
Output:  message = "You pressed 1"
```

---

## Code Explained

| Line | Meaning |
|------|---------|
| `pygame.KEYDOWN` | A key was pressed |
| `pygame.K_1` | The number 1 key |
| `pygame.K_2` ... `pygame.K_5` | Number keys 2-5 |
| `message = "..."` | Update the text shown on screen |

---

## 📝 Add to game.py

Add inside the `for event` loop, **after** `pygame.QUIT`:

```python
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                message = "You pressed 1"
            elif event.key == pygame.K_2:
                message = "You pressed 2"
            elif event.key == pygame.K_3:
                message = "You pressed 3"
            elif event.key == pygame.K_4:
                message = "You pressed 4"
            elif event.key == pygame.K_5:
                message = "You pressed 5"
```

> Run it — press 1-5 and the message should change each time.
