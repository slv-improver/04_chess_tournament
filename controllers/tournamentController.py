from datetime import datetime
from views.tournament import Tournament as TournamentView
from models.tournament import Tournament as TournamentModel
from .roundController import RoundController
from dao.tournamentDao import TournamentDAO


class TournamentController:

    def __init__(self):
        self.tournamentDao = TournamentDAO()
        self.tournamentView = TournamentView()
        self.tournamentView.displayTitle()
        self.tournamentModel = None
        self.askTournamentInfo()

    def askTournamentInfo(self):
        name = input('Quel est le nom du tournoi ? ')
        place = input('Le lieu ? ')
        date = (input('La date de début ? (Aujourd\'hui) ') or 
        datetime.today().strftime('%d/%m/%Y'))
        end_date = (input('La date de fin ? (Aujourd\'hui) ') or 
        datetime.today().strftime('%d/%m/%Y'))
        number_of_rounds = int(input('Le nombre de tours ? (4) ') or '4')
        t_m_choices = {'1': 'Bullet', '2': 'Blitz', '3': 'Coup rapide'}
        t_m_user_choice = int(input(
            'Le mode de jeu ?\n 1—Bullet - 2—Blitz - 3—Coup rapide : '
        ) or t_m_choices['1'])
        time_management = t_m_choices[t_m_user_choice]
        description = input(
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

    def clearprevious_opponents(self):
        for player in self.tournamentModel.player_list:
            del player.previous_opponents[:]

    def storeTournament(self):
        dictTournament = self.tournamentModel.toDict()
        self.tournamentDao.insertData(dictTournament)

    def updateRanking(self):
        for player in self.tournamentModel.player_list:
            player.ranking = int(input(
                f'Nouveau classment de \n \
                {player.last_name} {player.first_name}'
            ))
