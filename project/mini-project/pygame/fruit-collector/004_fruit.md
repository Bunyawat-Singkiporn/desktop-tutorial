# 🍎 ผลไม้

## เป้าหมาย
วาดผลไม้ 1 ลูกที่ตำแหน่งสุ่มบนหน้าจอ

## แนวคิด — random

`random.randint(a, b)` คือการสุ่มเลขจำนวนเต็มระหว่าง a ถึง b

```python
import random

fruit_x = random.randint(50, 750)   # x สุ่มระหว่าง 50–750
fruit_y = random.randint(50, 550)   # y สุ่มระหว่าง 50–550
```

| โค้ด | ทำอะไร |
|------|--------|
| `import random` | โหลด module random |
| `random.randint(50, 750)` | สุ่มเลขจาก 50 ถึง 750 |
| `pygame.draw.circle(screen, "red", (fx, fy), 15)` | วาดวงกลมรัศมี 15 pixel |

## ทำไมสุ่มแค่ 50 ถึง 750?

```
0   50                           750  800
│   │                             │   │
│   └─── สุ่มผลไม้ในช่วงนี้ ────┘   │
│                                     │
└── เว้นขอบซ้าย-ขวา 50px ────────────┘
```

## 📝 เพิ่มใน 003_player.py

**1.** เพิ่ม **บรรทัดบนสุด** หลัง `import pygame`:

```python
import random
```

**2.** เพิ่ม **ก่อน** `running = True`:

```python
# ผลไม้
fruit_x = random.randint(50, 750)
fruit_y = random.randint(50, 550)
```

**3.** เพิ่ม **หลัง** `pygame.draw.rect(...)`:

```python
    pygame.draw.circle(screen, "red", (fruit_x, fruit_y), 15)
```

> รันดู — เห็นผลไม้สีแดงบนหน้าจอ 🍎
> ทุกครั้งที่รันใหม่ ผลไม้จะอยู่คนละที่!
