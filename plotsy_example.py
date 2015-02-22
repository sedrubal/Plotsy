#!/usr/bin/env python
# coding=utf-8

from plotsy import *
from plotsy_color import *

# Define the drawing area
graph = Plotsy(width=30, height=30, background=
               Color.to_ansi(Color.BLACK, foreground=False) + ' ' + Color.to_ansi(Color.RESET, foreground=False))

# plotting some functions
for i in range(6):
    graph.plot(x=i**2, y=i, icon="@")

for i in range(6):
    graph.plot(x=i, y=i**2)

for i in range(8):
    graph.plot(x=28 - i, y=i)

# draw some lines (this will be a box around the drawing area)
graph.draw_v_line(x=0, y1=0, y2=30, fg_color=Color.BLUE, bg_color=Color.WHITE)
graph.draw_v_line(x=29, y1=0, y2=30, fg_color=Color.BLUE, bg_color=Color.WHITE)
graph.draw_h_line(x1=0, x2=30, y=0, fg_color=Color.BLUE, bg_color=Color.WHITE)
graph.draw_h_line(x1=0, x2=30, y=29, fg_color=Color.BLUE, bg_color=Color.WHITE)

# plot some randomness
import random
old = 10
max_val = old
for i in range(28):
    graph.plot(x=1 + i, y=old, icon='.', fg_color=Color.RED, bg_color=Color.GREEN)
    graph.label(x=1 + i, y=old + 1, text=str(old), fg_color=Color.RESET, bg_color=Color.BLUE)
    old = int(old - 2 + 4 * random.random())
    max_val = max(max_val, old)

# draw a vertical line. This is the maximum of the random output
graph.draw_h_line(x1=1, x2=29, y=max_val, fg_color=Color.RED)
# add a label
graph.label(x=23, y=max_val + 1, text=('max=%d' % max_val), fg_color=Color.RED)

# plot a label
graph.label(x=5, y=25, text='HELLO WORLD', fg_color=Color.GREEN, bg_color=Color.WHITE)
# draw a rectangle around the label
graph.draw_rect(x=4, y=24, width=13, height=3, fg_color=Color.RED, bg_color=Color.CYAN)

# print color palette
graph.label(2, 18, 'supported colors:', Color.GREEN, Color.WHITE)
x = 2
for c in Color:
    graph.plot(x, 17, 'f', fg_color=c)
    graph.plot(x, 16, 'b', bg_color=c)
    x += 1

# display the drawing
graph.draw()
