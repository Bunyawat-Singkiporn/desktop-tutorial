# ============================================================
# Week 6 - QUIZ ARENA (Feedback + Score)   (เฉลย)
# แนวคิด: เช็กคำตอบ, คะแนน, state โชว์เฉลย, จอสรุปผล, รีเซ็ตเกม
# รัน: python quiz.py
# ปุ่ม: 1-4 ตอบ | Space ไปต่อ | R เล่นใหม่ | Esc ออก
# ============================================================
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Quiz Arena - Week 6")
clock = pygame.time.Clock()

font_big = pygame.font.SysFont("tahoma", 40)
font_mid = pygame.font.SysFont("tahoma", 30)
font_sml = pygame.font.SysFont("tahoma", 20)

# ---------- สี ----------
BG      = (25, 30, 50)
BOX     = (45, 55, 90)
GREEN   = (40, 140, 70)
RED     = (170, 50, 60)
GREY    = (150, 160, 200)

# ---------- คลังคำถาม : [โจทย์, [ตัวเลือก], เฉลย 1-4] ----------
questions = [
    ["2 + 3 เท่ากับเท่าไร?", ["4", "5", "6", "7"], 2],
    ["สีของท้องฟ้าตอนกลางวัน?", ["แดง", "ฟ้า", "เขียว", "ดำ"], 2],
    ["Python ใช้คำสั่งใดแสดงผล?", ["show", "echo", "print", "say"], 3],
    ["1 สัปดาห์มีกี่วัน?", ["5", "6", "7", "8"], 3],
    ["สัตว์ชนิดใดไม่ใช่แมลง?", ["มด", "ผึ้ง", "แมงมุม", "แมลงวัน"], 3],
]

# ---------- ตัวแปรของเกม ----------
index = 0                # ข้อที่กำลังถาม
score = 0                # คะแนนสะสม
correct = 0              # จำนวนข้อที่ถูก
last_picked = 0          # ข้อที่ผู้เล่นเพิ่งเลือก
showing_result = False   # กำลังโชว์เฉลยอยู่ไหม
finished = False         # จบเกมหรือยัง

running = True
while running:

    # ================= INPUT =================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            # ----- จบเกมแล้ว : กด R เริ่มใหม่ -----
            if finished:
                if event.key == pygame.K_r:
                    index = 0
                    score = 0
                    correct = 0
                    last_picked = 0
                    showing_result = False
                    finished = False

            # ----- กำลังโชว์เฉลย : กด Space ไปต่อ -----
            elif showing_result:
                if event.key == pygame.K_SPACE:
                    showing_result = False
                    index += 1
                    if index >= len(questions):
                        finished = True

            # ----- กำลังถามคำถาม : กด 1-4 ตอบ -----
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
                    if picked == questions[index][2]:
                        score += 10
                        correct += 1
                    showing_result = True

    # ================= OUTPUT =================
    screen.fill(BG)

    title = font_big.render("QUIZ ARENA", True, "white")
    screen.blit(title, (50, 40))
    sc = font_mid.render(f"คะแนน {score}", True, "lightgreen")
    screen.blit(sc, (590, 50))

    if finished:
        # ---------- จอสรุปผล ----------
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
        screen.blit(font_mid.render(f"คะแนน {score} / {total * 10}", True, "white"), (250, 270))
        screen.blit(font_mid.render(f"ตอบถูก {correct} / {total} ข้อ", True, "white"), (250, 315))
        screen.blit(font_big.render(medal, True, "gold"), (250, 365))
        screen.blit(font_sml.render("กด R เพื่อเล่นใหม่  |  Esc เพื่อออก", True, GREY), (250, 480))

    else:
        # ---------- จอคำถาม ----------
        q = questions[index]
        choices = q[1]
        answer = q[2]

        page = font_sml.render(f"ข้อ {index + 1}/{len(questions)}", True, GREY)
        screen.blit(page, (60, 105))

        qtext = font_mid.render(q[0], True, "yellow")
        screen.blit(qtext, (60, 140))

        for i in range(4):
            y = 215 + i * 68
            number = i + 1
            color = BOX
            if showing_result:
                if number == answer:
                    color = GREEN
                elif number == last_picked:
                    color = RED

            pygame.draw.rect(screen, color, (100, y, 600, 55), border_radius=8)
            line = font_mid.render(f"{number})  {choices[i]}", True, "white")
            screen.blit(line, (125, y + 12))

        if showing_result:
            if last_picked == answer:
                msg = font_mid.render("ถูกต้อง! +10", True, "lightgreen")
            else:
                msg = font_mid.render(f"ผิด! คำตอบคือข้อ {answer}", True, "salmon")
            screen.blit(msg, (100, 500))
            screen.blit(font_sml.render("กด Space เพื่อไปข้อถัดไป", True, "white"), (100, 550))
        else:
            screen.blit(font_sml.render("กด 1-4 เพื่อตอบ  |  Esc ออก", True, GREY), (100, 550))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
