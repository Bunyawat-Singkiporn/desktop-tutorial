# 1) ตะกร้าที่เลื่อนได้

## เป้าหมาย
สร้างหน้าต่างเกม แล้วทำตะกร้าที่เลื่อนซ้าย-ขวาด้วยปุ่มลูกศร

---

## แนวคิด — กดค้าง ต่างจาก กดครั้งเดียว

เดือนที่แล้วเราใช้ `KEYDOWN` ตอบคำถาม — กด 1 ครั้งเกิด 1 ครั้ง
แต่การ **เดิน** ต้องกดค้างแล้วเคลื่อนที่เรื่อยๆ

```python
keys = pygame.key.get_pressed()      # ขอสถานะปุ่มทุกปุ่ม ณ ตอนนี้
if keys[pygame.K_LEFT]:
    basket_x = basket_x - speed
if keys[pygame.K_RIGHT]:
    basket_x = basket_x + speed
```

| วิธี | เกิดเมื่อ | เหมาะกับ |
|------|-----------|----------|
| `event.type == pygame.KEYDOWN` | กดลง 1 ครั้ง | เลือกคำตอบ, กระโดด, ยิง |
| `pygame.key.get_pressed()` | ทุกเฟรมที่ยังกดค้าง | เดิน, เลื่อนตะกร้า |

---

## แนวคิด — กันตะกร้าหลุดจอ

```python
if basket_x < 0:
    basket_x = 0
if basket_x > 800 - basket_w:
    basket_x = 800 - basket_w
```

```text
0                                         800
│                                          │
│  [====]                          [====]  │
│   ซ้ายสุด                        ขวาสุด  │
│   x = 0                     x = 800 - w  │
```

> ถ้าไม่กัน ตะกร้าจะวิ่งหายออกนอกจอแล้วไม่กลับมา

---

## 📝 สร้างไฟล์ `fruit.py`

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fruit Collector")
clock = pygame.time.Clock()
font = pygame.font.SysFont("tahoma", 24)

BASKET_W = 110
BASKET_H = 26
basket_x = 345
basket_y = 530
speed = 7

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        basket_x = basket_x - speed
    if keys[pygame.K_RIGHT]:
        basket_x = basket_x + speed

    if basket_x < 0:
        basket_x = 0
    if basket_x > 800 - BASKET_W:
        basket_x = 800 - BASKET_W

    screen.fill((30, 45, 60))
    pygame.draw.rect(screen, (200, 150, 80), (basket_x, basket_y, BASKET_W, BASKET_H), border_radius=6)
    screen.blit(font.render("ลูกศรซ้าย-ขวา เลื่อนตะกร้า", True, "white"), (20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

---

> รันดู — ตะกร้าต้องเลื่อนลื่นๆ และชนขอบจอแล้วหยุด ✅
> ลองเปลี่ยน `speed` เป็น 15 ดูว่าต่างกันยังไง
