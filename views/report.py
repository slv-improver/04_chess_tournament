from .base import Base


class Report(Base):

    def __init__(self):
        self.title = (
            '\n—— Génération de rapports ——\n'
        )

    def displayTournaments(self, tournaments):
        print('\n——— Liste des tournois passés :\n———')
        for i, tournament in enumerate(tournaments):
            print(
                f'{i+1}— Tournoi \'{tournament["name"]}\''
                f' — à {tournament["place"]}'
                f' — le {tournament["date"]}\n———'
            )
    def reportTournamentPlayers(self, tournament_name, players):
        print(f'\n———Voici les joueurs du tournoi {tournament_name} :\n———')
        for player in players:
            gender = 'M' if player["gender"] == 'M' else 'Mme'
            e = '' if player["gender"] == 'M' else 'e'
            print(
                f'— {gender} {player["last_name"]} {player["first_name"]}\n'
                f'né{e} le {player["birth_date"]}\n'
                f'Classement : {player["ranking"]}'
                'ème' if player["ranking"] > 1 else 'er'
            )

    def reportTournamentRounds(self, tournament_name, rounds):
        print(f'\n———Voici les tours du tournoi {tournament_name} :\n———')
        for round in rounds:
            print(
                f'— Le tour {round["name"]}\n'
                f'Début : {round["start_time"]}\n'
                f'Fin : {round["end_time"]}'
            )
