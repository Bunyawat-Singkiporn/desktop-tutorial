# ============================================================
# Week 10 - เช็คพอยต์ 1 : คลังคำ + หมวดหมู่
# แนวคิด: string, for ch in word, in / not in, list.append, ชีวิต, ชนะ/แพ้
# รัน: python game.py
# ปุ่ม: A-Z เดาตัวอักษร | R เล่นใหม่ | Esc ออก
# ============================================================
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Word Hunter - Week 9")
clock = pygame.time.Clock()

font_big = pygame.font.SysFont("tahoma", 56)
font_mid = pygame.font.SysFont("tahoma", 28)
font_sml = pygame.font.SysFont("tahoma", 20)

BG    = (30, 40, 35)
GREY  = (170, 180, 175)
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

MAX_LIVES = 6

words = [
    ["DOG",      "สัตว์เลี้ยงที่ชอบเห่า",       "สัตว์"],
    ["ELEPHANT", "ตัวใหญ่ มีงวงยาว",           "สัตว์"],
    ["PYTHON",   "ภาษาโปรแกรมที่เรากำลังเรียน", "คอมพิวเตอร์"],
    ["RAINBOW",  "เกิดหลังฝนตก มี 7 สี",       "ธรรมชาติ"],
    ["SCHOOL",   "สถานที่ที่เรามาเรียน",         "สถานที่"],
]
level = 0          # ลองเปลี่ยนเป็น 1, 2, 3 ดู
word = words[level][0]
hint = words[level][1]
category = words[level][2]

guessed = []          # ตัวอักษรที่เดาไปแล้ว
lives = MAX_LIVES
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

            # ----- เริ่มใหม่ -----
            if event.key == pygame.K_r:
                guessed = []
                lives = MAX_LIVES
                game_over = False
                win = False

            # ----- เดาตัวอักษร -----
            elif not game_over:
                letter = pygame.key.name(event.key).upper()
                if len(letter) == 1 and letter in ALPHA:
                    if letter not in guessed:
                        guessed.append(letter)
                        if letter not in word:
                            lives -= 1

    # ==================== PROCESS ====================
    win = True
    for ch in word:
        if ch not in guessed:
            win = False

    if win or lives <= 0:
        game_over = True

    # ==================== OUTPUT ====================
    screen.fill(BG)

    screen.blit(font_mid.render("WORD HUNTER", True, "white"), (40, 28))

    # ชีวิตเป็นวงกลม
    for i in range(MAX_LIVES):
        color = (220, 70, 70) if i < lives else (70, 80, 75)
        pygame.draw.circle(screen, color, (600 + i * 32, 42), 11)

    screen.blit(font_sml.render(f"[ {category} ]", True, "cyan"), (40, 96))
    screen.blit(font_mid.render(hint, True, "yellow"), (40, 122))

    # คำลับแบบซ่อน
    shown = ""
    for ch in word:
        if ch in guessed:
            shown += ch + " "
        else:
            shown += "_ "

    text = font_big.render(shown, True, "white")
    screen.blit(text, (400 - text.get_width() // 2, 185))

    # ตัวที่เดาไปแล้ว
    screen.blit(font_sml.render(f"เดาไปแล้ว : {' '.join(guessed)}", True, GREY), (40, 320))

    # ผลลัพธ์
    if game_over:
        if win:
            msg = font_mid.render("ชนะ! เก่งมาก", True, "lightgreen")
        else:
            msg = font_mid.render(f"แพ้! คำตอบคือ {word}", True, "salmon")
        screen.blit(msg, (40, 390))
        screen.blit(font_sml.render("กด R เพื่อเล่นใหม่  |  Esc ออก", True, GREY), (40, 440))
    else:
        screen.blit(font_sml.render("กดตัวอักษร A-Z เพื่อเดา  |  R เริ่มใหม่  |  Esc ออก", True, GREY), (40, 440))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
