# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 14:27:31 2021

@author: roor
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.io


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
    plt.show()


def imshowRgb(img):
    plt.imshow(img)
    plt.show()


# ----------------------------------------------------------------------------
# Reading MATLAB based data files
# ----------------------------------------------------------------------------
def load_data():
    dictData = {}
    for k in range(2):
        dataString = 'A{:d}'.format(k+1)
        dictData[dataString] = matRead('data/', dataString).astype('float')
        dataString = 'M{:d}'.format(k+1)
        dictData[dataString] = matRead('data/', dataString).astype('float')
    dictData['I'] = matRead('data/', 'I')
    dictData['skindata'] = matRead('data/', 'skindata')
    dictData['nonskindata'] = matRead('data/', 'nonskindata')
    dictData['test'] = plt.imread('data/test.jpg')/255.0
    dictData['maskTest'] = np.round(rgb2gray(plt.imread('data/maskTest.png')))
    return dictData


if __name__ == "__main__":

    testData = load_data()

    imshowRgb(testData['test'])
