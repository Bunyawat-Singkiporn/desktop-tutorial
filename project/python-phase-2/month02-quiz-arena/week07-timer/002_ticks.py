# Week 7 - เช็คพอยต์ 1 : รู้จัก get_ticks()
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Timer Test")
clock = pygame.time.Clock()
font = pygame.font.SysFont("tahoma", 40)

start = pygame.time.get_ticks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    passed = (pygame.time.get_ticks() - start) / 1000

    screen.fill("black")
    text = font.render(f"{round(passed, 1)} วินาที", True, "white")
    screen.blit(text, (100, 80))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
