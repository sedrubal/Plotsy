# coding=utf-8
"""
The Module Itself

Source code stuffies:
    The graph variable in the Plotsy class works like this -
    the lists within the outermost list is the Y (these lists
    will be printed on their own lines), and the values in
    those lists are for the X coordinate.
"""

from color import *


class Plotsy():
    def __init__(self, width, height, background=" "):
        """
        The constructor
        :param width: int: the width of the drawing area
        :param height: int: the height of the drawing area
        :param background: the characters for the background
        """
        # Make "size" usable throughout the object for math
        self.width = int(width)
        self.height = int(height)
        # Make  "background" usable through the object
        self.background = background
        # Create the grid
        self.graph = [[background] * self.width for _ in range(self.height)]

    def __del__(self):
        self.clear()

    def plot(self, x, y, icon="#", fg_color=Color.RESET, bg_color=Color.RESET):
        """
        Set the X position in list Y to the appropriate icon.
        :param x: int: the x coordinate of the first character
        :param y: int: the y coordinate of the first character
        :param icon: str: character for the point
        :param fg_color: COLOR: optional: the fore color of the plot
        :param bg_color: COLOR: optional: the back color of the plot
        """
        if x < self.width and self.height - y - 1 < self.width:
            self.graph[self.width - y - 1][x] = \
                Color.to_ansi(fg_color) + Color.to_ansi(bg_color, False) + icon + \
                Color.to_ansi(Color.RESET) + Color.to_ansi(Color.RESET, False)

    def label(self, x, y, text, fg_color=Color.RESET, bg_color=Color.RESET):
        """
        adds a text to the graph
        :param x: int: the x coordinate of the first character
        :param y: int: the y coordinate of the first character
        :param text: str: the text (only letters)
        :param fg_color: COLOR: optional: the fore color of the text
        :param bg_color: COLOR: optional: the back color of the text
        """
        for c in text:
            self.plot(x, y, c, fg_color, bg_color)
            x += 1

    def draw_h_line(self, x1, x2, y, fg_color=Color.RESET, bg_color=Color.RESET):
        """
        Draw a horizontal line
        :param x1: int: the first x coordinate (the start)
        :param x2: int: the second x coordinate (the end)
        :param y: int: the y coordinate of the line
        :param fg_color: COLOR: optional: the fore color of the line
        :param bg_color: COLOR: optional: the back color of the line
        """
        if x1 > x2:
            x1, x2 = x2, x1  # swap
        for x in range(x1, x2):
            self.plot(x, y, '–', fg_color, bg_color)

    def draw_v_line(self, x, y1, y2, fg_color=Color.RESET, bg_color=Color.RESET):
        """
        Draw a vertical line
        :param x: int: the x coordinate of the line
        :param y1: int: the first y coordinate (the start)
        :param y2: int: the second y coordinate (the end)
        :param fg_color: COLOR: optional: the fore color of the line
        :param bg_color: COLOR: optional: the back color of the line
        """
        if y1 > y2:
            y1, y2 = y2, y1  # swap
        for y in range(y1, y2):
            self.plot(x, y, '|', fg_color, bg_color)

    def draw_rect(self, x, y, width, height, fg_color=Color.RESET, bg_color=Color.RESET):
        """
        Draws a rectangle
        :param x: int: left x coordinate
        :param y: int: lower y coordinate
        :param width: int: width of the rectangle
        :param height: int: height of the rectangle
        :param fg_color: COLOR: optional: the fore color of the rectangle
        :param bg_color: COLOR: optional: the back color of the rectangle
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
        self.plot(x, y, '+', fg_color, bg_color)
        self.plot(x + width, y, '+', fg_color, bg_color)
        self.plot(x, y + height, '+', fg_color, bg_color)
        self.plot(x + width, y + height, '+', fg_color, bg_color)

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
        self.graph = [[self.background] * self.width for _ in range(self.height)]