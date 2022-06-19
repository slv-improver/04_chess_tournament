from datetime import datetime
from views.round import Round as RoundView
from models.round import Round as RoundModel
from .matchController import MatchController

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

    def generatePairsFirstRound(self, player_list):
        ordered_player_list = player_list
        ordered_player_list.sort(key=lambda x: x.ranking)
        half_list = int(len(ordered_player_list)/2)
        first_group = ordered_player_list[:half_list]
        second_group = ordered_player_list[half_list:]

        for i in range(half_list):
            match = MatchController(first_group[i], second_group[i])
            self.roundModel.matches_list.append(match.matchModel)
