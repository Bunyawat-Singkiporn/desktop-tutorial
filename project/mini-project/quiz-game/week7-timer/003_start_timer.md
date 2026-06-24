## เป้าหมาย

แสดงแถบเวลาบนหน้าจอ

---

## แนวคิด

ใช้ `pygame.draw.rect()` วาดสี่เหลี่ยม

```python
pygame.draw.rect(screen, color, (x, y, width, height))
```

แถบเวลา = แถบเทา (พื้นหลัง) + แถบสี (เวลาที่เหลือ)

---

## 📝 เพิ่มใน quiz.py

**1.** เพิ่ม **หลัง** `screen.fill` ก่อน if/else:

```python
    elapsed   = time.time() - start_time
    time_left = max(0, TIME_LIMIT - elapsed)
```

**2.** เพิ่มในบล็อก `if current_q < len(questions)` หลังแสดงคำถาม:

```python
        # แสดงเวลาที่เหลือ
        t_color = "red" if time_left < 4 else "black"
        t_surf = font_c.render(f"Time: {time_left:.1f}s", True, t_color)
        screen.blit(t_surf, (50, 130))

        # แถบเวลา
        bar_w = int((time_left / TIME_LIMIT) * 700)
        pygame.draw.rect(screen, "lightgray", (50, 155, 700, 15))
        pygame.draw.rect(screen, "green" if time_left > 4 else "red", (50, 155, bar_w, 15))
```

> รันดู — ควรเห็นแถบเวลาลดลง (ยังไม่ timeout)
