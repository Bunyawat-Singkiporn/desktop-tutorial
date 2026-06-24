import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Quiz Game")

font_q = pygame.font.Font(None, 48)   # แบบอักษรสำหรับคำถาม
font_c = pygame.font.Font(None, 36)   # แบบอักษรสำหรับตัวเลือก

questions = [
    "What is 2 + 2?",
    "What color is the sky?",
    "How many days in a week?",
    "Capital of Thailand?",
    "How many months in a year?"
]

choices = [
    ["2", "3", "4", "5"],
    ["red", "blue", "green", "yellow"],
    ["5", "6", "7", "8"],
    ["Bangkok", "Chiang Mai", "Phuket", "Pattaya"],
    ["10", "11", "12", "13"]
]

answers = [2, 1, 2, 0, 2]   # index ของตัวเลือกที่ถูก

current_q = 0
feedback  = ""

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and current_q < len(questions):
            key_map = {pygame.K_1: 0, pygame.K_2: 1,
                       pygame.K_3: 2, pygame.K_4: 3}
            if event.key in key_map:
                picked = key_map[event.key]
                if picked == answers[current_q]:
                    feedback = "Correct!"
                else:
                    feedback = "Wrong! Answer: " + choices[current_q][answers[current_q]]
                current_q += 1

    screen.fill("white")

    if current_q < len(questions):
        # แสดงคำถาม
        q_surf = font_q.render(questions[current_q], True, "black")
        screen.blit(q_surf, (50, 80))

        # แสดงตัวเลือก 4 ข้อ
        labels = ["1", "2", "3", "4"]
        for j in range(4):
            c_surf = font_c.render(f"{labels[j]}. {choices[current_q][j]}", True, "navy")
            screen.blit(c_surf, (100, 200 + j * 70))
    else:
        done_surf = font_q.render("Quiz Complete!", True, "black")
        screen.blit(done_surf, (230, 280))

    # แสดง feedback จากคำตอบก่อนหน้า
    if feedback:
        color = "green" if feedback == "Correct!" else "red"
        f_surf = font_c.render(feedback, True, color)
        screen.blit(f_surf, (50, 520))

    pygame.display.flip()

pygame.quit()
