# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 16:37:53 2021

@author: roor
"""
import matplotlib.pyplot as plt
from load_data import load_data
from cluster_kmeans import cluster_kmeans
from plot_clusters import plot_clusters

def test_kmeans():
    #Close all open plots
    plt.close('all')
    dictData = load_data()
    figures = []

    for k in range(10):
        dataString = 'data{:d}'.format(k+1)
        data = dictData[dataString]
        alpha = cluster_kmeans(data)
        figures.append(plot_clusters(data, alpha))

    return figures
