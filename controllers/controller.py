from views.welcome import Welcome
from views.menu import Menu
from .tournamentController import TournamentController
from .playerController import PlayerController
from dao.playerDao import PlayerDAO


class Controller:
    """Base controller"""

    def __init__(self):
        self.welcome()
        self.playerDao = PlayerDAO()
        self.players = PlayerController.getPlayers()
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
                    self.startTournament()
                case 2:
                    self.createPlayer()

        quit()

    def startTournament(self):
        self.tournament = TournamentController()
        self.choosePlayer()
        for round in range(self.tournament.tournamentModel.number_of_rounds):
            self.tournament.startRound(round + 1)

        self.tournament.declareWinner()

    def createPlayer(self):
        number_of_players = int(input('Combien de joueur ? '))
        for i in range(number_of_players):
            player = PlayerController().playerModel
            self.players.append(player)
        self.storePlayers(self.players)

    def choosePlayer(self):
        self.createPlayer()
        self.tournament.tournamentModel.player_list = self.players

    def storePlayers(self, players):
        serializedPlayers = []
        for player in players:
            serializedPlayers.append(player.serialize())
        print(serializedPlayers)
        self.playerDao.insertData(serializedPlayers)
