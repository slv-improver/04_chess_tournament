from views.round import Round as RoundView
from models.round import Round as RoundModel

class RoundController:

    def __init__(self, round_number):
        self.roundView = RoundView(round_number)
        print(self.roundView.display)
        self.roundModel = None
        self.askRoundInfo()

    def askRoundInfo(self):
        pass

# generate pairs of players
# ask for results
# return
