# Week 9 - เช็คพอยต์ 3 : ชีวิต + ชนะ/แพ้
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Word Hunter")
clock = pygame.time.Clock()

font_big = pygame.font.SysFont("tahoma", 56)
font_mid = pygame.font.SysFont("tahoma", 28)

word = "DOG"
hint = "สัตว์เลี้ยงที่ชอบเห่า"
guessed = []
lives = 6
game_over = False
win = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and not game_over:
            letter = pygame.key.name(event.key).upper()
            if len(letter) == 1 and letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                if letter not in guessed:
                    guessed.append(letter)
                    if letter not in word:
                        lives -= 1

    # ---- เช็กชนะ / แพ้ ----
    win = True
    for ch in word:
        if ch not in guessed:
            win = False

    if win or lives <= 0:
        game_over = True

    # ---- วาด ----
    screen.fill((30, 40, 35))

    screen.blit(font_mid.render("WORD HUNTER", True, "white"), (40, 30))
    screen.blit(font_mid.render(f"ชีวิต {lives}", True, "red"), (620, 30))
    screen.blit(font_mid.render(f"คำใบ้ : {hint}", True, "yellow"), (40, 110))

    shown = ""
    for ch in word:
        if ch in guessed:
            shown += ch + " "
        else:
            shown += "_ "

    screen.blit(font_big.render(shown, True, "white"), (250, 190))

    used = " ".join(guessed)
    screen.blit(font_mid.render(f"เดาไปแล้ว : {used}", True, (170, 180, 175)), (40, 330))

    if game_over:
        if win:
            msg = font_mid.render("ชนะ! เก่งมาก", True, "lightgreen")
        else:
            msg = font_mid.render(f"แพ้! คำตอบคือ {word}", True, "salmon")
        screen.blit(msg, (40, 420))
    else:
        screen.blit(font_mid.render("กดตัวอักษร A-Z เพื่อเดา", True, (170, 180, 175)), (40, 420))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
