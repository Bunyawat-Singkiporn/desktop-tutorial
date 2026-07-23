# 🪟 สร้างหน้าต่างเกม

## เป้าหมาย
สร้างหน้าต่าง pygame พื้นหลังสีกรมท่าสำหรับ Star Catcher

## แนวคิด

| โค้ด | ทำอะไร |
|------|--------|
| `pygame.init()` | เปิดใช้งาน pygame |
| `pygame.display.set_mode((800, 600))` | สร้างหน้าต่าง 800×600 |
| `while running:` | game loop — วนซ้ำทุก frame |
| `screen.fill("navy")` | ทาพื้นหลังสีกรมท่า (ท้องฟ้ากลางคืน) |
| `clock.tick(60)` | จำกัดความเร็ว 60 FPS |

## 📝 พิมพ์โค้ดนี้

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Star Catcher")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("navy")
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

> รันดู — เห็นหน้าต่างสีกรมท่า 🌌
