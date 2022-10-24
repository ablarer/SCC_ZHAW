# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 14:27:31 2021

@author: roor
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.io
from plot_clusters import plot_clusters


def csvRead(file):
    return np.loadtxt(file, delimiter=',')


def matRead(dir, name):
    data = scipy.io.loadmat(dir + name + '.mat')[name]
    if data.shape[1] == 1:
        data = data[:, 0]
    if data.shape[0] == 1:
        data = data[0, :]
    return data


def stringRead(name):
    with open(name+'.txt') as hFile:
        lines = hFile.readlines()
    return np.array(lines)


def rgb2gray(img):
    return np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])


def imshowGray(img):
    plt.imshow(img, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)


def imshowRgb(img):
    plt.imshow(img)


# ----------------------------------------------------------------------------
# Reading MATLAB based data files
# ----------------------------------------------------------------------------
def load_data():
    dictData = {}
    for k in range(10):
        dataString = 'data{:d}'.format(k+1)
        dictData[dataString] = matRead('data/', dataString)

    # moonRGB = plt.imread('data/moon.jpg')/255.0
    # dictData['moon'] = rgb2gray(moonRGB)
    dictData['moon'] = plt.imread('data/moon.jpg')/255.0

    return dictData


if __name__ == "__main__":

    testData = load_data()

    imshowRgb(testData['moon'])

    set1 = testData['data1']
    alpha = np.ones((len(set1),))
    alpha[[1, 2, 45, 12, 99]] = 2
    plot_clusters(testData['data1'], alpha)
