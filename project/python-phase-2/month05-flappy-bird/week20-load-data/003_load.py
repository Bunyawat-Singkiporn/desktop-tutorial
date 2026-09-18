# ============================================================
# Week 20 - เช็คพอยต์ 2 : โหลดสถิติตอนเปิดเกม
# รวม: dict + list ของ dict + แรงโน้มถ่วง + ตารางความยาก
#      + บันทึกลงไฟล์ + โหลดกลับ + หน้าเมนูพร้อมสถิติ
# รัน: python game.py   |   Space เริ่ม/กระโดด | R กลับเมนู | Esc ออก
# ============================================================
import pygame
import random
import os

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Flappy Bird v1.0")
clock = pygame.time.Clock()

font_big = pygame.font.SysFont("tahoma", 44)
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

SAVE_FILE = "flappy_save.txt"
HISTORY_FILE = "flappy_history.txt"

# ---------- ตารางความยาก ----------
LEVELS = [
    {"name": "ง่าย", "gap": 200, "speed": 2, "at": 0},
    {"name": "ปกติ", "gap": 160, "speed": 3, "at": 5},
    {"name": "ยาก", "gap": 130, "speed": 4, "at": 12},
    {"name": "โหด", "gap": 110, "speed": 5, "at": 20},
]

bird = {"x": 150, "y": 300, "speed": 0, "size": 18}
pipes = []
score = 0
state = "menu"


# ==================== ไฟล์ ====================
def load_best():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            text = f.read().strip()
            if text != "":
                return int(text)
    return 0


def save_best():
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        f.write(str(best))


def save_history():
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(str(score) + "," + current_level()["name"] + "\n")


def load_stats():
    return 0, 0


# ==================== เกม ====================
def current_level():
    result = LEVELS[0]
    for lv in LEVELS:
        if score >= lv["at"]:
            result = lv
    return result


def reset_game():
    global score, pipes
    bird["y"] = 300
    bird["speed"] = 0
    score = 0
    pipes = []
    for i in range(3):
        pipes.append({"x": 500 + i * 300,
                      "gap_y": random.randint(150, 420),
                      "scored": False})


def hit_pipe(pipe, gap):
    bx = bird["x"]
    by = bird["y"]
    r = bird["size"]
    near_x = bx + r > pipe["x"] and bx - r < pipe["x"] + PIPE_W
    in_gap = by - r > pipe["gap_y"] - gap // 2 and by + r < pipe["gap_y"] + gap // 2
    return near_x and not in_gap


best = load_best()
rounds, total_score = load_stats()
reset_game()

running = True
while running:
    level = current_level()
    gap = level["gap"]
    speed = level["speed"]

    # ==================== INPUT ====================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                if state == "menu":
                    reset_game()
                    state = "playing"
                elif state == "playing":
                    bird["speed"] = JUMP
                else:
                    reset_game()
                    state = "playing"
            if event.key == pygame.K_r and state == "gameover":
                state = "menu"

    # ==================== PROCESS ====================
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

        # ---------- จบเกม: บันทึก + โหลดสถิติใหม่ ----------
        if state == "gameover":
            save_history()
            if score > best:
                best = score
                save_best()
            rounds, total_score = load_stats()

    # ==================== OUTPUT ====================
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

    if state == "menu":
        pygame.draw.rect(screen, (250, 250, 250), (170, 130, 460, 340), border_radius=16)
        t = font_big.render("FLAPPY BIRD v1.0", True, DARK)
        screen.blit(t, (400 - t.get_width() // 2, 165))
        t = font_mid.render("กด Space เพื่อเริ่ม", True, (200, 130, 50))
        screen.blit(t, (400 - t.get_width() // 2, 250))

        if rounds > 0:
            average = total_score / rounds
        else:
            average = 0

        t = font_sml.render(f"สถิติสูงสุด  : {best}", True, DARK)
        screen.blit(t, (280, 320))
        t = font_sml.render(f"เล่นไปแล้ว   : {rounds} รอบ", True, DARK)
        screen.blit(t, (280, 352))
        t = font_sml.render(f"คะแนนเฉลี่ย : {average:.1f}", True, DARK)
        screen.blit(t, (280, 384))
        t = font_sml.render("Esc ออกจากเกม", True, (150, 165, 180))
        screen.blit(t, (280, 424))

    else:
        t = font_big.render(str(score), True, "white")
        screen.blit(t, (400 - t.get_width() // 2, 50))
        screen.blit(font_sml.render("ระดับ: " + level["name"], True, DARK), (640, 24))
        screen.blit(font_sml.render(f"ดีที่สุด {best}", True, DARK), (20, 24))

        if state == "gameover":
            pygame.draw.rect(screen, (250, 250, 250), (230, 210, 340, 180), border_radius=14)
            t = font_mid.render("เกมจบ!", True, DARK)
            screen.blit(t, (400 - t.get_width() // 2, 232))
            t = font_mid.render(f"คะแนน {score}", True, DARK)
            screen.blit(t, (400 - t.get_width() // 2, 272))
            if score >= best and score > 0:
                t = font_sml.render("สถิติใหม่!", True, (220, 140, 40))
                screen.blit(t, (400 - t.get_width() // 2, 310))
            t = font_sml.render("Space เล่นใหม่  |  R กลับเมนู", True, (110, 130, 150))
            screen.blit(t, (400 - t.get_width() // 2, 348))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
