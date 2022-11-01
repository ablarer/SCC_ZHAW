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


def imshowRgb(img):
    plt.imshow(img)


# ----------------------------------------------------------------------------
# Reading MATLAB based data files
# ----------------------------------------------------------------------------
def load_data():
    dictData = {}
    dictData['dataMat1'] = matRead('data/', 'dataMat1').astype('float')
    dictData['ITest'] = matRead('data/', 'ITest').astype('float')
    dictData['VTest'] = matRead('data/', 'VTest').astype('float')
    dictData['meanTest'] = matRead('data/', 'meanTest').astype('float')

    dictData['vecTest'] = np.array([0.5, 0.7])
    dictData['mTest'] = np.array([1.8100, 1.9100])
    dictData['vEigenTest1'] = np.array([[0.6779], [0.7352]])
    dictData['vEigenTest2'] = np.array([[0.6779, -0.7352], [0.7352, 0.6779]])

    dictData['faceDetection'] = plt.imread('data/FaceDetection.bmp')/255.

    return dictData


if __name__ == "__main__":

    testData = load_data()

    print(testData['dataMat1'])
    print(testData['vEigenTest2'])

    plt.figure(1)
    plt.clf()
    imshowGray(testData['faceDetection'])
