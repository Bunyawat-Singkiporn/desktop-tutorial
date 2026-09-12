# โบนัส — จับเวลา 30 วินาที

import pygame
import random
import math
import time

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fruit Collector")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
small_font = pygame.font.SysFont(None, 22)

player_x = 400
player_y = 300
player_speed = 5

fruit_colors = ["red", "orange", "green"]
fruit_points = [1, 2, 3]
fruit_labels = ["+1", "+2", "+3"]

# สร้างผลไม้ 5 ลูกตอนเริ่ม
fruits = []
for i in range(5):
    x = random.randint(50, 750)
    y = random.randint(50, 550)
    ftype = random.randint(0, 2)
    fruits.append([x, y, ftype])

score = 0
TIME_LIMIT = 30
start_time = time.time()
game_over = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # คำนวณเวลาที่เหลือ
    elapsed = time.time() - start_time
    time_left = max(0, TIME_LIMIT - elapsed)
    if time_left <= 0:
        game_over = True

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_UP]:
            player_y -= player_speed
        if keys[pygame.K_DOWN]:
            player_y += player_speed

        # เช็คเก็บผลไม้
        for fruit in fruits[:]:
            fx, fy, ftype = fruit
            distance = math.sqrt((player_x - fx)**2 + (player_y - fy)**2)
            if distance < 30:
                score += fruit_points[ftype]
                fruits.remove(fruit)
                new_x = random.randint(50, 750)
                new_y = random.randint(50, 550)
                new_type = random.randint(0, 2)
                fruits.append([new_x, new_y, new_type])

    screen.fill("lightgreen")
    pygame.draw.rect(screen, "blue", (player_x - 15, player_y - 15, 30, 30))

    # วาดผลไม้ทุกลูก + ป้ายคะแนน
    for fruit in fruits:
        fx, fy, ftype = fruit
        pygame.draw.circle(screen, fruit_colors[ftype], (fx, fy), 15)
        label = small_font.render(fruit_labels[ftype], True, "black")
        screen.blit(label, (fx - 8, fy + 18))

    score_text = font.render(f"Score: {score}", True, "black")
    screen.blit(score_text, (10, 10))

    time_text = font.render(f"Time: {time_left:.1f}", True, "black")
    screen.blit(time_text, (650, 10))

    if game_over:
        over = font.render("Time's Up!", True, "red")
        screen.blit(over, (320, 280))
        final = font.render(f"Final Score: {score}", True, "black")
        screen.blit(final, (280, 330))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
