from .base import Base


class Tournament(Base):

    def __init__(self):
        super().__init__()
        self.title = (
            '\n—— Le tournoi commence ——\n'
        )

    def theWinnerIs(self, winner, tournamentName):
        return (
            f'\nLe vainqeur du tournoi “{tournamentName}” est\n'
            f'——— {winner.last_name} {winner.first_name} ———\n'
            f'avec {winner.tournament_points} point(s)\n____\n_____'
        )
