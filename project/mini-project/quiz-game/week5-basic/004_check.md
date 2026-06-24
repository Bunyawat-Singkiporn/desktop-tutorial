## เป้าหมาย

แสดงคำถามและตัวเลือก 4 ข้อบนหน้าจอ

---

## แนวคิด

- `font.render(text, True, color)` → สร้าง surface
- `screen.blit(surface, (x, y))` → วางบนหน้าจอ
- `for j in range(4)` → วน 4 รอบแสดงตัวเลือก

---

## 📝 แก้ใน quiz.py

**แทนที่** `screen.fill("white")` ถึง `pygame.display.flip()` ด้วย:

```python
    screen.fill("white")

    if current_q < len(questions):
        # แสดงคำถาม
        q_surf = font_q.render(questions[current_q], True, "black")
        screen.blit(q_surf, (50, 80))

        # แสดงตัวเลือก 4 ข้อ
        labels = ["1", "2", "3", "4"]
        for j in range(4):
            c_surf = font_c.render(f"{labels[j]}. {choices[current_q][j]}", True, "navy")
            screen.blit(c_surf, (100, 200 + j * 70))
    else:
        done_surf = font_q.render("Quiz Complete!", True, "black")
        screen.blit(done_surf, (230, 280))

    pygame.display.flip()
```

> รันดู — ควรเห็นคำถามและตัวเลือก 4 ข้อ (ยังกดไม่ได้)
