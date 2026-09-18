# Week 9 - เช็คพอยต์ 2 : กดตัวอักษรเพื่อเดา
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

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            letter = pygame.key.name(event.key).upper()
            if len(letter) == 1 and letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                if letter not in guessed:
                    guessed.append(letter)

    screen.fill((30, 40, 35))

    screen.blit(font_mid.render("WORD HUNTER", True, "white"), (40, 30))
    screen.blit(font_mid.render(f"คำใบ้ : {hint}", True, "yellow"), (40, 110))

    shown = ""
    for ch in word:
        if ch in guessed:
            shown += ch + " "
        else:
            shown += "_ "

    screen.blit(font_big.render(shown, True, "white"), (250, 200))

    used = " ".join(guessed)
    screen.blit(font_mid.render(f"เดาไปแล้ว : {used}", True, (170, 180, 175)), (40, 340))
    screen.blit(font_mid.render("กดตัวอักษร A-Z เพื่อเดา", True, (170, 180, 175)), (40, 420))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
