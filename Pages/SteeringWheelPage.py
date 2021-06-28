from PygameWidgets.Widgets.TimeLabel import TimeLabel
import pygame
from PygameWidgets.Widgets.Page import Page
from PygameWidgets.Widgets.Column import Column 
from PygameWidgets.Widgets.Row import Row
from PygameWidgets.Widgets.GearDisplay import GearDisplay
from PygameWidgets.Widgets.ThrottleBar import ThrottleBar
from PygameWidgets.Widgets.HeaderBox import HeaderBox
from PygameWidgets.Widgets.TimeLabel import TimeLabel
from PygameWidgets.Widgets.ProgressBar import ProgressBar
from PygameWidgets.Widgets.EngineSpeed import EngineSpeed
from PygameWidgets.Widgets.OvertakeLabel import OvertakeLabel
import Utils.Colors as Colors

class SteeringWheelPage(Page):

    selector = "Steering-Wheel"

    def __init__(this, window):
        super().__init__(window, [])
    
    def build(this, pr):
        WINDOW = this.window
        WIDTH = this.window.get_width()
        HEIGHT = this.window.get_height()

        WINDOW.fill(Colors.BLACK)

        leftHeaderBoxValues = ("speed", "currentLapNum", "carPosition", "fuelRemainingLaps", "fuelInTank")
        rightHeaderBoxValues = ("bestLapTime", "tyresInnerTemperature")

        topRow = Row(WINDOW, 0, 0, [
            # Gear Widget
            GearDisplay(WINDOW, WIDTH//2, HEIGHT//6, 0, HEIGHT//6, \
                Colors.WHITE, Colors.WHITE, "gear", pr, 5),

            # LeftHeaderBox Widget     
            HeaderBox(WINDOW, 10, 10, WIDTH//3, HEIGHT//3, \
                Colors.BLACK, Colors.WHITE, leftHeaderBoxValues, pr, 2, HEIGHT//12),

            # RightHeaderBox Widget
            HeaderBox(WINDOW, WIDTH - 10 - WIDTH//3, 10, WIDTH//3, HEIGHT//3,\
                 Colors.BLACK, Colors.WHITE, rightHeaderBoxValues, pr, 2, HEIGHT//12, True),
        ])    	
        this.widgetList.append(topRow)

        # eng = EngineSpeed(WINDOW, WIDTH//2-700, topRow.bottomPosition + 50, 0, 0, "engineRPM", pr)
        # eng.draw()

        midColumn = Column(WINDOW, WIDTH//2, topRow.bottomPosition + HEIGHT//12, [
            # Delta Widget
            TimeLabel(WINDOW, 0, 0, WIDTH//9, HEIGHT//10,\
                 None, Colors.GREEN, "currentLapTime", pr),

            # Overtake Widget
            OvertakeLabel(WINDOW, 0, HEIGHT//6, WIDTH//1.5, HEIGHT//20,\
                 Colors.GREEN, Colors.WHITE, "ersDeployMode", pr),

            # ERS Widget
            ProgressBar(WINDOW, 0, 2 * HEIGHT//6, WIDTH//1.1, HEIGHT//50,\
                 Colors.BLACK, Colors.YELLOW, "ersStoreEnergy", pr)
        ], HEIGHT//3)
        this.widgetList.append(midColumn)

        bottomRow = Row(WINDOW, WIDTH//3.39, midColumn.bottomPosition + 1.5*(HEIGHT//12), [
            # D Widget
            ProgressBar(WINDOW, 0, 0, WIDTH//2.7, HEIGHT//50,\
                Colors.BLACK, Colors.WHITE, "ersHarvestedThisLapMGUK", pr),

            # W Widget     
            ProgressBar(WINDOW, WIDTH - WIDTH//1.695, 0, WIDTH//2.7, HEIGHT//50,\
                Colors.BLACK, Colors.WHITE, "ersHarvestedThisLapMGUH", pr),
        ])    	
        this.widgetList.append(bottomRow)