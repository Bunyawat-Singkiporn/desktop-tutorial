import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fruit Collector")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

player_x = 400
player_y = 300
player_speed = 5

fruit_x = random.randint(50, 750)
fruit_y = random.randint(50, 550)

score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # เช็คว่าเก็บผลไม้ได้ไหม
    distance = math.sqrt((player_x - fruit_x)**2 + (player_y - fruit_y)**2)
    if distance < 30:
        score += 1
        fruit_x = random.randint(50, 750)
        fruit_y = random.randint(50, 550)

    screen.fill("lightgreen")
    pygame.draw.rect(screen, "blue", (player_x - 15, player_y - 15, 30, 30))
    pygame.draw.circle(screen, "red", (fruit_x, fruit_y), 15)

    score_text = font.render(f"Score: {score}", True, "black")
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
