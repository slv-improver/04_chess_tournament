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
        tournament_points=0,
        previous_opponents=[]
    ):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking

        self.tournament_points = tournament_points
        self.previous_opponents = previous_opponents

    def addPoints(self, score):
        self.tournament_points += score

    @classmethod
    def toObject(cls, serializedPlayer):
        return cls(**serializedPlayer)
