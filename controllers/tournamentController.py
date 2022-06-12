from datetime import datetime
from views.tournament import Tournament as TournamentView
from models.tournament import Tournament as TournamentModel


class TournamentController:

    def __init__(self):
        self.tournamentView = TournamentView()
        print(tournamentView.display)
        self.tournamentModel = None
        self.askTournamentInfo()

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
        time_management = input(
            'Le mode de jeu ?\n Bullet - Blitz - Coup rapide : '
        )
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
