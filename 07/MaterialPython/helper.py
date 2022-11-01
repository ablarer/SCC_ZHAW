# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 14:27:31 2021

@author: roor
"""

import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
from load_data import load_data, imshowGray


# supplied by the lecturer
def loadAndScaleImage(personId, expression):
    img = plt.imread(f'data/s{personId}/f{expression}.png')
    img = img.astype('float')
    return img


def displaySourceImages(nPerson, nExpression):
    img = loadAndScaleImage(1, 1)
    sizeX, sizeY = img.shape
    fullImage = np.zeros((sizeX*nExpression, sizeY*nPerson))

    for personId in range(nPerson):
        for expression in range(nExpression):
            img = loadAndScaleImage(personId+1, expression+1)
            fullImage[sizeX*expression:sizeX*(expression+1),
                      sizeY*personId:sizeY*(personId+1)] = img

    imshowGray(fullImage)
    plt.axis('off')
    return None


def displayCompressionResult(imgOriginal, imgComp):

    plt.subplot(1, 2, 1)
    imshowGray(imgOriginal)
    plt.axis('off')
    plt.subplot(1, 2, 2)
    imshowGray(imgComp)
    plt.axis('off')
    return None


# templates to be completed
def ssd(p, q):                               # ssd calculation
    return  # norm of (p-q)


def faceDetection(imgF, d, vEigen, imgM):    # face detection
    (nImageY, nImageX) = imgF.shape
    (nY, nX) = imgM.shape

    return  # return array of ssd-values


# remove tests for students version
if __name__ == "__main__":

    np.set_printoptions(precision=4)

    d = load_data()
    print(d['VTest'])

    # Task 5
    img = loadAndScaleImage(7, 2)
    plt.figure(1)
    plt.clf()
    imshowGray(img)
    plt.axis('off')
