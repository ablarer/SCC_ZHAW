# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 14:40:47 2021

@author: roor
"""
import math

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import task1 as am

ce = np.array([5, 0, 1])  # start coordinates of earth
cm = np.array([7, 0, 1])  # start coordinates of moon
sun = np.array([0, 0, 1])  # coordinates of the sun

side_len_earth = 2.
side_len_moon = 0.5
n_per_day = 5
n_days = 36
n = n_days*n_per_day                         # number of iterations
phi_rotate_earth = 2*np.pi/n_days/n_per_day  # angular velocity earth sun
phi_spin_earth = 2*np.pi/n_days/n_per_day    # 2 = positive spin of earth
phi_rotate_moon = 2*np.pi/n_days
phi_spin_moon = 2*np.pi/n_days/n_per_day     # 2 = positive spin of moon

t_hori = np.array([side_len_earth/2, 0, 0])
t_vert = np.array([0, side_len_earth/2, 0])

t_hori_moon = np.array([side_len_moon/2, 0, 0])
t_vert_moon = np.array([0, side_len_moon/2, 0])

# coordinates of the four vertices s1, s2, s3, s4 of the square
se1 = ce - t_hori - t_vert
se2 = ce + t_hori - t_vert
se3 = ce + t_hori + t_vert
se4 = ce - t_hori + t_vert

sm1 = cm - t_hori_moon - t_vert_moon
sm2 = cm + t_hori_moon - t_vert_moon
sm3 = cm + t_hori_moon + t_vert_moon
sm4 = cm - t_hori_moon + t_vert_moon


ce_tuple_list = [[ce, se1, se2, se3, se4]]
cm_tuple_list = [[cm, sm1, sm2, sm3, sm4]]

for i in range(n):
    # Earth
    ce = ce_tuple_list[-1][0]

    # Moon
    cm = cm_tuple_list[-1][0]

    # Earth
    # Spin: Move earth "point"
    ce_rotated = am.rotate_around_point(ce, sun[0], sun[1], phi_rotate_earth)
    # Spin: Move earth "square"
    ce_tuple_rotated = am.rotate_tuple(ce_tuple_list[-1], sun[0], sun[1], phi_rotate_earth)
    # Rotate
    ce_tuple_list.append(am.rotate_tuple(ce_tuple_rotated, ce_rotated[0], ce_rotated[1], phi_spin_earth))

    # Moon
    # Spin: Move moon "point"
    cm_rotated = am.rotate_around_point(cm, ce[0], ce[1], phi_rotate_moon)
    # Spin: Move moon "square"
    cm_tuple_rotated = am.rotate_tuple(cm_tuple_list[-1], ce[0], ce[1], phi_rotate_moon)
    # Rotate
    cm_tuple_list.append(am.rotate_tuple(cm_tuple_rotated, sun[0], sun[1], phi_spin_earth))

fig, ax = plt.subplots()
plt.plot(sun[0], sun[1], '*y')  # Center Sun
ln1, = plt.plot([], [], '-r')  # red earth square side
ln2, = plt.plot([], [], '-k')  # black earth square side
ln3, = plt.plot([], [], '-k')  # black earth square side
# Moon
ln4, = plt.plot([], [], '-b')
ln5, = plt.plot([], [], '-k')
ln6, = plt.plot([], [], '.y')  # Center moon


def init():
    ax.axis([-10, 10, -10, 10])
    ax.set_aspect('equal', 'box')
    return ln1, ln2, ln3, ln4, ln5, ln6


def update(frame):
    ce, s1, s2, s3, s4 = ce_tuple_list[frame]
    square = np.stack([s1, s2, s3, s4, s1])
    x_data_square, y_data_square = square[:, 0], square[:, 1]
    side = np.stack([s4, s1])
    x_data_side, y_data_side = side[:, 0], side[:, 1] # extract x- and y-values from the three vectors
    ln1.set_data(x_data_square, y_data_square)
    ln2.set_data(x_data_side, y_data_side)
    ln3.set_data(ce[0], ce[1])

    cm, sm1, sm2, sm3, sm4 = cm_tuple_list[frame]
    square_moon = np.stack([sm1, sm2, sm3, sm4, sm1])
    x_data_square_moon, y_data_square_moon = square_moon[:, 0], square_moon[:, 1]
    side_moon = np.stack([s4, s1])
    x_data_side_moon, y_data_side_moon = side_moon[:, 0], side_moon[:, 1]  # extract x- and y-values from the three vectors
    ln4.set_data(x_data_square_moon, y_data_square_moon)
    ln5.set_data(x_data_side_moon, y_data_side_moon)
    # ln6.set_data(cm[0], cm[1])
    plt.plot(cm[0], cm[1], '.b-', markersize = 2)

    return ln1, ln2, ln3, ln4, ln5, ln6


ani = FuncAnimation(fig, update, frames=n, init_func=init, interval=10)
# ani.save('move_point.gif') # generates animated gif
plt.show()
