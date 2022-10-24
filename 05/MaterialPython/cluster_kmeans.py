# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 15:34:44 2021

@author: roor
"""

import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

from load_data import load_data
from plot_clusters import plot_clusters


def cluster_kmeans(data):

    N, d = data.shape
    alpha = np.ones((N, 4))             # alpha[:, i] assignment when number
                                        # of clusters is i+2
    silhouetteValue = np.zeros((4,))    # silhoutteValue[i]: silhouette value
                                        # for alpha(:,i)
    for k in range(4):
        kmeans = KMeans(n_clusters=k+2, random_state=0).fit(data)
        alpha[:, k] = kmeans.predict(data, k+2)
        silhouetteValue[k] = silhouette_score(data, alpha[:, k])

    i = silhouetteValue.argmax()        # finding index for optimal silhouette

    alphaOpt = alpha[:, i]

    return alphaOpt
