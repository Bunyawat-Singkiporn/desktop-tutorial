import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Guess The Number")

font = pygame.font.Font(None, 48)
message = "Guess Number 1-5"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                message = "You pressed 1"
            elif event.key == pygame.K_2:
                message = "You pressed 2"
            elif event.key == pygame.K_3:
                message = "You pressed 3"
            elif event.key == pygame.K_4:
                message = "You pressed 4"
            elif event.key == pygame.K_5:
                message = "You pressed 5"

    screen.fill("white")
    text = font.render(message, True, "black")
    screen.blit(text, (180, 250))
    pygame.display.flip()

pygame.quit()
