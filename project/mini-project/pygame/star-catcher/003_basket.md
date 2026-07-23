# 🧺 ตะกร้าผู้เล่น

## เป้าหมาย
วาดตะกร้าที่ด้านล่างหน้าจอ และเลื่อนซ้าย-ขวาด้วยลูกศร

## แนวคิด

ตะกร้าคือ **สี่เหลี่ยมสีน้ำตาล** ที่ด้านล่างหน้าจอ
เลื่อนได้แค่ **ซ้าย-ขวา** เท่านั้น (ไม่ต้องขึ้น-ลง)

```python
basket_x = 400   # กลางหน้าจอแนวนอน
basket_y = 550   # ใกล้ด้านล่าง
```

| โค้ด | ทำอะไร |
|------|--------|
| `pygame.draw.rect(screen, "brown", (x-40, y, 80, 20))` | วาดตะกร้ากว้าง 80 สูง 20 |
| `keys[pygame.K_LEFT]` | เช็คปุ่มลูกศรซ้าย |
| `basket_x -= 6` | เลื่อนซ้าย 6 pixel |
| `basket_x > 40` | ไม่ให้ออกนอกหน้าจอซ้าย |
| `basket_x < 760` | ไม่ให้ออกนอกหน้าจอขวา |

## ตะกร้ากว้าง 80 pixel

```
basket_x - 40          basket_x + 40
      │                      │
      ▼                      ▼
      ┌──────────────────────┐
      │    ตะกร้า (80px)     │
      └──────────────────────┘
              ↑
          basket_x (จุดกลาง)
```

## 📝 พิมพ์โค้ดนี้

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Star Catcher")
clock = pygame.time.Clock()

# ตะกร้า
basket_x     = 400
basket_y     = 550
basket_speed = 6

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # เลื่อนซ้าย-ขวา
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 40:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < 760:
        basket_x += basket_speed

    screen.fill("navy")
    pygame.draw.rect(screen, "brown", (basket_x - 40, basket_y, 80, 20))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

> รันดู — ตะกร้าเลื่อนซ้าย-ขวาได้! 🎮
