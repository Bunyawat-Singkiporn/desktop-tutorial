# เฉลย Week 2

import pygame
import random  # ใช้สุ่มความสูงท่อ

pygame.init()

# สร้างหน้าต่างเกม
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 48)  # ตัวอักษรแสดงคะแนน

# ตัวแปรนก
bird_x = 150
bird_y = 300
bird_size = 25
bird_speed = 0
GRAVITY = 0.4
JUMP = -8

# ตัวแปรท่อ
pipe_x = 800       # เริ่มที่ขวาสุด
pipe_w = 80        # ความกว้างท่อ
pipe_gap = 200     # ขนาดช่องว่าง
pipe_h = 180       # ความสูงท่อบน

score = 0

running = True
while running:

    # รับ Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_speed = JUMP

    # อัปเดตนก
    bird_speed += GRAVITY
    bird_y += bird_speed

    # ขยับท่อไปทางซ้าย
    pipe_x -= 3
    if pipe_x < -pipe_w:              # ท่อหายไปซ้าย → สร้างใหม่
        pipe_x = 800
        pipe_h = random.randint(100, 320)
        score += 1                    # ผ่านท่อ = ได้คะแนน

    # วาดหน้าจอ
    screen.fill("skyblue")
    pygame.draw.circle(screen, "yellow", (bird_x, int(bird_y)), bird_size)
    pygame.draw.rect(screen, "green", (pipe_x, 0, pipe_w, pipe_h))  # ท่อบน
    pygame.draw.rect(screen, "green", (pipe_x, pipe_h + pipe_gap, pipe_w, 600 - pipe_h - pipe_gap))  # ท่อล่าง

    score_text = font.render(f"Score: {score}", True, "white")
    screen.blit(score_text, (20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
