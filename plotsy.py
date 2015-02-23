# coding=utf-8
"""
The Module Itself

Source code stuffies:
    The graph variable in the Plotsy class works like this -
    the lists within the outermost list is the Y (these lists
    will be printed on their own lines), and the values in
    those lists are for the X coordinate.
"""

from plotsy_color import *
from os import popen


class Plotsy():
    def __init__(self, width=0, height=0, max_width=300, max_height=100, background=" "):
        """
        The constructor
        :type width: int
        :type height: int
        :type max_width: int
        :type max_height: int
        :type background: str
        :param width: optional: the width of the drawing area (default: the terminal width)
                                     if it is less than 0, the width will be the terminal width - width
        :param height: optional: the height of the drawing area (default: the terminal height)
                                     if it is less than 0, the height will be the terminal height - height
        :param max_width: the maximal width of a drawing area if width <= 0
        :param max_height: the maximal height of a drawing area if height <= 0
        :param background: the characters for the background
        """
        # <editor-fold desc="Get the terminal size">
        rows, columns = 0, 0
        if int(width) <= 0 or int(height) <= 0:
            if len(popen('stty size', 'r').read()) == 0:
                from logging import critical
                critical("This has to be executed in a terminal.")
                exit(1)
            rows, columns = popen('stty size', 'r').read().split()
        # </editor-fold>
        # Make "size" usable throughout the object for math
        self.width = min(int(max_width), int(columns) + int(width)) if int(width) <= 0 else int(width)
        self.height = min(int(max_height), int(rows) + int(height)) if int(height) <= 0 else int(height)
        # Make  "background" usable through the object
        self.background = background
        # Create the grid
        self.graph = [[background] * self.width for _ in range(self.height)]

    def plot(self, x, y, icon='x', fg_color=Color.RESET, bg_color=Color.RESET):
        """
        Set the X position in list Y to the appropriate icon.
        :type x: int
        :type y: int
        :type icon: char
        :type fg_color: Color
        :type bg_color: Color
        :param x: the x coordinate of the first character
        :param y: the y coordinate of the first character
        :param icon: a single character for the point
        :param fg_color: optional: the fore color of the plot
        :param bg_color: optional: the back color of the plot
        """
        y_coord = self.height - y - 1
        if 0 <= x < self.width and 0 <= y_coord < self.width:
            self.graph[y_coord][x] = \
                Color.to_ansi(fg_color) + Color.to_ansi(bg_color, False) + str(icon) + \
                Color.to_ansi(Color.RESET) + Color.to_ansi(Color.RESET, False)
        else:
            from logging import warning
            warning("This plot was out of bounce: '{i}' on position ({x}| {y})".format(x=x, y=y, i=icon))

    def label(self, x, y, text, fg_color=Color.RESET, bg_color=Color.RESET):
        """
        adds a text to the graph
        :type x: int
        :type y: int
        :type text: str
        :type fg_color: Color
        :type bg_color: Color
        :param x: the x coordinate of the first character
        :param y: the y coordinate of the first character
        :param text: the text (only letters)
        :param fg_color: optional: the fore color of the text
        :param bg_color: optional: the back color of the text
        """
        for c in str(text):
            self.plot(x, y, c, fg_color, bg_color)
            x += 1

    def draw_h_line(self, x1, x2, y, icon='–', fg_color=Color.RESET, bg_color=Color.RESET):
        """
        Draw a horizontal line
        :type x1: int
        :type x2: int
        :type y: int
        :type icon: unichar
        :type fg_color: Color
        :type bg_color: Color
        :param x1: the first x coordinate (the start)
        :param x2: the second x coordinate (the end)
        :param y: the y coordinate of the line
        :param icon: icon for the line
        :param fg_color: optional: the fore color of the line
        :param bg_color: optional: the back color of the line
        """
        if x1 > x2:
            x1, x2 = x2, x1  # swap
        for x in range(x1, x2):
            self.plot(x, y, icon, fg_color, bg_color)

    def draw_v_line(self, x, y1, y2, icon='|', fg_color=Color.RESET, bg_color=Color.RESET):
        """
        Draw a vertical line
        :type x: int
        :type y1: int
        :type y2: int
        :type icon: unichar
        :type fg_color: Color
        :type bg_color: Color
        :param x: the x coordinate of the line
        :param y1: the first y coordinate (the start)
        :param y2: the second y coordinate (the end)
        :param icon: icon for the line
        :param fg_color: optional: the fore color of the line
        :param bg_color: optional: the back color of the line
        """
        if y1 > y2:
            y1, y2 = y2, y1  # swap
        for y in range(y1, y2):
            self.plot(x, y, icon, fg_color, bg_color)

    def draw_rect(self, x, y, width, height,
                  v_icon='|', h_icon='–', tl_icon='+', tr_icon='+', bl_icon='+', br_icon='+',
                  fg_color=Color.RESET, bg_color=Color.RESET):
        """
        Draws a rectangle
        :type x: int
        :type y: int
        :type width: int
        :type height: int
        :type v_icon: str
        :type h_icon: str
        :type tl_icon: str
        :type tr_icon: str
        :type bl_icon: str
        :type br_icon: str
        :type fg_color: Color
        :type bg_color: Color
        :param x: left x coordinate
        :param y: lower y coordinate
        :param width: width of the rectangle
        :param height: height of the rectangle
        :param v_icon: optional: icon for vertical lines
        :param h_icon: optional: icon for horizontal lines
        :param tl_icon: optional: icon for top left corners
        :param tr_icon: optional: icon for top right corners
        :param bl_icon: optional: icon for bottom left corners
        :param br_icon: optional: icon for bottom right corners
        :param fg_color: optional: the fore color of the rectangle
        :param bg_color: optional: the back color of the rectangle
        :raise Exception: width and height must be at least 1
        """
        if width < 1 or height < 1:
            raise Exception('The width and the height must be at least 1')
        width -= 1
        height -= 1
        self.draw_h_line(x, x + width, y, h_icon, fg_color, bg_color)
        self.draw_h_line(x, x + width, y + height, h_icon, fg_color, bg_color)
        self.draw_v_line(x, y, y + height, v_icon, fg_color, bg_color)
        self.draw_v_line(x + width, y, y + height, v_icon, fg_color, bg_color)
        self.plot(x, y, bl_icon, fg_color, bg_color)
        self.plot(x + width, y, br_icon, fg_color, bg_color)
        self.plot(x, y + height, tl_icon, fg_color, bg_color)
        self.plot(x + width, y + height, tr_icon, fg_color, bg_color)

    def plot_dict(self, dct, icon='x', fg_color=Color.RESET, bg_color=Color.RESET):
        """
        Plots the values of a dict
        :type dct: dict
        :type icon: char
        :type fg_color: Color
        :type bg_color: Color
        :param dct: dictionary: a dictionary containing a float as key (x) and a float as value (y)
        :param icon: a single character to display a point
        :param fg_color: optional: the fore color of the rectangle
        :param bg_color: optional: the back color of the rectangle
        """
        val_range = [float('inf'), float('-inf')]
        key_range = [float('inf'), float('-inf')]
        for key, val in dct.items():
            key_range[0] = min(key, key_range[0])
            key_range[1] = max(key, key_range[1])
            val_range[0] = min(val, val_range[0])
            val_range[1] = max(val, val_range[1])
        for key, val in dct.items():
            self.plot(x=int(map_value(val=int(key), min_in=int(key_range[0]), max_in=int(key_range[1]),
                                      max_out=self.width - 1)),
                      y=int(map_value(val=int(val), min_in=int(val_range[0]), max_in=int(val_range[1]),
                                      max_out=self.height - 1)),
                      icon=icon, fg_color=fg_color, bg_color=bg_color)

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


def map_value(val, min_in=0, max_in=100, min_out=0, max_out=100):
    """
    Maps a value from an allowed range to a other range
    :type val: float
    :type min_in: float
    :type max_in: float
    :type min_out: float
    :type max_out:float
    :param val: the value to be mapped
    :param min_in: the minimal input value
    :param max_in: the maximal input value
    :param min_out: the minimal output value
    :param max_out: the maximal output value
    :return: :raise Exception: if maximum values are smaller or equal to minimal values
    or if the input value is not in the allowed range
    """
    if max_in <= min_in or max_out <= min_out:
        raise Exception('The max value must be larger than the min value')
    if not min_in <= val <= max_in:
        raise Exception('The input value is not between the minimal and the maximal input')
    return min_out + (val - min_in) * (max_out - min_out) / (max_in - min_in)
