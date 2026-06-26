# เฉลย Week 3

import pygame
import random

pygame.init()

# สร้างหน้าต่างเกม
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 48)

# ตัวแปรนก
bird_x = 150
bird_y = 300
bird_size = 25
bird_speed = 0
GRAVITY = 0.4
JUMP = -8

# ตัวแปรท่อ
pipe_x = 800
pipe_w = 80
pipe_gap = 200
pipe_h = 180

score = 0
game_over = False  # False = เล่นอยู่, True = แพ้แล้ว

running = True
while running:

    # รับ Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if game_over:
                # รีเซ็ตเกม (เล่นใหม่)
                bird_y = 300
                bird_speed = 0
                pipe_x = 800
                pipe_h = 180
                score = 0
                game_over = False
            else:
                bird_speed = JUMP  # กระโดด

    # อัปเดตเกม (เฉพาะตอนยังไม่แพ้)
    if not game_over:
        bird_speed += GRAVITY
        bird_y += bird_speed

        pipe_x -= 3
        if pipe_x < -pipe_w:
            pipe_x = 800
            pipe_h = random.randint(100, 320)
            score += 1

        # ตรวจชน: อยู่ตำแหน่งท่อ + อยู่นอกช่องว่าง
        if pipe_x < bird_x + bird_size and pipe_x + pipe_w > bird_x - bird_size:
            if bird_y - bird_size < pipe_h or bird_y + bird_size > pipe_h + pipe_gap:
                game_over = True

        # ชนขอบบน/ล่างของจอ
        if bird_y - bird_size < 0 or bird_y + bird_size > 600:
            game_over = True

    # วาดหน้าจอ
    screen.fill("skyblue")
    pygame.draw.circle(screen, "yellow", (bird_x, int(bird_y)), bird_size)
    pygame.draw.rect(screen, "green", (pipe_x, 0, pipe_w, pipe_h))
    pygame.draw.rect(screen, "green", (pipe_x, pipe_h + pipe_gap, pipe_w, 600 - pipe_h - pipe_gap))

    score_text = font.render(f"Score: {score}", True, "white")
    screen.blit(score_text, (20, 20))

    if game_over:
        over_text = font.render("Game Over! Space = Restart", True, "red")
        screen.blit(over_text, (180, 280))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
