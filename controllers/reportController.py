from views.report import Report as ReportView
from dao.tournamentDao import TournamentDAO
from dao.playerDao import PlayerDAO


class ReportController:

    def __init__(self):
        self.reportView = ReportView()
        self.reportView.displayTitle()
        self.tournamentDao = TournamentDAO()
        self.playerDao = PlayerDAO()

    def chooseReport(self):
        choices = {
                '1': self.reportPlayers,
                '2': self.reportTournaments
            }
        user_choice = self.reportView.askUser(
            '1— Tous les joueurs\n'
            '2— Tous les tournois\n'
        )
        choices[user_choice]()

    def reportPlayers(self):
        sort_by_rank = self.chooseSortingMethod()
        dictPlayers = self.sortPlayers(
            self.playerDao.getAll(),
            sort_by_rank
        )
        self.reportView.reportPlayers(dictPlayers)

    def reportTournaments(self):
        self.chooseTournament()

    def chooseTournament(self):
        dictTournaments = self.tournamentDao.getAll()
        self.reportView.displayTournaments(dictTournaments)
        user_tournament = int(self.reportView.askUser(
            'Choisissez un tournoi : '
        )) - 1
        choices = {
                '1': self.reportTournamentPlayers,
                '2': self.reportTournamentRounds,
                '3': self.reportTournamentMatches
            }
        user_choice = self.reportView.askUser(
            '——— Souhaitez-vous afficher :\n'
            '1— Les joueurs\n'
            '2— Les tours\n'
            '3— Les matchs\n'
        )
        choices[user_choice](dictTournaments[user_tournament])

    def reportTournamentPlayers(self, tournament):
        sort_by_rank = self.chooseSortingMethod()
        players = self.sortPlayers(
            tournament["player_list"],
            sort_by_rank
        )
        self.reportView.reportTournamentPlayers(tournament['name'], players)

    def reportTournamentRounds(self, tournament):
        rounds = []
        for round in tournament['round_list']:
            round_copy = round.copy()
            round_copy.pop('matches_list')
            rounds.append(round_copy)
        self.reportView.reportTournamentRounds(tournament['name'], rounds)

    def reportTournamentMatches(self, tournament):
        rounds = []
        for round in tournament['round_list']:
            round_copy = round['matches_list']
            rounds.append(round_copy)
        self.reportView.reportTournamentMatches(tournament['name'], rounds)

    def chooseSortingMethod(self):
        by_rank = self.reportView.askUser(
            'Lister les joueurs par classement ? '
            '(Par défaut : ordre alphabétique) : '
        )
        return 'ranking' if by_rank != '' else 'last_name'

    def sortPlayers(self, players, sorting_method):
        sorted_players = sorted(
            players,
            key=lambda x: (x[sorting_method])
        )
        return sorted_players
