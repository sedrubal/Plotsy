#!/usr/bin/env python
# coding=utf-8

from plotsy import *
from plotsy_color import *

# <editor-fold desc="example 1: plot chaos">
print("")
print("example 1: Print Chaos")
print("----------------------")
print("")
# Define the drawing area
graph = Plotsy(width=30, height=30, background=Color.to_ansi(Color.BLACK, foreground=False)
               + ' ' + Color.to_ansi(Color.RESET, foreground=False))

# <editor-fold desc="plotting some functions"
for i in range(6):
    graph.plot(x=i**2, y=i, icon="@")

for i in range(6):
    graph.plot(x=i, y=i**2)

for i in range(8):
    graph.plot(x=28 - i, y=i)
# </editor-fold>

# <editor-fold desc="draw some lines (this will be a box around the drawing area, you can also use plot_rect())">
graph.plot_v_line(x=0, fg_color=Color.BLUE, bg_color=Color.WHITE)  # y1=0, y2=30 is not needed, because this is default
graph.plot_v_line(x=29, fg_color=Color.BLUE, bg_color=Color.WHITE)
graph.plot_h_line(y=0, fg_color=Color.BLUE, bg_color=Color.WHITE)
graph.plot_h_line(y=29, fg_color=Color.BLUE, bg_color=Color.WHITE)
# </editor-fold>

# <editor-fold desc="plot some randomness">
from random import random
old = 10
max_val = old
for i in range(28):
    graph.plot(x=1 + i, y=old, icon='.', fg_color=Color.RED, bg_color=Color.GREEN)
    graph.plot_label(x=1 + i, y=old + 1, text=str(old), fg_color=Color.RESET, bg_color=Color.BLUE)
    old = max(0, int(old - 2 + 4 * random()))
    max_val = max(max_val, old)
# </editor-fold>

# draw a vertical line. This is the maximum of the random output
graph.plot_h_line(x1=1, x2=29, y=max_val, fg_color=Color.RED)
# add a label
graph.plot_label(x=23, y=max_val + 1, text=('max=%d' % max_val), fg_color=Color.RED)

# plot a label
graph.plot_label(x=5, y=25, text='HELLO WORLD', fg_color=Color.GREEN, bg_color=Color.WHITE)
# draw a rectangle around the label
graph.plot_rect(x=4, y=24, width=13, height=3, fg_color=Color.RED, bg_color=Color.CYAN)

# <editor-fold desc="print color palette">
graph.plot_label(2, 18, 'supported colors:', Color.GREEN, Color.WHITE)
x = 2
# noinspection PyTypeChecker
for c in Color:
    graph.plot(x, 17, 'f', fg_color=c)
    graph.plot(x, 16, 'b', bg_color=c)
    x += 1
# </editor-fold>

# display the drawing
graph.draw()
# </editor-fold>

# <editor-fold desc="example 2: plot a sqrt function">
print("")
print("example 2: Plot a sqrt function")
print("-------------------------------")
print("")
# create a new graph with a drawing are that is one line smaller than the current terminal
graph2 = Plotsy(height=-1)
# make a dict that contains x values as key and y values as values
dct = dict()
from math import sqrt
# this dict will contain a lot of values, the more the better
for x in range(250):
    dct[x] = sqrt(x)
# add a label for the x-axis ('x') and the y-axis ('sqrt(x)')
dct['x'] = 'sqrt(x)'
# plot this dict and draw a coordinate system to this values.
# The graph will be automatically stretched to the current drawing area
graph2.plot_dict(dct, cosys=True)
# and display the plot. Please ignore the rounding errors ;)
graph2.draw()
# </editor-fold>