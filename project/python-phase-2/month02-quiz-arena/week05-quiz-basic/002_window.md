# 1) หน้าต่างเกม + ตัวหนังสือไทย

## เป้าหมาย
เปิดหน้าต่างสีเข้ม แล้วเขียนคำว่า QUIZ ARENA

---

## แนวคิด — โครงกระดูกของทุกเกม Pygame

```python
import pygame
pygame.init()                                   # 1. เปิดระบบ

screen = pygame.display.set_mode((800, 600))    # 2. สร้างหน้าต่าง
clock  = pygame.time.Clock()

running = True
while running:                                  # 3. game loop
    for event in pygame.event.get():            #    - รับ event
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")                        #    - วาด
    pygame.display.flip()                       #    - ส่งขึ้นจอ
    clock.tick(60)                              #    - 60 เฟรม/วินาที

pygame.quit()                                   # 4. ปิดระบบ
```

| บรรทัด | ทำอะไร |
|--------|--------|
| `set_mode((800, 600))` | หน้าต่างกว้าง 800 สูง 600 |
| `pygame.QUIT` | ผู้เล่นกดกากบาทปิดหน้าต่าง |
| `screen.fill("black")` | ทาสีทับทั้งจอ (ลบภาพเก่า) |
| `display.flip()` | เอาภาพที่วาดไว้ขึ้นจอจริง |
| `clock.tick(60)` | คุมความเร็วเกม 60 FPS |

> ถ้าไม่มี `flip()` = วาดแล้วไม่มีอะไรขึ้นจอ (บั๊กยอดฮิตอันดับ 1)

---

## แนวคิด — ตัวหนังสือภาษาไทย

Pygame ต้องบอกว่าใช้ **ฟอนต์อะไร** ถึงจะแสดงภาษาไทยได้

```python
font_big   = pygame.font.SysFont("tahoma", 40)
font_mid   = pygame.font.SysFont("tahoma", 30)
```

> `tahoma` มีอยู่ในทุกเครื่อง Windows และรองรับภาษาไทย 🇹🇭
> ถ้าใช้ `SysFont(None, 40)` ภาษาไทยจะกลายเป็น □□□□

วาดตัวหนังสือ 2 ขั้นตอนเสมอ:

```python
text = font_big.render("QUIZ ARENA", True, "white")   # 1. ทำเป็นรูป
screen.blit(text, (50, 40))                           # 2. แปะลงจอที่ (50,40)
```

---

## 📝 สร้างไฟล์ `quiz.py`

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Quiz Arena")
clock = pygame.time.Clock()

font_big = pygame.font.SysFont("tahoma", 40)
font_mid = pygame.font.SysFont("tahoma", 30)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((25, 30, 50))

    title = font_big.render("QUIZ ARENA", True, "white")
    screen.blit(title, (50, 40))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

---

> รันดู — ต้องเห็นหน้าต่างสีน้ำเงินเข้ม มีคำว่า QUIZ ARENA มุมบนซ้าย ✅
> ลองเปลี่ยน `(25, 30, 50)` เป็น `"purple"` ดู
