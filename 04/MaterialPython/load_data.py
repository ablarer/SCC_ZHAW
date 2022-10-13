# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 14:27:31 2021

@author: roor
"""

import numpy as np
import scipy.io


def csvRead(file):
    return np.loadtxt(file, delimiter=',')


def matRead(name):
    data = scipy.io.loadmat(name+'.mat')[name]
    if data.shape[1] == 1:
        data = data[:, 0]
    if data.shape[0] == 1:
        data = data[0, :]
    return data


def stringRead(name):
    with open(name+'.txt') as hFile:
        lines = hFile.readlines()
    return np.array(lines)


# ----------------------------------------------------------------------------
# Reading MATLAB based data files
# ----------------------------------------------------------------------------
def loadData():
    dict = {}

    dict['tokenArray'] = stringRead('tokenArray')

    dict['testLabels'] = matRead('testLabels').astype(int)
    dict['testMatrix'] = matRead('testMatrix').astype(int)
    dict['trainLabels'] = matRead('trainLabels').astype(int)
    dict['trainMatrix'] = matRead('trainMatrix').astype(int)

    dict['testLabelsEx1'] = matRead('testLabels'+'Ex1').astype(int)
    dict['testMatrixEx1'] = matRead('testMatrix'+'Ex1').astype(int)
    dict['trainLabelsEx1'] = matRead('trainLabels'+'Ex1').astype(int)
    dict['trainMatrixEx1'] = matRead('trainMatrix'+'Ex1').astype(int)

    dict['testLabelsEx2'] = matRead('testLabels'+'Ex2').astype(int)
    dict['testMatrixEx2'] = matRead('testMatrix'+'Ex2').astype(int)
    dict['trainLabelsEx2'] = matRead('trainLabels'+'Ex2').astype(int)
    dict['trainMatrixEx2'] = matRead('trainMatrix'+'Ex2').astype(int)

    dict['testLabelsEx3'] = matRead('testLabels'+'Ex3').astype(int)
    dict['testMatrixEx3'] = matRead('testMatrix'+'Ex3').astype(int)
    dict['trainLabelsEx3'] = matRead('trainLabels'+'Ex3').astype(int)
    dict['trainMatrixEx3'] = matRead('trainMatrix'+'Ex3').astype(int)

    dict['probNonSpamEx3'] = matRead('probNonSpam'+'Ex3')
    dict['probSpamEx3'] = matRead('probSpam'+'Ex3')

    return dict
