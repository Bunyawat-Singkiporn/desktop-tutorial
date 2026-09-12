# ============================================================
# Week 8 - BUGGY QUIZ : เกมนี้มีบั๊ก 4 ตัว ตามล่าให้เจอ!
# ภารกิจ: หาบั๊ก 4 ตัวแล้วแก้ให้ถูก (เฉลยอยู่ใน 003_fix.md)
# รัน: python quiz.py
# ปุ่ม: 1-4 ตอบ | Space ไปต่อ | R เล่นใหม่ | Esc ออก
# ============================================================
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Quiz Arena - Week 7")
clock = pygame.time.Clock()

font_big = pygame.font.SysFont("tahoma", 40)
font_mid = pygame.font.SysFont("tahoma", 30)
font_sml = pygame.font.SysFont("tahoma", 20)

BG    = (25, 30, 50)
BOX   = (45, 55, 90)
GREEN = (40, 140, 70)
RED   = (170, 50, 60)
GREY  = (150, 160, 200)

questions = [
    ["2 + 3 เท่ากับเท่าไร?", ["4", "5", "6", "7"], 2],
    ["สีของท้องฟ้าตอนกลางวัน?", ["แดง", "ฟ้า", "เขียว", "ดำ"], 2],
    ["Python ใช้คำสั่งใดแสดงผล?", ["show", "echo", "print", "say"], 3],
    ["1 สัปดาห์มีกี่วัน?", ["5", "6", "7", "8"], 3],
    ["สัตว์ชนิดใดไม่ใช่แมลง?", ["มด", "ผึ้ง", "แมงมุม", "แมลงวัน"], 3],
]

TIME_LIMIT = 10          # วินาทีต่อข้อ
BAR_W = 600

index = 0
score = 0
correct = 0
last_picked = 0          # 0 = หมดเวลา (ไม่ได้เลือก)
last_bonus = 0
showing_result = False
finished = False

question_start = pygame.time.get_ticks()
time_left = TIME_LIMIT

running = True
while running:
    score = 0        # <-- ตรงนี้น่าสงสัยไหม?

    # ================= INPUT =================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            # ----- จบเกม : R เริ่มใหม่ -----
            if finished:
                if event.key == pygame.K_r:
                    index = 0
                    score = 0
                    correct = 0
                    last_picked = 0
                    last_bonus = 0
                    showing_result = False
                    finished = False
                    question_start = pygame.time.get_ticks()

            # ----- โชว์เฉลย : Space ไปต่อ -----
            elif showing_result:
                if event.key == pygame.K_SPACE:
                    showing_result = False
                    index += 1
                    if index > len(questions):
                        finished = True

            # ----- ถามคำถาม : 1-4 ตอบ -----
            else:
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
                    last_bonus = 0
                    if picked == questions[index][1]:
                        last_bonus = int(time_left)      # ตอบไว = โบนัสเยอะ
                        score += 10 + last_bonus
                        correct += 1
                    showing_result = True

    # ================= PROCESS : เวลา =================
    if not finished and not showing_result:
        passed = (pygame.time.get_ticks() - question_start) / 1000
        time_left = TIME_LIMIT - passed

        if time_left <= 0:
            time_left = 0
            last_picked = 0            # หมดเวลา
            last_bonus = 0
            showing_result = True

    # ================= OUTPUT =================
    screen.fill(BG)

    screen.blit(font_big.render("QUIZ ARENA", True, "white"), (50, 30))
    screen.blit(font_mid.render(f"คะแนน {score}", True, "lightgreen"), (590, 40))

    if finished:
        total = len(questions)
        if correct == total:
            medal = "GOLD"
        elif correct >= total / 2:
            medal = "SILVER"
        elif correct > 0:
            medal = "BRONZE"
        else:
            medal = "ลองใหม่นะ"

        pygame.draw.rect(screen, BOX, (150, 170, 500, 280), border_radius=12)
        screen.blit(font_big.render("จบเกม!", True, "white"), (330, 195))
        screen.blit(font_mid.render(f"คะแนนรวม {score}", True, "white"), (250, 270))
        screen.blit(font_mid.render(f"ตอบถูก {correct} / {total} ข้อ", True, "white"), (250, 315))
        screen.blit(font_big.render(medal, True, "gold"), (250, 365))
        screen.blit(font_sml.render("กด R เพื่อเล่นใหม่  |  Esc เพื่อออก", True, GREY), (250, 480))

    else:
        q = questions[index]
        choices = q[1]
        answer = q[2]

        screen.blit(font_sml.render(f"ข้อ {index + 1}/{len(questions)}", True, GREY), (52, 85))

        # ---------- แถบเวลา ----------
        ratio = time_left / TIME_LIMIT
        if ratio < 0:
            ratio = 0

        if time_left > 5:
            bar_color = (60, 200, 110)
        elif time_left > 2:
            bar_color = (240, 200, 60)
        else:
            bar_color = (230, 70, 70)

        pygame.draw.rect(screen, (60, 65, 90), (100, 112, BAR_W, 16), border_radius=8)
        pygame.draw.rect(screen, bar_color, (100, 112, int(BAR_W * ratio), 16), border_radius=8)
        screen.blit(font_sml.render(f"{round(time_left, 1)} วิ", True, bar_color), (712, 108))

        # ---------- คำถาม ----------
        screen.blit(font_mid.render(q[0], True, "yellow"), (60, 148))

        for i in range(4):
            y = 210 + i * 68
            number = i + 1
            color = BOX
            if showing_result:
                if number == answer:
                    color = GREEN
                elif number == last_picked:
                    color = RED

            pygame.draw.rect(screen, color, (100, y, 600, 55), border_radius=8)
            screen.blit(font_mid.render(f"{number})  {choices[i]}", True, "white"), (125, y + 12))

        # ---------- feedback ----------
        if showing_result:
            if last_picked == 0:
                msg = font_mid.render(f"หมดเวลา! คำตอบคือข้อ {answer}", True, "orange")
            elif last_picked == answer:
                msg = font_mid.render(f"ถูกต้อง! +{10 + last_bonus}  (โบนัสเร็ว +{last_bonus})", True, "lightgreen")
            else:
                msg = font_mid.render(f"ผิด! คำตอบคือข้อ {answer}", True, "salmon")
            screen.blit(msg, (100, 495))
            screen.blit(font_sml.render("กด Space เพื่อไปข้อถัดไป", True, "white"), (100, 548))
        else:
            screen.blit(font_sml.render("กด 1-4 เพื่อตอบ  |  ตอบไวได้โบนัส", True, GREY), (100, 548))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
