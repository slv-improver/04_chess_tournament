from abc import ABC


class Base(ABC):

    def displayTitle(self):
        print(self.title)

    def askUser(self, message):
        return input(message)

    @classmethod
    def displayMessage(self, message):
        print(message)
