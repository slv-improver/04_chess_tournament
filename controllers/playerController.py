from datetime import date
from views.player import Player as PlayerView
from models.player import Player as PlayerModel
from dao.playerDao import PlayerDAO


class PlayerController:
    """Manage Player creation"""

    def __init__(self, master=False):
        self.playerDao = PlayerDAO()
        self.playerView = PlayerView()
        self.playerModel = None
        if not master:
            self.askPlayerInfo()
            print(self.playerView.display)
        else:
            self.playerModel = PlayerModel()

    def askPlayerInfo(self):
        last_name = input('Nom du joueur : ')
        first_name = input('Prénom : ')
        d_birth = int(input('Date de naissance :\nJJ :'))
        m_birth = int(input('MM :'))
        y_birth = int(input('AAAA :'))
        birth_date = date(y_birth, m_birth, d_birth).strftime('%d/%m/%Y')
        gender = input('M / F : ')
        ranking = int(input('Rang : '))

        self.playerModel = PlayerModel(
            last_name,
            first_name,
            birth_date,
            gender = gender,
            ranking = ranking
        )
        # Remember to handle errors

    def storePlayers(self, players):
        serializedPlayers = []
        for player in players:
            serializedPlayers.append(player.serialize())
        print(serializedPlayers)
        self.playerDao.insertData(serializedPlayers)

    def getPlayers(self):
        serializedPlayers = self.playerDao.getAll()
        players = []
        for serializedPlayer in serializedPlayers:
            players.append(
                self.playerModel.unserialize(serializedPlayer)
            )
        return players
