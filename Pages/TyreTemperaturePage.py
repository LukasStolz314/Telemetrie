import pygame
from PygameWidgets.Widgets.Page import Page
from PygameWidgets.Widgets.Column import Column 
from PygameWidgets.Widgets.Row import Row
from PygameWidgets.Widgets.GearDisplay import GearDisplay
from PygameWidgets.Widgets.Tyre import Tyre
import Utils.Colors as Colors

class TyreTemperaturePage(Page):

    selector = "Tyre-Temperature"

    def __init__(this, window):
        super().__init__(window, [])

    def build(this, pr):
        WINDOW = this.window
        WIDTH = this.window.get_width()
        HEIGHT = this.window.get_height()

        WINDOW.fill(Colors.BLACK)

        tyreInfoValues = ("tyresWear", "tyresInnerTemperature", "tyresSurfaceTemperature")

        tireWidth = 100
        lineHeight = 150
        fontSize = 100

        topRow = Row(WINDOW, 0, 500, [
        Tyre(WINDOW, WIDTH * 0.4, HEIGHT//3, tireWidth, lineHeight, fontSize, 'RL', tyreInfoValues, pr), # Rear left tyre
        Tyre(WINDOW, WIDTH - WIDTH * 0.4, HEIGHT//3, tireWidth, lineHeight, fontSize, 'RR', tyreInfoValues, pr), # Rear right tyre
        Tyre(WINDOW, WIDTH * 0.4, - HEIGHT//4, tireWidth, lineHeight, fontSize, 'FL', tyreInfoValues, pr), # Front left tyre
        Tyre(WINDOW, WIDTH - WIDTH * 0.4, - HEIGHT//4, tireWidth, lineHeight, fontSize, 'FR', tyreInfoValues, pr), # Front right tyre
        ])
        this.widgetList.append(topRow)