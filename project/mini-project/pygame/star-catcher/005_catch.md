# ✅ จับดาว + ชีวิต

## เป้าหมาย
เช็คว่าตะกร้ารับดาวได้ไหม → คะแนน + ชีวิต + Game Over

## แนวคิด — เช็คการจับ

ตะกร้ารับดาวได้เมื่อ **เงื่อนไข 2 ข้อ** เป็นจริงพร้อมกัน:

1. ดาวตกถึงระดับตะกร้า → `star_y > 530`
2. ดาวอยู่ในช่วงความกว้างตะกร้า → `abs(star_x - basket_x) < 50`

```python
if star_y > 530 and abs(star_x - basket_x) < 50:
    score += 1   # จับได้!
```

## ภาพประกอบ

```
basket_x - 50             basket_x + 50
      │                         │
      ▼                         ▼
──────┼─────────────────────────┼──────
      │    ⭐ อยู่ในช่วงนี้     │    ← จับได้ (star_y > 530)
──────┼─────────────────────────┼──────
      │       ตะกร้า 80px       │
      └─────────────────────────┘
```

## แนวคิด — Lives

| โค้ด | ทำอะไร |
|------|--------|
| `lives = 3` | เริ่มต้น 3 ชีวิต |
| `abs(a - b)` | ค่าสัมบูรณ์ — ระยะห่างเสมอ ≥ 0 |
| `lives -= 1` | ชีวิตลด 1 |
| `if lives <= 0:` | ถ้าชีวิตหมด → Game Over |

## 📝 เพิ่มโค้ดนี้

```python
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Star Catcher")
clock = pygame.time.Clock()
font  = pygame.font.SysFont(None, 36)

basket_x     = 400
basket_y     = 550
basket_speed = 6

star_x     = random.randint(20, 780)
star_y     = -20
star_speed = 4

score = 0   # ← เพิ่ม
lives = 3   # ← เพิ่ม

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

    star_y += star_speed

    # จับได้! ← เพิ่ม
    if star_y > 530 and abs(star_x - basket_x) < 50:
        score += 1
        star_x = random.randint(20, 780)
        star_y = -20
    # พลาด! ← เพิ่ม
    elif star_y > 620:
        lives -= 1
        star_x = random.randint(20, 780)
        star_y = -20

    if lives <= 0:
        running = False

    screen.fill("navy")
    pygame.draw.rect(screen, "brown", (basket_x - 40, basket_y, 80, 20))
    pygame.draw.circle(screen, "yellow", (star_x, star_y), 12)

    # HUD ← เพิ่ม
    score_text = font.render(f"Score: {score}", True, "white")
    lives_text = font.render(f"Lives: {lives}", True, "red")
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 50))

    pygame.display.flip()
    clock.tick(60)

# Game Over Screen
screen.fill("navy")
over_text  = font.render(f"Game Over!  Score: {score}", True, "yellow")
screen.blit(over_text, (200, 280))
pygame.display.flip()
pygame.time.wait(3000)

pygame.quit()
```

> รันดู — พยายามรับดาว ถ้าพลาด 3 ครั้ง Game Over! 🎮
