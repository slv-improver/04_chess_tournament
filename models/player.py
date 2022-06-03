class Player:
    """The chess player"""

    def __init__(
        self,
        last_name,
        first_name,
        birth_date,
        gender,
        *,
        ranking,
        player_id=None
    ):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.ranking = ranking
        self.player_id = player_id
