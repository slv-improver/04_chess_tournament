from .base import Base


class Report(Base):

    def __init__(self):
        self.title = (
            '\n—— Génération de rapports ——\n'
        )

    def displayTitle(self):
        print(self.title)

    def displayTournaments(self, tournamentsModel):
        for i, tournament in enumerate(tournamentsModel):
            print(
                f'{i}— Tournoi \'{tournament.name}\''
                f' — à {tournament.place}'
                f' — le {tournament.date}\n———'
            )
