from .base import Base


class Player(Base):
    """The chess player"""

    def __init__(
        self,
        last_name='',
        first_name='',
        birth_date='',
        gender='',
        *,
        ranking=0,
        player_id=None,
        tournamentPoints=0,
        previousOpponents=[]
    ):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking

        self.tournamentPoints = tournamentPoints
        self.previousOpponents = previousOpponents

    def addPoints(self, score):
        self.tournamentPoints += score

    def toDict(self):
        dictPlayer = {
            'last_name': self.last_name,
            'first_name': self.first_name,
            'birth_date': self.birth_date,
            'gender': self.gender,
            'ranking': self.ranking,
            'tournamentPoints': self.tournamentPoints,
            'previousOpponents': self.previousOpponents
        }
        return dictPlayer

    @classmethod
    def toObject(cls, serializedPlayer):
        return cls(**serializedPlayer)
