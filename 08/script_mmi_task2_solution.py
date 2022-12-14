"""
This script does the following:
1) calls the function calculate_border_task1.m
2) calculates the centroid (center of mass) and bounding box
   with cv2.moments() and cv2.boundingRect()
3) shows the cropped RGB picture with the centroid and the bounding box

Created on Mon Nov  8 18:26:54 2021
@author: knaa
"""

import numpy as np
import os
import cv2
from calculate_border_task1_solution import calculate_border_task1_solution
import matplotlib.pyplot as plt

# Define path
os.chdir('C:\\Users\\knaa\\Documents\\01-Sync\\SCC\\Ressources\\02_Skin_Cancer_Detection\\Assignement\\Solutions')
path = '.'
img ='B496a.png'
#img='test3.jpg'
path_img = path+'\\'+img
print('Processed Picture: ',img)

    
# Step 1: Read Image and calculate border of lesion
#         by calling calculate_border_task1.m

# 10% is cut away from each side of the image, then the image is blurred using
# a Gaussian filter with sigma 10. Then the contour is of the lesion is
# calculated. Output is the cropped color image, the cropped grey scale
# image and the borders of the contour.

cropped_img_cl,cropped_img_gs,cropped_img_mask,border = calculate_border_task1_solution(path_img, 0.1, 5)
    
# Step 2: Calculate the centroid (center of mass) and bounding box
# using cv2.moments() and cv2.boundingRect(), see online help for details

IGA = np.copy(cropped_img_cl)

for c in border:
    M = cv2.moments(c)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX, cY = 0, 0
    x,y,w,h = cv2.boundingRect(c)

# Step 3: show the cropped RGB picture with the centroid and the bounding box.
# Use cv2.rectangle() to plot the bounding box, cv2.drawContours() for the 
# contours, cv2.circle() for the centroid 

cv2.rectangle(IGA,(x,y),(x+w,y+h),(0,255,0),2)
cv2.drawContours(IGA,border,-1,(255,255,0),4)
cv2.circle(IGA, (cX, cY), 5, (255, 255, 255), -1)

## The following commands do not work properly ... why?
#cv2.imshow('img',IGA)
#cv2.waitKey(1) 
#cv2.destroyAllWindows()

plt.figure(2)
plt.imshow(cv2.cvtColor(IGA,cv2.COLOR_BGR2RGB))

    
