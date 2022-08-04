from datetime import datetime
from views.tournament import Tournament as TournamentView
from models.tournament import Tournament as TournamentModel
from .roundController import RoundController
from dao.tournamentDao import TournamentDAO


class TournamentController:

    def __init__(self):
        self.tournamentDao = TournamentDAO()
        self.tournamentModel = None
        self.tournamentView = TournamentView()

    def launchTournament(self):
        self.tournamentView.displayTitle()
        self.askTournamentInfo()

    def askTournamentInfo(self):
        name = self.tournamentView.askUser('Quel est le nom du tournoi ? ')
        place = self.tournamentView.askUser('Le lieu ? ')
        date = (self.tournamentView.askUser(
            'La date de début ? (Aujourd\'hui) '
        ) or datetime.today().strftime('%d/%m/%Y'))
        end_date = (self.tournamentView.askUser(
            'La date de fin ? (Aujourd\'hui) '
        ) or datetime.today().strftime('%d/%m/%Y'))
        number_of_rounds = int(self.tournamentView.askUser(
            'Le nombre de tours ? (4) '
        ) or '4')
        t_m_choices = {'1': 'Bullet', '2': 'Blitz', '3': 'Coup rapide'}
        t_m_user_choice = self.tournamentView.askUser(
            'Le mode de jeu ?\n 1—Bullet - 2—Blitz - 3—Coup rapide : '
        ) or '1'
        time_management = t_m_choices[t_m_user_choice]
        description = self.tournamentView.askUser(
            'Remarques relatives au tournoi : '
        ) or "Pas de remarques"

        self.tournamentModel = TournamentModel(
            name,
            place,
            date,
            end_date=end_date,
            number_of_rounds=number_of_rounds,
            round_list=[],
            player_list=[],
            time_management=time_management,
            description=description
        )
        # Remember to handle errors

    def startRound(self, round_number):
        round = RoundController(round_number)
        self.tournamentModel.round_list.append(round.roundModel)
        if round_number == 1:
            round.generatePairsFirstRound(
                self.tournamentModel.player_list
            )
        else:
            round.generatePairsOtherRounds(
                self.tournamentModel.player_list
            )
        round.askMatchResult()
        round.completeRound()

    def declareWinner(self):
        ranking = sorted(
            self.tournamentModel.player_list,
            key=lambda x: (x.tournament_points, -x.ranking),
            reverse=True
        )
        self.tournamentView.theWinnerIs(
            ranking[0],
            self.tournamentModel.name
        )
        self.tournamentView.displayRanking(ranking[1:])

    def clearPreviousOpponents(self):
        for player in self.tournamentModel.player_list:
            del player.previous_opponents[:]

    def clearTournamentPoints(self):
        for player in self.tournamentModel.player_list:
            player.tournament_points = 0

    def storeTournament(self):
        dictTournament = self.tournamentModel.toDict()
        self.tournamentDao.insertData(dictTournament)
