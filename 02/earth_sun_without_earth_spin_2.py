# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 14:40:47 2021

@author: roor
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import task1 as am

ce = np. array([5, 0, 1]) # start coordinates of earth
sun = np. array([0, 0, 1]) # coordinates of the sun

side_len_earth = 2.
n_per_day = 12
n_days = 36
n = n_days*n_per_day                   # number of iterations
phi_rotate = 2*np.pi/n_days/n_per_day  # angular velocity earth sun

t_hori = np. array([side_len_earth/2, 0, 0])
t_vert = np. array([0, side_len_earth/2, 0])

# coordinates of the four vertices s1, s2, s3, s4 of the square
s1 = ce - t_hori - t_vert
s2 = ce + t_hori - t_vert
s3 = ce + t_hori + t_vert
s4 = ce - t_hori + t_vert
print('Two point vector: s4', s4)

# initialization (from now on, use homogeneous coordinates)
ce = np.append(ce, 1)
s1 = np.append(s1, 1)
s2 = np.append(s2, 1)
s3 = np.append(s3, 1)
s4 = np.append(s4, 1)
print('Three point vector: s4', s4)

ce_tuple_list = [[ce, s1, s2, s3, s4]]
for i in range(n):
    ce_tuple_list.append(am.rotate_tuple(ce_tuple_list[-1], sun[0], sun[1], phi_rotate))

fig, ax = plt.subplots()
plt.plot(sun[0], sun[1], '*b')
ln1 = plt.plot([], [], '-r')
ln2 = plt.plot([], [], '-k')
ln3 = plt.plot([], [], '.k')

def init():
    ax.axis([-10, 10, -10, 10])
    ax.set_aspect('equal', 'box')
    return ln1, ln2, ln3


def update(frame):
    ce, s1, s2, s3, s4 = ce_tuple_list[frame]
    square = np.stack([s1, s2, s3, s4, s1])
    x_data_square, y_data_square = square[:, 0], square[:, 1]
    side = np.stack([s4, s1])
    x_data_side, y_data_side = side[:, 0], side[:, 1]


ani = FuncAnimation(fig, update, frames=n, init_func=init, interval=10)
# ani.save('move_point.gif') # generates animated gif
plt.show()
