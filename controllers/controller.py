from views.welcome import Welcome
from views.menu import Menu
from .tournamentController import TournamentController
from .playerController import PlayerController
from .reportController import ReportController


class Controller:
    """Base controller"""

    def __init__(self):
        self.welcome()
        self.master_player = PlayerController(master=True)
        self.players = self.master_player.getPlayers()
        self.players_for_tournament = []
        self.tournament = None
        self.reportController = None
        self.handleGame()

    def printError(self, message):
        print(f'   —————\n  |  {message}\n   —————')

    def welcome(self):
        welcome = Welcome()
        welcome.displayTitle()

    def menuLister(self):
        menu = Menu()
        menu.displayMenu()
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
                    self.managePlayers()
                case 3:
                    self.generateReport()

        quit()

    def startTournament(self):
        self.tournament = TournamentController()
        self.players_for_tournament = self.master_player.choosePlayers(
            self.players,
            int(input('Combien de joueurs participent ? '))
        )
        self.tournament.tournamentModel.player_list = (
            self.players_for_tournament
        )
        for round in range(self.tournament.tournamentModel.number_of_rounds):
            self.tournament.startRound(round + 1)

        self.tournament.tournamentModel.player_list.sort(
            key=lambda x: (-x.tournament_points, x.ranking)
        )
        self.tournament.declareWinner()
        self.tournament.clearprevious_opponents()
        self.tournament.updateRanking()
        self.tournament.storeTournament()

    def managePlayers(self):
        self.createPlayer()

    def createPlayer(self):
        number_of_players = int(input('Combien de joueur ? '))
        for i in range(number_of_players):
            player = PlayerController().playerModel
            self.players.append(player)
        self.master_player.storePlayers(self.players)

    def generateReport(self):
        self.reportController = ReportController()
