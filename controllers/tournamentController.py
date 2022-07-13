from datetime import datetime
from views.tournament import Tournament as TournamentView
from models.tournament import Tournament as TournamentModel
from .roundController import RoundController
from dao.tournamentDao import TournamentDAO


class TournamentController:

    def __init__(self):
        self.tournamentDao = TournamentDAO()
        self.tournamentView = TournamentView()
        print(self.tournamentView.display)
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
        time_management = int(input(
            'Le mode de jeu ?\n 1—Bullet - 2—Blitz - 3—Coup rapide : '
        ))
        match time_management:
            case 1:
                time_management = 'Bullet'
            case 2:
                time_management = 'Blitz'
            case 3:
                time_management = 'Coup rapide'
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
        winner = max(
            self.tournamentModel.player_list,
            key=lambda x: (x.tournament_points, -x.ranking)
        )
        print(
            self.tournamentView.theWinnerIs(
                winner,
                self.tournamentModel.name
            )
        )

    def clearprevious_opponents(self):
        for player in self.tournamentModel.player_list:
            del player.previous_opponents[:]

    def storeTournament(self):
        dictTournament = self.tournamentModel.toDict()
        self.tournamentDao.insertData(dictTournament)
