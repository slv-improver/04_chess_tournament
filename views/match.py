from .base import Base


class Match(Base):

    def __init__(self, player1, player2):
        self.title = (
            f'\n———— Match : \n\
            {player1.last_name} {player1.first_name} \n\
            contre \n\
            {player2.last_name} {player2.first_name} \n————'
        )
