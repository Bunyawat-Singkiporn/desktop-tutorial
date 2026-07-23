# 🖱️ คลิกได้ + คะแนน

## เป้าหมาย
เมื่อคลิกโดนวงกลม → คะแนน +1 → วงกลมย้ายที่ใหม่

## แนวคิด — Mouse Click Event

การรับ mouse click ต่างจาก keyboard:
- **keyboard** → `pygame.key.get_pressed()` ทำในลูปหลัก
- **mouse click** → ฟังใน `event loop` เหมือน `pygame.QUIT`

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.MOUSEBUTTONDOWN:   # ← เพิ่ม
        mx, my = event.pos                     # ตำแหน่งที่คลิก
```

## แนวคิด — เช็คว่าคลิกโดนไหม

ใช้ `math.sqrt` คำนวณระยะห่าง เหมือน Fruit Collector:

```python
import math
distance = math.sqrt((mx - dot_x)**2 + (my - dot_y)**2)
if distance < 30:   # 30 = รัศมีวงกลม
    # โดน!
```

| โค้ด | ทำอะไร |
|------|--------|
| `pygame.MOUSEBUTTONDOWN` | event เมื่อกดเมาส์ |
| `event.pos` | tuple (x, y) ของเมาส์ตอนคลิก |
| `mx, my = event.pos` | แยก x, y ออกมา |
| `distance < 30` | ถ้าคลิกอยู่ในรัศมีวงกลม |

## 📝 เพิ่มโค้ดนี้

```python
import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Click the Dot")
clock = pygame.time.Clock()
font  = pygame.font.SysFont(None, 36)

dot_x = random.randint(50, 750)
dot_y = random.randint(50, 550)
score = 0   # ← เพิ่ม

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:   # ← เพิ่ม
            mx, my = event.pos
            distance = math.sqrt((mx - dot_x)**2 + (my - dot_y)**2)
            if distance < 30:
                score += 1
                dot_x = random.randint(50, 750)
                dot_y = random.randint(50, 550)

    screen.fill("white")
    pygame.draw.circle(screen, "red", (dot_x, dot_y), 30)

    score_text = font.render(f"Score: {score}", True, "black")   # ← เพิ่ม
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

> รันดู — คลิกที่วงกลมแดง คะแนนขึ้น แล้ววงกลมย้ายที่ใหม่! 🎉

## โบนัส
คลิกนอกวงกลมก็นับ "miss" ได้:
```python
else:
    miss += 1
```
