from datetime import datetime
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
            name = f'Round {self.round_number}'

        self.roundModel = RoundModel(name, start_time=datetime.today())

    def generatePairs(self, player_list):
        ordered_player_list = player_list
        if self.round_number == 1:
            ordered_player_list.sort(key=lambda x: x.ranking)
        else:
            pass
            # sort players by points then ranking
        middle = int(len(ordered_player_list/2))
        first_group = ordered_player_list[:middle]
        second_group = ordered_player_list[middle:]

# ask for results
# return
