from .dao import DAO


class PlayerDAO(DAO):

    def __init__(self):
        super().__init__()
        self.players_table = self.db.table('players')

    def getAll(self):
        return self.players_table.all()

    def clearTable(self):
        self.players_table.truncate()

    def insertData(self, serializedData):
        self.clearTable()
        self.players_table.insert_multiple(serializedData)
