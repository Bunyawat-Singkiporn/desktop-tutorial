# 🧍 ผู้เล่น

## เป้าหมาย
วาดผู้เล่นและเดินได้ด้วยปุ่มลูกศร 4 ทิศทาง

## แนวคิด — ตำแหน่ง (x, y)

ผู้เล่นคือ **สี่เหลี่ยม** ที่มีตำแหน่ง x, y

```python
player_x = 400   # กลางหน้าจอแนวนอน
player_y = 300   # กลางหน้าจอแนวตั้ง
```

| โค้ด | ทำอะไร |
|------|--------|
| `player_x = 400` | เริ่มกลางหน้าจอ |
| `pygame.draw.rect(screen, "blue", (x-15, y-15, 30, 30))` | วาดสี่เหลี่ยม 30×30 จากมุมซ้ายบน |
| `keys = pygame.key.get_pressed()` | เช็คว่ากดปุ่มอะไรอยู่ |
| `if keys[pygame.K_LEFT]:` | ถ้ากดลูกศรซ้าย |
| `player_x -= 5` | เลื่อนซ้าย 5 pixel |

## การเคลื่อนที่ 4 ทิศ

```
              ↑ K_UP
              │  player_y -= 5
              │
K_LEFT ──── 🔵 ──── K_RIGHT
player_x -= 5    player_x += 5
              │
              │  player_y += 5
              ↓ K_DOWN
```

## 📝 พิมพ์โค้ดนี้

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fruit Collector")
clock = pygame.time.Clock()

# ผู้เล่น
player_x = 400
player_y = 300
player_speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # เคลื่อนที่ด้วยลูกศร
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
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

> รันดู — กดลูกศรเดินได้ 4 ทิศ 🎮

## โบนัส
ลองเพิ่มเงื่อนไขไม่ให้ออกนอกหน้าจอ:
```python
if player_x < 15:
    player_x = 15
if player_x > 785:
    player_x = 785
```
