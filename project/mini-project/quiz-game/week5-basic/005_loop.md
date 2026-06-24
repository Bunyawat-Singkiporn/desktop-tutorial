## เป้าหมาย

ตรวจการกดปุ่ม 1/2/3/4 และตรวจคำตอบ

---

## แนวคิด

`key_map` เชื่อม key กับ index ตัวเลือก:

```python
key_map = {pygame.K_1: 0, pygame.K_2: 1, pygame.K_3: 2, pygame.K_4: 3}
```

กด `K_1` → index `0` → เทียบกับ `answers[current_q]`

---

## 📝 เพิ่มใน quiz.py

**1.** เพิ่มใน for event loop หลัง `pygame.QUIT`:

```python
        if event.type == pygame.KEYDOWN and current_q < len(questions):
            key_map = {pygame.K_1: 0, pygame.K_2: 1,
                       pygame.K_3: 2, pygame.K_4: 3}
            if event.key in key_map:
                picked = key_map[event.key]
                if picked == answers[current_q]:
                    feedback = "Correct!"
                else:
                    feedback = "Wrong! Answer: " + choices[current_q][answers[current_q]]
                current_q += 1
```

**2.** เพิ่มก่อน `pygame.display.flip()`:

```python
    if feedback:
        color = "green" if feedback == "Correct!" else "red"
        f_surf = font_c.render(feedback, True, color)
        screen.blit(f_surf, (50, 520))
```

> รันทดสอบ — กด 1/2/3/4 ได้แล้ว!
