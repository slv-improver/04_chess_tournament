from .base import Base


class Round(Base):
    """List of matches"""

    def __init__(self, name, start_time):
        self.name = name
        self.matches_list = []
        self.start_time = start_time
        self.end_time = None
