# Week 10 - เช็คพอยต์ 3 : ผลไม้หล่นลงมา
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fruit Collector")
clock = pygame.time.Clock()
font = pygame.font.SysFont("tahoma", 24)

BASKET_W = 110
BASKET_H = 26
basket_x = 345
basket_y = 530
speed = 7

fruits = [
    [120, 40],
    [300, 150],
    [520, 90],
    [680, 220],
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        basket_x = basket_x - speed
    if keys[pygame.K_RIGHT]:
        basket_x = basket_x + speed

    if basket_x < 0:
        basket_x = 0
    if basket_x > 800 - BASKET_W:
        basket_x = 800 - BASKET_W

    for fruit in fruits:
        fruit[1] = fruit[1] + 3
        if fruit[1] > 620:
            fruit[1] = -20

    screen.fill((30, 45, 60))
    pygame.draw.rect(screen, (200, 150, 80), (basket_x, basket_y, BASKET_W, BASKET_H), border_radius=6)

    for fruit in fruits:
        pygame.draw.circle(screen, (230, 70, 70), (fruit[0], fruit[1]), 16)

    screen.blit(font.render("ลูกศรซ้าย-ขวา เลื่อนตะกร้า", True, "white"), (20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
