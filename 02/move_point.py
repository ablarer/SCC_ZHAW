# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 10:39:47 2021

@author: roor
"""

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# warmup example: point moving along diagonal line

x_step = 0.5        # increment of x-coordinate in one step
y_step = 0.25       # increment of y-coordinate in one step
n = 200             # number of steps

# data generation
xdata = [0]
ydata = [0]
for i in range(n):
    xdata.append(xdata[-1]+x_step)
    ydata.append(ydata[-1]+y_step)

# setup of animation
fig, ax = plt.subplots()
ln, = plt.plot([], [], 'r.')


def init():
    ax.axis([-12, 120, -12, 120])
    ax.set_aspect('equal', 'box')
    return ln,


def update(frame):
    ln.set_data(xdata[frame], ydata[frame])
    return ln,


ani = FuncAnimation(fig, update, frames=n, init_func=init, interval=10)

plt.show()