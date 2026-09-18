# Week 9 - เช็คพอยต์ 1 : แสดงคำลับแบบซ่อน
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Word Hunter")
clock = pygame.time.Clock()

font_big = pygame.font.SysFont("tahoma", 56)
font_mid = pygame.font.SysFont("tahoma", 28)

word = "DOG"
hint = "สัตว์เลี้ยงที่ชอบเห่า"
guessed = ["D"]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 40, 35))

    screen.blit(font_mid.render("WORD HUNTER", True, "white"), (40, 30))
    screen.blit(font_mid.render(f"คำใบ้ : {hint}", True, "yellow"), (40, 110))

    shown = ""
    for ch in word:
        if ch in guessed:
            shown += ch + " "
        else:
            shown += "_ "

    screen.blit(font_big.render(shown, True, "white"), (250, 210))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
