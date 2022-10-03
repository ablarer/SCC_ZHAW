# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 10:39:47 2021

@author: roor
"""

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# warmup example: point moving along diagonal line

x_step = 0.5  # increment of x-coordinate in one step
y_step = 0.25  # increment of y-coordinate in one step
n = 200  # number of steps

# data generation
xdata = [0]
ydata = [0]
for i in range(n):
    xdata.append(xdata[-1] + x_step)  # List, add element to list
    ydata.append(ydata[-1] + y_step)  # List, add element to list

# setup of animation
fig, ax = plt.subplots()
ln, = plt.plot([], [], 'r.')  # plot empty list, Das Komma braucht es!


def init():
    ax.axis([-12, 120, -12, 120])
    ax.set_aspect('equal', 'box')  # aspect ratio x and y are the same, with box

    return ln,


def update(frame):
    ln.set_data(xdata[frame], ydata[frame])  # set object on the line object

    return ln,


ani = FuncAnimation(fig, update, frames=n, init_func=init, interval=10)
# ani.save('move_point.gif') # generates animated gif
plt.show()
