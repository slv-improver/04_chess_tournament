from .dao import DAO


class TournamentDAO(DAO):

    def __init__(self):
        super().__init__()
        self.tournaments_table = self.db.table('tournaments')

    def getAll(self):
        return self.tournaments_table.all()

    def insertData(self, serializedData):
        self.tournaments_table.insert(serializedData)
