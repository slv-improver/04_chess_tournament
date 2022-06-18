from views.match import Match as MatchView


class MatchController:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.matchView = MatchView(player1, player2)
