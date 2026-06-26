# เฉลย Week 1

import pygame

pygame.init()

# สร้างหน้าต่างเกม
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()  # จำกัดความเร็วเกม 60 เฟรม/วินาที

# ตัวแปรนก
bird_x = 150       # ตำแหน่งซ้าย-ขวา
bird_y = 300       # ตำแหน่งบน-ล่าง
bird_size = 25     # ขนาดวงกลม
bird_speed = 0     # ความเร็วขึ้น/ลง
GRAVITY = 0.4      # แรงดึงลงทุกเฟรม
JUMP = -8          # กระโดด (เลขติดลบ = ขึ้น)

running = True
while running:

    # รับ Input จากผู้เล่น
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_speed = JUMP

    # อัปเดตตำแหน่ง (แรงโน้มถ่วง)
    bird_speed += GRAVITY
    bird_y += bird_speed

    # วาดหน้าจอ
    screen.fill("skyblue")
    pygame.draw.circle(screen, "yellow", (bird_x, int(bird_y)), bird_size)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
