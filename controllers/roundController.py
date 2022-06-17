from views.round import Round as RoundView
from models.round import Round as RoundModel

class RoundController:

    def __init__(self, round_number):
        self.round_number = round_number
        self.roundView = RoundView(self.round_number)
        print(self.roundView.display)
        self.roundModel = None
        self.askRoundInfo()

    def askRoundInfo(self):
        name = input(f'Le nom du tour : (Round {self.round_number}) ')
        if name == '':
            name = f'Round{self.round_number}'

        self.roundModel = RoundModel(name)

# generate pairs of players
# ask for results
# return
