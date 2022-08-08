from .base import Base


class Tournament(Base):
    """The tournament will manage matches between players"""

    def __init__(
        self,
        name,
        place,
        date,
        *,
        end_date,
        number_of_rounds=4,
        round_list=[],
        player_list=[],
        time_management='',  # ('bullet', 'blitz', 'coup rapide')
        description="Pas de remarques"
    ):
        self.name = name
        self.place = place
        self.date = date
        self.end_date = end_date
        self.number_of_rounds = number_of_rounds
        self.round_list = round_list
        self.player_list = player_list
        self.time_management = time_management
        self.description = description

    def toInterrupted(self):
        dictInterrupted = {
            'interrupted': True,

            'name': self.name,
            'place': self.place,
            'date': self.date,
            'end_date': self.date,
            'number_of_rounds': self.number_of_rounds,
            'round_list': [],
            'player_list': [],
            'time_management': self.time_management,
            'description': self.description
        }
        if self.player_list:
            for player in self.player_list:
                dictInterrupted['player_list'].append(
                    player.player_id
                )
        if self.round_list:
            for round in self.round_list:
                dictRound = {
                    'name': round.name,
                    'matches_list': [],
                    'start_time': round.start_time,
                    'end_time': round.end_time
                }
                if round.matches_list:
                    for match in round.matches_list:
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
                dictInterrupted['round_list'].append(dictRound)
