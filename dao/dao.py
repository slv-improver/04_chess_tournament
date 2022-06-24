from tinydb import TinyDB
from abc import ABC


class DAO(ABC):

    def __init__(self):
        self.db = TinyDB('db.json')
