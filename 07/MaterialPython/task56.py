# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 09:55:40 2021

@author: roor
"""

import numpy as np
import matplotlib.pyplot as plt
import helper as hlp
from load_data import imshowGray, load_data

###########################################################################
# Globale Parameter
#
nPerson = 37           # #persons used (<=37)
nExpression = 10       # #expressions used per person (<=10)
nEVShown = 20          # #EV shown as image
nEVConsidered = 100    # #EV evaluated (maximal number to be used)

###########################################################################
# Loading of the pictures
#
plt.figure(1)
hlp.displaySourceImages(nPerson, nExpression)
plt.title(f'All images one matrix: {nPerson} persons, {nExpression}, expressions')
plt.show()

###########################################################################
# Parameter
#
nId = 30                # used number of persons (nId <= 37)
nExpr = 8               # used number of poses (nExpr <= 10)

nY, nX = hlp.loadAndScaleImage(1, 1).shape     # pixels in x- und y-direction

###########################################################################
# Saving of the faces as matrix rows and visualization
#
fullPicture = np.zeros((nExpr*nY, nId*nX))                    # gallery
imgSet = np.zeros((nId*nExpr, nY*nX))

for i in range(nId):
    for j in range(nExpr):
        k = i*nExpr + j
        img = hlp.loadAndScaleImage(i+1, j+1)                 # Face in
        fullPicture[j*nY:(j+1)*nY, i*nX:(i+1)*nX] = img       # gallery
        imgSet[k, :], dims = hlp.transformImageToVector(img)  # as vector

plt.figure(2)
# plt.clf()
imshowGray(fullPicture)
plt.title(f'Some images one matrix: {nId} persons, {nExpr}, expressions')
plt.axis('off')
plt.show()


###########################################################################
# Setup of compression algorithm
#
vecMean = hlp.getMean(imgSet)                           # mean image (vector)
imgMean = hlp.transformVectorToImage(vecMean, dims)     # mean image

plt.figure(3)                                           # Darstellung mean
plt.clf()
imshowGray(imgMean)
plt.title(f'One mean image of a face.')
plt.axis('off')
plt.show()

evMatrix = hlp.getEigenvectors(imgSet, nEVConsidered)   # eigen vector matrix

nEVShown = 20                                           # Anzahl EV im Bild
imgEV = np.zeros((nY, nX*nEVShown))
for i in range(nEVShown):
    imgVector = evMatrix[:, i]
    minV = np.min(imgVector)
    maxV = np.max(imgVector)
    imgVector = (imgVector-minV)/(maxV-minV)            # Umskalierung (Grafik)
    imgEV[:, nX*i:nX*(i+1)] = hlp.transformVectorToImage(imgVector, dims)

plt.figure(4)                                           # Darstellung EV
imshowGray(imgEV)
plt.title(f'Eigenvector images of on face.')
plt.axis('off')
plt.show()


###########################################################################
# Task 5 - Application I: Face Compression
#
# First use image *inside* training set, with different compression levels,
# e.g., 50, 20 and 10, respectively eigenvalues
# Then try an image that lies outside the training set
#

# inside training set
imgOrig = hlp.loadAndScaleImage(2, 4)

### your code
compressedImage = hlp.compressPCAImage(imgOrig, 50, evMatrix, imgMean)
imgComp1 = hlp.displayCompressionResult(imgOrig, compressedImage)
plt.figure(5)

compressedImage = hlp.compressPCAImage(imgOrig, 20, evMatrix, imgMean)
imgComp2 = hlp.displayCompressionResult(imgOrig, compressedImage)
plt.figure(6)

compressedImage = hlp.compressPCAImage(imgOrig, 10, evMatrix, imgMean)
imgComp3 = hlp.displayCompressionResult(imgOrig, compressedImage)
plt.figure(7)

plt.show()
### your code

# inside training set
imgOrig = hlp.loadAndScaleImage(31, 9)



###########################################################################
# Task 6 - Application II: Face Detection
#
data = load_data()
imgScene = data['faceDetection']

### your code