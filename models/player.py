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
        tournament_points=0,
        previous_opponents=[],
        player_id=0
    ):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking

        self.tournament_points = tournament_points
        self.previous_opponents = previous_opponents

        self.player_id = player_id

    def addPoints(self, score):
        self.tournament_points += score

    def toInterrupted(self):
        return self.player_id

    @classmethod
    def toObject(cls, serializedPlayer):
        return cls(**serializedPlayer, player_id=serializedPlayer.doc_id)
