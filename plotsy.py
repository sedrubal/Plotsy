# coding=utf-8
"""
The Module Itself

Source code stuffies:
    The graph variable in the Plotsy class works like this -
    the lists within the outermost list is the Y (these lists
    will be printed on their own lines), and the values in
    those lists are for the X coordinate.
"""

from colorama import Fore
from colorama import Back


class Plotsy():
    def __init__(self, size, background=" "):
        """
        The constructor
        :param size: the dimensions [int, int] of the drawing area
        :param background: the characters for the background
        """
        # Make "size" usable throughout the object for math
        self.size = size
        # Make  "background" usable through the object
        self.background = background
        # Create the grid
        self.graph = [[background] * self.size[1] for _ in range(self.size[0])]

    def __del__(self):
        self.clear()

    def plot(self, coords, icon="#", fg_color=Fore.RESET, bg_color=Back.RESET):
        """
        Set the X position in list Y to the appropriate icon.
        :param coords: the coordinates of the first character
        :param icon: character for the point
        :param fg_color: optional: the fore color of the plot (AnsiFore colors)
        :param bg_color: optional: the back color of the plot (AnsiBack colors)
        """
        if coords[0] < self.size[0] and self.size[1] - coords[1] - 1 < self.size[1]:
            self.graph[self.size[1] - coords[1] - 1][coords[0]] = fg_color + bg_color + icon + Fore.RESET + Back.RESET

    def label(self, coords, text, fg_color=Fore.RESET, bg_color=Back.RESET):
        """
        adds a text to the graph
        :param coords: the coordinates of the first character
        :param text: the text (only letters)
        :param fg_color: optional: the fore color of the text (AnsiFore colors)
        :param bg_color: optional: the back color of the text (AnsiBack colors)
        """
        for c in text:
            self.plot(coords, c, fg_color, bg_color)
            coords[0] += 1

    def draw_h_line(self, x1, x2, y, fg_color=Fore.RESET, bg_color=Back.RESET):
        """
        Draw a horizontal line
        :param x1: the first x coordinate (the start)
        :param x2: the second x coordinate (the end)
        :param y: the y coordinate of the line
        :param fg_color: optional: the fore color of the line (AnsiFore colors)
        :param bg_color: optional: the back color of the line (AnsiBack colors)
        """
        if x1 > x2:
            x1, x2 = x2, x1  # swap
        for x in range(x1, x2):
            self.plot([x, y], '–', fg_color, bg_color)

    def draw_v_line(self, x, y1, y2, fg_color=Fore.RESET, bg_color=Back.RESET):
        """
        Draw a vertical line
        :param x: the x coordinate of the line
        :param y1: the first y coordinate (the start)
        :param y2: the second y coordinate (the end)
        :param fg_color: optional: the fore color of the line (AnsiFore colors)
        :param bg_color: optional: the back color of the line (AnsiBack colors)
        """
        if y1 > y2:
            y1, y2 = y2, y1  # swap
        for y in range(y1, y2):
            self.plot([x, y], '|', fg_color, bg_color)

    def draw_rect(self, x, y, width, height, fg_color=Fore.RESET, bg_color=Back.RESET):
        """
        Draws a rectangle
        :param x: left x coordinate
        :param y: lower y coordinate
        :param width: width of the rectangle
        :param height: height of the rectangle
        :param fg_color: optional: the fore color of the rectangle (AnsiFore colors)
        :param bg_color: optional: the back color of the rectangle (AnsiBack colors)
        :raise Exception: width and height must be at least 1
        """
        if width < 1 or height < 1:
            raise Exception('The width and the height must be at least 1')
        width -= 1
        height -= 1
        self.draw_h_line(x, x + width, y, fg_color, bg_color)
        self.draw_h_line(x, x + width, y + height, fg_color, bg_color)
        self.draw_v_line(x, y, y + height, fg_color, bg_color)
        self.draw_v_line(x + width, y, y + height, fg_color, bg_color)
        self.plot([x, y], '+', fg_color, bg_color)
        self.plot([x + width, y], '+', fg_color, bg_color)
        self.plot([x, y + height], '+', fg_color, bg_color)
        self.plot([x + width, y + height], '+', fg_color, bg_color)

    def draw(self):
        """
        Draw the graph to the terminal
        """
        for i in self.graph:
            print("".join(str(x) for x in i))

    def clear(self):
        """
        Clear the graph
        """
        self.graph = [[self.background] * self.size[1] for _ in range(self.size[0])]
