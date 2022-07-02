from abc import ABC
import json


class Base(ABC):

    def serialize(self):
        serializedData = {}
        for key, value in vars(self).items():
            try:
                json.dumps(value)
                serializedData[key] = value
            except TypeError:
                serializedData[key] = value.serialize()
        return serializedData
