import pygame
from PygameWidgets.Widgets.Page import Page
from PygameWidgets.Widgets.Column import Column 
from PygameWidgets.Widgets.Row import Row
from PygameWidgets.Widgets.GearDisplay import GearDisplay
import Utils.Colors as Colors

class TyreTemperaturePage(Page):

    def __init__(this, window):
        super().__init__(window, "Tyre Temperature", [])

    def build(this):
        WINDOW = this.window
        WIDTH = this.window.get_width()
        HEIGHT = this.window.get_height()

        WINDOW.fill(Colors.BLACK)

        topRow = Row(WINDOW, 0, 500, [
        # Gear Widget
        GearDisplay(WINDOW, WIDTH//2, HEIGHT//6, 0, HEIGHT//6, \
            Colors.WHITE, Colors.WHITE, -1, 5),
        ])    	
        this.widgetList.append(topRow)