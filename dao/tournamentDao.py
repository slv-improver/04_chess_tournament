from .dao import DAO


class TournamentDAO(DAO):

    def __init__(self):
        super().__init__()
        self.tournaments_table = self.db.table('tournament')

    def getAll(self):
        return self.tournaments_table.all()

    def clearTable(self):
        self.tournaments_table.truncate()

    def insertData(self, serializedData):
        self.clearTable()
        self.tournaments_table.insert_multiple(serializedData)
