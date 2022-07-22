from .base import Base


class Report(Base):

    def __init__(self):
        self.title = (
            '\n—— Génération de rapports ——\n'
        )

    def displayTitle(self):
        print(self.title)
