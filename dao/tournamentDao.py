from .dao import DAO
from tinydb import Query


class TournamentDAO(DAO):

    def __init__(self):
        super().__init__()
        self.tournaments_table = self.db.table('tournaments')
        self.Tournament = Query()

    def getAll(self):
        return self.tournaments_table.all()

    def insertData(self, serializedData):
        self.tournaments_table.insert(serializedData)

    def searchForInterrupted(self):
        interrupted_tournament = self.tournaments_table.search(
            self.Tournament.interrupted == "True"
        )
        del interrupted_tournament['interrupted']
        return interrupted_tournament

    def saveInterruptedTournament(self, interrupted_tournament):
        print(interrupted_tournament)
