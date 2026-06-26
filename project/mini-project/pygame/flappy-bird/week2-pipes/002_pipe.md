## เป้าหมาย

วาดท่อบนและท่อล่าง

---

## แนวคิด

ท่อ = สี่เหลี่ยม 2 อัน มีช่องว่างตรงกลาง

```text
🟩🟩🟩  ← ท่อบน (สูง pipe_h)
         
   ⬜    ← ช่องว่าง (pipe_gap = 200)
         
🟩🟩🟩  ← ท่อล่าง
```

```python
pygame.draw.rect(screen, สี, (x, y, กว้าง, สูง))
```

| ตัวแปร | ความหมาย |
|--------|----------|
| `pipe_x` | ท่ออยู่ซ้าย-ขวาตรงไหน (เริ่มที่ 800 = ขวาสุด) |
| `pipe_w` | ความกว้างท่อ |
| `pipe_h` | ความสูงท่อบน |
| `pipe_gap` | ขนาดช่องว่างให้นกบินผ่าน |

---

## อธิบายท่อล่าง

```python
(pipe_x, pipe_h + pipe_gap, pipe_w, 600 - pipe_h - pipe_gap)
#        ↑ เริ่มหลังช่องว่าง    ↑ สูงพอดีถึงขอบล่างจอ
```

---

## 📝 เพิ่มใน flappy.py

**1.** เพิ่ม **หลัง** `pygame.display.set_caption(...)`:

```python
font = pygame.font.Font(None, 48)
```

`font` = ตัวอักษรสำหรับแสดงคะแนน (ใช้ในขั้นถัดไป)

**2.** เพิ่ม **หลัง** `JUMP = -8`:

```python
pipe_x = 800
pipe_w = 80
pipe_gap = 200
pipe_h = 180
```

**3.** เพิ่ม **หลัง** `pygame.draw.circle(...)`:

```python
    pygame.draw.rect(screen, "green", (pipe_x, 0, pipe_w, pipe_h))
    pygame.draw.rect(screen, "green", (pipe_x, pipe_h + pipe_gap, pipe_w, 600 - pipe_h - pipe_gap))
```

> รันดู — ควรเห็นท่อสีเขียวขวาจอ (ยังไม่ขยับ)
