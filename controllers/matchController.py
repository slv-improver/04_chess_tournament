from views.match import Match as MatchView
from models.match import Match as MatchModel


class MatchController:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.matchView = MatchView(player1, player2)
        self.matchView.displayTitle()
        self.matchModel = MatchModel(
            ([self.player1, 0], [self.player2, 0])
        )

    def askMatchResult(self):
        result = int(input(
            f'—————— Qui a gagné ?\n'
            f'1— {self.player1.last_name} {self.player1.first_name}\n'
            f'2— {self.player2.last_name} {self.player2.first_name}\n'
            f'0— Match nul\n'
        ))
        scores = {
            1: [1, 0],
            2: [0, 1],
            0: [0.5, 0.5]
        }
        self.matchModel.updateScores(*scores[result])

        self.player1.addPoints(scores[result][0])
        self.player2.addPoints(scores[result][1])

        self.player1.previous_opponents.append(self.player2)
        self.player2.previous_opponents.append(self.player1)
