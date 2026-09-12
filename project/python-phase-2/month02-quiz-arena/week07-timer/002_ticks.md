# 1) รู้จักเวลาใน Pygame

## เป้าหมาย
โชว์ตัวเลขวินาทีที่ผ่านไปตั้งแต่เปิดเกม

---

## แนวคิด — `pygame.time.get_ticks()`

คืนค่า **มิลลิวินาที** ที่ผ่านไปนับตั้งแต่ `pygame.init()`

```python
now = pygame.time.get_ticks()    # เช่น 5230  = 5.23 วินาที
seconds = now / 1000             # 5.23
```

| หน่วย | ค่า |
|-------|-----|
| 1 วินาที | 1000 มิลลิวินาที |
| 1000 ms | 1.0 วิ |
| 5230 ms | 5.23 วิ |

> ทำไมไม่นับเฟรมแทน? เพราะเครื่องช้า-เร็วไม่เท่ากัน แต่ **เวลาจริงเท่ากันทุกเครื่อง** ⏱️

---

## แนวคิด — จับ "เวลาเริ่ม" ไว้

การจับเวลาต้องมี 2 ค่าเสมอ

```python
start = pygame.time.get_ticks()          # จำไว้ตอนเริ่ม

# ...ผ่านไปสักพัก...

now = pygame.time.get_ticks()            # ขอเวลาตอนนี้
passed = (now - start) / 1000            # ผ่านไปกี่วินาที
```

```text
start   = 2000 ms
now     = 7500 ms
passed  = (7500 - 2000) / 1000 = 5.5 วินาที
```

---

## แนวคิด — ปัดทศนิยม

```python
round(5.4321, 1)     # 5.4   ← ทศนิยม 1 ตำแหน่ง
int(5.9)             # 5     ← ตัดทิ้ง
```

---

## 📝 ลองก่อน — สร้างไฟล์ `timer_test.py`

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 200))
clock = pygame.time.Clock()
font = pygame.font.SysFont("tahoma", 40)

start = pygame.time.get_ticks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    passed = (pygame.time.get_ticks() - start) / 1000

    screen.fill("black")
    text = font.render(f"{round(passed, 1)} วินาที", True, "white")
    screen.blit(text, (100, 80))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

---

> รันดู — ตัวเลขต้องวิ่งขึ้นเรื่อยๆ ✅
