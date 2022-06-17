from datetime import datetime


class Round:
    """List of matches"""

    def __init__(self, name):
        self.name = name
        self.matches_list = []
        self.start_time = datetime.today()
        self.end_time = None
