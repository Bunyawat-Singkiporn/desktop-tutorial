# Week 5 - เช็คพอยต์ 3 : กด 1-4 ตอบ + ไปข้อถัดไป
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Quiz Arena")
clock = pygame.time.Clock()

font_big = pygame.font.SysFont("tahoma", 40)
font_mid = pygame.font.SysFont("tahoma", 30)

questions = [
    ["2 + 3 เท่ากับเท่าไร?", ["4", "5", "6", "7"], 2],
    ["สีของท้องฟ้าตอนกลางวัน?", ["แดง", "ฟ้า", "เขียว", "ดำ"], 2],
    ["Python ใช้คำสั่งใดแสดงผล?", ["show", "echo", "print", "say"], 3],
    ["1 สัปดาห์มีกี่วัน?", ["5", "6", "7", "8"], 3],
]
index = 0
finished = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not finished:
            picked = 0
            if event.key == pygame.K_1:
                picked = 1
            if event.key == pygame.K_2:
                picked = 2
            if event.key == pygame.K_3:
                picked = 3
            if event.key == pygame.K_4:
                picked = 4

            if picked > 0:
                index += 1
                if index >= len(questions):
                    finished = True

    screen.fill((25, 30, 50))

    title = font_big.render("QUIZ ARENA", True, "white")
    screen.blit(title, (50, 40))

    if finished:
        end = font_big.render("จบเกม!", True, "white")
        screen.blit(end, (300, 280))
    else:
        q = questions[index]
        choices = q[1]

        qtext = font_mid.render(q[0], True, "yellow")
        screen.blit(qtext, (60, 140))

        for i in range(4):
            y = 220 + i * 70
            pygame.draw.rect(screen, (45, 55, 90), (100, y, 600, 55), border_radius=8)
            line = font_mid.render(f"{i+1})  {choices[i]}", True, "white")
            screen.blit(line, (125, y + 12))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
