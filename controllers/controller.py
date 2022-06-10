from views.welcome import Welcome

class Controller:
    """Base controller"""

    def __init__(self):
        self.welcome()

    def welcome(self):
        welcome = Welcome()
        print(welcome.display)
