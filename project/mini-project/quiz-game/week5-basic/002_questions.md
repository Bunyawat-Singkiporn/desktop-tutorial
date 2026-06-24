## เป้าหมาย

สร้างหน้าต่างเกม (เหมือน guessing game)

---

## แนวคิด

โครงสร้างเหมือนเดิม: import → init → window → font → game loop

เพิ่ม `font` สองชนิด: `font_q` (คำถาม ใหญ่กว่า) และ `font_c` (ตัวเลือก เล็กกว่า)

---

## ผลลัพธ์

หน้าต่างสีขาว ชื่อ "Quiz Game"

---

## 📝 พิมพ์ใน quiz.py (ทั้งไฟล์)

```python
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Quiz Game")

font_q = pygame.font.Font(None, 48)   # แบบอักษรสำหรับคำถาม
font_c = pygame.font.Font(None, 36)   # แบบอักษรสำหรับตัวเลือก

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    pygame.display.flip()

pygame.quit()
```

> รันดู — ควรเห็นหน้าต่างสีขาวชื่อ "Quiz Game"
