# ⭐⭐⭐ ดาวหลายดวง

## เป้าหมาย
เพิ่มดาวหลายดวงพร้อมกัน แต่ละดวงความเร็วต่างกัน โดยใช้ **list**

## แนวคิด — เปลี่ยนจาก 1 ดาว เป็น list ของดาว

แทนที่ `star_x, star_y, star_speed` สามตัว ใช้ list เก็บทุกดวง:

```python
# ดาวแต่ละดวง = [x, y, ความเร็ว]
stars = [
    [100, -20,  3],
    [400, -80,  5],
    [650, -50,  4],
]
```

| โค้ด | ทำอะไร |
|------|--------|
| `for star in stars:` | วนลูปดาวทุกดวง |
| `star[1] += star[2]` | ดาวดวงนั้นตก (y เพิ่ม) |
| `sx, sy, sp = star` | แยก x, y, speed ออกมา |
| `star[0] = random.randint(...)` | เปลี่ยน x ของดาวดวงนั้น |
| `random.randint(3, 7)` | ความเร็วสุ่ม 3–7 |

## 📝 แก้ไข 005_catch.py

**1.** **แทนที่** `star_x`, `star_y`, `star_speed` สามบรรทัด ด้วย list:

```python
# ดาวหลายดวง [x, y, speed]
stars = []
for i in range(2):
    x     = random.randint(20, 780)
    y     = random.randint(-500, -50)
    speed = random.randint(2, 4)
    stars.append([x, y, speed])
```

**2.** **แทนที่** `star_y += star_speed` และ `if star_y > 620:` block ด้วย:

```python
    # ขยับดาวทุกดวง
    for star in stars:
        star[1] += star[2]

    # เช็คจับ / พลาด
    for star in stars:
        sx, sy = star[0], star[1]
        if sy > 530 and abs(sx - basket_x) < 50:
            score += 1
            star[0] = random.randint(20, 780)
            star[1] = random.randint(-500, -50)
            star[2] = random.randint(2, 4)
        elif sy > 620:
            lives -= 1
            star[0] = random.randint(20, 780)
            star[1] = random.randint(-500, -50)
            star[2] = random.randint(2, 4)
```

**3.** **แทนที่** `pygame.draw.circle(...)` ด้วย:

```python
    for star in stars:
        pygame.draw.circle(screen, "yellow", (star[0], star[1]), 12)
```

> รันดู — ดาว 2 ดวงตกพร้อมกัน ความเร็วต่างกัน! 🎉

## โบนัส
ลองเพิ่มดาวอีกดวงเมื่อคะแนนถึง 10:
```python
if score >= 10 and len(stars) < 4:
    stars.append([random.randint(20, 780), -20, random.randint(4, 8)])
    score = 0   # รีเซ็ตนับใหม่
```
