"""
This script does the following:
1) calls the function calculate_border_task1.m
2) calculates the centroid (center of mass) and bounding box
   with cv2.moments() and cv2.boundingRect()
3) shows the cropped RGB picture with the centroid and the bounding box

Created on Mon Nov  8 18:26:54 2021
@author: knaa
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

from calculate_border_task1 import calculate_border_task1

# Define path
# os.chdir('C:\\Users\\knaa\\Documents\\01-Sync\\SCC\\Ressources\\02_Skin_Cancer_Detection\\Assignement\\Solutions')
path = '.'
img = 'B496a.png'
# img ='IMG_4106.jpg'
path_img = path + '/' + img
print('Processed Picture: ', img)

# Step 1: Read Image and calculate border of lesion
#         by calling calculate_border_task1.m

# 10% is cut away from each side of the image, then the image is blurred using
# a Gaussian filter with sigma 10. Then the contour is of the lesion is
# calculated. Output is the cropped color image, the cropped grey scale
# image and the borders of the contour.

cropped_img_cl, cropped_img_gs, cropped_img_mask, border = calculate_border_task1(path_img, 0.1, 10)

# Step 2: Calculate the centroid (center of mass) and bounding box
# using cv2.moments() and cv2.boundingRect(), see online help for details

IGA = np.copy(cropped_img_cl)

# loop over the contours
for c in border:
    M = cv2.moments(c)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX, CY = 0, 0
    x, y, w, h = cv2.boundingRect(c)

# Step 3: show the cropped RGB picture with the centroid and the bounding box.
# Use cv2.rectangle() to plot the bounding box, cv2.drawContours() for the 
# contours, cv2.circle() for the centroid 

""" ... YOUR CODE COMES HERE ... """

cv2.rectangle(IGA, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.drawContours(IGA, border, -1, (255, 255, 0), 4)
cv2.circle(IGA, (cX, cY), 5, (255, 255, 255), -1)
# The following commands do not work ... why?
plt.imshow(IGA)
plt.show()
