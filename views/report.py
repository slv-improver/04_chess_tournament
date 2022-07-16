from .base import Base


class Report(Base):

    def __init__(self):
        super().__init__()
        self.title = (
            '\n—— Génération de rapport ——\n'
        )

    def displayTitle(self):
        print(self.title)
