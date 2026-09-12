# Week 5 - เช็คพอยต์ 1 : หน้าต่างเกม
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Quiz Arena")
clock = pygame.time.Clock()

font_big = pygame.font.SysFont("tahoma", 40)
font_mid = pygame.font.SysFont("tahoma", 30)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((25, 30, 50))

    title = font_big.render("QUIZ ARENA", True, "white")
    screen.blit(title, (50, 40))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
