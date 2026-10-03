import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Star Catcher")
clock = pygame.time.Clock()
font  = pygame.font.SysFont(None, 36)

basket_x     = 400
basket_y     = 550
basket_speed = 8   # เร็วขึ้น ไล่จับดาว 2 ดวงได้ทัน

# ดาวหลายดวง [x, y, speed]
# วาง y ห่างกันชัดๆ — ไม่ตกพร้อมกัน
stars = []
for i in range(2):
    x     = random.randint(20, 780)
    y     = -80 - i * 320          # ดวงที่ 2 อยู่สูงกว่ามาก
    speed = random.randint(2, 3)   # ช้าพอให้เด็กเล่นได้
    stars.append([x, y, speed])

score = 0
lives = 5

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

    # ขยับดาวทุกดวง
    for star in stars:
        star[1] += star[2]

    # เช็คจับ / พลาด
    for star in stars:
        sx, sy = star[0], star[1]
        if sy > 520 and abs(sx - basket_x) < 65:
            score += 1
            star[0] = random.randint(20, 780)
            star[1] = random.randint(-480, -280)  # เกิดใหม่สูงๆ เว้นจังหวะ
            star[2] = random.randint(2, 3)
        elif sy > 620:
            lives -= 1
            star[0] = random.randint(20, 780)
            star[1] = random.randint(-480, -280)
            star[2] = random.randint(2, 3)

    if lives <= 0:
        running = False

    screen.fill("navy")
    pygame.draw.rect(screen, "brown", (basket_x - 40, basket_y, 80, 20))

    for star in stars:
        pygame.draw.circle(screen, "yellow", (star[0], star[1]), 12)

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
