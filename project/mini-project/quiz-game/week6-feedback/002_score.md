## เป้าหมาย

เพิ่มตัวแปร `score` และแสดงบนหน้าจอ

---

## แนวคิด

ตั้ง `score = 0` ก่อน game loop  
ทุกครั้งตอบถูก → `score += 1`  
แสดง `score` บนหน้าจอด้านขวาบน

---

## 📝 เพิ่มใน quiz.py

**1.** เพิ่ม `score = 0` หลัง `feedback = ""`:

```python
score = 0
```

**2.** เพิ่ม `score += 1` ใน `if picked == answers[current_q]:`:

```python
                if picked == answers[current_q]:
                    feedback = "Correct!"
                    score += 1     # ← เพิ่มบรรทัดนี้
```

**3.** เพิ่มแสดง score มุมบนขวา (**หลัง** `screen.fill`):

```python
    s_surf = font_c.render(f"Score: {score}/{len(questions)}", True, "black")
    screen.blit(s_surf, (600, 30))
```

> รันดู — คะแนนควรเพิ่มขึ้นทุกครั้งตอบถูก
