from .base import Base


class Match(Base):
    """Each match played by the players"""

    def __init__(self, scores):
        self.scores = scores  # ([player1, 0], [player2, 0])

    def updateScores(self, score1, score2):
        self.scores[0][1] = score1
        self.scores[1][1] = score2

    def toDict(self):
        p1 = self.scores[0]
        p2 = self.scores[1]
        dictData = {
            'scores': (
                [f'{p1[0].last_name} {p1[0].first_name}', p1[1]],
                [f'{p2[0].last_name} {p2[0].first_name}', p2[1]]
            )
        }
        return dictData
