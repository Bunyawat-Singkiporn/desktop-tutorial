## เป้าหมาย

สร้างหน้าต่างเกมแรกด้วย Pygame

---

## import pygame

ใช้สำหรับนำ Pygame มาใช้งาน

### ตัวอย่าง

```python
import pygame
```

---

## pygame.init()

ใช้สำหรับเริ่มต้นการทำงานของ Pygame

### ตัวอย่าง

```python
pygame.init()
```

---

## สร้างหน้าต่างเกม

### ตัวอย่าง

```python
screen = pygame.display.set_mode((800, 600))
```

800 = ความกว้าง

600 = ความสูง

---

## ตั้งชื่อเกม

```python
pygame.display.set_caption("Guess The Number")
```

---

## Game Loop

เกมต้องทำงานตลอดเวลา

```python
running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
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

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

pygame.quit()
```