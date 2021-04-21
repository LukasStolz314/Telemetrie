import pygame
from PygameWidgets.Widgets.GearDisplay import GearDisplay
from PygameWidgets.Widgets.ThrottleBar import ThrottleBar
from PygameWidgets.Widgets.HeaderBox import HeaderBox
from PygameWidgets.Widgets.Label import Label
from PygameWidgets.Widgets.ProgressBar import ProgressBar
from pygame import Rect

pygame.font.init()

# Set window settings
WIDTH, HEIGHT = 700, 350
FPS = 20
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
pygame.display.set_caption("Formel 1 Telemetrie")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

def main():
    run = True

    # Just to demonstration (will be removed later)
    gearsVar = 1

    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Just to demonstration (will be removed later)
                if event.key == pygame.K_RIGHT:
                    gearsVar += 1
                if event.key == pygame.K_LEFT:
                    gearsVar -= 1

        draw_window(gearsVar)
    
    pygame.display.quit()


def draw_window(gearsVar):
    WINDOW.fill(BLACK)

    # Gear Widget
    x, y, w, h = WIDTH//2, HEIGHT//6, None, None
    gear = GearDisplay(WINDOW, x, y, w, h, None, WHITE, 5, (HEIGHT//2))
    gearSize = gear.draw(gearsVar)

    # # Throttle Widget
    # throttle = ThrottleWidget(WINDOW, 0, 0, WIDTH//4, HEIGHT, BLACK)
    # throttle.draw(throttleVar)

    # LeftHeaderBox Widget
    x, y, w, h = 10, 10, WIDTH//3, HEIGHT//3
    leftHeaderBox = HeaderBox(WINDOW, x, y, w, h, BLACK, WHITE, 2, 5, HEIGHT//12)
    leftHeaderBox = leftHeaderBox.draw("298 KPH", ("L3", "P2"), ("12", "P2"))

    # RightHeaderBox Widget
    x, y, w, h = WIDTH - 10 - WIDTH//3, 10, WIDTH//3, HEIGHT//3
    rightHeaderBox = HeaderBox(WINDOW, x, y, w, h, BLACK, WHITE, 2, 5, HEIGHT//12)
    rightHeaderBoxSize = rightHeaderBox.draw("14.235", ("100°C", "96°C"), ("94°C", "90°C"))

    # Delta Widget
    x, y, w, h = WIDTH//2, gearSize[3], WIDTH//9, WIDTH//9
    delta = Label(WINDOW, x, y, w, h, None, GREEN, 50)
    deltaSize = delta.draw("-0.002")

    # Overtake Widget
    x, y, w, h = WIDTH//2, deltaSize[1] + deltaSize[3], WIDTH//1.5, 40
    overtake = Label(WINDOW, x, y, w, h, GREEN, WHITE, 30)
    overtakeSize = overtake.drawWithBackground("Overtake", GREEN)

    # ERS Widget
    x, y, w, h = WIDTH//2, overtakeSize[1] + overtakeSize[3], WIDTH//1.3, 10
    ers = ProgressBar(WINDOW, x, y, w, h, BLACK, YELLOW)
    ersSize = ers.draw(50)

    # D Widget
    x, y, w, h = WIDTH//3.39, ersSize[1] + ersSize[3] + HEIGHT//18, WIDTH//2.8, 10
    d = ProgressBar(WINDOW, x, y, w, h, BLACK, WHITE)
    dSize = d.draw(30)

    # H Widget
    x, y, w, h = WIDTH - WIDTH//3.39, ersSize[1] + ersSize[3] + HEIGHT//18, WIDTH//2.8, 10
    d = ProgressBar(WINDOW, x, y, w, h, BLACK, WHITE)
    dSize = d.draw(60)


    pygame.display.update()

if __name__ == "__main__":
    main()

