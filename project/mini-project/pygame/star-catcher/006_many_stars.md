# ⭐⭐⭐ ดาวหลายดวง

## เป้าหมาย
เพิ่มดาวหลายดวงพร้อมกัน แต่ละดวงความเร็วต่างกัน โดยใช้ **list**

## แนวคิด — เปลี่ยนจาก 1 ดาว เป็น list ของดาว

แทนที่ `star_x, star_y, star_speed` สามตัว ใช้ list เก็บทุกดวง:

```python
# ดาวแต่ละดวง = [x, y, ความเร็ว]
stars = [
    [100, -80,  2],
    [400, -400, 3],
]
```

| โค้ด | ทำอะไร |
|------|--------|
| `for star in stars:` | วนลูปดาวทุกดวง |
| `star[1] += star[2]` | ดาวดวงนั้นตก (y เพิ่ม) |
| `sx, sy = star[0], star[1]` | แยก x, y ออกมา |
| `star[0] = random.randint(...)` | เปลี่ยน x ของดาวดวงนั้น |
| `random.randint(2, 3)` | ความเร็วสุ่ม 2–3 (เล่นได้) |

> ทิป: วาง `y` ห่างกัน (เช่น `-80` กับ `-400`) จะไม่ตกพร้อมกัน — เล่นง่ายขึ้นมาก

## 📝 แก้ไข 005_catch.py

**0.** (แนะนำ) เร่งตะกร้า + เพิ่มชีวิต ให้จับดาว 2 ดวงทัน:

```python
basket_speed = 8
lives = 5
```

**1.** **แทนที่** `star_x`, `star_y`, `star_speed` สามบรรทัด ด้วย list:

```python
# ดาวหลายดวง [x, y, speed]
# วาง y ห่างกันชัดๆ — ไม่ตกพร้อมกัน
stars = []
for i in range(2):
    x     = random.randint(20, 780)
    y     = -80 - i * 320
    speed = random.randint(2, 3)
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
        if sy > 520 and abs(sx - basket_x) < 65:
            score += 1
            star[0] = random.randint(20, 780)
            star[1] = random.randint(-480, -280)
            star[2] = random.randint(2, 3)
        elif sy > 620:
            lives -= 1
            star[0] = random.randint(20, 780)
            star[1] = random.randint(-480, -280)
            star[2] = random.randint(2, 3)
```

**3.** **แทนที่** `pygame.draw.circle(...)` ด้วย:

```python
    for star in stars:
        pygame.draw.circle(screen, "yellow", (star[0], star[1]), 12)
```

> รันดู — ดาว 2 ดวงผลัดกันตก ความเร็วไม่แรงเกินไป! 🎉

## โบนัส
ลองเพิ่มดาวอีกดวงเมื่อคะแนนถึง 10:
```python
if score >= 10 and len(stars) < 3:
    stars.append([random.randint(20, 780), -400, random.randint(2, 3)])
```
