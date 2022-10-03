# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 14:40:47 2021

@author: roor
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import auxiliary_methods as am

ce =                                        # start coordinates of earth
sun =                                       # coordinates of the sun

n_per_day =  
n_days =  
n = n_days*n_per_day                        # number of iterations
phi_rotate =                                # angular velocity earth - sun

ce_list = [ce]
for i in range(n):
    ce_list.append(...)                     # generate coordinates

fig, ax = plt.subplots()
plt.plot(sun[0], sun[1], '*b')
ln, = plt.plot([], [], 'or')


def init():
    ...
    return ln,


def update(frame):
    ...
    return ln,


ani = FuncAnimation(fig, update, frames=n, init_func=init, interval=10)

plt.show()
