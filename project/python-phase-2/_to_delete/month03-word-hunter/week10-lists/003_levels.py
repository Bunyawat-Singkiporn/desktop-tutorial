# ============================================================
# Week 10 - เช็คพอยต์ 2 : เล่นหลายด่านต่อกัน
# แนวคิด: list ซ้อน list, level, รีเซ็ตด่าน, สูตรคะแนน, guard
# รัน: python game.py
# ปุ่ม: A-Z เดา | Space ไปด่านถัดไป | R เล่นใหม่ | Esc ออก
# ============================================================
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Word Hunter - Week 10")
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
]

# ---------- ตัวแปรทั้งเกม ----------
level = 0
score = 0

# ---------- ตัวแปรของด่าน ----------
guessed = []
lives = MAX_LIVES
stage_over = False
game_over = False
win = False

running = True
while running:

    # ==================== INPUT ====================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            # ----- เริ่มเกมใหม่ทั้งหมด -----
            if event.key == pygame.K_r:
                level = 0
                score = 0
                guessed = []
                lives = MAX_LIVES
                stage_over = False
                game_over = False
                win = False

            # ----- จบด่าน (ชนะ) : Space ไปด่านถัดไป -----
            elif stage_over and not game_over:
                if event.key == pygame.K_SPACE:
                    level += 1
                    if level >= len(words):
                        level = len(words) - 1
                        game_over = True
                    else:
                        guessed = []
                        lives = MAX_LIVES
                        stage_over = False

            # ----- กำลังเล่น : เดาตัวอักษร -----
            elif not game_over:
                letter = pygame.key.name(event.key).upper()
                if len(letter) == 1 and letter in ALPHA:
                    if letter not in guessed:
                        guessed.append(letter)
                        if letter not in words[level][0]:
                            lives -= 1

    # ==================== PROCESS ====================
    word     = words[level][0]
    hint     = words[level][1]
    category = words[level][2]

    win = True
    for ch in word:
        if ch not in guessed:
            win = False

    # จบด่าน (guard: ทำครั้งเดียว)
    if not stage_over:
        if win:
            stage_over = True
        elif lives <= 0:
            stage_over = True
            game_over = True                    # ชีวิตหมด = จบเกม

    # ==================== OUTPUT ====================
    screen.fill(BG)

    screen.blit(font_mid.render("WORD HUNTER", True, "white"), (40, 22))
    screen.blit(font_sml.render(f"ด่าน {level + 1}/{len(words)}", True, GREY), (330, 30))

    for i in range(MAX_LIVES):
        color = (220, 70, 70) if i < lives else (70, 80, 75)
        pygame.draw.circle(screen, color, (600 + i * 32, 36), 11)

    if game_over:
        # ---------- จอสรุป ----------
        pygame.draw.rect(screen, (45, 60, 52), (150, 130, 500, 240), border_radius=14)
        if win:
            screen.blit(font_big.render("ผ่านทุกด่าน!", True, "lightgreen"), (250, 165))
        else:
            screen.blit(font_big.render("เกมจบ", True, "salmon"), (330, 165))
            screen.blit(font_sml.render(f"คำตอบคือ {word}", True, "white"), (320, 235))
        screen.blit(font_sml.render("กด R เพื่อเล่นใหม่  |  Esc ออก", True, GREY), (280, 325))

    else:
        # ---------- จอเล่น ----------
        screen.blit(font_sml.render(f"[ {category} ]", True, "cyan"), (40, 100))
        screen.blit(font_mid.render(hint, True, "yellow"), (40, 126))

        shown = ""
        for ch in word:
            if ch in guessed:
                shown += ch + " "
            else:
                shown += "_ "

        text = font_big.render(shown, True, "white")
        screen.blit(text, (400 - text.get_width() // 2, 195))

        screen.blit(font_sml.render(f"เดาไปแล้ว : {' '.join(guessed)}", True, GREY), (40, 320))

        if stage_over:
            screen.blit(font_mid.render("ผ่านด่าน!", True, "lightgreen"), (40, 385))
            screen.blit(font_sml.render("กด Space เพื่อไปด่านถัดไป", True, "white"), (40, 435))
        else:
            screen.blit(font_sml.render("กดตัวอักษร A-Z เพื่อเดา  |  R เริ่มใหม่  |  Esc ออก", True, GREY), (40, 435))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
