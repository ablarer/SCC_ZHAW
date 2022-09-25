# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 14:40:47 2021

@author: roor
"""
import math

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import auxiliary_methods as am

sun = [0.5, 0.5]                          # coordinates of the sun
ce = sun + [4, 4]                         # start coordinates of earth


n_per_day =  5
n_days =  20
n = n_days*n_per_day                        # number of iterations
phi_rotate = 0.5                           # angular velocity earth - sun

ce_list = [ce]
for i in range(n):
    ce_list.append(...)                     # generate coordinates

fig, ax = plt.subplots()
plt.plot(sun[0], sun[1], '*b')
ln, = plt.plot([], [], 'or')


def init():
    sun = [0.5, 0.5]
    earthStart = sun + [4, 4]
    moonStart = earthStart + [2.75, 2.75]
    earthSideLen = 2
    moonSideLen = earthSideLen / 2

    return ln,


def update(frame):
    ln.set_data(xdata[frame], ydata[frame])
    return ln,


ani = FuncAnimation(fig, update, frames=n, init_func=init, interval=10)

plt.show()


def rotateAroundPoint(p_old, a, b, phi):
    # Rotation matrix
    R = [[math.cos(phi), -math.sin(phi), 0],[math.sin(phi), math.cos(phi), 0], [0, 0, 1]]

    # Translation matrices
    T1 = [[1, 0 ,a], [0 ,1 ,b], [0 ,0 ,1]]
    T2 = [[1, 0, -a], [0, 1 -b], [0, 0, 1]]

    p_new = T1*R*T2*p_old;

    return p_new

def translate(p_old, u, v):
    p_new = [[1, 0, u] [0, 1, v] [0, 0, 1]] * p_old;
    return p_new

def scale(p_old, factor):
    p_new = [[factor, 0, 0], [0, factor, 0], [0, 0, 1]] * p_old;
    return p_new

# test cases
p_test_1 = rotateAroundPoint([2, 5, 1], 6, 9, math.pi/2)
print(f'p_test 1: Soll-Wert: [10, 5, 1], Ist-Wert: {p_test_1}')

p_test_2 = rotateAroundPoint([-2 ,8 ,1], 5, 7, math.pi)
print(f'p_test 1: Soll-Wert: [12, 6, 1], Ist-Wert: {p_test_2}')


