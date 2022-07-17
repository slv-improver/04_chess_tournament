from abc import ABC


class Base(ABC):

    def displayTitle(self):
        print(self.title)
