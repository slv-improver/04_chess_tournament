from .base import Base


class Player(Base):

    def __init__(self):
        super().__init__()
        self.title = (
            '\n—— Création de joueur ——\n'
        )
