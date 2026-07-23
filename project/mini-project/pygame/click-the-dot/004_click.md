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

## 📝 เพิ่มใน 003_dot.py

**1.** เพิ่ม **หลัง** `import random`:

```python
import math
```

**2.** เพิ่ม **หลัง** `clock = pygame.time.Clock()`:

```python
font  = pygame.font.SysFont(None, 36)
```

**3.** เพิ่ม **ก่อน** `running = True`:

```python
score = 0
```

**4.** เพิ่ม **ใน** `for event in pygame.event.get():` (หลัง `running = False`):

```python
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            distance = math.sqrt((mx - dot_x)**2 + (my - dot_y)**2)
            if distance < 30:
                score += 1
                dot_x = random.randint(50, 750)
                dot_y = random.randint(50, 550)
```

**5.** เพิ่ม **ก่อน** `pygame.display.flip()`:

```python
    score_text = font.render(f"Score: {score}", True, "black")
    screen.blit(score_text, (10, 10))
```

> รันดู — คลิกที่วงกลมแดง คะแนนขึ้น แล้ววงกลมย้ายที่ใหม่! 🎉

## โบนัส
คลิกนอกวงกลมก็นับ "miss" ได้:
```python
else:
    miss += 1
```
