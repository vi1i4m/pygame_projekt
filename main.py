import pygame
import sys

WINDOW_HEIGHT = 720
WINDOW_WIDTH = 1280


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill("blue")
            pygame.display.set_caption("Skuska")

            pygame.display.flip()

            self.clock.tick(60)



if __name__ == "__main__":
    hra = Game()
    hra.run()



