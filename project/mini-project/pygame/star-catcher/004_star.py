import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Star Catcher")
clock = pygame.time.Clock()

basket_x     = 400
basket_y     = 550
basket_speed = 6

# ดาว
star_x     = random.randint(20, 780)
star_y     = -20
star_speed = 4

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

    # ดาวตก
    star_y += star_speed

    # ถ้าออกนอกหน้าจอ → เริ่มใหม่
    if star_y > 620:
        star_x = random.randint(20, 780)
        star_y = -20

    screen.fill("navy")
    pygame.draw.rect(screen, "brown", (basket_x - 40, basket_y, 80, 20))
    pygame.draw.circle(screen, "yellow", (star_x, star_y), 12)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
