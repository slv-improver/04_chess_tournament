from .base import Base


class Menu(Base):
    """Display the menu"""

    def __init__(self):
        self.choices = (
            '\n1— Créer un tournoi\n'
            '2— Gérer les joueurs\n'
            '3— Générer un rapport\n'
            '4— Quitter\n'
        )

    def displayMenu(self):
        print(self.choices)
