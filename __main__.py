# Entry point of the program

from pynput import keyboard
from controllers.controller import Controller


game_controller = Controller()

def saveGame():
    game_controller.saveGame()

def main():
    game_controller.launchGame()


if __name__ == '__main__':
    with keyboard.GlobalHotKeys({
        '<ctrl>+s': saveGame
    }):
        main()
