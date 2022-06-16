from views.welcome import Welcome
from views.menu import Menu
from .tournamentController import TournamentController
from .playerController import PlayerController


class Controller:
    """Base controller"""

    def __init__(self):
        self.welcome()
        self.tournament = None
        self.players = []
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
                    self.startTournament()
                case 2:
                    self.createPlayer()

        quit()

    def startTournament(self):
        self.tournament = TournamentController()
        self.choosePlayer()
        for round in range(tournament.tournamentModel.number_of_rounds):
            self.startRound()

    def createPlayer(self):
        number_of_players = int(input('Combien de joueur ? '))
        for i in range(number_of_players):
            player = PlayerController().PlayerModel
            self.players.append(player)

    def choosePlayer(self):
        self.createPlayer()
        self.tournament.tournamentModel.player_list = self.players

    def startRound(self):
        pass
        # generate pairs of players
        # ask for results
        # return
