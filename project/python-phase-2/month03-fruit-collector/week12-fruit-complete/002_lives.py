# ============================================================
# Week 12 - เช็คพอยต์ 1 : ระบบชีวิต
# รวม: หน้าเริ่ม + ตะกร้า + ผลไม้สุ่ม 4 ชนิด + ระเบิด + คะแนน
#      + ชีวิต 3 ดวง + นับถอยหลัง + จอสรุป + สถิติสูงสุด + เล่นใหม่
# รัน: python game.py
# ปุ่ม: Space เริ่ม | ลูกศรซ้าย-ขวา เลื่อนตะกร้า | R กลับเมนู | Esc ออก
# ============================================================
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fruit Collector v1.0")
clock = pygame.time.Clock()

font_big = pygame.font.SysFont("tahoma", 40)
font_mid = pygame.font.SysFont("tahoma", 24)
font_sml = pygame.font.SysFont("tahoma", 17)

BG     = (30, 45, 60)
PANEL  = (45, 62, 82)
GREY   = (150, 170, 190)

BASKET_W = 110
BASKET_H = 26
TIME_LIMIT = 45
MAX_LIVES = 3
FRUIT_COUNT = 8

#            0 แอปเปิล      1 ส้ม          2 แตงโม        3 ระเบิด
COLORS = [(230, 70, 70), (240, 150, 40), (80, 190, 90), (60, 60, 70)]
POINTS = [1,             2,              3,             -5]
LABELS = ["+1",          "+2",           "+3",          "BOMB"]
KIND_POOL = [0, 0, 0, 1, 1, 2, 3]

# ---------- อยู่ตลอดไป ----------
best = 0

# ---------- ของรอบการเล่น ----------
state = "menu"
score = 0
lives = MAX_LIVES
basket_x = 345
basket_y = 530
speed = 7
time_left = TIME_LIMIT
start_time = 0
end_reason = ""
fruits = []

running = True
while running:

    # ==================== INPUT ====================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if state == "menu" and event.key == pygame.K_SPACE:
                # ----- รีเซ็ตทุกอย่างก่อนเริ่มรอบใหม่ -----
                state = "playing"
                score = 0
                lives = MAX_LIVES
                basket_x = 345
                time_left = TIME_LIMIT
                start_time = pygame.time.get_ticks()
                end_reason = ""
                fruits = []
                for i in range(FRUIT_COUNT):
                    fruits.append([random.randint(20, 780),
                                   random.randint(-400, -20),
                                   random.randint(2, 6),
                                   random.choice(KIND_POOL)])

            elif state == "gameover" and event.key == pygame.K_r:
                state = "menu"

    # ==================== PROCESS ====================
    if state == "playing":

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            basket_x = basket_x - speed
        if keys[pygame.K_RIGHT]:
            basket_x = basket_x + speed
        if basket_x < 0:
            basket_x = 0
        if basket_x > 800 - BASKET_W:
            basket_x = 800 - BASKET_W

        # ----- ผลไม้ -----
        for fruit in fruits:
            fruit[1] = fruit[1] + fruit[2]

            caught = (fruit[1] > basket_y and fruit[1] < basket_y + BASKET_H + 10
                      and fruit[0] > basket_x and fruit[0] < basket_x + BASKET_W)
            missed = fruit[1] > 620

            if caught:
                score = score + POINTS[fruit[3]]
                if score < 0:
                    score = 0

            if missed and fruit[3] != 3:      # ผลไม้ดีตกพื้น = เสียชีวิต
                lives = lives - 1

            if caught or missed:
                fruit[0] = random.randint(20, 780)
                fruit[1] = random.randint(-400, -20)
                fruit[2] = random.randint(2, 6)
                fruit[3] = random.choice(KIND_POOL)

        # ----- เช็กจบเกม -----
        if lives <= 0:
            lives = 0
            end_reason = "ชีวิตหมด"
            state = "gameover"

        if state == "gameover" and score > best:
            best = score

    # ==================== OUTPUT ====================
    screen.fill(BG)

    # ---------- หน้าเริ่ม ----------
    if state == "menu":
        pygame.draw.rect(screen, PANEL, (150, 130, 500, 330), border_radius=16)
        t = font_big.render("FRUIT COLLECTOR", True, "white")
        screen.blit(t, (400 - t.get_width() // 2, 170))
        t = font_sml.render(f"รับผลไม้ให้ได้มากที่สุดใน {TIME_LIMIT} วินาที", True, GREY)
        screen.blit(t, (400 - t.get_width() // 2, 245))
        t = font_sml.render("ปล่อยผลไม้ตกพื้น = เสียชีวิต  |  ระเบิดปล่อยได้", True, GREY)
        screen.blit(t, (400 - t.get_width() // 2, 272))

        for i in range(3):
            pygame.draw.circle(screen, COLORS[i], (330 + i * 70, 320), 16)
        pygame.draw.circle(screen, COLORS[3], (540, 320), 16)

        t = font_mid.render("กด Space เพื่อเริ่ม", True, "yellow")
        screen.blit(t, (400 - t.get_width() // 2, 365))
        if best > 0:
            t = font_sml.render(f"สถิติสูงสุด {best}", True, "gold")
            screen.blit(t, (400 - t.get_width() // 2, 415))

    # ---------- จอสรุป ----------
    elif state == "gameover":
        pygame.draw.rect(screen, PANEL, (150, 150, 500, 290), border_radius=16)
        t = font_big.render("จบเกม!", True, "white")
        screen.blit(t, (400 - t.get_width() // 2, 180))
        t = font_sml.render(end_reason, True, "salmon")
        screen.blit(t, (400 - t.get_width() // 2, 240))
        t = font_mid.render(f"คะแนน {score}", True, "yellow")
        screen.blit(t, (400 - t.get_width() // 2, 285))
        t = font_mid.render(f"สถิติสูงสุด {best}", True, "gold")
        screen.blit(t, (400 - t.get_width() // 2, 330))
        t = font_sml.render("กด R กลับเมนู  |  Esc ออก", True, GREY)
        screen.blit(t, (400 - t.get_width() // 2, 390))

    # ---------- กำลังเล่น ----------
    else:
        pygame.draw.rect(screen, (40, 60, 45), (0, 560, 800, 40))

        # แถบเวลา
        ratio = time_left / TIME_LIMIT
        if ratio < 0:
            ratio = 0
        if time_left > 15:
            bar_color = (80, 200, 130)
        elif time_left > 5:
            bar_color = (240, 200, 70)
        else:
            bar_color = (235, 80, 80)
        pygame.draw.rect(screen, (60, 75, 95), (20, 56, 760, 12), border_radius=6)
        pygame.draw.rect(screen, bar_color, (20, 56, int(760 * ratio), 12), border_radius=6)

        # ตะกร้า
        pygame.draw.rect(screen, (200, 150, 80), (basket_x, basket_y, BASKET_W, BASKET_H), border_radius=6)
        pygame.draw.rect(screen, (150, 105, 50), (basket_x, basket_y, BASKET_W, 8), border_radius=6)

        # ผลไม้
        for fruit in fruits:
            kind = fruit[3]
            pygame.draw.circle(screen, COLORS[kind], (fruit[0], fruit[1]), 16)
            if kind == 3:
                pygame.draw.circle(screen, (230, 120, 40), (fruit[0], fruit[1] - 18), 4)
            else:
                pygame.draw.circle(screen, (90, 170, 90), (fruit[0] + 6, fruit[1] - 16), 5)
            tag = font_sml.render(LABELS[kind], True, "white")
            screen.blit(tag, (fruit[0] - tag.get_width() // 2, fruit[1] + 18))

        # แถบข้อมูล
        screen.blit(font_mid.render(f"คะแนน {score}", True, "yellow"), (20, 18))
        screen.blit(font_mid.render(f"{int(time_left)} วิ", True, bar_color), (380, 18))
        for i in range(MAX_LIVES):
            color = (230, 70, 90) if i < lives else (70, 80, 95)
            pygame.draw.circle(screen, color, (700 + i * 34, 30), 11)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
