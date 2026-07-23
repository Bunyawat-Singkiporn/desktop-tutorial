import pygame

# ==========================
# START PYGAME
# ==========================
pygame.init()

# ==========================
# GAME WINDOW
# ==========================
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Guess The Number")

# ==========================
# FONT
# ==========================
font = pygame.font.Font(None, 48)

# ==========================
# GAME VARIABLES
# ==========================
message = "Guess Number 1-5"
secret_number = 3
score = 0

# ==========================
# GAME LOOP
# ==========================
running = True
while running:

    # --- EVENTS ---
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # --- INPUT ---
        if event.type == pygame.KEYDOWN:
            guess = None

            if event.key == pygame.K_1:
                guess = 1
            elif event.key == pygame.K_2:
                guess = 2
            elif event.key == pygame.K_3:
                guess = 3
            elif event.key == pygame.K_4:
                guess = 4
            elif event.key == pygame.K_5:
                guess = 5

            # --- PROCESS ---
            if guess is not None:
                if guess == secret_number:
                    message = "Correct!"
                    score += 1
                elif guess < secret_number:
                    message = "Too Low!"
                else:
                    message = "Too High!"

    # --- DRAW ---
    screen.fill("white")

    text = font.render(message, True, "black")
    screen.blit(text, (180, 250))

    score_text = font.render(f"Score: {score}", True, "blue")
    screen.blit(score_text, (20, 20))

    pygame.display.flip()

pygame.quit()
