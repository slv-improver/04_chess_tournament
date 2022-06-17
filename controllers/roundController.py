from views.round import Round as RoundView

class RoundController:

    def __init__(self, round_number):
        self.roundView = RoundView(round_number)
        print(self.roundView.display)

# generate pairs of players
# ask for results
# return