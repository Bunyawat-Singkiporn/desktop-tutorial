import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption(
    "Guess The Number"
)

# NEW: สร้างตัวอักษร
font = pygame.font.Font(None, 48)

# NEW: ข้อความที่จะแสดง
message = "Guess Number 1-5"

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    # NEW: สร้างข้อความจากตัวแปร message
    text = font.render(
        message,
        True,
        "black"
    )

    # NEW: แสดงข้อความบนหน้าจอ
    screen.blit(
        text,
        (180, 250)
    )

    pygame.display.flip()

pygame.quit()