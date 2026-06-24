import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Quiz Game")

font_q = pygame.font.Font(None, 48)
font_c = pygame.font.Font(None, 36)

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

answers = [2, 1, 2, 0, 2]

current_q = 0
feedback  = ""
score     = 0       # NEW: track score

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
                    score += 1          # NEW
                else:
                    feedback = "Wrong! Answer: " + choices[current_q][answers[current_q]]
                current_q += 1

    screen.fill("white")

    # NEW: show score in top-right corner
    s_surf = font_c.render(f"Score: {score}/{len(questions)}", True, "black")
    screen.blit(s_surf, (600, 30))

    if current_q < len(questions):
        q_surf = font_q.render(questions[current_q], True, "black")
        screen.blit(q_surf, (50, 80))

        labels = ["1", "2", "3", "4"]
        for j in range(4):
            c_surf = font_c.render(f"{labels[j]}. {choices[current_q][j]}", True, "navy")
            screen.blit(c_surf, (100, 200 + j * 70))
    else:
        # NEW: result screen
        sc_surf = font_q.render(f"Score: {score}/{len(questions)}", True, "black")
        screen.blit(sc_surf, (230, 200))

        if score == len(questions):
            msg, col = "Perfect!", "gold"
        elif score >= 3:
            msg, col = "Good job!", "green"
        else:
            msg, col = "Keep practicing!", "red"

        m_surf = font_q.render(msg, True, col)
        screen.blit(m_surf, (280, 300))

    if feedback:
        color = "green" if feedback == "Correct!" else "red"
        f_surf = font_c.render(feedback, True, color)
        screen.blit(f_surf, (50, 520))

    pygame.display.flip()

pygame.quit()
