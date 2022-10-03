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
cm = np. array([5, 0, 1]) # start coordinates of moon # TODO Korrigieren
sun = np. array([0, 0, 1]) # coordinates of the sun

side_len_earth = 2.
n_per_day = 12
n_days = 36
n = n_days*n_per_day                   # number of iterations
phi_rotate_earth = 2*np.pi/n_days/n_per_day  # angular velocity earth sun
phi_spin_earth = 2*np.pi/n_days/n_per_day    # 2 = positive spin of earth
phi_spin_moon = 2*np.pi/n_days/n_per_day    # 2 = positive spin of moon # TODO Korrigieren

t_hori = np. array([side_len_earth/2, 0, 0])
t_vert = np. array([0, side_len_earth/2, 0])

# coordinates of the four vertices s1, s2, s3, s4 of the square
se1 = ce - t_hori - t_vert
se2 = ce + t_hori - t_vert
se3 = ce + t_hori + t_vert
se4 = ce - t_hori + t_vert

sm1 = cm - t_hori - t_vert
sm2 = cm + t_hori - t_vert
sm3 = cm + t_hori + t_vert
sm4 = cm - t_hori + t_vert


ce_tuple_list = [[ce, se1, se2, se3, se4]]
cm_tuple_list = [[cm, sm1, sm2, sm3, sm4]]

for i in range(n):
    ce = ce_tuple_list[-1][0]
    cm = cm_tuple_list[-1][0]

    # System earth/moon orbiting the sun
    ce_rotated = am.rotate_around_point(ce, sun[0], sun[1], phi_rotate_earth)
    ce_tuple_rotated = am.rotate_tuple(ce_tuple_list[-1], sun[0], sun[1], phi_rotate_earth)

    cm_rotated = am.rotate_around_point(cm, sun[0], sun[1], phi_rotate_earth)
    cm_tuple_rotated = am.rotate_tuple(cm_tuple_list[-1], sun[0], sun[1], phi_rotate_earth)
# Todo Code weiter für den Mond entwickeln.
    ce_tuple_list.append(am.rotate_tuple(ce_tuple_rotated, ce_rotated[0],ce_rotated[1], phi_spin_earth))

fig, ax = plt.subplots()
plt.plot(sun[0], sun[1], '*b')
ln1, = plt.plot([], [], '-r')
ln2, = plt.plot([], [], '-k')
ln3, = plt.plot([], [], '.k')


def init():
    ax.axis([-10, 10, -10, 10])
    ax.set_aspect('equal','*box')
    return ln1, ln2, ln3


def update(frame):
    ce, s1, s2, s3, s4 = ce_tuple_list[frame]
    square = np.stack([s1, s2, s3, s4, s1])
    x_data_square, y_data_square = square[:, 0], square[:, 1]
    side = np.stack([s4, s1])
    x_data_side, y_data_side = side[:, 0], side[:, 1] # extract x- and y-values from the three vectors
    ln1.set_data(x_data_square, y_data_square)
    ln2.set_data(x_data_side, y_data_side)
    ln3.set_data(ce[0], ce[1])
    return ln1, ln2, ln3


ani = FuncAnimation(fig, update, frames=n, init_func=init, interval=10)
# ani.save('move_point.gif') # generates animated gif
plt.show()
