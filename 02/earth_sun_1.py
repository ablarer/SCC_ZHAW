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
n = n_days*n_per_day                             # number of iterations / frames
phi = 2*np.pi/(n_days * n_per_day) # fraction of angle per day and year, angular velocity earth - sun
ce_list = [ce]


for i in range(n):
    # generate coordinates for earth orbit
    # p = starting point earth, a = x-coordination sun, b = y-coordination sun, phi
    ce = am.rotate_around_point(ce, sun[0], sun[1], phi)
    # print(ce)
    ce_list.append(ce)
# print('ce_list first item: ', ce_list[0])
# print('ce_list last item: ', ce_list[-1])
# print('ce_list item somewhere in the middle of the list: ', ce_list[500])



fig, ax = plt.subplots()
plt.plot(sun[0], sun[1], '*r')  # Sun
ln, = plt.plot([], [], 'ob')    # Line for earth

def init():
    # define plot parameters
    ax.axis([-5, 5, -5, 5])
    ax.set_aspect('equal', 'box')
    return ln,

def update(frame):
    x_data, y_data, z_data = ce_list[frame]
    ln.set_data(x_data, y_data)
    return ln,


ani = FuncAnimation(fig, update, frames=n, init_func=init, interval=10)
# ani.save('move_point.gif') # generates animated gif
plt.show()
