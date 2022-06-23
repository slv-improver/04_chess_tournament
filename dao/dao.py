from tinydb import TinyDB


class DAO:

    def __init__(self):
        self.db = TinyDB('db.json')