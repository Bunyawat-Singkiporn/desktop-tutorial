# 🪟 สร้างหน้าต่างเกม

## เป้าหมาย
สร้างหน้าต่าง pygame พื้นหลังสีขาว

## 📝 พิมพ์โค้ดนี้

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Click the Dot")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

> รันดู — เห็นหน้าต่างสีขาว 🟩
