import pygame
from Pages.SteeringWheelPage import SteeringWheelPage
from Pages.TyreTemperaturePage import TyreTemperaturePage
from pygame import Rect
from python_f1_packetreader import packetreader
from threading import Thread
import logging
import Utils.Colors as Colors

pygame.font.init()

# Set window settings
FPS = 30
WINDOW = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = pygame.display.get_window_size()
pygame.display.set_caption("Formel 1 Telemetrie")

pageList = [SteeringWheelPage(WINDOW), TyreTemperaturePage(WINDOW)]

def main():
    logging.basicConfig(format="%(levelname)s - %(message)s", level=logging.DEBUG)

    pr = packetreader.PacketReader('127.0.0.1', 20777)
    prThread = Thread(target=pr.run)
    prThread.start()

    print(vars(pr)['gear'])

    logging.info("Packetreader thread started")

    pageIndex = 0
    for page in pageList:
        page.build(pr)

    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                if event.key == pygame.K_UP:
                    pr.speed += 1
                    print(pr.gear)
                if event.key == pygame.K_DOWN:
                    pr.currentLapTime += 1
                    print(pr.gear)
        pageIndex = draw_window(pageIndex)
    pygame.display.quit()


def draw_window(pageIndex):
    if pageIndex < len(pageList) - 1 and pageIndex >= 0:
        WINDOW.fill(Colors.BLACK)
        pageList[pageIndex].drawWidgets()
    
    return pageIndex


if __name__ == "__main__":
    main()
