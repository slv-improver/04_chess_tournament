from abc import ABC


class Base(ABC):

    def __init__(self):
        self.title = (
            ''
        )
        self.displayTitle()

    def displayTitle(self):
        print(self.title)
