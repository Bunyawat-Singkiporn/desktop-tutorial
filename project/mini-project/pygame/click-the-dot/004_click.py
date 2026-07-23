import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Click the Dot")
clock = pygame.time.Clock()
font  = pygame.font.SysFont(None, 36)

dot_x = random.randint(50, 750)
dot_y = random.randint(50, 550)
score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            distance = math.sqrt((mx - dot_x)**2 + (my - dot_y)**2)
            if distance < 30:
                score += 1
                dot_x = random.randint(50, 750)
                dot_y = random.randint(50, 550)

    screen.fill("white")
    pygame.draw.circle(screen, "red", (dot_x, dot_y), 30)

    score_text = font.render(f"Score: {score}", True, "black")
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
