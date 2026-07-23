import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Click the Dot")
clock = pygame.time.Clock()

# วงกลม
dot_x = random.randint(50, 750)
dot_y = random.randint(50, 550)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    pygame.draw.circle(screen, "red", (dot_x, dot_y), 30)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
