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
from math import log10, ceil


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
        rows, columns = max_height, max_width
        if int(width) <= 0 or int(height) <= 0:
            term_size = popen('stty size', 'r').read()
            if len(term_size) == 0:
                from logging import critical
                critical("This has to be executed in a terminal.")
                # exit(1)
            else:
                rows, columns = term_size.split()
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

    def plot_label(self, x, y, text, fg_color=Color.RESET, bg_color=Color.RESET):
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

    def plot_h_line(self, y, x1=0, x2=0, icon='–', fg_color=Color.RESET, bg_color=Color.RESET):
        """
        Draw a horizontal line
        :type x1: int
        :type x2: int
        :type y: int
        :type icon: chr
        :type fg_color: Color
        :type bg_color: Color
        :param x1: the first x coordinate (the start)
        :param x2: the second x coordinate (the end). If it is smaller than 1, x2 = height - |x2|
        :param y: the y coordinate of the line
        :param icon: icon for the line
        :param fg_color: optional: the fore color of the line
        :param bg_color: optional: the back color of the line
        """
        if x2 < 1:
            x2 = self.width + x2
        if x1 > x2:
            x1, x2 = x2, x1  # swap
        for x in range(x1, x2):
            self.plot(x, y, icon, fg_color, bg_color)

    def plot_v_line(self, x, y1=0, y2=0, icon='|', fg_color=Color.RESET, bg_color=Color.RESET):
        """
        Draw a vertical line
        :type x: int
        :type y1: int
        :type y2: int
        :type icon: chr
        :type fg_color: Color
        :type bg_color: Color
        :param x: the x coordinate of the line
        :param y1: the first y coordinate (the start)
        :param y2: the second y coordinate (the end). If it is smaller than 1, y2 = height - |y2|
        :param icon: icon for the line
        :param fg_color: optional: the fore color of the line
        :param bg_color: optional: the back color of the line
        """
        if y2 < 1:
            y2 = self.height + y2
        if y1 > y2:
            y1, y2 = y2, y1  # swap
        for y in range(y1, y2):
            self.plot(x, y, icon, fg_color, bg_color)

    def plot_rect(self, x, y, width, height,
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
        self.plot_h_line(y, x, x + width, h_icon, fg_color, bg_color)
        self.plot_h_line(y + height, x, x + width, h_icon, fg_color, bg_color)
        self.plot_v_line(x, y, y + height, v_icon, fg_color, bg_color)
        self.plot_v_line(x + width, y, y + height, v_icon, fg_color, bg_color)
        self.plot(x, y, bl_icon, fg_color, bg_color)
        self.plot(x + width, y, br_icon, fg_color, bg_color)
        self.plot(x, y + height, tl_icon, fg_color, bg_color)
        self.plot(x + width, y + height, tr_icon, fg_color, bg_color)

    def plot_dict(self, dct, map_values=True, cosys=False, icon='x', fg_color=Color.RESET, bg_color=Color.RESET):
        """
        Plots the values of a dict
        :type dct: dict
        :type icon: char
        :type map_values: bool
        :type cosys: bool
        :type fg_color: Color
        :type bg_color: Color
        :param dct: dictionary: a dictionary containing a float as key (x) and a float as value (y).
        If it contains a key and a value which are str, then they will be handled as label of the x- and y- axis.
        :param icon: a single character to display a point
        :param map_values: map values to the drawing area? true if cosys
        :param cosys: draw a coordinate system? implicates map_values
        :param fg_color: optional: the fore color of the rectangle
        :param bg_color: optional: the back color of the rectangle
        """
        x_label = 'x'
        y_label = 'y'
        if cosys:
            val_range = [float(0), float(0)]
            key_range = [float(0), float(0)]
        else:
            val_range = [float('inf'), float('-inf')]
            key_range = [float('inf'), float('-inf')]
        for key, val in dct.items():
            if isinstance(key, str) or isinstance(val, str):
                x_label = key
                y_label = val
            else:
                key_range[0] = min(key, key_range[0])
                key_range[1] = max(key, key_range[1])
                val_range[0] = min(val, val_range[0])
                val_range[1] = max(val, val_range[1])
        if cosys:
            self.plot_cosys(min_x=key_range[0], max_x=key_range[1],
                            min_y=val_range[0], max_y=val_range[1], x_label=x_label, y_label=y_label)
        for key, val in dct.items():
            if not isinstance(key, str) or not isinstance(val, str):
                if map_values or cosys:
                    self.plot(x=int(map_value(val=key, min_in=key_range[0], max_in=key_range[1],
                                              max_out=self.width - 1)),
                              y=int(map_value(val=val, min_in=val_range[0], max_in=val_range[1],
                                              max_out=self.height - 1)),
                              icon=icon, fg_color=fg_color, bg_color=bg_color)
                else:
                    self.plot(x=int(key), y=int(val), icon=icon, fg_color=fg_color, bg_color=bg_color)

    def plot_cosys(self, min_x=0, max_x=10, min_y=0, max_y=10, x_label='x', y_label='y',
                   fg_color=Color.LIGHTBLACK_EX, bg_color=Color.RESET):
        """
        Draws a coordinate system in the entire drawing area (unfortunately there are many rounding errors)
        :type min_x: float
        :type max_x: float
        :type min_y: float
        :type max_y: float
        :type x_label: str
        :type y_label: str
        :type fg_color: Color
        :type bg_color: Color
        :param min_x: The minimal x-value, that should be displayed (<= 0)
        :param max_x: The maximal x-value, that should be displayed
        :param min_y: The minimal y-value, that should be displayed (<= 0)
        :param max_y: The maximal y-value, that should be displayed
        :param x_label: The x-axis description that should be printed
        :param y_label: The y-axis description that should be printed
        :param fg_color: optional: the fore color of the coordinate system
        :param bg_color: optional: the back color of the coordinate system
        :raise Exception: If the minimal values are bigger than 0
        """
        # <editor-fold desc="error check and helper variables">
        if min_x > 0 or min_y > 0:
            raise Exception('Sorry, the origin must be included in the range. '
                            'The ranges are: {min_x} <=x <= {max_x}; {min_y} <= y <= {max_y}'
                            .format(min_x, max_x, min_y, max_y))
        origin_x = int(map_value(0, min_x, max_x, 0, self.width - 1))
        origin_y = int(map_value(0, min_y, max_y, 0, self.height - 1))
        # the y coordinate for the x labels. For the y label, it must be calculated dynamically:
        y_coord_x_label = origin_y - 1 if origin_y > 0 else origin_y + 1
        # </editor-fold>
        self.plot_v_line(x=origin_x, y2=-1, fg_color=fg_color, bg_color=bg_color)
        self.plot_h_line(y=origin_y, x2=-1, fg_color=fg_color, bg_color=bg_color)
        # <editor-fold desc="add legends and origin and arrowheads">
        self.plot(x=origin_x, y=origin_y, icon='0', fg_color=fg_color, bg_color=bg_color)
        self.plot(x=origin_x, y=self.height - 1, icon='^', fg_color=fg_color, bg_color=bg_color)
        self.plot(x=self.width - 1, y=origin_y, icon='>', fg_color=fg_color, bg_color=bg_color)
        self.plot_label(x=origin_x - len(y_label) if origin_x >= len(y_label) else origin_x + 1,
                        y=self.height - 1, text=y_label, fg_color=fg_color, bg_color=bg_color)
        self.plot_label(x=self.width - len(x_label), y=y_coord_x_label, text=x_label,
                        fg_color=fg_color, bg_color=bg_color)
        # </editor-fold>
        # <editor-fold desc="add legend to axis">
        # <editor-fold desc="add legend to y axis">
        old_label = ""
        for y in range(0, self.height - 2, 2):
            txt = str(round_to_n(map_value(val=float(y), min_in=0, max_in=self.height - 2,
                                           min_out=min_y, max_out=max_y), n=0 if max_y == 0 else log10(abs(max_y))))
            if txt != old_label and y != origin_y and txt != '0.0':
                self.plot(x=origin_x, y=y, icon='–', fg_color=fg_color, bg_color=bg_color)
                self.plot_label(x=origin_x - len(txt) if origin_x >= len(txt) else origin_x + 1, y=y,
                                text=txt, fg_color=fg_color, bg_color=bg_color)
            old_label = txt
        # </editor-fold>
        # <editor-fold desc="add legend to x-axis>
        old_label = ""
        for x in range(0, self.width - 2, max((2 + len(str(max_x))), self.width / (max_x - min_x), self.width / 20)):
            txt = str(round_to_n(map_value(val=float(x), min_in=0, max_in=self.width - 2,
                                           min_out=min_x, max_out=max_x), n=0 if max_x == 0 else log10(abs(max_x))))
            if txt != old_label and x != origin_x and txt != '0.0':
                self.plot(x=x, y=origin_y, icon='|', fg_color=fg_color, bg_color=bg_color)
                self.plot_label(x=x - len(txt) / 2, y=y_coord_x_label,
                                text=txt, fg_color=fg_color, bg_color=bg_color)
            old_label = txt
        # </editor-fold>
        # </editor-fold>

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
    if max_in == min_in:
        return (max_out - min_out) / 2
    if max_in < min_in:
        raise Exception('The max input value must be larger than the min input value. min={min}; max={max}'
                        .format(min=max_in, max=max_in))
    if max_out < min_out:
        raise Exception('The max output value must be larger than the min output value. min={min}; max={max}'
                        .format(min=max_in, max=max_in))
    if not min_in <= val <= max_in:
        raise Exception('The input value is not between the minimal and the maximal input.'
                        ' min={min}; val={val}; max={max}'.format(min=min_in, val=val, max=max_in))
    return min_out + (val - min_in) * (max_out - min_out) / (max_in - min_in)


def round_to_n(x, n=2):
    """
    Rounds a number to n significant digit
    :type x: float
    :param x: the number to round
    :return: the number x rounded to n significant digit
    """
    pre = 1
    if x < 0:
        x = -x
        pre = -1
    elif x == 0:
        return 0
    return pre * round(x, int(n - ceil(log10(abs(x)))))