from views.player import Player as PlayerView
from models.player import Player as PlayerModel

class PlayerController:
    """Manage Player creation"""

    def __init__(self):
        self.playerView = PlayerView()
        print(self.playerView.display)
        self.PlayerModel = None
        self.askPlayerInfo()

    def askPlayerInfo(self):
        last_name = input('Nom du joueur : ')
        first_name = input('Prénom : ')
        birth_date = input('Date de naissance : ')
        gender = input('M / F : ')
        ranking = input('Rang : ')

        self.PlayerModel = PlayerModel(
            last_name,
            first_name,
            birth_date,
            gender = gender,
            ranking = ranking
        )
