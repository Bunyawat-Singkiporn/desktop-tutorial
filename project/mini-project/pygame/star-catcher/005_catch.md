# ✅ จับดาว + ชีวิต

## เป้าหมาย
เช็คว่าตะกร้ารับดาวได้ไหม → คะแนน + ชีวิต + Game Over

## แนวคิด — เช็คการจับ

ตะกร้ารับดาวได้เมื่อ **เงื่อนไข 2 ข้อ** เป็นจริงพร้อมกัน:

1. ดาวตกถึงระดับตะกร้า → `star_y > 530`
2. ดาวอยู่ในช่วงความกว้างตะกร้า → `abs(star_x - basket_x) < 50`

```python
if star_y > 530 and abs(star_x - basket_x) < 50:
    score += 1   # จับได้!
```

## ภาพประกอบ

```
basket_x - 50             basket_x + 50
      │                         │
      ▼                         ▼
──────┼─────────────────────────┼──────
      │    ⭐ อยู่ในช่วงนี้     │    ← จับได้ (star_y > 530)
──────┼─────────────────────────┼──────
      │       ตะกร้า 80px       │
      └─────────────────────────┘
```

## แนวคิด — Lives

| โค้ด | ทำอะไร |
|------|--------|
| `lives = 3` | เริ่มต้น 3 ชีวิต |
| `abs(a - b)` | ค่าสัมบูรณ์ — ระยะห่างเสมอ ≥ 0 |
| `lives -= 1` | ชีวิตลด 1 |
| `if lives <= 0:` | ถ้าชีวิตหมด → Game Over |

## 📝 เพิ่มใน 004_star.py

**1.** เพิ่ม **หลัง** `clock = pygame.time.Clock()`:

```python
font  = pygame.font.SysFont(None, 36)
```

**2.** เพิ่ม **ก่อน** `running = True`:

```python
score = 0
lives = 3
```

**3.** **แทนที่** `if star_y > 620:` block ด้วย:

```python
    # จับได้!
    if star_y > 530 and abs(star_x - basket_x) < 50:
        score += 1
        star_x = random.randint(20, 780)
        star_y = -20
    # พลาด!
    elif star_y > 620:
        lives -= 1
        star_x = random.randint(20, 780)
        star_y = -20

    if lives <= 0:
        running = False
```

**4.** เพิ่ม **ก่อน** `pygame.display.flip()`:

```python
    score_text = font.render(f"Score: {score}", True, "white")
    lives_text = font.render(f"Lives: {lives}", True, "red")
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 50))
```

**5.** เพิ่ม **หลัง** `while running:` loop (ก่อน `pygame.quit()`):

```python
# Game Over Screen
screen.fill("navy")
over_text = font.render(f"Game Over!  Score: {score}", True, "yellow")
screen.blit(over_text, (200, 280))
pygame.display.flip()
pygame.time.wait(3000)
```

> รันดู — พยายามรับดาว ถ้าพลาด 3 ครั้ง Game Over! 🎮
