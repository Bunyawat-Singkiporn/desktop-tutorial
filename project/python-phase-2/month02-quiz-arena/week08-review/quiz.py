# ============================================================
# QUIZ ARENA v1.0  -  เกมสมบูรณ์ปิดเดือน 2  (เฉลย Week 8)
# รวม: หน้าเริ่มเกม + คำถามสลับ + จับเวลา + feedback + คะแนน
#      + โบนัสความเร็ว + สรุปผล + เหรียญ + สถิติสูงสุด + เล่นใหม่
# รัน: python quiz.py
# ปุ่ม: Space เริ่ม/ไปต่อ | 1-4 ตอบ | R เล่นใหม่ | Esc ออก
# ============================================================
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Quiz Arena v1.0")
clock = pygame.time.Clock()

font_big = pygame.font.SysFont("tahoma", 40)
font_mid = pygame.font.SysFont("tahoma", 30)
font_sml = pygame.font.SysFont("tahoma", 20)

# ---------- สี ----------
BG    = (25, 30, 50)
BOX   = (45, 55, 90)
GREEN = (40, 140, 70)
RED   = (170, 50, 60)
GREY  = (150, 160, 200)

# ---------- คลังคำถาม : [โจทย์, [ตัวเลือก 4], เฉลย 1-4] ----------
questions = [
    ["2 + 3 เท่ากับเท่าไร?", ["4", "5", "6", "7"], 2],
    ["สีของท้องฟ้าตอนกลางวัน?", ["แดง", "ฟ้า", "เขียว", "ดำ"], 2],
    ["Python ใช้คำสั่งใดแสดงผล?", ["show", "echo", "print", "say"], 3],
    ["1 สัปดาห์มีกี่วัน?", ["5", "6", "7", "8"], 3],
    ["สัตว์ชนิดใดไม่ใช่แมลง?", ["มด", "ผึ้ง", "แมงมุม", "แมลงวัน"], 3],
    ["ดาวเคราะห์ที่อยู่ใกล้ดวงอาทิตย์ที่สุด?", ["โลก", "ศุกร์", "พุธ", "อังคาร"], 3],
]

TIME_LIMIT = 10
BAR_W = 600

# ---------- ตัวแปรทั้งเกม ----------
best = 0                 # สถิติสูงสุด (อยู่นอกการรีเซ็ต)

# ---------- ตัวแปรของรอบการเล่น ----------
index = 0
score = 0
correct = 0
last_picked = 0
last_bonus = 0
showing_result = False
finished = False
started = False
question_start = pygame.time.get_ticks()
time_left = TIME_LIMIT

running = True
while running:

    # ==================== INPUT ====================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            # ----- state 1 : หน้าเริ่มเกม -----
            if not started:
                if event.key == pygame.K_SPACE:
                    random.shuffle(questions)
                    started = True
                    question_start = pygame.time.get_ticks()

            # ----- state 4 : จบเกม -----
            elif finished:
                if event.key == pygame.K_r:
                    random.shuffle(questions)
                    index = 0
                    score = 0
                    correct = 0
                    last_picked = 0
                    last_bonus = 0
                    showing_result = False
                    finished = False
                    question_start = pygame.time.get_ticks()

            # ----- state 3 : โชว์เฉลย -----
            elif showing_result:
                if event.key == pygame.K_SPACE:
                    showing_result = False
                    index += 1
                    if index >= len(questions):
                        finished = True
                        if score > best:
                            best = score
                    else:
                        question_start = pygame.time.get_ticks()

            # ----- state 2 : กำลังถามคำถาม -----
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
                    if picked == questions[index][2]:
                        last_bonus = int(time_left)
                        score += 10 + last_bonus
                        correct += 1
                    showing_result = True

    # ==================== PROCESS ====================
    if started and not finished and not showing_result:
        passed = (pygame.time.get_ticks() - question_start) / 1000
        time_left = TIME_LIMIT - passed
        if time_left <= 0:
            time_left = 0
            last_picked = 0
            last_bonus = 0
            showing_result = True

    # ==================== OUTPUT ====================
    screen.fill(BG)

    # ---------- state 1 : หน้าเริ่มเกม ----------
    if not started:
        pygame.draw.rect(screen, BOX, (140, 150, 520, 300), border_radius=14)
        screen.blit(font_big.render("QUIZ ARENA v1.0", True, "white"), (230, 185))
        screen.blit(font_sml.render(f"คำถาม {len(questions)} ข้อ  |  ข้อละ {TIME_LIMIT} วินาที", True, GREY), (245, 260))
        screen.blit(font_sml.render("ตอบไวได้คะแนนโบนัส", True, GREY), (245, 292))
        screen.blit(font_mid.render("กด Space เพื่อเริ่ม", True, "yellow"), (275, 350))
        if best > 0:
            screen.blit(font_sml.render(f"สถิติสูงสุด {best}", True, "gold"), (330, 410))

    # ---------- state 4 : จอสรุปผล ----------
    elif finished:
        total = len(questions)
        if correct == total:
            medal = "GOLD"
        elif correct >= total / 2:
            medal = "SILVER"
        elif correct > 0:
            medal = "BRONZE"
        else:
            medal = "ลองใหม่นะ"

        pygame.draw.rect(screen, BOX, (140, 140, 520, 330), border_radius=14)
        screen.blit(font_big.render("จบเกม!", True, "white"), (330, 165))
        screen.blit(font_mid.render(f"คะแนนรวม {score}", True, "white"), (250, 245))
        screen.blit(font_mid.render(f"ตอบถูก {correct} / {total} ข้อ", True, "white"), (250, 290))
        screen.blit(font_big.render(medal, True, "gold"), (250, 340))
        screen.blit(font_sml.render(f"สถิติสูงสุด {best}", True, "gold"), (250, 405))
        screen.blit(font_sml.render("กด R เล่นใหม่  |  Esc ออก", True, GREY), (250, 435))

    # ---------- state 2-3 : กำลังเล่น ----------
    else:
        q = questions[index]
        choices = q[1]
        answer = q[2]

        screen.blit(font_big.render("QUIZ ARENA", True, "white"), (50, 25))
        screen.blit(font_mid.render(f"คะแนน {score}", True, "lightgreen"), (590, 35))
        screen.blit(font_sml.render(f"ข้อ {index + 1}/{len(questions)}", True, GREY), (52, 80))

        # แถบความคืบหน้า
        done_ratio = index / len(questions)
        pygame.draw.rect(screen, (60, 65, 90), (150, 86, 500, 8), border_radius=4)
        pygame.draw.rect(screen, (90, 130, 220), (150, 86, int(500 * done_ratio), 8), border_radius=4)

        # แถบเวลา
        ratio = time_left / TIME_LIMIT
        if ratio < 0:
            ratio = 0
        if time_left > 5:
            bar_color = (60, 200, 110)
        elif time_left > 2:
            bar_color = (240, 200, 60)
        else:
            bar_color = (230, 70, 70)

        pygame.draw.rect(screen, (60, 65, 90), (100, 110, BAR_W, 16), border_radius=8)
        pygame.draw.rect(screen, bar_color, (100, 110, int(BAR_W * ratio), 16), border_radius=8)
        screen.blit(font_sml.render(f"{round(time_left, 1)} วิ", True, bar_color), (712, 106))

        # คำถาม
        screen.blit(font_mid.render(q[0], True, "yellow"), (60, 146))

        # ตัวเลือก
        for i in range(4):
            y = 208 + i * 68
            number = i + 1
            color = BOX
            if showing_result:
                if number == answer:
                    color = GREEN
                elif number == last_picked:
                    color = RED

            pygame.draw.rect(screen, color, (100, y, 600, 55), border_radius=8)
            screen.blit(font_mid.render(f"{number})  {choices[i]}", True, "white"), (125, y + 12))

        # feedback
        if showing_result:
            if last_picked == 0:
                msg = font_mid.render(f"หมดเวลา! คำตอบคือข้อ {answer}", True, "orange")
            elif last_picked == answer:
                msg = font_mid.render(f"ถูกต้อง! +{10 + last_bonus} (โบนัสเร็ว +{last_bonus})", True, "lightgreen")
            else:
                msg = font_mid.render(f"ผิด! คำตอบคือข้อ {answer}", True, "salmon")
            screen.blit(msg, (100, 492))
            screen.blit(font_sml.render("กด Space เพื่อไปข้อถัดไป", True, "white"), (100, 545))
        else:
            screen.blit(font_sml.render("กด 1-4 เพื่อตอบ  |  ตอบไวได้โบนัส  |  Esc ออก", True, GREY), (100, 545))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
