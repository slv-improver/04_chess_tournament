from views.welcome import Welcome
from views.menu import Menu
from .tournamentController import TournamentController
from .playerController import PlayerController


class Controller:
    """Base controller"""

    def __init__(self):
        self.welcome()
        self.tournament = None
        self.handleGame()

    def printError(self, message):
        print(f'   —————\n  |  {message}\n   —————')

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
                self.printError('Le nombre n\'est pas compris dans la liste')
        except ValueError:
            self.printError('Il faut entrer un nombre')
            return 0

    def handleGame(self):
        user_input = 0
        while user_input != 4:
            user_input = self.menuLister()

            match user_input:
                case 1:
                    self.tournament = TournamentController()
                case 2:
                    self.players = PlayerController()

        quit()
