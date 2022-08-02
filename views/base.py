from abc import ABC


class Base(ABC):

    def displayTitle(self):
        print(self.title)

    def askUser(self, message):
        return input(message)

    def displayMessage(self, message):
        print(message)
