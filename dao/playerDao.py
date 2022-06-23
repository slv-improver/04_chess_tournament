class PlayerDAO(DAO):

    def __init(self):
        super().__init()
        self.players_table = self.db.table('players')
