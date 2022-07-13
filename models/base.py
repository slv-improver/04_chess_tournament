from abc import ABC
import json


class Base(ABC):

    def toDict(self):
        dictData = {}
        for key, value in vars(self).items():
            try:
                # try serialization to raise error if not serializable
                json.dumps(value)
                dictData[key] = value
            except TypeError:
                if hasattr(value, '__iter__'): 
                    new_value = self.iterate(value)
                    dictData[key] = new_value
                else:
                    dictData[key] = value.toDict()
        return dictData

    def iterate(self, iterable):
        list_of_dict = []
        for model in iterable:
            list_of_dict.append(model.toDict())
        return list_of_dict
