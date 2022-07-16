from .base import Base


class Report(Base):

    def __init__(self):
        self.title = (
            '\n—— Génération de rapport ——\n'
        )

    def displayTitle(self):
        print(self.title)
