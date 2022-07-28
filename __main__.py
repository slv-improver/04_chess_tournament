# Entry point of the program

from pynput import keyboard
from controllers.controller import Controller


def main():
    Controller()


if __name__ == '__main__':
    with keyboard.GlobalHotKeys({
        '<ctrl>+s': saveGame,
        '<ctrl>+w': loadGame,
        '<ctrl>+q': quitGame
    }):
        main()
