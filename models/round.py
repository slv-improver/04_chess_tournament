from .base import Base


class Round(Base):
    """List of matches"""

    def __init__(self, name, start_time):
        self.name = name
        self.matches_list = []
        self.start_time = start_time
        self.end_time = None

    def toInterrupted(self):
        dictRound = {
            'name': self.name,
            'matches_list': [],
            'start_time': self.start_time,
            'end_time': self.end_time
        }
        if self.matches_list:
            for match in self.matches_list:
                dictMatch = {
                    'scores': (
                        [
                            match.scores[0][0].player_id,
                            match.scores[0][1],
                        ],
                        [
                            match.scores[1][0].player_id,
                            match.scores[1][1],
                        ]
                    )
                }
                dictRound['matches_list'].append(dictMatch)

        return dictRound
