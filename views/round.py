from .base import Base


class Round(Base):

    def __init__(self, round_number):
        self.title = (
            f'\n——— Tour n°{round_number} ———\n'
        )
