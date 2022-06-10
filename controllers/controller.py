from views.welcome import Welcome
from views.menu import Menu

class Controller:
    """Base controller"""

    def __init__(self):
        self.welcome()
        self.menuLister()

    def welcome(self):
        welcome = Welcome()
        print(welcome.display)

    def menuLister(self):
        menu = Menu()
        print(menu.display)
