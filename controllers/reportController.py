from views.report import Report as ReportView


class ReportController:

    def __init__(self):
        self.reportView = ReportView()
        self.reportView.displayTitle()

    def chooseReport(self):
        choices = {
                '1': self.reportPlayers(),
                '2': self.reportTournaments()
            }
        user_choice = input(
            '1— Joueurs\n'
            '2— Tournois\n'
        )
        choices[user_input]()

    def reportPlayers(self):
        pass

    def reportTournaments(self):
        pass
