# ⭐ ดาวตกลงมา

## เป้าหมาย
วาดดาวที่ตกลงมาจากด้านบนทุก frame

## แนวคิด — ทำให้ดาวตก

ทุก frame เพิ่ม `star_y` ขึ้น → ดาวเลื่อนลงมาเรื่อยๆ

```python
star_y += star_speed   # เพิ่มทุก frame = ดาวตกลง
```

| โค้ด | ทำอะไร |
|------|--------|
| `star_x = random.randint(20, 780)` | สุ่มตำแหน่ง x |
| `star_y = -20` | เริ่มเหนือหน้าจอ (ยังมองไม่เห็น) |
| `star_speed = 4` | ความเร็วตก (pixel ต่อ frame) |
| `star_y += star_speed` | ตกลงมาทุก frame |
| `pygame.draw.circle(screen, "yellow", (star_x, star_y), 12)` | วาดดาว |

## ดาวตกอย่างไร

```
star_y = -20   ← เริ่มต้น (เหนือหน้าจอ)
     ↓  += 4 ทุก frame
star_y = 100
     ↓
star_y = 300
     ↓
star_y = 600   ← ออกนอกหน้าจอ → เริ่มใหม่
```

## 📝 เพิ่มใน 003_basket.py

**1.** เพิ่ม **บรรทัดบนสุด** หลัง `import pygame`:

```python
import random
```

**2.** เพิ่ม **ก่อน** `running = True`:

```python
# ดาว
star_x     = random.randint(20, 780)
star_y     = -20
star_speed = 4
```

**3.** เพิ่ม **ก่อน** `screen.fill(...)`:

```python
    # ดาวตก
    star_y += star_speed

    # ถ้าออกนอกหน้าจอ → เริ่มใหม่
    if star_y > 620:
        star_x = random.randint(20, 780)
        star_y = -20
```

**4.** เพิ่ม **หลัง** `pygame.draw.rect(...)`:

```python
    pygame.draw.circle(screen, "yellow", (star_x, star_y), 12)
```

> รันดู — เห็นดาวตกลงมาทุก frame ⭐
> ดาวเกิดใหม่ทุกครั้งที่ตกพ้นหน้าจอ
