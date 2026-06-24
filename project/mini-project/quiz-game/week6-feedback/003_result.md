## เป้าหมาย

สร้างหน้าสรุปเมื่อตอบครบทุกข้อ

---

## แนวคิด

เมื่อ `current_q == len(questions)` → แสดงสกอร์และข้อความแทน "Quiz Complete!"

```
score == 5  →  "Perfect!"
score >= 3  →  "Good job!"
อื่นๆ    →  "Keep practicing!"
```

---

## 📝 แก้ใน quiz.py

**แทนที่** บล็อก `else: done_surf...` ด้วย:

```python
    else:
        # แสดงสกอร์
        sc_surf = font_q.render(f"Score: {score}/{len(questions)}", True, "black")
        screen.blit(sc_surf, (230, 200))

        # ข้อความตามผล
        if score == len(questions):
            msg = "Perfect!"
            col = "gold"
        elif score >= 3:
            msg = "Good job!"
            col = "green"
        else:
            msg = "Keep practicing!"
            col = "red"

        m_surf = font_q.render(msg, True, col)
        screen.blit(m_surf, (280, 300))
```

> รันทดสอบ — ตอบครบควรเห็นหน้าสรุป
