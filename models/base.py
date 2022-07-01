from abc import ABC


class Base(ABC):

    def serialize(self):
        serializedData = {}
        for key, value in vars(self).items():
            try:
                serializedData[key] = value
            except TypeError:
                serializedData[key] = value.serialize()
        return serializedData
