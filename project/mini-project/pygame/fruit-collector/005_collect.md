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

## 📝 เพิ่มใน 004_fruit.py

**1.** เพิ่ม **หลัง** `import random`:

```python
import math
```

**2.** เพิ่ม **หลัง** `clock = pygame.time.Clock()`:

```python
font = pygame.font.SysFont(None, 36)
```

**3.** เพิ่ม **ก่อน** `running = True`:

```python
score = 0
```

**4.** เพิ่ม **หลัง** key movement block (หลัง `player_y += player_speed`):

```python
    # เช็คว่าเก็บผลไม้ได้ไหม
    distance = math.sqrt((player_x - fruit_x)**2 + (player_y - fruit_y)**2)
    if distance < 30:
        score += 1
        fruit_x = random.randint(50, 750)
        fruit_y = random.randint(50, 550)
```

**5.** เพิ่ม **ก่อน** `pygame.display.flip()`:

```python
    score_text = font.render(f"Score: {score}", True, "black")
    screen.blit(score_text, (10, 10))
```

> รันดู — เดินชนผลไม้แล้วคะแนนขึ้น! 🎉
> ผลไม้หายแล้วเกิดใหม่ที่ตำแหน่งสุ่ม
