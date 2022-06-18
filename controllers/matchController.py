from views.match import Match as MatchView


class MatchController:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.matchView = MatchView(player1, player2)

    def askMatchResult(self):
        result = int(input(
            f'1— {self.player1}\n'
            f'2— {self.player2}\n'
            f'0— Match nul'
        ))

        score1 = score2 = 0
        match result:
            case 0:
                score1 = score2 = 0.5
            case 1:
                score1 = 1
            case 2:
                score2 = 1
