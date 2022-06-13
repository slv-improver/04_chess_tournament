from views.player import Player as PlayerView

class PlayerController:
    """Manage Player creation"""

    def __init__(self):
        self.playerView = PlayerView()
        print(self.playerView.display)
        self.askPlayerInfo()

    def askPlayerInfo(self):
        last_name = input('Nom du joueur : ')
        first_name = input('Prénom : ')
        birth_date = input('Date de naissance : ')
        gender = input('M / F')
        ranking = input('Rang : ')
