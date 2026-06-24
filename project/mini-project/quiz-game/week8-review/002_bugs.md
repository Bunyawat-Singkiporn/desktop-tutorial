## เป้าหมาย

ฝึก debug โค้ดที่มี bug

---

## โค้ดที่มีปัญหา

หา bug ให้ครบ **3 ที่** แล้วแก้:

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
font_q = pygame.font.Font(None, 48)
font_c = pygame.font.Font(None, 36)

questions = ["What is 2 + 2?", "Color of sky?"]
choices   = [["2","3","4","5"], ["red","blue","green","yellow"]]
answers   = [2, 1]

current_q = 0
feedback  = ""
score     = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and current_q < len(questions):
            key_map = {pygame.K_1: 0, pygame.K_2: 1, pygame.K_3: 2, pygame.K_4: 3}
            if event.key in key_map:
                picked = key_map[event.key]
                if picked == answers[current_q]:
                    feedback = "Correct!"
                else:
                    feedback = "Wrong!"
                    score += 1          # Bug 1
                current_q = current_q  # Bug 2

    screen.fill("white")

    if current_q < len(questions):
        q_surf = font_q.render(questions[current_q], True, "black")
        screen.blit(q_surf, (50, 80))
        labels = ["1", "2", "3", "4"]
        for j in range(4):
            c_surf = font_c.render(f"{labels[j]}. {choices[current_q][j]}", True, "navy")
            screen.blit(c_surf, (100, 200 + j * 70))

    if feedback:
        color = "green" if feedback == "Correct!" else "red"
        f_surf = font_c.render(feedback, True, color)
                screen.blit(f_surf, (50, 520))  # Bug 3

    pygame.display.flip()

pygame.quit()
```

---

## เฉลย

| Bug | ปัญหา | แก้เป็น |
|-----|--------|---------|
| Bug 1 | `score += 1` อยู่ใน `else` (ผิด) | ย้ายไปอยู่ใน `if picked == ...` |
| Bug 2 | `current_q = current_q` ไม่เปลี่ยน | `current_q += 1` |
| Bug 3 | `screen.blit` indent เกิน | ลด indent ให้ตรงกับ `f_surf = ...` |
