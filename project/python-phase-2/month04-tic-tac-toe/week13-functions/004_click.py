# Week 13 - เช็คพอยต์ 3 : คลิกวาง X
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 640))
pygame.display.set_caption("Tic-Tac-Toe")
clock = pygame.time.Clock()

font_big = pygame.font.SysFont("tahoma", 38)
font_mid = pygame.font.SysFont("tahoma", 24)
font_sml = pygame.font.SysFont("tahoma", 17)

BG   = (28, 38, 52)
LINE = (120, 150, 180)
XCOL = (240, 100, 100)
OCOL = (90, 190, 230)
GREY = (150, 168, 188)

CELL = 160
BX = 60
BY = 120

board = [["", "", ""], ["", "", ""], ["", "", ""]]


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


def cell_from_mouse(mx, my):
    c = (mx - BX) // CELL
    r = (my - BY) // CELL
    if r < 0 or r > 2 or c < 0 or c > 2:
        return -1, -1
    return r, c


def draw_title():
    t = font_big.render("TIC - TAC - TOE", True, "white")
    screen.blit(t, (300 - t.get_width() // 2, 36))
    t = font_sml.render("คลิกช่องเพื่อวาง X  |  Esc ออก", True, GREY)
    screen.blit(t, (300 - t.get_width() // 2, 610))


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            r, c = cell_from_mouse(mx, my)
            if r >= 0 and board[r][c] == "":
                board[r][c] = "X"

    screen.fill(BG)
    draw_title()
    draw_grid()
    draw_marks()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
