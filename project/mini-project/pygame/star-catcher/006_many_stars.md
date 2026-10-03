# ⭐⭐⭐ ดาวหลายดวง

## เป้าหมาย
เพิ่มดาวหลายดวงโดยใช้ **list**

## แนวคิด — เปลี่ยนจาก 1 ดาว เป็น list ของดาว

แทนที่ `star_x, star_y, star_speed` สามตัว ใช้ list เก็บทุกดวง:

```python
# ดาวแต่ละดวง = [x, y, ความเร็ว]
stars = [
    [100, -50,  2],
    [400, -350, 2],
]
```

| โค้ด | ทำอะไร |
|------|--------|
| `for star in stars:` | วนลูปดาวทุกดวง |
| `star[1] += star[2]` | ดาวดวงนั้นตก (y เพิ่ม) |
| `stars[1 - i]` | ดาวอีกดวง (เมื่อมี 2 ดวง) |
| `other_y - 300` | วางสูงกว่าอีกดวง 300 px |

> ใช้ความเร็วเท่ากัน (`2`) และห่าง `y` ชัดๆ จะไม่ถึงตะกร้าพร้อมกัน

## 📝 แก้ไข 005_catch.py

**0.** เร่งตะกร้า + เพิ่มชีวิต:

```python
basket_speed = 8
lives = 5
```

**1.** **แทนที่** `star_x`, `star_y`, `star_speed` ด้วย list:

```python
# ดาว 2 ดวง [x, y, speed]
stars = [
    [random.randint(20, 780), -50,  2],
    [random.randint(20, 780), -350, 2],
]
```

**2.** **แทนที่** `star_y += star_speed` และบล็อกจับ/พลาด ด้วย:

```python
    # ขยับดาวทุกดวง
    for star in stars:
        star[1] += star[2]

    # เช็คจับ / พลาด
    for i in range(len(stars)):
        star = stars[i]
        sx, sy = star[0], star[1]
        other_y = stars[1 - i][1]   # y ของดาวอีกดวง

        if sy > 520 and abs(sx - basket_x) < 65:
            score += 1
            star[0] = random.randint(20, 780)
            star[1] = min(other_y - 300, -50)  # สูงกว่าอีกดวง
        elif sy > 620:
            lives -= 1
            star[0] = random.randint(20, 780)
            star[1] = min(other_y - 300, -50)
```

**3.** **แทนที่** `pygame.draw.circle(...)` ด้วย:

```python
    for star in stars:
        pygame.draw.circle(screen, "yellow", (star[0], star[1]), 12)
```

> รันดู — ดาว 2 ดวงผลัดกันตก! 🎉

## โบนัส
อยากยากขึ้น ลองเปลี่ยน `-350` เป็น `-250` (ห่างน้อยลง) หรือเพิ่มความเร็วเป็น `3`
