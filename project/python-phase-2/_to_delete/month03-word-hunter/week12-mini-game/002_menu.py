# ============================================================
# Week 12 - เช็คพอยต์ 1 : หน้าเริ่มเกม + สถิติสูงสุด
# รวม: หน้าเริ่มเกม + คลังคำสุ่ม + คำใบ้ + ระบบชีวิต + เหตุการณ์สุ่ม
#      + ตัวคูณคะแนน + แป้น A-Z + แถบความคืบหน้า + สรุปผล + high score
# รัน: python game.py
# ปุ่ม: Space เริ่ม/ไปด่านถัดไป | A-Z เดา | R กลับเมนู | Esc ออก
# ============================================================
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 560))
pygame.display.set_caption("Word Hunter v1.0")
clock = pygame.time.Clock()

font_big = pygame.font.SysFont("tahoma", 46)
font_mid = pygame.font.SysFont("tahoma", 26)
font_sml = pygame.font.SysFont("tahoma", 19)

BG    = (30, 40, 35)
PANEL = (45, 60, 52)
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

# ---------- ตัวแปรที่อยู่ตลอดไป ----------
best = 0

# ---------- ตัวแปรของรอบการเล่น ----------
started = False
level = 0
score = 0
guessed = []
lives = MAX_LIVES
multiplier = 1
event = events[4]
stage_over = False
game_over = False
win = False
new_stage = False

running = True
while running:

    # ==================== INPUT ====================
    for event_pg in pygame.event.get():
        if event_pg.type == pygame.QUIT:
            running = False

        if event_pg.type == pygame.KEYDOWN:
            if event_pg.key == pygame.K_ESCAPE:
                running = False

            # ----- state 1 : หน้าเริ่มเกม -----
            if not started:
                if event_pg.key == pygame.K_SPACE:
                    random.shuffle(words)
                    started = True
                    level = 0
                    score = 0
                    stage_over = False
                    game_over = False
                    win = False
                    new_stage = True

            # ----- state 4 : จบเกม -----
            elif game_over:
                if event_pg.key == pygame.K_r:
                    started = False        # กลับหน้าเมนู

            # ----- state 3 : จบด่าน -----
            elif stage_over:
                if event_pg.key == pygame.K_SPACE:
                    level += 1
                    if level >= len(words):
                        level = len(words) - 1
                        game_over = True
                        if score > best:
                            best = score
                    else:
                        stage_over = False
                        new_stage = True

            # ----- state 2 : กำลังเดา -----
            else:
                letter = pygame.key.name(event_pg.key).upper()
                if len(letter) == 1 and letter in ALPHA:
                    if letter not in guessed:
                        guessed.append(letter)
                        if letter not in words[level][0]:
                            lives -= 1

    # ==================== PROCESS ====================
    if started:

        # ---------- ตั้งค่าด่านใหม่ (ทำครั้งเดียว) ----------
        if new_stage:
            new_stage = False
            guessed = []
            lives = MAX_LIVES
            multiplier = 1
            event = random.choice(events)

            if event[0] == "lucky":
                guessed.append(random.choice(words[level][0]))
            elif event[0] == "bless":
                lives += 1
            elif event[0] == "trap":
                lives -= 1
            elif event[0] == "bonus":
                multiplier = 2

        word     = words[level][0]
        hint     = words[level][1]
        category = words[level][2]

        # ---------- เช็กชนะด่าน ----------
        win = True
        for ch in word:
            if ch not in guessed:
                win = False

        # ---------- จบด่าน (guard) ----------
        if not stage_over and not game_over:
            if win:
                score += (len(word) + lives * 2) * multiplier
                stage_over = True
            elif lives <= 0:
                stage_over = True
                game_over = True
                if score > best:
                    best = score

    # ==================== OUTPUT ====================
    screen.fill(BG)

    # ---------- state 1 : หน้าเริ่มเกม ----------
    if not started:
        pygame.draw.rect(screen, PANEL, (140, 110, 520, 340), border_radius=16)

        t = font_big.render("WORD HUNTER v1.0", True, "white")
        screen.blit(t, (400 - t.get_width() // 2, 150))

        t = font_sml.render(f"ทายคำจากคำใบ้ {len(words)} ด่าน", True, GREY)
        screen.blit(t, (400 - t.get_width() // 2, 230))
        t = font_sml.render("ระวังกับดัก เก็บโบนัส!", True, GREY)
        screen.blit(t, (400 - t.get_width() // 2, 260))

        t = font_mid.render("กด Space เพื่อเริ่ม", True, "yellow")
        screen.blit(t, (400 - t.get_width() // 2, 320))

        if best > 0:
            t = font_sml.render(f"สถิติสูงสุด : {best}", True, "gold")
            screen.blit(t, (400 - t.get_width() // 2, 390))

    # ---------- state 4 : จอสรุปผล ----------
    elif game_over:
        pygame.draw.rect(screen, PANEL, (140, 130, 520, 300), border_radius=16)

        if win:
            t = font_big.render("ผ่านทุกด่าน!", True, "lightgreen")
        else:
            t = font_big.render("เกมจบ", True, "salmon")
        screen.blit(t, (400 - t.get_width() // 2, 165))

        if not win:
            t = font_sml.render(f"คำตอบคือ {words[level][0]}", True, "white")
            screen.blit(t, (400 - t.get_width() // 2, 235))

        t = font_mid.render(f"คะแนนรวม {score}", True, "gold")
        screen.blit(t, (400 - t.get_width() // 2, 275))
        t = font_sml.render(f"สถิติสูงสุด {best}", True, "gold")
        screen.blit(t, (400 - t.get_width() // 2, 320))
        t = font_sml.render("กด R เพื่อกลับเมนู  |  Esc ออก", True, GREY)
        screen.blit(t, (400 - t.get_width() // 2, 370))

    # ---------- state 2-3 : กำลังเล่น ----------
    else:
        # แถบบน
        screen.blit(font_mid.render("WORD HUNTER", True, "white"), (40, 18))
        screen.blit(font_sml.render(f"คะแนน {score}", True, "lightgreen"), (40, 54))
        screen.blit(font_sml.render(f"ด่าน {level + 1}/{len(words)}", True, GREY), (330, 24))

        # แถบความคืบหน้า
        pygame.draw.rect(screen, (60, 75, 68), (330, 50, 200, 8), border_radius=4)
        pygame.draw.rect(screen, (90, 190, 130),
                         (330, 50, int(200 * (level / len(words))), 8), border_radius=4)

        # ชีวิต
        for i in range(MAX_LIVES + 1):
            color = (220, 70, 70) if i < lives else (70, 80, 75)
            pygame.draw.circle(screen, color, (580 + i * 30, 30), 10)

        # เหตุการณ์
        if event[0] == "trap":
            ev_color = "salmon"
        elif event[0] == "none":
            ev_color = GREY
        else:
            ev_color = "orange"
        screen.blit(font_sml.render(f"เหตุการณ์: {event[1]}", True, ev_color), (40, 82))

        # คำใบ้
        screen.blit(font_sml.render(f"[ {category} ]", True, "cyan"), (40, 116))
        screen.blit(font_mid.render(hint, True, "yellow"), (40, 140))

        # คำลับ
        shown = ""
        for ch in word:
            if ch in guessed:
                shown += ch + " "
            else:
                shown += "_ "
        t = font_big.render(shown, True, "white")
        screen.blit(t, (400 - t.get_width() // 2, 200))

        screen.blit(font_sml.render(f"เดาไปแล้ว : {' '.join(guessed)}", True, GREY), (40, 300))

        # ข้อความล่าง
        if stage_over:
            got = (len(word) + lives * 2) * multiplier
            screen.blit(font_mid.render(f"ผ่านด่าน! +{got} คะแนน", True, "lightgreen"), (40, 400))
            screen.blit(font_sml.render("กด Space เพื่อไปด่านถัดไป", True, "white"), (40, 445))
        else:
            screen.blit(font_sml.render("กดตัวอักษร A-Z เพื่อเดา  |  Esc ออก", True, GREY), (40, 445))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
