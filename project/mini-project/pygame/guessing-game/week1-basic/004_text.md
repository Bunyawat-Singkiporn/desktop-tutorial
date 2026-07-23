## เป้าหมาย

แสดงข้อความบนหน้าจอ

---

## แนวคิด

**ตัวแปร (Variable)** เก็บข้อความที่จะแสดง

```python
message = "Guess Number 1-5"   # str = ข้อความ
```

ใน Python-beginner เราเรียน `variable = value`
ที่นี่ `message` เป็นตัวแปรเก็บ **ข้อความ** — พอข้อความเปลี่ยน แค่แก้ `message` เดียว

วิธีแสดงข้อความใน pygame มี 3 ขั้น:

```text
1. สร้าง font   →  pygame.font.Font(None, 48)
2. render text  →  font.render(message, True, "black")
3. วางบนจอ     →  screen.blit(text, (x, y))
```

---

## อธิบายโค้ด

| บรรทัด | ความหมาย |
|--------|----------|
| `pygame.font.Font(None, 48)` | สร้างฟอนต์ ขนาด 48 |
| `font.render(message, True, "black")` | แปลงข้อความเป็นภาพ สีดำ |
| `screen.blit(text, (180, 250))` | วางที่ตำแหน่ง x=180, y=250 |

ตำแหน่ง (x, y) — เหมือนแกน x,y:

```text
(0,0) ─────────────→ x
  │
  │    (180, 250) ← ข้อความอยู่ตรงนี้
  ↓
  y
```

---

## 📝 เพิ่มใน game.py

**1.** เพิ่ม **หลัง** `pygame.display.set_caption(...)`:

```python
font = pygame.font.Font(None, 48)
message = "Guess Number 1-5"
```

**2.** เพิ่ม **ก่อน** `pygame.display.flip()` ใน game loop:

```python
    text = font.render(message, True, "black")
    screen.blit(text, (180, 250))
```

> รันดู — ควรเห็นข้อความ "Guess Number 1-5" กลางจอ
