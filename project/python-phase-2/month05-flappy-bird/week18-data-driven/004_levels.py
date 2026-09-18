# ============================================================
# Week 18 - เช็คพอยต์ 3 : ตารางความยาก
# แนวคิด: การชนสี่เหลี่ยม, flag กันนับซ้ำ, data-driven difficulty
# รัน: python game.py   |   Space กระโดด/เริ่มใหม่ | Esc ออก
# ============================================================
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Flappy Bird - Week 18")
clock = pygame.time.Clock()

font_big = pygame.font.SysFont("tahoma", 46)
font_mid = pygame.font.SysFont("tahoma", 24)
font_sml = pygame.font.SysFont("tahoma", 18)

SKY    = (120, 190, 220)
GREEN  = (70, 170, 90)
DGREEN = (50, 130, 70)
GROUND = (200, 180, 120)
DARK   = (40, 60, 80)

GRAVITY = 0.5
JUMP = -9
PIPE_W = 70
FLOOR_Y = 540

# ---------- ตารางความยาก (แก้ที่นี่ที่เดียว) ----------
LEVELS = [
    {"name": "ง่าย", "gap": 200, "speed": 2, "at": 0},
    {"name": "ปกติ", "gap": 160, "speed": 3, "at": 5},
    {"name": "ยาก", "gap": 130, "speed": 4, "at": 12},
    {"name": "โหด", "gap": 110, "speed": 5, "at": 20},
]

bird = {"x": 150, "y": 300, "speed": 0, "size": 18}
pipes = []
score = 0
state = "playing"


def reset_game():
    global score, state, pipes
    bird["y"] = 300
    bird["speed"] = 0
    score = 0
    state = "playing"
    pipes = []
    for i in range(3):
        pipes.append({"x": 500 + i * 300,
                      "gap_y": random.randint(150, 420),
                      "scored": False})


def current_level():
    result = LEVELS[0]
    for lv in LEVELS:
        if score >= lv["at"]:
            result = lv
    return result


def hit_pipe(pipe, gap):
    bx = bird["x"]
    by = bird["y"]
    r = bird["size"]
    near_x = bx + r > pipe["x"] and bx - r < pipe["x"] + PIPE_W
    in_gap = by - r > pipe["gap_y"] - gap // 2 and by + r < pipe["gap_y"] + gap // 2
    return near_x and not in_gap


reset_game()

running = True
while running:
    level = current_level()
    gap = level["gap"]
    speed = level["speed"]

    # ===== INPUT =====
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                if state == "playing":
                    bird["speed"] = JUMP
                else:
                    reset_game()

    # ===== PROCESS =====
    if state == "playing":
        bird["speed"] = bird["speed"] + GRAVITY
        bird["y"] = bird["y"] + bird["speed"]

        if bird["y"] < bird["size"]:
            bird["y"] = bird["size"]
            bird["speed"] = 0

        for pipe in pipes:
            pipe["x"] = pipe["x"] - speed

            if pipe["scored"] == False and pipe["x"] + PIPE_W < bird["x"]:
                score = score + 1
                pipe["scored"] = True

            if pipe["x"] < -PIPE_W:
                pipe["x"] = 800
                pipe["gap_y"] = random.randint(150, 420)
                pipe["scored"] = False

            if hit_pipe(pipe, gap):
                state = "gameover"

        if bird["y"] + bird["size"] >= FLOOR_Y:
            bird["y"] = FLOOR_Y - bird["size"]
            state = "gameover"

    # ===== OUTPUT =====
    screen.fill(SKY)

    for pipe in pipes:
        top_h = pipe["gap_y"] - gap // 2
        bottom_y = pipe["gap_y"] + gap // 2
        pygame.draw.rect(screen, GREEN, (pipe["x"], 0, PIPE_W, top_h))
        pygame.draw.rect(screen, DGREEN, (pipe["x"] - 5, top_h - 22, PIPE_W + 10, 22))
        pygame.draw.rect(screen, GREEN, (pipe["x"], bottom_y, PIPE_W, FLOOR_Y - bottom_y))
        pygame.draw.rect(screen, DGREEN, (pipe["x"] - 5, bottom_y, PIPE_W + 10, 22))

    pygame.draw.rect(screen, GROUND, (0, FLOOR_Y, 800, 60))
    pygame.draw.circle(screen, (250, 210, 70), (bird["x"], int(bird["y"])), bird["size"])
    pygame.draw.circle(screen, (40, 40, 40), (bird["x"] + 7, int(bird["y"]) - 5), 3)

    t = font_big.render(str(score), True, "white")
    screen.blit(t, (400 - t.get_width() // 2, 50))
    screen.blit(font_sml.render("ระดับ: " + level["name"], True, DARK), (640, 24))

    if state == "gameover":
        pygame.draw.rect(screen, (250, 250, 250), (230, 220, 340, 150), border_radius=14)
        t = font_mid.render("เกมจบ!", True, DARK)
        screen.blit(t, (400 - t.get_width() // 2, 245))
        t = font_mid.render(f"คะแนน {score}", True, DARK)
        screen.blit(t, (400 - t.get_width() // 2, 285))
        t = font_sml.render("กด Space เล่นใหม่", True, (110, 130, 150))
        screen.blit(t, (400 - t.get_width() // 2, 330))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
