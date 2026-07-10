import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()

bird_x = 150
bird_y = 300
bird_size = 25
bird_speed = 0
GRAVITY = 0.4

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    bird_speed += GRAVITY
    bird_y += bird_speed

    screen.fill("skyblue")
    pygame.draw.circle(screen, "yellow", (bird_x, int(bird_y)), bird_size)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
