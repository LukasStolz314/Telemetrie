import pygame
import PygameWidgets.Provider as events
from Pages.SteeringWheelPage import SteeringWheelPage
from Pages.TyreTemperaturePage import TyreTemperaturePage
from Pages.MenuPage import MenuPage
from pygame import Rect

pygame.font.init()

# Set window settings
FPS = 20
WINDOW = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = pygame.display.get_window_size()
pygame.display.set_caption("Formel 1 Telemetrie")

pageList = [MenuPage(WINDOW), SteeringWheelPage(WINDOW), TyreTemperaturePage(WINDOW)]

def main():
    run = True
    pageIndex = 0
    events.__init__()
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    run = False
                if event.key == pygame.K_r:
                    pageIndex = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                events.mouseClickEvents.append(event)
        pageIndex = draw_window(pageIndex)
        events.mouseClickEvents = []
    
    pygame.display.quit()


def draw_window(pageIndex):
    if not pageIndex > len(pageList) - 1 and pageIndex >= 0:
        selector = pageList[pageIndex].build()
        if selector != "" and selector != None:
            for page in pageList:
                if page.selector == selector:
                    pageIndex = pageList.index(page)
        else:
            pageList[pageIndex].drawWidgets()
    
    return pageIndex


if __name__ == "__main__":
    main()
