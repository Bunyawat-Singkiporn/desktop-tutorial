## เป้าหมาย

วาดนกบนหน้าจอ

---

## แนวคิด

**ตัวแปร** = กล่องเก็บข้อมูล

```python
bird_x = 150    # ตำแหน่งซ้าย-ขวา (ยิ่งมาก ยิ่งขวา)
bird_y = 300    # ตำแหน่งบน-ล่าง (ยิ่งมาก ยิ่งลง)
bird_size = 25  # ขนาดนก (รัศมีวงกลม)
```

```python
pygame.draw.circle(screen, "yellow", (bird_x, bird_y), bird_size)
#                  หน้าจอ  สี      จุดกลาง           ขนาด
```

---

## อธิบายแกน X, Y

```text
(0,0) ────────────→ X (ขวา)
  │
  │      🟡 (150, 300) ← นกอยู่ตรงนี้
  │
  ↓
  Y (ลง)
```

---

## 📝 เพิ่มใน flappy.py

**1.** เพิ่ม **หลัง** `pygame.display.set_caption(...)` ก่อน `running = True`:

```python
bird_x = 150
bird_y = 300
bird_size = 25
```

**2.** **แทนที่** `screen.fill("skyblue")` ถึง `pygame.display.flip()` ด้วย:

```python
    screen.fill("skyblue")
    pygame.draw.circle(screen, "yellow", (bird_x, bird_y), bird_size)
    pygame.display.flip()
```

> รันดู — ควรเห็นวงกลมสีเหลือง (นก) กลางจอ
