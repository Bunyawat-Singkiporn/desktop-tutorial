## เป้าหมาย

แสดงข้อความบนหน้าจอ

---

## Variable

ใช้เก็บข้อความ

```python
message = "Guess Number 1-5"
```

---

## Font

สร้างตัวอักษร

```python
font = pygame.font.Font(None, 48)
```

---

## Render Text

สร้างข้อความ

```python
text = font.render(
    message,
    True,
    "black"
)
```

---

## Show Text

แสดงข้อความ

```python
screen.blit(
    text,
    (180, 250)
)
```

---

## Update Screen

อัปเดตหน้าจอ

```python
pygame.display.flip()
```

---

## โค้ดทั้งหมด

```python
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption(
    "Guess The Number"
)

font = pygame.font.Font(None, 48)

message = "Guess Number 1-5"

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    text = font.render(
        message,
        True,
        "black"
    )

    screen.blit(
        text,
        (180, 250)
    )

    pygame.display.flip()

pygame.quit()
```