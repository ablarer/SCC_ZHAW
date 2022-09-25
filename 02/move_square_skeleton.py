# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 10:39:47 2021

@author: roor
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# warmup example: point moving along diagonal line

x_step = 0.5                # increment of x-coordinate in one step
y_step = 0.25               # increment of y-coordinate in one step
n = 200                     # number of steps

cs = np.array([3., 4.])     # coordinates of the center of the square
                            # arbitrarily chosen values
side_len = 8.               # side length of the squaere
side_len_half = side_len / 2

# coordinates of the four vertices s1, s2, s3, s4 of the square
s1 = cs - [-side_len_half, +side_len_half]
s2 = cs - [+side_len_half, +side_len_half]
s3 = cs - [+side_len_half, -side_len_half]
s4 = cs - [-side_len_half, -side_len_half]

# initialization (from now on, use homogeneous coordinates)
cs = cs
s1 = cs - [-side_len_half, +side_len_half]
s2 = cs - [+side_len_half, +side_len_half]
s3 = cs - [+side_len_half, -side_len_half]
s4 = cs - [-side_len_half, -side_len_half]


list_points = []
for i in range(n):
    xdata.append(xdata[-1]+x_step)
    ydata.append(ydata[-1]+y_step)...
    ...     # update cs, s1, ..., s4
    ...
    list_points.append(...)


fig, ax = plt.subplots()
ln1, = plt.plot([], [], 'r')
ln2, = plt.plot([], [], '.k')


def init():
    ...
    return ln1, ln2,


def update(frame):
    def rotate_around_point(coord_old, a, b, phi):

    cs, s1, s2, s3, s4 = rotate_around_point(coord_old, a, b, phi)
    ...     # update the data objects of plots
    ...
    return ln1, ln2,


ani = FuncAnimation(fig, update, frames=n, init_func=init, interval=25)

plt.show()
