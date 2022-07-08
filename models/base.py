from abc import ABC
import json


class Base(ABC):

    def toDict(self):
        dictData = {}
        for key, value in vars(self).items():
            try:
                json.dumps(value)
                dictData[key] = value
            except TypeError:
                dictData[key] = value.toDict()
        return dictData
