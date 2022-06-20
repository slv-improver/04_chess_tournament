from datetime import date
from views.player import Player as PlayerView
from models.player import Player as PlayerModel

class PlayerController:
    """Manage Player creation"""

    def __init__(self):
        self.playerView = PlayerView()
        print(self.playerView.display)
        self.playerModel = None
        self.askPlayerInfo()

    def askPlayerInfo(self):
        last_name = input('Nom du joueur : ')
        first_name = input('Prénom : ')
        d_birth = int(input('Date de naissance :\nJJ :'))
        m_birth = int(input('MM :'))
        y_birth = int(input('AAAA :'))
        birth_date = date(y_birth, m_birth, d_birth)
        gender = input('M / F : ')
        ranking = int(input('Rang : '))

        self.playerModel = PlayerModel(
            last_name,
            first_name,
            birth_date,
            gender = gender,
            ranking = ranking
        )
