# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 15:52:55 2021

@author: roor
"""

# import numpy as np
import matplotlib.pyplot as plt

from sys import exit


def plot_clusters(X, alpha):
    # input:
    # alpha[i] denotes the cluster of point data[i, :]
    # the number k of clusters must be between 2 and 5
    # plots points such that points of the same cluster get the same color

    k = max(alpha)
    if not (k >= 1 and k <= 4):
        exit('Error (plot_clusters): wrong number of clusters')

    fig = plt.figure()
    plt.clf()

    P1 = X[alpha == 0, :]
    P2 = X[alpha == 1, :]
    P3 = X[alpha == 2, :]
    P4 = X[alpha == 3, :]
    P5 = X[alpha == 4, :]

    plt.plot(P1[:, 0], P1[:, 1], 'b.')
    plt.plot(P2[:, 0], P2[:, 1], 'r.')
    if (k >= 2):
        plt.plot(P3[:, 0], P3[:, 1], 'g.')
    if (k >= 3):
        plt.plot(P4[:, 0], P4[:, 1], 'm.')
    if (k >= 4):
        plt.plot(P5[:, 0], P5[:, 1], 'y.')
    return fig
