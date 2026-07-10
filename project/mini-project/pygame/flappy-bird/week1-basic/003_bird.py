import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Flappy Bird")

bird_x = 150
bird_y = 300
bird_size = 25

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("skyblue")
    pygame.draw.circle(screen, "yellow", (bird_x, bird_y), bird_size)
    pygame.display.flip()

pygame.quit()
