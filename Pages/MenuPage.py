import pygame
from PygameWidgets.Widgets.Page import Page
from PygameWidgets.Widgets.Column import Column 
from PygameWidgets.Widgets.Row import Row
from PygameWidgets.Widgets.ImageButton import ImageButton
from .SteeringWheelPage import SteeringWheelPage
from .TyreTemperaturePage import TyreTemperaturePage
import Utils.Colors as Colors

class MenuPage(Page):

    selector = "Menu"

    def __init__(this, window):
        super().__init__(window, [])

        
    def build(this):
        WINDOW = this.window
        WIDTH = this.window.get_width()
        HEIGHT = this.window.get_height()

        WINDOW.fill(Colors.BLACK)
        
        topRow = Row(WINDOW, 0, HEIGHT//3.5, [
            # First ImageButton Widget 
            ImageButton(WINDOW, 1*(WIDTH//8), 0, 322, 221, None, None,\
                "PygameWidgets/Images/SteeringWheel.png", SteeringWheelPage.selector),

            # Second ImageButton Widget     
            ImageButton(WINDOW, 3*(WIDTH//8), 0, 322, 221, None, None,\
                "PygameWidgets/Images/SteeringWheel.png", TyreTemperaturePage.selector),

            # Third ImageButton Widget 
            ImageButton(WINDOW, 5*(WIDTH//8), 0, 322, 221, None, None,\
                "PygameWidgets/Images/SteeringWheel.png", SteeringWheelPage.selector),

            # Fourth ImageButton Widget 
            ImageButton(WINDOW, 7*(WIDTH//8), 0, 322, 221, None, None,\
                "PygameWidgets/Images/SteeringWheel.png", SteeringWheelPage.selector)
        ])    	
        this.widgetList.append(topRow)

        for btn in topRow.Widgets:
            selector = btn.checkClick()
            if selector != "":
                return selector

        bottomRow = Row(WINDOW, 0, 2.5*(HEIGHT//3.5), [
            # First ImageButton Widget 
            ImageButton(WINDOW, 1*(WIDTH//8), 0, 322, 221, None, None,\
                "PygameWidgets/Images/SteeringWheel.png", SteeringWheelPage.selector),

            # Second ImageButton Widget     
            ImageButton(WINDOW, 3*(WIDTH//8), 0, 322, 221, None, None,\
                "PygameWidgets/Images/SteeringWheel.png", SteeringWheelPage.selector),

            # Third ImageButton Widget 
            ImageButton(WINDOW, 5*(WIDTH//8), 0, 322, 221, None, None,\
                "PygameWidgets/Images/SteeringWheel.png", SteeringWheelPage.selector),

            # Fourth ImageButton Widget 
            ImageButton(WINDOW, 7*(WIDTH//8), 0, 322, 221, None, None,\
                "PygameWidgets/Images/SteeringWheel.png", SteeringWheelPage.selector)
        ])    	
        this.widgetList.append(bottomRow)

        for btn in bottomRow.Widgets:
            selector = btn.checkClick()
            if selector != "":
                return selector
