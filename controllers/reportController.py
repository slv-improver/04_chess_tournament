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
            '1— Tous les joueurs\n'
            '2— Tous les tournois\n'
        )
        choices[user_choice]()

    def reportPlayers(self):
        pass

    def reportTournaments(self):
        self.chooseTournament()

    def chooseTournament(self):
        dictTournaments = self.tournamentDao.getAll()
        self.reportView.displayTournaments(dictTournaments)
        user_tournament = int(input('Choisissez un tournoi : ')) - 1
        choices = {
                '1': self.reportTournamentPlayers,
                '2': self.reportTournamentRounds,
                '3': self.reportTournamentMatches
            }
        user_choice = input(
            '——— Souhaitez-vous afficher :\n'
            '1— Les joueurs\n'
            '2— Les tours\n'
            '3— Les matchs\n'
        )
        choices[user_choice](dictTournaments[user_tournament])

    def reportTournamentPlayers(self, tournament):
        players = tournament["player_list"]
        self.reportView.reportTournamentPlayers(tournament['name'], players)

    def reportTournamentRounds(self, tournament):
        rounds = []
        for round in tournament['round_list']:
            round_copy = round.copy()
            round_copy.pop('matches_list')
            rounds.append(round_copy)
        self.reportView.reportTournamentRounds(tournament['name'], rounds)

    def reportTournamentMatches(self, tournament):
        pass
