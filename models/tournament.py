from datetime import date


class Tournament:
    """The tournament will manage matches between players"""

    def __init__(
        self,
        /,
        name,
        place,
        date=date.today(),
        *,
        end_date=date.today(),
        number_of_rounds=4,
        round_list=[],
        player_list=[],
        time_management=None,  # ('bullet', 'blitz', 'coup rapide')
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
