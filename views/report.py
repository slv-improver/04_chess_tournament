from .base import Base


class Report(Base):

    def __init__(self):
        self.title = (
            '\n—— Génération de rapports ——\n'
        )

    def displayTitle(self):
        print(self.title)

    def displayTournaments(self, tournaments):
        print('\n——— Liste des tournois passés :\n———')
        for i, tournament in enumerate(tournaments):
            print(
                f'{i+1}— Tournoi \'{tournament["name"]}\''
                f' — à {tournament["place"]}'
                f' — le {tournament["date"]}\n———'
            )
