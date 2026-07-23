## เป้าหมาย

สร้างหน้าต่างเกม

---

## แนวคิด

โครงสร้างเกม pygame เหมือนกันทุกครั้ง:

```text
import pygame        ← เรียกใช้ pygame
pygame.init()        ← เปิดระบบ
screen = ...         ← สร้างหน้าต่าง
while running:       ← เกมวนซ้ำตลอด
```

`while running:` = **while loop** — วนซ้ำตราบที่ `running` ยังเป็น `True`
(เหมือนที่เรียน while loop ใน Python-beginner)

---

## อธิบายโค้ด

| บรรทัด | ความหมาย |
|--------|----------|
| `set_mode((800, 600))` | สร้างหน้าต่าง กว้าง 800 สูง 600 |
| `set_caption("Guess The Number")` | ตั้งชื่อที่แถบด้านบน |
| `running = True` | **ตัวแปร** บอกว่าเกมยังเล่นอยู่ |
| `while running:` | วนซ้ำจนกว่าจะปิดเกม |
| `event.get()` | ดูว่าผู้เล่นทำอะไร |
| `pygame.QUIT` | กดปุ่มปิดหน้าต่าง → `running = False` |
| `screen.fill("white")` | ทาสีพื้นหลังขาว |
| `display.flip()` | อัปเดตหน้าจอ (ต้องมีทุกรอบ!) |

---

## ผลลัพธ์

หน้าต่างสีขาว ชื่อ "Guess The Number"

---

## 📝 พิมพ์ใน game.py (ทั้งไฟล์)

```python
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Guess The Number")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    pygame.display.flip()

pygame.quit()
```

> รันดู — ควรเห็นหน้าต่างสีขาวชื่อ "Guess The Number"
