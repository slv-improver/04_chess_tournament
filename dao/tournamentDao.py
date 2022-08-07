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
        print(self.tournaments_table.search(
            self.Tournament.interrupted == True
        ))
    def saveInterruptedTournament(self, interruptedTournament):
        print(interruptedTournament)
