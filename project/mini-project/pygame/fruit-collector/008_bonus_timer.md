# ⏱️ โบนัส — จับเวลา (Timer)

## เป้าหมาย

นับถอยหลัง 30 วินาที — หมดเวลาแล้วเก็บผลไม้ไม่ได้

---

## แนวคิด

```text
start_time = ตอนเริ่มเกม
elapsed    = เวลาที่ใช้ไป
time_left  = 30 - elapsed
```

ถ้า `time_left <= 0` → Game Over

---

## อธิบายโค้ด

| โค้ด | ทำอะไร |
|------|--------|
| `import time` | ใช้จับเวลาจริง |
| `time.time()` | ได้เวลาปัจจุบัน (วินาที) |
| `TIME_LIMIT = 30` | เล่นได้ 30 วินาที |
| `time_left = TIME_LIMIT - elapsed` | เวลาที่เหลือ |
| `if time_left > 0:` | ยังไม่หมดเวลา → เล่นต่อ |

---

## 📝 เพิ่มใน 006_more_fruits.py (หรือ game.py ของคุณ)

**1.** เพิ่ม **บนสุด** ข้าง `import pygame`:

```python
import time
```

**2.** เพิ่ม **หลัง** `score = 0`:

```python
TIME_LIMIT = 30
start_time = time.time()
game_over = False
```

**3.** เพิ่ม **ก่อน** การเคลื่อนที่ (`keys = ...`) ใน game loop:

```python
    # คำนวณเวลาที่เหลือ
    elapsed = time.time() - start_time
    time_left = max(0, TIME_LIMIT - elapsed)
    if time_left <= 0:
        game_over = True
```

**4.** ครอบการเดิน + เก็บผลไม้ ด้วย `if not game_over:`

**แทนที่** บล็อกจาก `keys = pygame.key.get_pressed()` ถึงจบ `fruits.append(...)` ด้วย:

```python
    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_UP]:
            player_y -= player_speed
        if keys[pygame.K_DOWN]:
            player_y += player_speed

        # เช็คเก็บผลไม้
        for fruit in fruits[:]:
            fx, fy, ftype = fruit
            distance = math.sqrt((player_x - fx)**2 + (player_y - fy)**2)
            if distance < 30:
                score += fruit_points[ftype]
                fruits.remove(fruit)
                new_x = random.randint(50, 750)
                new_y = random.randint(50, 550)
                new_type = random.randint(0, 2)
                fruits.append([new_x, new_y, new_type])
```

**5.** เพิ่มแสดงเวลา — **หลัง** `score_text` / `screen.blit(score_text...)`:

```python
    time_text = font.render(f"Time: {time_left:.1f}", True, "black")
    screen.blit(time_text, (650, 10))
```

**6.** เพิ่มข้อความ Game Over — **ก่อน** `pygame.display.flip()`:

```python
    if game_over:
        over = font.render("Time's Up!", True, "red")
        screen.blit(over, (320, 280))
        final = font.render(f"Final Score: {score}", True, "black")
        screen.blit(final, (280, 330))
```

> รันทดสอบ — เล่น 30 วินาที แล้วควรหยุดและขึ้น Time's Up!

---

## เช็คเฉลย

เปิด `008_bonus_timer.py` เปรียบเทียบกับของคุณ
