# ✅ เก็บผลไม้ได้!

## เป้าหมาย
เช็คว่าผู้เล่นชนผลไม้ไหม → เก็บได้ + คะแนน + ผลไม้เกิดใหม่

## แนวคิด — Collision ด้วย Distance

วัดระยะห่างระหว่างผู้เล่นกับผลไม้ด้วย Pythagorean theorem:

```
ระยะห่าง = √( (x1 - x2)² + (y1 - y2)² )
```

ถ้าระยะห่าง **< 30** → ถือว่าชนกัน!

```python
import math
distance = math.sqrt((player_x - fruit_x)**2 + (player_y - fruit_y)**2)
if distance < 30:
    # เก็บได้!
```

## แนวคิด — Score และแสดงข้อความ

| โค้ด | ทำอะไร |
|------|--------|
| `score = 0` | เริ่มคะแนนที่ 0 |
| `score += 1` | บวกคะแนน 1 |
| `font = pygame.font.SysFont(None, 36)` | สร้าง font ขนาด 36 |
| `text = font.render(f"Score: {score}", True, "black")` | สร้าง surface ข้อความ |
| `screen.blit(text, (10, 10))` | วางข้อความที่ตำแหน่ง (10, 10) |

## 📝 เพิ่มโค้ดนี้

```python
import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fruit Collector")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

player_x = 400
player_y = 300
player_speed = 5

fruit_x = random.randint(50, 750)
fruit_y = random.randint(50, 550)

score = 0  # ← เพิ่ม

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

    # เช็คว่าเก็บผลไม้ได้ไหม ← เพิ่ม
    distance = math.sqrt((player_x - fruit_x)**2 + (player_y - fruit_y)**2)
    if distance < 30:
        score += 1
        fruit_x = random.randint(50, 750)
        fruit_y = random.randint(50, 550)

    screen.fill("lightgreen")
    pygame.draw.rect(screen, "blue", (player_x - 15, player_y - 15, 30, 30))
    pygame.draw.circle(screen, "red", (fruit_x, fruit_y), 15)

    # แสดงคะแนน ← เพิ่ม
    score_text = font.render(f"Score: {score}", True, "black")
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

> รันดู — เดินชนผลไม้แล้วคะแนนขึ้น! 🎉
> ผลไม้หายแล้วเกิดใหม่ที่ตำแหน่งสุ่ม
