# ============================================================
# TIC-TAC-TOE v1.1  -  เกมสมบูรณ์ปิดเดือน 4  (เฉลย Week 16)
# รวม: เมนู + วิธีเล่น + ผลัดตา X/O + ตรวจผู้ชนะ 8 แนว + เสมอ + สถิติ
#      + เส้นขีดทับช่องที่ชนะ + ไฮไลต์ช่องที่เมาส์ชี้
# รัน: python game.py
# ปุ่ม: ลูกศร/Enter เมนู | คลิกวางเครื่องหมาย | R เริ่มใหม่ | Esc กลับเมนู
# ============================================================
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 640))
pygame.display.set_caption("Tic-Tac-Toe v1.0")
clock = pygame.time.Clock()

font_big = pygame.font.SysFont("tahoma", 34)
font_mid = pygame.font.SysFont("tahoma", 24)
font_sml = pygame.font.SysFont("tahoma", 17)

BG    = (28, 38, 52)
PANEL = (44, 58, 76)
LINE  = (120, 150, 180)
XCOL  = (240, 100, 100)
OCOL  = (90, 190, 230)
GREY  = (150, 168, 188)

CELL = 150
BX = 75
BY = 150

board = [["", "", ""], ["", "", ""], ["", "", ""]]
menu_items = ["เริ่มเกมใหม่", "วิธีเล่น", "ออกจากเกม"]
selected = 0
state = "menu"
turn = "X"
winner = ""
score_x = 0
score_o = 0
score_draw = 0
win_line = []


def reset_game():
    global turn, winner, win_line
    for r in range(3):
        for c in range(3):
            board[r][c] = ""
    turn = "X"
    winner = ""
    win_line = []


def check_winner():
    global win_line
    # แนวนอน
    for r in range(3):
        if board[r][0] != "" and board[r][0] == board[r][1] and board[r][1] == board[r][2]:
            win_line = [(r, 0), (r, 1), (r, 2)]
            return board[r][0]
    # แนวตั้ง
    for c in range(3):
        if board[0][c] != "" and board[0][c] == board[1][c] and board[1][c] == board[2][c]:
            win_line = [(0, c), (1, c), (2, c)]
            return board[0][c]
    # แนวทแยง
    if board[0][0] != "" and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        win_line = [(0, 0), (1, 1), (2, 2)]
        return board[0][0]
    if board[0][2] != "" and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        win_line = [(0, 2), (1, 1), (2, 0)]
        return board[0][2]
    return ""


def board_full():
    for r in range(3):
        for c in range(3):
            if board[r][c] == "":
                return False
    return True


def cell_from_mouse(mx, my):
    c = (mx - BX) // CELL
    r = (my - BY) // CELL
    if r < 0 or r > 2 or c < 0 or c > 2:
        return -1, -1
    return r, c


def draw_title(text):
    t = font_big.render(text, True, "white")
    screen.blit(t, (300 - t.get_width() // 2, 34))


def draw_grid():
    for i in range(1, 3):
        pygame.draw.line(screen, LINE, (BX + i * CELL, BY), (BX + i * CELL, BY + 3 * CELL), 6)
        pygame.draw.line(screen, LINE, (BX, BY + i * CELL), (BX + 3 * CELL, BY + i * CELL), 6)


def draw_hover():
    mx, my = pygame.mouse.get_pos()
    r, c = cell_from_mouse(mx, my)
    if r >= 0 and board[r][c] == "":
        x = BX + c * CELL
        y = BY + r * CELL
        pygame.draw.rect(screen, (40, 55, 74), (x + 4, y + 4, CELL - 8, CELL - 8), border_radius=8)


def draw_win_line():
    if len(win_line) == 3:
        r1, c1 = win_line[0]
        r2, c2 = win_line[2]
        x1 = BX + c1 * CELL + CELL // 2
        y1 = BY + r1 * CELL + CELL // 2
        x2 = BX + c2 * CELL + CELL // 2
        y2 = BY + r2 * CELL + CELL // 2
        pygame.draw.line(screen, (250, 220, 90), (x1, y1), (x2, y2), 10)


def draw_marks():
    for r in range(3):
        for c in range(3):
            cx = BX + c * CELL + CELL // 2
            cy = BY + r * CELL + CELL // 2
            if board[r][c] == "X":
                pygame.draw.line(screen, XCOL, (cx - 38, cy - 38), (cx + 38, cy + 38), 10)
                pygame.draw.line(screen, XCOL, (cx + 38, cy - 38), (cx - 38, cy + 38), 10)
            if board[r][c] == "O":
                pygame.draw.circle(screen, OCOL, (cx, cy), 42, 10)


def draw_turn():
    if turn == "X":
        text = "ตาของ ผู้เล่น 1 (X)"
        color = XCOL
    else:
        text = "ตาของ ผู้เล่น 2 (O)"
        color = OCOL
    t = font_mid.render(text, True, color)
    screen.blit(t, (300 - t.get_width() // 2, 96))


def draw_score():
    t = font_sml.render(f"X {score_x}   -   O {score_o}   -   เสมอ {score_draw}", True, GREY)
    screen.blit(t, (300 - t.get_width() // 2, 614))


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
        "ถ้ากระดานเต็มแต่ไม่มีใครเรียงครบ = เสมอ",
        "",
        "กด Esc เพื่อกลับเมนู",
    ]
    for i in range(len(lines)):
        t = font_sml.render(lines[i], True, GREY)
        screen.blit(t, (300 - t.get_width() // 2, 220 + i * 34))


def draw_result():
    pygame.draw.rect(screen, PANEL, (70, 250, 460, 170), border_radius=14)
    if winner == "draw":
        text = "เสมอ!"
        color = GREY
    elif winner == "X":
        text = "ผู้เล่น 1 (X) ชนะ!"
        color = XCOL
    else:
        text = "ผู้เล่น 2 (O) ชนะ!"
        color = OCOL
    t = font_big.render(text, True, color)
    screen.blit(t, (300 - t.get_width() // 2, 290))
    t = font_sml.render("กด R เล่นอีกครั้ง  |  Esc กลับเมนู", True, GREY)
    screen.blit(t, (300 - t.get_width() // 2, 360))


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
                        reset_game()
                        state = "playing"
                    if selected == 1:
                        state = "howto"
                    if selected == 2:
                        running = False

            elif event.key == pygame.K_r and (state == "playing" or state == "result"):
                reset_game()
                state = "playing"

        if event.type == pygame.MOUSEBUTTONDOWN and state == "playing":
            mx, my = event.pos
            r, c = cell_from_mouse(mx, my)
            if r >= 0 and board[r][c] == "":
                board[r][c] = turn

                winner = check_winner()
                if winner != "":                     # ตรวจผู้ชนะก่อนเสมอเสมอ
                    state = "result"
                    if winner == "X":
                        score_x = score_x + 1
                    else:
                        score_o = score_o + 1
                elif board_full():
                    winner = "draw"
                    state = "result"
                    score_draw = score_draw + 1
                else:
                    if turn == "X":
                        turn = "O"
                    else:
                        turn = "X"

    # ==================== OUTPUT ====================
    screen.fill(BG)

    if state == "menu":
        draw_menu()
    elif state == "howto":
        draw_howto()
    else:
        draw_title("TIC - TAC - TOE")
        if state == "playing":
            draw_turn()
            draw_hover()
        draw_grid()
        draw_marks()
        draw_win_line()
        draw_score()
        if state == "result":
            draw_result()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
