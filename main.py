import pygame
from Pages.SteeringWheelPage import SteeringWheelPage
from pygame import Rect

pygame.font.init()

# Set window settings
<<<<<<< HEAD
FPS = 20
WINDOW = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = pygame.display.get_window_size()
pygame.display.set_caption("Formel 1 Telemetrie")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)


def main():
    run = True

=======
WIDTH, HEIGHT = 700, 350
FPS = 30
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
pygame.display.set_caption("Formel 1 Telemetrie")

def main():
    run = True
>>>>>>> TryMoreFlexibleLayout
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    run = False

        draw_window()
    
    pygame.display.quit()


def draw_window():
    page1 = SteeringWheelPage(WINDOW)
    page1.buildPage()
    page1.drawWidgets()


if __name__ == "__main__":
    main()
