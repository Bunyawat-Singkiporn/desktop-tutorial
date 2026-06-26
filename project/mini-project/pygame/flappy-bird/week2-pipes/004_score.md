## เป้าหมาย

นับคะแนนเมื่อผ่านท่อ + แสดงบนหน้าจอ

---

## แนวคิด

ท่อหายไปทางซ้าย = นกผ่านสำเร็จ → `score += 1`

```python
score = 0        # เริ่มที่ 0
score += 1       # เพิ่มทีละ 1 (เหมือน Quiz Game)
```

---

## อธิบายการแสดงคะแนน

```python
score_text = font.render(f"Score: {score}", True, "white")
#                        ↑ ข้อความ        สีขาว
screen.blit(score_text, (20, 20))
#           ↑ วางข้อความที่มุมซ้ายบน
```

`f"Score: {score}"` = ข้อความที่มีตัวเลขคะแนน เช่น `"Score: 3"`

---

## 📝 เพิ่มใน flappy.py

**1.** เพิ่ม **หลัง** `pipe_h = 180`:

```python
score = 0
```

**2.** เพิ่ม `score += 1` ใน `if pipe_x < -pipe_w:`:

```python
    if pipe_x < -pipe_w:
        pipe_x = 800
        pipe_h = random.randint(100, 320)
        score += 1
```

**3.** เพิ่ม **ก่อน** `pygame.display.flip()`:

```python
    score_text = font.render(f"Score: {score}", True, "white")
    screen.blit(score_text, (20, 20))
```

> รันทดสอบ — ผ่านท่อแล้วคะแนนเพิ่ม! 🎉

---

## เช็คเฉลย

เปิด `flappy.py` ในโฟลเดอร์นี้ (ไฟล์เฉลย) เปรียบเทียบกับของคุณ

> สัปดาห์หน้า: ชนท่อ = Game Over
