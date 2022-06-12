class Match:
    """Each match played by the players"""

    def __init__(self, scores=([None, 0], [None, 0])):
        self.scores = scores
