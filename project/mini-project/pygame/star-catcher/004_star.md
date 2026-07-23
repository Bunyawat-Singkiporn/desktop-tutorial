# ⭐ ดาวตกลงมา

## เป้าหมาย
วาดดาวที่ตกลงมาจากด้านบนทุก frame

## แนวคิด — ทำให้ดาวตก

ทุก frame เพิ่ม `star_y` ขึ้น → ดาวเลื่อนลงมาเรื่อยๆ

```python
star_y += star_speed   # เพิ่มทุก frame = ดาวตกลง
```

| โค้ด | ทำอะไร |
|------|--------|
| `star_x = random.randint(20, 780)` | สุ่มตำแหน่ง x |
| `star_y = -20` | เริ่มเหนือหน้าจอ (ยังมองไม่เห็น) |
| `star_speed = 4` | ความเร็วตก (pixel ต่อ frame) |
| `star_y += star_speed` | ตกลงมาทุก frame |
| `pygame.draw.circle(screen, "yellow", (star_x, star_y), 12)` | วาดดาว |

## ดาวตกอย่างไร

```
star_y = -20   ← เริ่มต้น (เหนือหน้าจอ)
     ↓  += 4 ทุก frame
star_y = 100
     ↓
star_y = 300
     ↓
star_y = 600   ← ออกนอกหน้าจอ → เริ่มใหม่
```

## 📝 เพิ่มโค้ดนี้

```python
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Star Catcher")
clock = pygame.time.Clock()

basket_x     = 400
basket_y     = 550
basket_speed = 6

# ดาว
star_x     = random.randint(20, 780)
star_y     = -20
star_speed = 4

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 40:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < 760:
        basket_x += basket_speed

    # ดาวตก
    star_y += star_speed

    # ถ้าออกนอกหน้าจอ → เริ่มใหม่
    if star_y > 620:
        star_x = random.randint(20, 780)
        star_y = -20

    screen.fill("navy")
    pygame.draw.rect(screen, "brown", (basket_x - 40, basket_y, 80, 20))
    pygame.draw.circle(screen, "yellow", (star_x, star_y), 12)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

> รันดู — เห็นดาวตกลงมาทุก frame ⭐
> ดาวเกิดใหม่ทุกครั้งที่ตกพ้นหน้าจอ
