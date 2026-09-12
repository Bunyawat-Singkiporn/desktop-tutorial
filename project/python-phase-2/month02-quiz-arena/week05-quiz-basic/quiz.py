# ============================================================
# Week 5 - QUIZ ARENA (Basic)   (เฉลย)
# แนวคิด: pygame window + list ซ้อน list + KEYDOWN + state
# รัน: python quiz.py     |     กด 1-4 เพื่อตอบ
# ============================================================
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Quiz Arena - Week 5")
clock = pygame.time.Clock()

# ---------- ฟอนต์ (tahoma รองรับภาษาไทย) ----------
font_big = pygame.font.SysFont("tahoma", 40)
font_mid = pygame.font.SysFont("tahoma", 30)
font_sml = pygame.font.SysFont("tahoma", 20)

# ---------- คลังคำถาม : [โจทย์, [ตัวเลือก 4], เฉลย 1-4] ----------
questions = [
    ["2 + 3 เท่ากับเท่าไร?", ["4", "5", "6", "7"], 2],
    ["สีของท้องฟ้าตอนกลางวัน?", ["แดง", "ฟ้า", "เขียว", "ดำ"], 2],
    ["Python ใช้คำสั่งใดแสดงผล?", ["show", "echo", "print", "say"], 3],
    ["1 สัปดาห์มีกี่วัน?", ["5", "6", "7", "8"], 3],
]

index = 0            # ตอนนี้อยู่คำถามข้อไหน
finished = False     # จบเกมหรือยัง

# ---------- Game Loop ----------
running = True
while running:

    # ===== INPUT =====
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if not finished:
                picked = 0
                if event.key == pygame.K_1:
                    picked = 1
                if event.key == pygame.K_2:
                    picked = 2
                if event.key == pygame.K_3:
                    picked = 3
                if event.key == pygame.K_4:
                    picked = 4

                # ===== PROCESS =====
                if picked > 0:
                    index += 1
                    if index >= len(questions):
                        finished = True

    # ===== OUTPUT =====
    screen.fill((25, 30, 50))

    title = font_big.render("QUIZ ARENA", True, "white")
    screen.blit(title, (50, 40))

    if finished:
        end = font_big.render("จบเกม!", True, "white")
        screen.blit(end, (300, 260))
        hint = font_sml.render("กด Esc เพื่อออก", True, (150, 160, 200))
        screen.blit(hint, (300, 330))
    else:
        # เลขข้อ มุมขวาบน
        page = font_mid.render(f"ข้อ {index + 1}/{len(questions)}", True, (150, 160, 200))
        screen.blit(page, (600, 50))

        q = questions[index]
        choices = q[1]

        qtext = font_mid.render(q[0], True, "yellow")
        screen.blit(qtext, (60, 140))

        for i in range(4):
            y = 220 + i * 70
            pygame.draw.rect(screen, (45, 55, 90), (100, y, 600, 55), border_radius=8)
            line = font_mid.render(f"{i + 1})  {choices[i]}", True, "white")
            screen.blit(line, (125, y + 12))

        hint = font_sml.render("กด 1-4 เพื่อตอบ  |  Esc เพื่อออก", True, (150, 160, 200))
        screen.blit(hint, (100, 545))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
