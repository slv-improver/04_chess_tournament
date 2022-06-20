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
        self.matches_list = []

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
            self.__appendMatch()

        self.__typeEnterToContinue()

    def generatePairsOtherRounds(self, player_list):
        ordered_player_list = player_list
        ordered_player_list.sort(
            key=lambda x: (-x.tournamentPoints, x.ranking)
        )

        while len(ordered_player_list) > 0:
            i_player1 = 0
            i_player2 = 1
            # Check player1 did not play with player2
            while ordered_player_list[i_player1] \
            in ordered_player_list[i_player2].previousOpponents:
                i_player2 += 1
            match = MatchController(
                ordered_player_list.pop(i_player1),
                ordered_player_list.pop(i_player2)
            )
            self.__appendMatch()

        self.__typeEnterToContinue()

    def __appendMatch(self, match):
        self.matches_list.append(match)
        self.roundModel.matches_list.append(match.matchModel)

    def __typeEnterToContinue(self):
        while input(
            'Appuyez sur ́“Entrer” lorsque les matchs sont terminés '
        ) != '':
            continue

    def askMatchResult(self):
        for match in self.matches_list:
            match.askMatchResult()

    def completeRound(self):
        self.roundModel.end_time = datetime.today()
