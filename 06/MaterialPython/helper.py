# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 14:27:31 2021

@author: roor
"""

import numpy as np


# supplied by the lecturer
def distance(p, q):
    dif = p - q
    return np.linalg.norm(dif, 2)


def classify_nearestmean(A, M, k):
    # classification by nearest mean
    t = M.shape[0]
    r, d = A.shape
    N = r // k

    means = np.zeros((k, d))
    alpha = np.zeros((t,))
    for i in range(k):
        T = A[N * i:N * (i + 1)]
        means[i, :] = np.mean(T, axis=0)
    # print(means)
    dist_to_mean = np.zeros((k,))
    for i in range(t):
        P = M[i, :]
        for j in range(k):
            dist_to_mean[j] = distance(P, means[j, :])
        alpha[i] = dist_to_mean.argmin()

    return alpha


"""
def classifyNearestNeighbor(A, M, k):
    d = A.shape[1]
    N = A.shape[0]/k
    t = M.shape[0]
    s = M.shape[1]

    # Means matrix stores the mean of each class
    means = np.zeros((k, d))

    # Stores the probability density value for each point p
    probDensity = np.zeros((t, k))

    # T: subset of rows of A belonging to class i
    for i in range(k):
        T = A((i-1)*N+1:N*i, :)
        for j in range(d):
            means(i,j) = mean(T(:, j))

        covMatrix = cov(T)
        probDensity(:,i) = mvnpdf(M, means(i,:), covMatrix)

    for i in range(s):
        [m, alpha(i)] = max(probDensity(i,:))

    return alpha
    
"""
