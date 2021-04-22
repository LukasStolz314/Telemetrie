import pygame
from PygameWidgets.Widgets.Page import Page
from PygameWidgets.Widgets.Column import Column 
from PygameWidgets.Widgets.Row import Row
from PygameWidgets.Widgets.GearDisplay import GearDisplay
from PygameWidgets.Widgets.ThrottleBar import ThrottleBar
from PygameWidgets.Widgets.HeaderBox import HeaderBox
from PygameWidgets.Widgets.Label import Label
from PygameWidgets.Widgets.ProgressBar import ProgressBar
import Utils.Colors as Colors

class SteeringWheelPage(Page):

    def __init__(this, window):
        super().__init__(window, "Steering Wheel")
    
    def buildPage(this):
        pageWidgetList = []

        WINDOW = this.window
        WIDTH = this.window.get_width()
        HEIGHT = this.window.get_height()

        WINDOW.fill(Colors.BLACK)

        leftHeaderBoxValues = ("298 KPH", ("L3", "P2"), ("12", "P2"))
        rightHeaderBoxValues = ("14.235", ("100°C", "96°C"), ("94°C", "90°C"))

        topRow = Row(WINDOW, 0, 0, [
            # Gear Widget
            GearDisplay(WINDOW, WIDTH//2, HEIGHT//6, 0, 0, \
                Colors.WHITE, Colors.WHITE, 8, 5, HEIGHT//2),

            # LeftHeaderBox Widget     
            HeaderBox(WINDOW, 10, 10, WIDTH//3, HEIGHT//3, \
                Colors.BLACK, Colors.WHITE, leftHeaderBoxValues, 2, 5, HEIGHT//12),

            # RightHeaderBox Widget    
            HeaderBox(WINDOW, WIDTH - 10 - WIDTH//3, 10, WIDTH//3, HEIGHT//3,\
                 Colors.BLACK, Colors.WHITE, rightHeaderBoxValues, 2, 5, HEIGHT//12),
        ])    	
        pageWidgetList.append(topRow)

        midColumn = Column(WINDOW, WIDTH//2, WIDTH//4.25, [
            # Delta Widget
            Label(WINDOW, 0, 0, WIDTH//9, WIDTH//9,\
                 None, Colors.GREEN, "-0.002", 50),

            # Overtake Widget
            Label(WINDOW, 0, HEIGHT//6, WIDTH//1.5, 40,\
                 Colors.GREEN, Colors.WHITE, ("Overtake", Colors.GREEN), 30),

            # ERS Widget
            ProgressBar(WINDOW, 0, 2 * HEIGHT//6, WIDTH//1.3, 10,\
                 Colors.BLACK, Colors.YELLOW, 50)
        ])
        pageWidgetList.append(midColumn)

        bottomRow = Row(WINDOW, WIDTH//3.39, 300, [
            # D Widget
            ProgressBar(WINDOW, 0, 0, WIDTH//2.8, 10,\
                Colors.BLACK, Colors.WHITE, 30),

            # W Widget     
            ProgressBar(WINDOW, WIDTH - WIDTH//1.695, 0, WIDTH//2.8, 10,\
                Colors.BLACK, Colors.WHITE, 60),
        ])    	
        pageWidgetList.append(bottomRow)

        this.widgets = pageWidgetList