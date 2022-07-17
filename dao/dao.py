from abc import ABC
from json import JSONEncoder
from tinydb import TinyDB


class ObjectEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class DAO(ABC):

    def __init__(self):
        self.db = TinyDB('db.json', indent=4, cls=ObjectEncoder)
