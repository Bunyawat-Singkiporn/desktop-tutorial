## เป้าหมาย

ชนท่อหรือชนขอบจอ → Game Over

---

## แนวคิด

ตรวจ 2 ขั้น (ถามทีละคำถาม):

**คำถาม 1:** นกอยู่ตำแหน่งเดียวกับท่อไหม? (แนวนอน)

```python
pipe_x < bird_x + bird_size and pipe_x + pipe_w > bird_x - bird_size
```

**คำถาม 2:** นกอยู่นอกช่องว่างไหม? (แนวตั้ง)

```python
bird_y - bird_size < pipe_h              # ชนท่อบน
bird_y + bird_size > pipe_h + pipe_gap   # ชนท่อล่าง
```

ถ้าทั้ง 2 ข้อใช่ → `game_over = True`

---

## อธิบาย game_over

```python
game_over = False    # เริ่มเกม = ยังไม่แพ้
game_over = True     # ชนแล้ว = แพ้
```

```python
if not game_over:    # ถ้ายังไม่แพ้ → อัปเดตเกม
    bird_speed += GRAVITY
    ...
```

`not` = **ยังไม่** (ถ้า game_over เป็น False → not game_over เป็น True)

---

## 📝 เพิ่มใน flappy.py

**1.** เพิ่ม **หลัง** `score = 0`:

```python
game_over = False
```

**2.** **แทนที่** บล็อกจาก `bird_speed += GRAVITY` ถึง `score += 1` ด้วย:

```python
    if not game_over:
        bird_speed += GRAVITY
        bird_y += bird_speed

        pipe_x -= 3
        if pipe_x < -pipe_w:
            pipe_x = 800
            pipe_h = random.randint(100, 320)
            score += 1

        if pipe_x < bird_x + bird_size and pipe_x + pipe_w > bird_x - bird_size:
            if bird_y - bird_size < pipe_h or bird_y + bird_size > pipe_h + pipe_gap:
                game_over = True

        if bird_y - bird_size < 0 or bird_y + bird_size > 600:
            game_over = True
```

**3.** แก้การกด Space — กระโดดได้เฉพาะตอนยังไม่ Game Over:

```python
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_speed = JUMP
```

(จะแก้ให้เล่นใหม่ในขั้นถัดไป)

**4.** เพิ่ม **ก่อน** `pygame.display.flip()`:

```python
    if game_over:
        over_text = font.render("Game Over! Space = Restart", True, "red")
        screen.blit(over_text, (180, 280))
```

> รันดู — ชนท่อแล้วเกมหยุด แสดง Game Over
