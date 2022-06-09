from datetime import datetime

class Round:
    """List of matches"""

    def __init__(self, name, matches_list):
        self.name = name
        self.matches_list = matches_list
        self.start_time = datetime.today()
        self.end_time = datetime.today()
