from views.report import Report as ReportView
from dao.tournamentDao import TournamentDAO
from models.tournament import Tournament


class ReportController:

    def __init__(self):
        self.reportView = ReportView()
        self.reportView.displayTitle()
        self.tournamentDao = TournamentDAO()

    def chooseReport(self):
        choices = {
                '1': self.reportPlayers,
                '2': self.reportTournaments
            }
        user_choice = input(
            '1— Joueurs\n'
            '2— Tournois\n'
        )
        choices[user_input]()

    def reportPlayers(self):
        pass

    def reportTournaments(self):
        self.chooseTournament()

    def chooseTournament(self):
        dictTournaments = self.tournamentDao.getAll()
        self.reportView.displayTournaments(dictTournaments)
        user_choice = input('Choisissez un tournoi : ')
