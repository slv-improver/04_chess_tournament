from tinydb import TinyDB


class DAO(ABC):

    def __init__(self):
        self.db = TinyDB('db.json')