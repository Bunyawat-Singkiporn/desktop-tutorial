import pygame
import random

pygame.init()

# ─── หน้าต่าง ────────────────────────────────────────────
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Star Catcher")
clock      = pygame.time.Clock()
font       = pygame.font.SysFont(None, 48)
small_font = pygame.font.SysFont(None, 28)

# ─── ตะกร้า ──────────────────────────────────────────────
basket_x     = 400
basket_y     = 550
basket_speed = 6

# ─── ดาว  [x, y, speed] ─────────────────────────────────
stars = []
for i in range(2):
    x     = random.randint(20, 780)
    y     = random.randint(-500, -50)   # เริ่มห่างกัน ไม่ตกพร้อมกัน
    speed = random.randint(2, 4)        # ช้าพอให้เล่นได้
    stars.append([x, y, speed])

# ─── สถานะเกม ─────────────────────────────────────────────
score     = 0
lives     = 3
game_over = False

# ─── Game Loop ────────────────────────────────────────────
running = True
while running:
    # ── Events ──
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # ── ขยับตะกร้า ──
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]  and basket_x > 40:
            basket_x -= basket_speed
        if keys[pygame.K_RIGHT] and basket_x < 760:
            basket_x += basket_speed

        # ── ดาวตก ──
        for star in stars:
            star[1] += star[2]

        # ── เช็คจับดาว / พลาด ──
        for star in stars:
            sx, sy = star[0], star[1]
            if sy > 530 and abs(sx - basket_x) < 50:
                # จับได้!
                score += 1
                star[0] = random.randint(20, 780)
                star[1] = random.randint(-500, -50)
                star[2] = random.randint(2, 4)
            elif sy > 620:
                # พลาด!
                lives -= 1
                star[0] = random.randint(20, 780)
                star[1] = random.randint(-500, -50)
                star[2] = random.randint(2, 4)

        if lives <= 0:
            game_over = True

    # ── วาด ──
    screen.fill("navy")

    if not game_over:
        # วาดตะกร้า
        pygame.draw.rect(screen, "brown", (basket_x - 40, basket_y, 80, 20))

        # วาดดาวทุกดวง
        for star in stars:
            pygame.draw.circle(screen, "yellow", (star[0], star[1]), 12)
            pygame.draw.circle(screen, "white",  (star[0], star[1]),  4)

        # HUD
        score_text = font.render(f"Score: {score}", True, "white")
        lives_text = font.render(f"Lives: {lives}", True, "red")
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 60))

        hint = small_font.render("Left / Right arrow keys to move", True, (100, 100, 200))
        screen.blit(hint, (10, 572))

    else:
        # Game Over Screen
        over_text  = font.render("GAME OVER", True, "yellow")
        score_text = font.render(f"Final Score: {score}", True, "white")
        hint_text  = small_font.render("Close the window to exit", True, "gray")
        screen.blit(over_text,  (260, 230))
        screen.blit(score_text, (220, 300))
        screen.blit(hint_text,  (265, 380))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
