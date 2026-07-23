import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Star Catcher")
clock = pygame.time.Clock()

# ตะกร้า
basket_x     = 400
basket_y     = 550
basket_speed = 6

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # เลื่อนซ้าย-ขวา
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 40:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < 760:
        basket_x += basket_speed

    screen.fill("navy")
    pygame.draw.rect(screen, "brown", (basket_x - 40, basket_y, 80, 20))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
