# 🍎 ผลไม้

## เป้าหมาย
วาดผลไม้ 1 ลูกที่ตำแหน่งสุ่มบนหน้าจอ

## แนวคิด — random

`random.randint(a, b)` คือการสุ่มเลขจำนวนเต็มระหว่าง a ถึง b

```python
import random

fruit_x = random.randint(50, 750)   # x สุ่มระหว่าง 50–750
fruit_y = random.randint(50, 550)   # y สุ่มระหว่าง 50–550
```

| โค้ด | ทำอะไร |
|------|--------|
| `import random` | โหลด module random |
| `random.randint(50, 750)` | สุ่มเลขจาก 50 ถึง 750 |
| `pygame.draw.circle(screen, "red", (fx, fy), 15)` | วาดวงกลมรัศมี 15 pixel |

## ทำไมสุ่มแค่ 50 ถึง 750?

```
0   50                           750  800
│   │                             │   │
│   └─── สุ่มผลไม้ในช่วงนี้ ────┘   │
│                                     │
└── เว้นขอบซ้าย-ขวา 50px ────────────┘
```

## 📝 เพิ่มโค้ดนี้

```python
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fruit Collector")
clock = pygame.time.Clock()

# ผู้เล่น
player_x = 400
player_y = 300
player_speed = 5

# ผลไม้ (สุ่มตำแหน่งตอนเริ่ม)
fruit_x = random.randint(50, 750)
fruit_y = random.randint(50, 550)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    screen.fill("lightgreen")
    pygame.draw.rect(screen, "blue", (player_x - 15, player_y - 15, 30, 30))
    pygame.draw.circle(screen, "red", (fruit_x, fruit_y), 15)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

> รันดู — เห็นผลไม้สีแดงบนหน้าจอ 🍎
> ทุกครั้งที่รันใหม่ ผลไม้จะอยู่คนละที่!
