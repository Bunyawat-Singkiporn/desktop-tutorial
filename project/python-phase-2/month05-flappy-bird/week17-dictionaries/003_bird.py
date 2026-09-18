# Week 17 - เช็คพอยต์ 2 : นก + แรงโน้มถ่วง
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
font = pygame.font.SysFont("tahoma", 22)

SKY = (120, 190, 220)
GRAVITY = 0.5
JUMP = -9

bird = {
    "x": 150,
    "y": 300,
    "speed": 0,
    "size": 18,
}

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird["speed"] = JUMP
            if event.key == pygame.K_ESCAPE:
                running = False

    bird["speed"] = bird["speed"] + GRAVITY
    bird["y"] = bird["y"] + bird["speed"]

    if bird["y"] < bird["size"]:
        bird["y"] = bird["size"]
        bird["speed"] = 0
    if bird["y"] > 600 - bird["size"]:
        bird["y"] = 600 - bird["size"]
        bird["speed"] = 0

    screen.fill(SKY)
    pygame.draw.circle(screen, (250, 210, 70), (bird["x"], int(bird["y"])), bird["size"])
    screen.blit(font.render("กด Space ให้นกกระโดด  |  Esc ออก", True, (40, 60, 80)), (20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
