# ============================================================
# Week 11 - เช็คพอยต์ 2 : ตารางเหตุการณ์ (ยังไม่มีผลจริง)
# แนวคิด: random.shuffle / random.choice, ตารางเหตุการณ์, ตัวคูณคะแนน, ธง new_stage
# รัน: python game.py
# ปุ่ม: A-Z เดา | Space ไปด่านถัดไป | R เล่นใหม่ | Esc ออก
# ============================================================
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Word Hunter - Week 11")
clock = pygame.time.Clock()

font_big = pygame.font.SysFont("tahoma", 50)
font_mid = pygame.font.SysFont("tahoma", 26)
font_sml = pygame.font.SysFont("tahoma", 20)

BG    = (30, 40, 35)
GREY  = (170, 180, 175)
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MAX_LIVES = 6

# ---------- คลังคำ : [คำ, คำใบ้, หมวด] ----------
words = [
    ["DOG",      "สัตว์เลี้ยงที่ชอบเห่า",       "สัตว์"],
    ["ELEPHANT", "ตัวใหญ่ มีงวงยาว",           "สัตว์"],
    ["PYTHON",   "ภาษาโปรแกรมที่เรากำลังเรียน", "คอมพิวเตอร์"],
    ["RAINBOW",  "เกิดหลังฝนตก มี 7 สี",       "ธรรมชาติ"],
    ["SCHOOL",   "สถานที่ที่เรามาเรียน",         "สถานที่"],
    ["KEYBOARD", "อุปกรณ์ที่ใช้พิมพ์",           "คอมพิวเตอร์"],
]

# ---------- ตารางเหตุการณ์ : [รหัส, ข้อความ] ----------
events = [
    ["lucky", "โชคดี! เปิดให้ 1 ตัวฟรี"],
    ["bless", "ได้รับพร! ชีวิต +1"],
    ["trap",  "กับดัก! ชีวิต -1"],
    ["bonus", "โบนัส! ด่านนี้คะแนนคูณ 2"],
    ["none",  "ด่านธรรมดา"],
    ["none",  "ด่านธรรมดา"],
]

# ---------- ตัวแปรทั้งเกม ----------
random.shuffle(words)
level = 0
score = 0

# ---------- ตัวแปรของด่าน ----------
guessed = []
lives = MAX_LIVES
multiplier = 1
event = events[4]
stage_over = False
game_over = False
win = False
new_stage = True        # ธง: ขอตั้งค่าด่านใหม่

running = True
while running:

    # ==================== INPUT ====================
    for event_pg in pygame.event.get():
        if event_pg.type == pygame.QUIT:
            running = False

        if event_pg.type == pygame.KEYDOWN:
            if event_pg.key == pygame.K_ESCAPE:
                running = False

            # ----- เริ่มเกมใหม่ทั้งหมด -----
            if event_pg.key == pygame.K_r:
                random.shuffle(words)
                level = 0
                score = 0
                stage_over = False
                game_over = False
                win = False
                new_stage = True

            # ----- จบด่าน : Space ไปด่านถัดไป -----
            elif stage_over and not game_over:
                if event_pg.key == pygame.K_SPACE:
                    level += 1
                    if level >= len(words):
                        level = len(words) - 1
                        game_over = True
                    else:
                        stage_over = False
                        new_stage = True

            # ----- กำลังเล่น : เดาตัวอักษร -----
            elif not game_over:
                letter = pygame.key.name(event_pg.key).upper()
                if len(letter) == 1 and letter in ALPHA:
                    if letter not in guessed:
                        guessed.append(letter)
                        if letter not in words[level][0]:
                            lives -= 1

    # ==================== PROCESS ====================

    # ---------- ตั้งค่าด่านใหม่ (ทำครั้งเดียว) ----------
    if new_stage:
        new_stage = False
        guessed = []
        lives = MAX_LIVES
        multiplier = 1
        event = random.choice(events)


    word     = words[level][0]
    hint     = words[level][1]
    category = words[level][2]

    # ---------- เช็กชนะ ----------
    win = True
    for ch in word:
        if ch not in guessed:
            win = False

    # ---------- จบด่าน (guard) ----------
    if not stage_over:
        if win:
            score += (len(word) + lives * 2) * multiplier
            stage_over = True
        elif lives <= 0:
            stage_over = True
            game_over = True

    # ==================== OUTPUT ====================
    screen.fill(BG)

    screen.blit(font_mid.render("WORD HUNTER", True, "white"), (40, 20))
    screen.blit(font_sml.render(f"คะแนน {score}", True, "lightgreen"), (40, 56))
    screen.blit(font_sml.render(f"ด่าน {level + 1}/{len(words)}", True, GREY), (330, 28))

    for i in range(MAX_LIVES + 1):
        color = (220, 70, 70) if i < lives else (70, 80, 75)
        pygame.draw.circle(screen, color, (580 + i * 30, 34), 10)

    if game_over:
        pygame.draw.rect(screen, (45, 60, 52), (150, 130, 500, 240), border_radius=14)
        if win:
            screen.blit(font_big.render("ผ่านทุกด่าน!", True, "lightgreen"), (250, 165))
        else:
            screen.blit(font_big.render("เกมจบ", True, "salmon"), (330, 165))
            screen.blit(font_sml.render(f"คำตอบคือ {word}", True, "white"), (320, 235))
        screen.blit(font_mid.render(f"คะแนนรวม {score}", True, "gold"), (310, 275))
        screen.blit(font_sml.render("กด R เพื่อเล่นใหม่  |  Esc ออก", True, GREY), (280, 325))

    else:
        # ---------- ข้อความเหตุการณ์ ----------
        if event[0] == "trap":
            ev_color = "salmon"
        elif event[0] == "none":
            ev_color = GREY
        else:
            ev_color = "orange"
        screen.blit(font_sml.render(f"เหตุการณ์: {event[1]}", True, ev_color), (40, 84))

        screen.blit(font_sml.render(f"[ {category} ]", True, "cyan"), (40, 118))
        screen.blit(font_mid.render(hint, True, "yellow"), (40, 142))

        shown = ""
        for ch in word:
            if ch in guessed:
                shown += ch + " "
            else:
                shown += "_ "

        text = font_big.render(shown, True, "white")
        screen.blit(text, (400 - text.get_width() // 2, 210))

        screen.blit(font_sml.render(f"เดาไปแล้ว : {' '.join(guessed)}", True, GREY), (40, 330))

        if stage_over:
            got = (len(word) + lives * 2) * multiplier
            screen.blit(font_mid.render(f"ผ่านด่าน! +{got} คะแนน", True, "lightgreen"), (40, 385))
            screen.blit(font_sml.render("กด Space เพื่อไปด่านถัดไป", True, "white"), (40, 435))
        else:
            screen.blit(font_sml.render("กดตัวอักษร A-Z เพื่อเดา  |  R เริ่มใหม่  |  Esc ออก", True, GREY), (40, 435))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
