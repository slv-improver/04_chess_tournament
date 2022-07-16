from .base import Base


class Tournament(Base):

    def __init__(self):
        self.title = (
            '\n—— Le tournoi commence ——\n'
        )

    def theWinnerIs(self, winner, tournamentName):
        print(
            f'\nLe vainqeur du tournoi “{tournamentName}” est\n'
            f'——— {winner.last_name} {winner.first_name} ———\n'
            f'avec {winner.tournament_points} point(s)\n___'
        )

    def displayRanking(self, losers):
        print('s\'en suit :')
        for player in losers:
            print(
                f'— {player.last_name} {player.first_name} '
                f'avec {player.tournament_points} point(s)'
            )
