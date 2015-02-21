#!/usr/bin/env python
# coding=utf-8

from plotsy import *
from colorama import Fore
from colorama import Back

# Define the drawing area
graph = Plotsy([30, 30], Back.BLACK + ' ' + Back.RESET)

# plotting some functions
for i in range(6):
    graph.plot([i**2, i], "@")

for i in range(6):
    graph.plot([i, i**2])

for i in range(8):
    graph.plot([28 - i, i])

# draw some lines (this will be a box around the drawing area)
graph.draw_v_line(x=0, y1=0, y2=30, fg_color=Fore.BLUE, bg_color=Back.WHITE)
graph.draw_v_line(x=29, y1=0, y2=30, fg_color=Fore.BLUE, bg_color=Back.WHITE)
graph.draw_h_line(x1=0, x2=30, y=0, fg_color=Fore.BLUE, bg_color=Back.WHITE)
graph.draw_h_line(x1=0, x2=30, y=29, fg_color=Fore.BLUE, bg_color=Back.WHITE)

# plot some randomness
import random
old = 10
max_val = old
for i in range(28):
    graph.plot([1 + i, old], '.', Fore.RED, Back.GREEN)
    graph.label([1 + i, old + 1], str(old), Fore.RESET, Back.BLUE)
    old = int(old - 2 + 4 * random.random())
    max_val = max(max_val, old)

# draw a vertical line. This is the maximum of the random output
graph.draw_h_line(x1=1, x2=29, y=max_val, fg_color=Fore.RED)
# add a label
graph.label([23, max_val + 1], 'max=%d' % max_val, Fore.RED)

# plot a label
graph.label([5, 25], 'HELLO WORLD', Fore.GREEN, Back.WHITE)
# draw a rectangle around the label
graph.draw_rect(4, 24, 13, 3, Fore.RED, Back.CYAN)

# display the drawing
graph.draw()
