import pygame
import sys

WINDOW_HEIGHT = 720
WINDOW_WIDTH = 1280


def get_font(size):
    return pygame.font.Font("assets/UpheavalPro.ttf", size)


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

            self.screen.fill("black")
            pygame.display.set_caption("Hra")
            MainMenu().run()

            pygame.display.update()

            self.clock.tick(60)

class Button:
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

class MainMenu:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.bg = pygame.image.load("assets/main_screen.png")

    def run(self):
        self.screen.blit(self.bg, (0,0))
        pygame.display.set_caption("Black Boy")
        while True:

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = get_font(100).render("BLACK BOY", True, "#000000")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            PLAY_BUTTON = Button(image=pygame.image.load("assets/button.png"), pos=(640, 250), text_input="PLAY", font=get_font(75), base_color="#cc7f00", hovering_color="White")
            OPTIONS_BUTTON = Button(image=pygame.image.load("assets/button.png"), pos=(640, 350), text_input="OPTIONS", font=get_font(75), base_color="#cc7f00",hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load("assets/button.png"), pos=(640, 450), text_input="QUIT", font=get_font(75), base_color="#cc7f00", hovering_color="White")

            self.screen.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.screen.fill("white")
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.screen.fill("yellow")
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()


if __name__ == "__main__":
    hra = Game()
    hra.run()



