import pygame

WINDOW_HEIGHT = 720
WINDOW_WIDTH = 1280

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("blue")

    pygame.display.flip()

    clock.tick(60)

pygame.quit()