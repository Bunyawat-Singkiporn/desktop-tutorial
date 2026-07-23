import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Star Catcher")
clock = pygame.time.Clock()
font  = pygame.font.SysFont(None, 36)

basket_x     = 400
basket_y     = 550
basket_speed = 6

star_x     = random.randint(20, 780)
star_y     = -20
star_speed = 4

score = 0
lives = 3

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 40:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < 760:
        basket_x += basket_speed

    star_y += star_speed

    # จับได้!
    if star_y > 530 and abs(star_x - basket_x) < 50:
        score += 1
        star_x = random.randint(20, 780)
        star_y = -20
    # พลาด!
    elif star_y > 620:
        lives -= 1
        star_x = random.randint(20, 780)
        star_y = -20

    if lives <= 0:
        running = False

    screen.fill("navy")
    pygame.draw.rect(screen, "brown", (basket_x - 40, basket_y, 80, 20))
    pygame.draw.circle(screen, "yellow", (star_x, star_y), 12)

    score_text = font.render(f"Score: {score}", True, "white")
    lives_text = font.render(f"Lives: {lives}", True, "red")
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 50))

    pygame.display.flip()
    clock.tick(60)

# Game Over Screen
screen.fill("navy")
over_text = font.render(f"Game Over!  Score: {score}", True, "yellow")
screen.blit(over_text, (200, 280))
pygame.display.flip()
pygame.time.wait(3000)

pygame.quit()
