# 🍊🍉 ผลไม้หลายชนิด

## เป้าหมาย
เพิ่มผลไม้ 3 ชนิด แต่ละชนิดให้คะแนนต่างกัน โดยใช้ **list**

## แนวคิด — List ของผลไม้

แทนที่จะเก็บ `fruit_x`, `fruit_y` แยกกัน ใช้ list เก็บผลไม้ทุกลูก:

```python
# ผลไม้แต่ละลูก = [x, y, ประเภท]
fruits = [
    [100, 200, 0],   # แอปเปิ้ล
    [300, 400, 1],   # ส้ม
    [500, 150, 2],   # แตงโม
]
```

## แนวคิด — สีและคะแนนตามประเภท

```python
# ประเภท 0 = แอปเปิ้ล (สีแดง,  1 คะแนน)
# ประเภท 1 = ส้ม      (สีส้ม,  2 คะแนน)
# ประเภท 2 = แตงโม   (สีเขียว, 3 คะแนน)

fruit_colors = ["red", "orange", "green"]
fruit_points = [1, 2, 3]
```

| โค้ด | ทำอะไร |
|------|--------|
| `for fruit in fruits:` | วนลูปผลไม้ทุกลูก |
| `fx, fy, ftype = fruit` | แยก x, y, ประเภทออกมา |
| `fruit_colors[ftype]` | เลือกสีตามประเภท |
| `fruit_points[ftype]` | เลือกคะแนนตามประเภท |
| `fruits[:]` | copy list ก่อนวนลูปเพื่อลบของได้ปลอดภัย |
| `fruits.remove(fruit)` | ลบผลไม้ออกจาก list |
| `fruits.append([x, y, t])` | เพิ่มผลไม้ใหม่เข้า list |

## 📝 แก้ไข 005_collect.py

**1.** **แทนที่** `fruit_x = ...` และ `fruit_y = ...` ด้วย:

```python
# ผลไม้หลายชนิด
fruit_colors = ["red", "orange", "green"]
fruit_points = [1, 2, 3]

# สร้างผลไม้ 5 ลูกตอนเริ่ม
fruits = []
for i in range(5):
    x     = random.randint(50, 750)
    y     = random.randint(50, 550)
    ftype = random.randint(0, 2)
    fruits.append([x, y, ftype])
```

**2.** **แทนที่** collision block (`distance = ...` ถึง `fruit_y = ...`) ด้วย:

```python
    # เช็คเก็บผลไม้
    for fruit in fruits[:]:          # fruits[:] = copy ของ list
        fx, fy, ftype = fruit
        distance = math.sqrt((player_x - fx)**2 + (player_y - fy)**2)
        if distance < 30:
            score += fruit_points[ftype]
            fruits.remove(fruit)
            new_x    = random.randint(50, 750)
            new_y    = random.randint(50, 550)
            new_type = random.randint(0, 2)
            fruits.append([new_x, new_y, new_type])
```

**3.** **แทนที่** `pygame.draw.circle(...)` ด้วย:

```python
    for fruit in fruits:
        fx, fy, ftype = fruit
        pygame.draw.circle(screen, fruit_colors[ftype], (fx, fy), 15)
```

> รันดู — เห็นผลไม้ 3 สี คะแนนต่างกัน! 🎉

---

## โบนัส — ป้ายคะแนนใต้ผลไม้

ให้เด็กเห็นว่าผลไม้แต่ละลูกให้กี่คะแนน เช่น `+1` `+2` `+3`

### เพิ่มตรงไหน

**1.** เพิ่ม **หลัง** `font = pygame.font.SysFont(None, 36)`:

```python
small_font = pygame.font.SysFont(None, 22)
```

**2.** เพิ่ม **หลัง** `fruit_points = [1, 2, 3]`:

```python
fruit_labels = ["+1", "+2", "+3"]
```

**3.** เพิ่ม **ใน** ลูปวาดผลไม้ — **หลัง** `pygame.draw.circle(...)`:

```python
    for fruit in fruits:
        fx, fy, ftype = fruit
        pygame.draw.circle(screen, fruit_colors[ftype], (fx, fy), 15)
        # ← เพิ่ม 2 บรรทัดนี้
        label = small_font.render(fruit_labels[ftype], True, "black")
        screen.blit(label, (fx - 8, fy + 18))
```

`(fx - 8, fy + 18)` = วางข้อความใต้ผลไม้นิดหน่อย

> รันดู — ใต้ผลไม้ควรมี +1 / +2 / +3