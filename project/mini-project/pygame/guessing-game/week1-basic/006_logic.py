import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Guess The Number")

font = pygame.font.Font(None, 48)
message = "Guess Number 1-5"
secret_number = 3

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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

            if guess is not None:
                if guess == secret_number:
                    message = "Correct!"
                elif guess < secret_number:
                    message = "Too Low!"
                else:
                    message = "Too High!"

    screen.fill("white")
    text = font.render(message, True, "black")
    screen.blit(text, (180, 250))
    pygame.display.flip()

pygame.quit()
