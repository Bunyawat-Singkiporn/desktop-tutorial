# ============================================================
# Week 10 - FRUIT COLLECTOR #1 : ตะกร้า + list ผลไม้หล่น  (เฉลย)
# แนวคิด: list ซ้อน list, for วาดทุกลูก, key.get_pressed(), การเคลื่อนที่
# รัน: python game.py    |    ลูกศรซ้าย-ขวา เลื่อนตะกร้า | Esc ออก
# ============================================================
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fruit Collector - Week 10")
clock = pygame.time.Clock()
font = pygame.font.SysFont("tahoma", 22)

BG = (30, 45, 60)
BASKET_W = 110
BASKET_H = 26
FALL_SPEED = 3

basket_x = 345
basket_y = 530
speed = 7

# ---------- ผลไม้ : [x, y] ----------
fruits = [
    [120, 40],
    [300, 150],
    [520, 90],
    [680, 220],
    [220, 300],
    [440, 380],
]

running = True
while running:

    # ===== INPUT =====
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        basket_x = basket_x - speed
    if keys[pygame.K_RIGHT]:
        basket_x = basket_x + speed

    # ===== PROCESS =====
    if basket_x < 0:
        basket_x = 0
    if basket_x > 800 - BASKET_W:
        basket_x = 800 - BASKET_W

    for fruit in fruits:
        fruit[1] = fruit[1] + FALL_SPEED
        if fruit[1] > 620:
            fruit[1] = -20

    # ===== OUTPUT =====
    screen.fill(BG)

    # พื้น
    pygame.draw.rect(screen, (40, 60, 45), (0, 560, 800, 40))

    # ตะกร้า
    pygame.draw.rect(screen, (200, 150, 80), (basket_x, basket_y, BASKET_W, BASKET_H), border_radius=6)
    pygame.draw.rect(screen, (150, 105, 50), (basket_x, basket_y, BASKET_W, 8), border_radius=6)

    # ผลไม้ทุกลูก
    for fruit in fruits:
        pygame.draw.circle(screen, (230, 70, 70), (fruit[0], fruit[1]), 16)
        pygame.draw.circle(screen, (90, 170, 90), (fruit[0] + 6, fruit[1] - 16), 5)

    screen.blit(font.render(f"ผลไม้บนจอ {len(fruits)} ลูก", True, "white"), (20, 18))
    screen.blit(font.render("ลูกศรซ้าย-ขวา เลื่อนตะกร้า  |  Esc ออก", True, (150, 170, 190)), (20, 46))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
