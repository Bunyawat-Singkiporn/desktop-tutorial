# Week 6 - เช็คพอยต์ 2 : feedback ถูก/ผิด ด้วยสี
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Quiz Arena")
clock = pygame.time.Clock()

font_big = pygame.font.SysFont("tahoma", 40)
font_mid = pygame.font.SysFont("tahoma", 30)
font_sml = pygame.font.SysFont("tahoma", 20)

questions = [
    ["2 + 3 เท่ากับเท่าไร?", ["4", "5", "6", "7"], 2],
    ["สีของท้องฟ้าตอนกลางวัน?", ["แดง", "ฟ้า", "เขียว", "ดำ"], 2],
    ["Python ใช้คำสั่งใดแสดงผล?", ["show", "echo", "print", "say"], 3],
    ["1 สัปดาห์มีกี่วัน?", ["5", "6", "7", "8"], 3],
]

index = 0
score = 0
last_picked = 0
showing_result = False
finished = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and not finished:
            # --- ตอบคำถาม ---
            if not showing_result:
                picked = 0
                if event.key == pygame.K_1:
                    picked = 1
                if event.key == pygame.K_2:
                    picked = 2
                if event.key == pygame.K_3:
                    picked = 3
                if event.key == pygame.K_4:
                    picked = 4

                if picked > 0:
                    last_picked = picked
                    if picked == questions[index][2]:
                        score += 10
                    showing_result = True

            # --- ไปข้อถัดไป ---
            else:
                if event.key == pygame.K_SPACE:
                    showing_result = False
                    index += 1
                    if index >= len(questions):
                        finished = True

    screen.fill((25, 30, 50))

    title = font_big.render("QUIZ ARENA", True, "white")
    screen.blit(title, (50, 40))
    sc = font_mid.render(f"คะแนน {score}", True, "lightgreen")
    screen.blit(sc, (600, 50))

    if finished:
        end = font_big.render("จบเกม!", True, "white")
        screen.blit(end, (300, 280))
    else:
        q = questions[index]
        choices = q[1]
        answer = q[2]

        qtext = font_mid.render(q[0], True, "yellow")
        screen.blit(qtext, (60, 140))

        for i in range(4):
            y = 220 + i * 70
            number = i + 1
            color = (45, 55, 90)
            if showing_result:
                if number == answer:
                    color = (40, 140, 70)
                elif number == last_picked:
                    color = (170, 50, 60)

            pygame.draw.rect(screen, color, (100, y, 600, 55), border_radius=8)
            line = font_mid.render(f"{number})  {choices[i]}", True, "white")
            screen.blit(line, (125, y + 12))

        if showing_result:
            if last_picked == answer:
                msg = font_mid.render("ถูกต้อง! +10", True, "lightgreen")
            else:
                msg = font_mid.render(f"ผิด! คำตอบคือข้อ {answer}", True, "salmon")
            screen.blit(msg, (100, 500))
            hint = font_sml.render("กด Space เพื่อไปข้อถัดไป", True, "white")
            screen.blit(hint, (100, 550))
        else:
            hint = font_sml.render("กด 1-4 เพื่อตอบ", True, (150, 160, 200))
            screen.blit(hint, (100, 550))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
