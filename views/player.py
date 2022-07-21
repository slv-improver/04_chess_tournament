from .base import Base


class Player(Base):

    def __init__(self):
        self.title = (
            '\n—— Création de joueur ——\n'
        )

    def displayPlayers(self, players):
        for i, player in enumerate(players):
            print(
                f'{i+1} — {player.last_name} '
                f'{player.first_name} '
                f'{player.ranking}'
            )
