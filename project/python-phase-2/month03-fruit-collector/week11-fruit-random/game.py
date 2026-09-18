# ============================================================
# Week 11 - FRUIT COLLECTOR #2 : สุ่ม + รับได้ + หลายชนิด  (เฉลย)
# แนวคิด: random.randint / random.choice, การชน 2 แกน, ตารางข้อมูล (data-driven)
# รัน: python game.py   |   ลูกศรซ้าย-ขวา | Esc ออก
# ============================================================
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fruit Collector - Week 11")
clock = pygame.time.Clock()
font = pygame.font.SysFont("tahoma", 22)
small = pygame.font.SysFont("tahoma", 16)

BG = (30, 45, 60)
BASKET_W = 110
BASKET_H = 26

# ---------- ตารางข้อมูลของที่ตกลงมา ----------
#            0 แอปเปิล      1 ส้ม          2 แตงโม        3 ระเบิด
COLORS = [(230, 70, 70), (240, 150, 40), (80, 190, 90), (60, 60, 70)]
POINTS = [1,             2,              3,             -5]
LABELS = ["+1",          "+2",           "+3",          "BOMB"]
KIND_POOL = [0, 0, 0, 1, 1, 2, 3]      # ใส่ซ้ำ = โอกาสออกเยอะขึ้น

basket_x = 345
basket_y = 530
speed = 7
score = 0


fruits = []
for i in range(8):
    fruits.append([random.randint(20, 780), random.randint(-400, -20),
                   random.randint(2, 6), random.choice(KIND_POOL)])

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
    if basket_x < 0:
        basket_x = 0
    if basket_x > 800 - BASKET_W:
        basket_x = 800 - BASKET_W

    # ===== PROCESS =====
    for fruit in fruits:
        fruit[1] = fruit[1] + fruit[2]

        caught = (fruit[1] > basket_y and fruit[1] < basket_y + BASKET_H + 10
                  and fruit[0] > basket_x and fruit[0] < basket_x + BASKET_W)
        missed = fruit[1] > 620

        if caught:
            score = score + POINTS[fruit[3]]
            if score < 0:
                score = 0

        if caught or missed:
            fruit[0] = random.randint(20, 780)
            fruit[1] = random.randint(-400, -20)
            fruit[2] = random.randint(2, 6)
            fruit[3] = random.choice(KIND_POOL)

    # ===== OUTPUT =====
    screen.fill(BG)
    pygame.draw.rect(screen, (40, 60, 45), (0, 560, 800, 40))

    pygame.draw.rect(screen, (200, 150, 80), (basket_x, basket_y, BASKET_W, BASKET_H), border_radius=6)
    pygame.draw.rect(screen, (150, 105, 50), (basket_x, basket_y, BASKET_W, 8), border_radius=6)

    for fruit in fruits:
        kind = fruit[3]
        pygame.draw.circle(screen, COLORS[kind], (fruit[0], fruit[1]), 16)
        if kind == 3:
            pygame.draw.circle(screen, (230, 120, 40), (fruit[0], fruit[1] - 18), 4)
        else:
            pygame.draw.circle(screen, (90, 170, 90), (fruit[0] + 6, fruit[1] - 16), 5)
        tag = small.render(LABELS[kind], True, "white")
        screen.blit(tag, (fruit[0] - tag.get_width() // 2, fruit[1] + 18))

    screen.blit(font.render(f"คะแนน {score}", True, "yellow"), (20, 18))
    screen.blit(small.render("รับผลไม้ให้ได้ หลบระเบิด  |  Esc ออก", True, (150, 170, 190)), (20, 48))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
