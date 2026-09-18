# Week 14 - เช็คพอยต์ 2 : สลับหน้าจอ menu / howto / playing
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

menu_items = ["เริ่มเกมใหม่", "วิธีเล่น", "ออกจากเกม"]
selected = 0
state = "menu"


def reset_game():
    for r in range(3):
        for c in range(3):
            board[r][c] = ""


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


def draw_title(text):
    t = font_big.render(text, True, "white")
    screen.blit(t, (300 - t.get_width() // 2, 40))


def draw_menu():
    draw_title("TIC - TAC - TOE")
    for i in range(len(menu_items)):
        y = 250 + i * 55
        if i == selected:
            text = "> " + menu_items[i]
            color = "yellow"
        else:
            text = "   " + menu_items[i]
            color = GREY
        t = font_mid.render(text, True, color)
        screen.blit(t, (190, y))
    t = font_sml.render("ลูกศรขึ้น-ลง เลือก  |  Enter ยืนยัน", True, GREY)
    screen.blit(t, (300 - t.get_width() // 2, 470))


def draw_howto():
    draw_title("วิธีเล่น")
    lines = [
        "ผู้เล่น 2 คนผลัดกันวางเครื่องหมาย",
        "ผู้เล่น 1 = X     ผู้เล่น 2 = O",
        "ใครเรียงได้ 3 ช่องติดกันก่อนชนะ",
        "แนวนอน แนวตั้ง หรือแนวทแยงก็ได้",
        "",
        "กด Esc เพื่อกลับเมนู",
    ]
    for i in range(len(lines)):
        t = font_sml.render(lines[i], True, GREY)
        screen.blit(t, (300 - t.get_width() // 2, 230 + i * 34))


running = True
while running:

    # ==================== INPUT ====================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if state == "menu":
                    running = False
                else:
                    state = "menu"

            elif state == "menu":
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(menu_items)
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(menu_items)
                if event.key == pygame.K_RETURN:
                    if selected == 0:
                        state = "playing"
                    if selected == 1:
                        state = "howto"
                    if selected == 2:
                        running = False

            elif state == "playing":
                if event.key == pygame.K_r:
                    reset_game()

        if event.type == pygame.MOUSEBUTTONDOWN and state == "playing":
            mx, my = event.pos
            r, c = cell_from_mouse(mx, my)
            if r >= 0 and board[r][c] == "":
                board[r][c] = "X"

    # ==================== OUTPUT ====================
    screen.fill(BG)

    if state == "menu":
        draw_menu()
    elif state == "howto":
        draw_howto()
    else:
        draw_title("TIC - TAC - TOE")
        draw_grid()
        draw_marks()
        t = font_sml.render("คลิกวาง X  |  R เริ่มใหม่  |  Esc กลับเมนู", True, GREY)
        screen.blit(t, (300 - t.get_width() // 2, 612))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
