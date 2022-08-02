from datetime import datetime
from views.round import Round as RoundView
from models.round import Round as RoundModel
from .matchController import MatchController


class RoundController:

    def __init__(self, round_number):
        self.round_number = round_number
        self.roundView = RoundView(self.round_number)
        self.roundView.displayTitle()
        self.roundModel = None
        self.askRoundInfo()
        self.matches_list = []

    def askRoundInfo(self):
        name = self.roundView.askUser(
            f'Le nom du tour : (Round {self.round_number}) '
        )
        if name == '':
            name = f'Round {self.round_number}'

        self.roundModel = RoundModel(
            name,
            start_time=datetime.today().strftime('%d/%m/%Y-%H:%M:%S')
        )

    def generatePairsFirstRound(self, player_list):
        ordered_player_list = sorted(
            player_list,
            key=lambda x: x.ranking
        )
        half_list = int(len(ordered_player_list)/2)
        first_group = ordered_player_list[:half_list]
        second_group = ordered_player_list[half_list:]

        for i in range(half_list):
            match = MatchController(first_group[i], second_group[i])
            self.__appendMatch(match)

        self.__typeEnterToContinue()

    def generatePairsOtherRounds(self, player_list):
        ordered_player_list = sorted(
            player_list,
            key=lambda x: (-x.tournament_points, x.ranking)
        )

        while len(ordered_player_list) > 0:
            i_player1 = 0
            i_player2 = 1
            # Don't pairs top player with someone he has already play against
            if len(ordered_player_list) == len(player_list):
                while ordered_player_list[i_player1] \
                in ordered_player_list[i_player2].previous_opponents:
                    i_player2 += 1
            match = MatchController(
                ordered_player_list[i_player1],
                ordered_player_list[i_player2]
            )
            del ordered_player_list[i_player2], ordered_player_list[i_player1]
            
            self.__appendMatch(match)

        self.__typeEnterToContinue()

    def __appendMatch(self, match):
        self.matches_list.append(match)
        self.roundModel.matches_list.append(match.matchModel)

    def __typeEnterToContinue(self):
        while self.roundView.askUser(
            'Appuyez sur ́“Entrer” lorsque les matchs sont terminés '
        ) != '':
            continue

    def askMatchResult(self):
        for match in self.matches_list:
            match.askMatchResult()

    def completeRound(self):
        self.roundModel.end_time = datetime.today().strftime(
            '%d/%m/%Y-%H:%M:%S'
        )
