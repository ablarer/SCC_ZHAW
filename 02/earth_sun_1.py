# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 14:40:47 2021

@author: roor
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import task1 as am # Auxiliary method

ce = np.array([5., 0., 1.])       # start coordinates of earth
sun = np. array([0., 0., 1.])     # coordinates of the sun

n_per_day = 3
n_days = 365
n = n_days*n_per_day                             # number of iterations
phi = phi_rotate = 2*np.pi/n_days/n_per_day      # angular velocity earth - sun

ce_list = [ce]


for i in range(n):
    # generate coordinates
    e = am.rotate_around_point(ce, sun[0], sun[1], phi)
    print(e)
    ce_list.append(e)

fig, ax = plt.subplots()
plt.plot(sun[0], sun[1], '*b')
ln, = plt.plot([], [], '.r')


def init():
    ax.axis([-5, 5, -5, 5])
    ax.set_aspect('equal', 'box')
    return ln,


def update(frame):
    ln.set_data(ce_list[frame])
    return ln,


ani = FuncAnimation(fig, update, frames=n, init_func=init, interval=10)
# ani.save('move_point.gif') # generates animated gif
plt.show()
