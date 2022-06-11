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
        try:
            user_input = int(input('Faites votre choix : '))
            if user_input > 0 and user_input <= 4:
                return user_input
            else:
                print('———\n!! Le nombre n\'est pas compris dans la liste.\n———' )
        except ValueError:
            print('———\n!! Il faut entrer un nombre.\n———')
            return 0

    def handleGame(self):
        user_input = 0
        while user_input != 4:
            user_input = self.menuLister()
        quit()
