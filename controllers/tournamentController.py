from datetime import datetime
from views.tournament import Tournament as TournamentView
from models.tournament import Tournament as TournamentModel
from .roundController import RoundController


class TournamentController:

    def __init__(self):
        self.tournamentView = TournamentView()
        print(self.tournamentView.display)
        self.tournamentModel = None
        self.askTournamentInfo()
        self.round = None

    def askTournamentInfo(self):
        name = input('Quel est le nom du tournoi ? ')
        place = input('Le lieu ? ')
        date = input('La date de début ? (Aujourd\'hui) ')
        if date == '':
            date = datetime.today()
        end_date = input('La date de fin ? (Aujourd\'hui) ')
        if end_date == '':
            end_date = datetime.today()
        number_of_rounds = input('Le nombre de tours ? (4)')
        if number_of_rounds == '':
            number_of_rounds = 4
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
        description = input('Remarques relatives au tournoi : ')
        if description == '':
            description = "Pas de remarques"

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

    def startRound(self):
        self.round = RoundController()
