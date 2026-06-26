## เป้าหมาย

สร้างหน้าต่างเกม (เหมือน Quiz Game)

---

## แนวคิด

โครงสร้างเหมือนเดิม: import → init → window → game loop

```text
import pygame       ← เรียกใช้ pygame
pygame.init()       ← เปิดระบบ
screen = ...        ← สร้างหน้าต่าง
while running:      ← เกมวนซ้ำตลอด
```

---

## อธิบายโค้ด

| บรรทัด | ความหมาย |
|--------|----------|
| `set_mode((800, 600))` | สร้างหน้าต่าง กว้าง 800 สูง 600 |
| `set_caption("Flappy Bird")` | ตั้งชื่อที่แถบด้านบน |
| `running = True` | เกมยังเล่นอยู่ |
| `while running:` | วนซ้ำจนกว่าจะปิดเกม |
| `event.get()` | ดูว่าผู้เล่นทำอะไร (เช่น กดปิด) |
| `screen.fill("skyblue")` | ทาสีพื้นหลังทั้งจอ |
| `display.flip()` | อัปเดตหน้าจอ (ต้องมีทุกรอบ!) |

---

## ผลลัพธ์

หน้าต่างสีฟ้า ชื่อ "Flappy Bird"

---

## 📝 พิมพ์ใน flappy.py (ทั้งไฟล์)

```python
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Flappy Bird")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("skyblue")
    pygame.display.flip()

pygame.quit()
```

> รันดู — ควรเห็นหน้าต่างสีฟ้าชื่อ "Flappy Bird"
