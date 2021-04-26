import pygame
from Pages.SteeringWheelPage import SteeringWheelPage
from Pages.TyreTemperaturePage import TyreTemperaturePage
from pygame import Rect

pygame.font.init()

# Set window settings
FPS = 20
WINDOW = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = pygame.display.get_window_size()
pygame.display.set_caption("Formel 1 Telemetrie")

pageList = [SteeringWheelPage(WINDOW), TyreTemperaturePage(WINDOW)]

def main():
    run = True
    pageIndex = 0
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    run = False
                if event.key == pygame.K_UP:
                    pageIndex += 1 
                if event.key == pygame.K_DOWN:
                    pageIndex -= 1 
        pageIndex = draw_window(pageIndex)
    
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
