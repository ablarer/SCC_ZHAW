# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 10:39:47 2021

@author: roor
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# warmup example: point moving along diagonal line

x_step = 0.5  # increment of x-coordinate in one step
y_step = 0.25  # increment of y-coordinate in one step
n = 250  # number of steps / frames

cs = np.array([3., 4.])  # coordinates of the center of the square
# arbitrarily chosen values
side_len = 8.  # side length of the square

tHori = np.array([side_len / 2, 0])  # horizontal translation (half side length)
tVert = np.array([0, side_len / 2])  # vertical translation (half side length)

# coordinates of the four vertices s1, s2, s3, s4 of the square
s1 = cs - tHori - tVert
s2 = cs + tHori - tVert
s3 = cs + tHori + tVert
s4 = cs - tHori + tVert
print('Two point vector: s4', s4)

# initialization (from now on, use homogeneous coordinates)
cs = np.append(cs, 1)
s1 = np.append(s1, 1)
s2 = np.append(s2, 1)
s3 = np.append(s3, 1)
s4 = np.append(s4, 1)
print('Three point vector: s4', s4)

T = np.array([[1, 0, x_step], [0, 1, y_step], [0, 0, 1]])  # translation matrix
print(T)

list_points = []
for i in range(n):
    cs = T @ cs
    s1 = T @ s1
    s2 = T @ s2
    s3 = T @ s3
    s4 = T @ s4
    list_points.append([cs, s1, s2, s3, s4])
# print('cs ', cs, 's1 ', s1, 's2 ', s2, 's3 ', s3, 's4 ',s4)

fig, ax = plt.subplots()
ln1, = plt.plot([], [], 'r')  # Box lines, For the box, plot empty list, Das Komma braucht es!
ln2, = plt.plot([], [], '*b')  # Box center, For the center, plot empty list, Das Komma braucht es!


def init():
    ax.axis([-12, 120, -12, 120])
    ax.set_aspect('equal', 'box')
    return ln1, ln2,


def update(frame):
    cs, s1, s2, s3, s4 = list_points[frame]
    square = np.stack([s1, s2, s3, s4, s1]) # Stack points to be able to plot a square
    x_data, y_data = square[:, 0], square[:, 1] # extract x- and y-values from the three vectors
    ln1.set_data(x_data, y_data)
    ln2.set_data(cs[0], cs[1]) # x- and y-coordinates for the center
    return ln1, ln2,


ani = FuncAnimation(fig, update, frames=n, init_func=init, interval=25)
# ani.save('move_point.gif') # generates animated gif
plt.show()