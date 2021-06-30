import pygame
from Pages.SteeringWheelPage import SteeringWheelPage
from Pages.TyreTemperaturePage import TyreTemperaturePage
from pygame import Rect
from python_f1_packetreader import packetreader
from threading import Thread
import logging
import Utils.Colors as Colors
import argparse

parser = argparse.ArgumentParser(prog="F1-2020-Telemetry udp receiver", description="Collects telemetry data from F1 2020 udp server")
parser.add_argument("-i", "--ip", help="Local ip address or listen on all interfaces e.g. 0.0.0.0", required=True)
parser.add_argument("-p", "--port", help="Port of the udp server. Default: 20777", type=int, default=20777)
parser.add_argument("-P", "--page", help="Starting Page 0 or 1", type=int, default=0)

args = parser.parse_args()

pygame.font.init()

# Set window settings
FPS = 30
WINDOW = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = pygame.display.get_window_size()
pygame.display.set_caption("Formel 1 Telemetrie")

pageList = [SteeringWheelPage(WINDOW), TyreTemperaturePage(WINDOW)]

def main():
    logging.basicConfig(format="%(levelname)s - %(message)s", level=logging.DEBUG)

    pr = packetreader.PacketReader(args.ip, args.port)
    prThread = Thread(target=pr.run)
    prThread.start()

    logging.info("Packetreader thread started")

    pageIndex = args.page
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
        pageIndex = draw_window(pageIndex)
    pygame.display.quit()


def draw_window(pageIndex):
    if pageIndex < len(pageList) and pageIndex >= 0:
        WINDOW.fill(Colors.BLACK)
        pageList[pageIndex].drawWidgets()
    
    return pageIndex


if __name__ == "__main__":
    main()
