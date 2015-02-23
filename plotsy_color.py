"""
Color staff
"""

from colorama import Fore
from colorama import Back
from enum import Enum


class Color(Enum):
    BLACK = 0
    RED = 1
    GREEN = 2
    YELLOW = 3
    BLUE = 4
    MAGENTA = 5
    CYAN = 6
    WHITE = 7
    RESET = 9

    # These are fairly well supported, but not part of the standard.
    LIGHTBLACK_EX = 10
    LIGHTRED_EX = 11
    LIGHTGREEN_EX = 12
    LIGHTYELLOW_EX = 13
    LIGHTBLUE_EX = 14
    LIGHTMAGENTA_EX = 15
    LIGHTCYAN_EX = 16
    LIGHTWHITE_EX = 17

    @staticmethod
    def to_ansi(color, foreground=True):
        if color == Color.BLACK:
            return Fore.BLACK if foreground else Back.BLACK
        elif color == Color.RED:
            return Fore.RED if foreground else Back.RED
        elif color == Color.GREEN:
            return Fore.GREEN if foreground else Back.GREEN
        elif color == Color.YELLOW:
            return Fore.YELLOW if foreground else Back.YELLOW
        elif color == Color.BLUE:
            return Fore.BLUE if foreground else Back.BLUE
        elif color == Color.MAGENTA:
            return Fore.MAGENTA if foreground else Back.MAGENTA
        elif color == Color.CYAN:
            return Fore.CYAN if foreground else Back.CYAN
        elif color == Color.WHITE:
            return Fore.WHITE if foreground else Back.WHITE
        elif color == Color.RESET:
            return Fore.RESET if foreground else Back.RESET
        elif color == Color.LIGHTBLACK_EX:
            return Fore.LIGHTBLACK_EX if foreground else Back.LIGHTBLACK_EX
        elif color == Color.LIGHTRED_EX:
            return Fore.LIGHTRED_EX if foreground else Back.LIGHTRED_EX
        elif color == Color.LIGHTGREEN_EX:
            return Fore.LIGHTGREEN_EX if foreground else Back.LIGHTGREEN_EX
        elif color == Color.LIGHTYELLOW_EX:
            return Fore.LIGHTYELLOW_EX if foreground else Back.LIGHTYELLOW_EX
        elif color == Color.LIGHTBLUE_EX:
            return Fore.LIGHTBLUE_EX if foreground else Back.LIGHTBLUE_EX
        elif color == Color.LIGHTMAGENTA_EX:
            return Fore.LIGHTMAGENTA_EX if foreground else Back.LIGHTMAGENTA_EX
        elif color == Color.LIGHTCYAN_EX:
            return Fore.LIGHTCYAN_EX if foreground else Back.LIGHTCYAN_EX
        elif color == Color.LIGHTWHITE_EX:
            return Fore.LIGHTWHITE_EX if foreground else Back.LIGHTWHITE_EX
        else:
            return color