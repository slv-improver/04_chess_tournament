from views.welcome import Welcome
from views.menu import Menu

class Controller:
    """Base controller"""

    def __init__(self):
        self.welcome()
        self.handleGame()

    def welcome(self):
        welcome = Welcome()
        print(welcome.display)

    def menuLister(self):
        menu = Menu()
        print(menu.display)
        return int(input('Faites votre choix : '))

    def handleGame(self):
        user_input = 0
        while user_input != 4:
            user_input = self.menuLister()
        quit()
