import pygame
from Pages.SteeringWheelPage import SteeringWheelPage
from Pages.TyreTemperaturePage import TyreTemperaturePage
from pygame import Rect
from python_f1_packetreader import packetreader
from threading import Thread
import logging

pygame.font.init()

# Set window settings
FPS = 30
WINDOW = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = pygame.display.get_window_size()
pygame.display.set_caption("Formel 1 Telemetrie")

pageList = [SteeringWheelPage(WINDOW), TyreTemperaturePage(WINDOW)]

def main():
    logging.basicConfig(format="%(levelname)s - %(message)s", level=logging.DEBUG)

    #pr = packetreader.PacketReader('127.0.0.1', 20777)
    #prThread = Thread(target=pr.run)
    #prThread.start()

    counter = 0

    logging.info("Packetreader thread started")

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
        print(counter)
        counter += 1
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
