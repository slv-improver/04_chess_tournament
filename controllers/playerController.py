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
            self.playerView.displayTitle()
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

    def choosePlayers(self, all_players, number_of_players):
        players_for_tournament = []
        hidden_players = []
        while (len(players_for_tournament) < number_of_players):
            for j, player in enumerate(all_players):
                if (j not in hidden_players):
                    print(f'{j+1} — {player.last_name} {player.first_name}')
            choice = int(input('Entrez le numéro du joueur à ajouter : '))
            if (choice-1 in hidden_players or 
            choice-1 < 0 or 
            choice-1 >= len(all_players)):
                print('Vérifiez le nombre')
                continue
            players_for_tournament.append(all_players[choice-1])
            hidden_players.append(choice-1)
        return players_for_tournament

    def storePlayers(self, players):
        dictPlayers = []
        for player in players:
            dictPlayers.append(player.toDict())
        self.playerDao.insertData(dictPlayers)

    def getPlayers(self):
        dictPlayers = self.playerDao.getAll()
        players = []
        for dictPlayer in dictPlayers:
            players.append(
                self.playerModel.toObject(dictPlayer)
            )
        return players
