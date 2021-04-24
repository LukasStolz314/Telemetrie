import pygame
from Pages.SteeringWheelPage import SteeringWheelPage
from pygame import Rect

pygame.font.init()

# Set window settings
FPS = 20
WINDOW = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = pygame.display.get_window_size()
pygame.display.set_caption("Formel 1 Telemetrie")

def main():
    run = True

    #test
    test = 0

    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    run = False
                if event.key == pygame.K_DOWN:
                    test -= 1
                if event.key == pygame.K_UP:
                    test += 1

        draw_window(test)
    
    pygame.display.quit()


def draw_window(test):
    page1 = SteeringWheelPage(WINDOW)
    page1.buildPage(test)
    page1.drawWidgets()


if __name__ == "__main__":
    main()
