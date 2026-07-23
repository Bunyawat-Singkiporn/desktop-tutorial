# 🪟 สร้างหน้าต่างเกม

## เป้าหมาย
สร้างหน้าต่าง pygame พื้นหลังสีเขียวสำหรับ Fruit Collector

## แนวคิด

เริ่มต้นทุก pygame game ด้วย 4 ส่วนหลัก:

| โค้ด | ทำอะไร |
|------|--------|
| `pygame.init()` | เปิดใช้งาน pygame |
| `pygame.display.set_mode((800, 600))` | สร้างหน้าต่าง 800×600 |
| `while running:` | game loop — วนซ้ำทุก frame |
| `screen.fill("lightgreen")` | ทาพื้นหลังสีเขียว |
| `pygame.display.flip()` | อัปเดตหน้าจอ |
| `clock.tick(60)` | จำกัด 60 FPS |

## แกน X, Y

```
(0,0) ────────────────── (800,0)
  │                           │
  │      หน้าจอ 800×600       │
  │      x เพิ่มไปทางขวา →   │
  │      y เพิ่มลงข้างล่าง ↓ │
  │                           │
(0,600) ──────────────── (800,600)
```

## 📝 พิมพ์โค้ดนี้

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fruit Collector")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("lightgreen")
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

> รันดู — ควรเห็นหน้าต่างพื้นหลังสีเขียว 🟩
