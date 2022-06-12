from datetime import datetime
from views.tournament import Tournament as TournamentView


class TournamentController:

    def __init__(self):
        self.tournamentView = TournamentView()
        print(tournamentView.display)
