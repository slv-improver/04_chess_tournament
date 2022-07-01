class Tournament:
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

    def serialize(self):
        serializedData = {}
        for key, value in vars(self).items():
            try:
                serializedData[key] = value
            except TypeError:
                serializedData[key] = value.serialize()
        return serializedData
