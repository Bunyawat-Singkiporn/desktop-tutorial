import pygame
import random
import math

pygame.init()

# ─── หน้าต่าง ─────────────────────────────────────────────
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Click the Dot")
clock      = pygame.time.Clock()
font       = pygame.font.SysFont(None, 48)
small_font = pygame.font.SysFont(None, 28)

# ─── วงกลม ────────────────────────────────────────────────
dot_x      = random.randint(50, 750)
dot_y      = random.randint(50, 550)
dot_radius = 30

# ─── คะแนน ────────────────────────────────────────────────
score = 0
miss  = 0

# ─── Game Loop ────────────────────────────────────────────
running = True
while running:
    # ── Events ──
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my   = event.pos
            distance = math.sqrt((mx - dot_x)**2 + (my - dot_y)**2)
            if distance < dot_radius:
                # โดน! → คะแนน + ย้ายวงกลม
                score     += 1
                dot_x      = random.randint(50, 750)
                dot_y      = random.randint(50, 550)
            else:
                # พลาด!
                miss += 1

    # ── วาด ──
    screen.fill("white")
    pygame.draw.circle(screen, "red",     (dot_x, dot_y), dot_radius)
    pygame.draw.circle(screen, "darkred", (dot_x, dot_y), dot_radius, 3)   # ขอบ

    # HUD
    score_text = font.render(f"Score: {score}", True, "black")
    miss_text  = small_font.render(f"Miss: {miss}", True, "gray")
    hint_text  = small_font.render("Click the red dot!", True, "lightcoral")
    screen.blit(score_text, (10, 10))
    screen.blit(miss_text,  (10, 65))
    screen.blit(hint_text,  (10, 572))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
