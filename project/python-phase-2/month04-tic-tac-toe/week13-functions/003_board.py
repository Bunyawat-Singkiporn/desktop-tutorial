# Week 13 - เช็คพอยต์ 2 : กระดาน 3x3 + วาดด้วยฟังก์ชัน
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 640))
pygame.display.set_caption("Tic-Tac-Toe")
clock = pygame.time.Clock()

BG   = (28, 38, 52)
LINE = (120, 150, 180)
XCOL = (240, 100, 100)
OCOL = (90, 190, 230)

CELL = 160
BX = 60
BY = 120

board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
]
board[0][0] = "X"
board[1][1] = "O"


def draw_grid():
    for i in range(1, 3):
        pygame.draw.line(screen, LINE, (BX + i * CELL, BY), (BX + i * CELL, BY + 3 * CELL), 6)
        pygame.draw.line(screen, LINE, (BX, BY + i * CELL), (BX + 3 * CELL, BY + i * CELL), 6)


def draw_marks():
    for r in range(3):
        for c in range(3):
            cx = BX + c * CELL + CELL // 2
            cy = BY + r * CELL + CELL // 2
            if board[r][c] == "X":
                pygame.draw.line(screen, XCOL, (cx - 40, cy - 40), (cx + 40, cy + 40), 10)
                pygame.draw.line(screen, XCOL, (cx + 40, cy - 40), (cx - 40, cy + 40), 10)
            if board[r][c] == "O":
                pygame.draw.circle(screen, OCOL, (cx, cy), 45, 10)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG)
    draw_grid()
    draw_marks()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
