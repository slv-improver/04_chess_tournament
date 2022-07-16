from .base import Base


class Welcome(Base):
    """Display the Welcome message"""

    def __init__(self):
        self.title = """
        ————————————————————
        |  Welcome to the  |
        | Chess Tournament |
        |      program     |
        ————————————————————
        """
