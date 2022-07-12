from views.match import Match as MatchView
from models.match import Match as MatchModel


class MatchController:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.matchView = MatchView(player1, player2)
        print(self.matchView.display)
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

        score1 = score2 = 0
        match result:
            case 0:
                score1 = score2 = 0.5
            case 1:
                score1 = 1
            case 2:
                score2 = 1

        self.matchModel.updateScores(score1, score2)

        self.player1.addPoints(score1)
        self.player2.addPoints(score2)

        self.player1.previous_opponents.append(self.player2)
        self.player2.previous_opponents.append(self.player1)
