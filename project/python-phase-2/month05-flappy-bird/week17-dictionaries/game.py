# ============================================================
# Week 17 - FLAPPY BIRD #1 : dict + list ของ dict   (เฉลย)
# แนวคิด: dict เก็บนก, list ของ dict เก็บท่อ, แรงโน้มถ่วง, recycle ท่อ
# รัน: python game.py   |   Space กระโดด | Esc ออก
# ============================================================
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Flappy Bird - Week 17")
clock = pygame.time.Clock()
font = pygame.font.SysFont("tahoma", 22)

SKY    = (120, 190, 220)
GREEN  = (70, 170, 90)
DGREEN = (50, 130, 70)
GROUND = (200, 180, 120)

GRAVITY = 0.5
JUMP = -9
SPEED = 3
GAP = 160
PIPE_W = 70

bird = {"x": 150, "y": 300, "speed": 0, "size": 18}

pipes = []
for i in range(3):
    pipes.append({"x": 500 + i * 300,
                  "gap_y": random.randint(150, 420),
                  "scored": False})

running = True
while running:

    # ===== INPUT =====
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird["speed"] = JUMP
            if event.key == pygame.K_ESCAPE:
                running = False

    # ===== PROCESS =====
    bird["speed"] = bird["speed"] + GRAVITY
    bird["y"] = bird["y"] + bird["speed"]

    if bird["y"] < bird["size"]:
        bird["y"] = bird["size"]
        bird["speed"] = 0
    if bird["y"] > 540 - bird["size"]:
        bird["y"] = 540 - bird["size"]
        bird["speed"] = 0

    for pipe in pipes:
        pipe["x"] = pipe["x"] - SPEED
        if pipe["x"] < -PIPE_W:
            pipe["x"] = 800
            pipe["gap_y"] = random.randint(150, 420)
            pipe["scored"] = False

    # ===== OUTPUT =====
    screen.fill(SKY)

    for pipe in pipes:
        top_h = pipe["gap_y"] - GAP // 2
        bottom_y = pipe["gap_y"] + GAP // 2
        pygame.draw.rect(screen, GREEN, (pipe["x"], 0, PIPE_W, top_h))
        pygame.draw.rect(screen, DGREEN, (pipe["x"] - 5, top_h - 22, PIPE_W + 10, 22))
        pygame.draw.rect(screen, GREEN, (pipe["x"], bottom_y, PIPE_W, 540 - bottom_y))
        pygame.draw.rect(screen, DGREEN, (pipe["x"] - 5, bottom_y, PIPE_W + 10, 22))

    pygame.draw.rect(screen, GROUND, (0, 540, 800, 60))
    pygame.draw.circle(screen, (250, 210, 70), (bird["x"], int(bird["y"])), bird["size"])
    pygame.draw.circle(screen, (40, 40, 40), (bird["x"] + 7, int(bird["y"]) - 5), 3)

    screen.blit(font.render("กด Space ให้นกกระโดด  |  Esc ออก", True, (40, 60, 80)), (20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
