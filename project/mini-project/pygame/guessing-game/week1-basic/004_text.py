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

    screen.fill("white")
    text = font.render(message, True, "black")
    screen.blit(text, (180, 250))
    pygame.display.flip()

pygame.quit()
