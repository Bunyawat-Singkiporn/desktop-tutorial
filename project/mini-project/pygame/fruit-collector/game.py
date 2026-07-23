import pygame
import random
import math

pygame.init()

# ─── หน้าต่าง ────────────────────────────────────────────
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fruit Collector")
clock      = pygame.time.Clock()
font       = pygame.font.SysFont(None, 40)
small_font = pygame.font.SysFont(None, 24)

# ─── ผู้เล่น ──────────────────────────────────────────────
player_x     = 400
player_y     = 300
player_speed = 5

# ─── ผลไม้ ────────────────────────────────────────────────
# ประเภท 0 = แอปเปิ้ล  (แดง,   1 คะแนน)
# ประเภท 1 = ส้ม       (ส้ม,   2 คะแนน)
# ประเภท 2 = แตงโม    (เขียว,  3 คะแนน)
fruit_colors = ["red", "orange", "green"]
fruit_points = [1, 2, 3]
fruit_labels = ["+1", "+2", "+3"]

# สร้างผลไม้เริ่มต้น 5 ลูก
fruits = []
for i in range(5):
    x     = random.randint(50, 750)
    y     = random.randint(50, 550)
    ftype = random.randint(0, 2)
    fruits.append([x, y, ftype])

# ─── คะแนน ────────────────────────────────────────────────
score = 0

# ─── Game Loop ────────────────────────────────────────────
running = True
while running:
    # ── Events ──
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ── เคลื่อนที่ (ไม่ออกนอกหน้าจอ) ──
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]  and player_x > 15:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < 785:
        player_x += player_speed
    if keys[pygame.K_UP]    and player_y > 15:
        player_y -= player_speed
    if keys[pygame.K_DOWN]  and player_y < 585:
        player_y += player_speed

    # ── เช็คเก็บผลไม้ ──
    for fruit in fruits[:]:          # ใช้ fruits[:] เพื่อ copy ก่อนลบ
        fx, fy, ftype = fruit
        distance = math.sqrt((player_x - fx)**2 + (player_y - fy)**2)
        if distance < 30:
            score += fruit_points[ftype]
            fruits.remove(fruit)
            # เกิดผลไม้ใหม่แทน
            new_x    = random.randint(50, 750)
            new_y    = random.randint(50, 550)
            new_type = random.randint(0, 2)
            fruits.append([new_x, new_y, new_type])

    # ── วาด ──
    screen.fill("lightgreen")

    # วาดผู้เล่น (สีน้ำเงิน)
    pygame.draw.rect(screen, "blue", (player_x - 15, player_y - 15, 30, 30))

    # วาดผลไม้ทุกลูก + ป้ายคะแนน
    for fruit in fruits:
        fx, fy, ftype = fruit
        pygame.draw.circle(screen, fruit_colors[ftype], (fx, fy), 15)
        label = small_font.render(fruit_labels[ftype], True, "black")
        screen.blit(label, (fx - 8, fy + 17))

    # วาดคะแนน
    score_text = font.render(f"Score: {score}", True, "black")
    screen.blit(score_text, (10, 10))

    # คำแนะนำ
    hint = small_font.render("Arrow keys to move", True, "darkgreen")
    screen.blit(hint, (10, 572))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
