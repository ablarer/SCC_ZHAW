"""
% This script does the following:
% 1) Define the path to the test image(s) 
% 2) Defines the input parameters for the sub-functions to be called
% 3) Define arrays for the asymmetry and colour score for nevi and melanoma
% 4) Runs a parfor (see MATLAB Parallel Computing Toolbox) loop,
%    calling the subfunctions calculate_border.m, calculate_polar_coordinates.m,
%    calculate_asymmetry.m,calculate_color.m. 
%    (optional: these subfunctions can be summarized in asubfunction calculate_all.m)
%
% Date: November, 2, 2017; RK
"""

import numpy as np
import os
import cv2
from calculate_border_task1 import calculate_border_task1
from calculate_color_task3 import calculate_color_task3
from calculate_polar_coordinates_task4 import calculate_polar_coordinates_task4
from calculate_asymmetry_task4 import calculate_asymmetry_task4

# 1) Define paths
# os.chdir('C:\\Users\\knaa\\Documents\\01-Sync\\SCC\\Ressources\\02_Skin_Cancer_Detection\\Assignement\\Solutions')
path = 'Skin Cancer Detection Python - Part 1'
img ='B496a.png'
# img ='IMG_4106.jpg'
path_img = path+'/'+img
print('Processed Picture: ',img)

# 2) Defines the input parameters for the sub-functions to be called
crop_factor_nevi = 0.01        # 1% of the edges of nevi images is cut away
crop_factor_melanoma1 = 0.1    # 10% of the edges of nevi images is cut away
sigma = 5                      # sigma for imgaussfilt.m 
rel_diff = 0.1                 # the relative difference between radii to increase the SFA index for the asymmetry calculation
sfa_thresh = 140               # SFA index value used for the asymmetry score 
color_threshold = 0.01         # trheshold for the color calculation
plot_image = 1                 # if set to 1, plots are generated

color_table = np.empty([6,3])      # this color table defines the specific colors relevant for the color score in RGB!
color_table[0,:] = [255, 255, 255] # white
color_table[1,:] = [204, 51, 51]   # red
color_table[2,:] = [153, 102, 0]   # light brown
color_table[3,:] = [51, 0, 0]      # dark brown
color_table[4,:] = [51, 153, 255]  # blue gray
color_table[5,:] = [0, 0, 0]       # black

# 3) Define arrays for the SFA index, asymmetry score, colour score
#    and variance in RGB for nevi and melanoma

num_pic_nevi = 10
#num_pic_nevi = length(NEVI);
sfa_all_nevi=np.empty(num_pic_nevi)
asymmetry_all_nevi=np.empty(num_pic_nevi)
color_score_all_nevi=np.empty(num_pic_nevi)
variance_all_nevi=np.empty((num_pic_nevi, 3))

num_pic_melanoma1 = 10
#num_pic_melanoma1 = len(MELANOMA1)
sfa_all_melanoma1=np.empty(num_pic_melanoma1)
asymmetry_all_melanoma1=np.empty(num_pic_melanoma1)
color_score_all_melanoma1=np.empty(num_pic_melanoma1)
variance_all_melanoma1=np.empty((num_pic_melanoma1, 3))

# 4) Runs a loop,
#    calling the subfunctions calculate_border_task1.m, calculate_polar_coordinates(),
#    calculate_color_task3(), calculate_polar_coordinates_task4(),calculate_asymmetry_task4()
#    The results are written to the arrays sfa_all_nevi,
#    asymmetry_all_nevi, color_score_all_nevi, variance_all_nevi.


for k in np.arange(0,1):    
    # Read Image and calculate border of lesion
    cropped_img_cl,cropped_img_gs,cropped_img_mask,border = calculate_border_task1(path_img, crop_factor_melanoma1, sigma)
    
    #Calculate the centroid (center of mass) and bounding box    
    for c in border:
        M = cv2.moments(c)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        else:
            cX, cY = 0, 0

    #Calculate the color score and the variance of all the pixels inside the lesion in the R,G,B channels
    color_score, count, average_color_diff,variance = calculate_color_task3(cropped_img_cl,cropped_img_mask,color_table,color_threshold,plot_image)

    #Calculate polar coordinates (radii and angles), sort in ascending order
    r, alpha, r_sort, alpha_sort, alpha_index, r_bin, alpha_bin = calculate_polar_coordinates_task4(cX,cY,border)
    
    #Calculate asymmetry score and the sum of the SFA index divided by its length (360)
    sfa,sfa_major_axis,ind_major_axis,sfa_minor_axis,ind_minor_axis,asymmetry = calculate_asymmetry_task4(r_bin,rel_diff, sfa_thresh)

    #Display results
    print('asymmetry score: ',asymmetry)
    print('color score: ',color_score)
    print('variance: ',variance[0],variance[1],variance[2])

    #Write results into arrays (sfa is summed up and devided by its length 360)
    sfa_all_melanoma1[k]=np.sum(sfa)/len(sfa)
    asymmetry_all_melanoma1[k]=asymmetry
    color_score_all_melanoma1[k]=color_score
    variance_all_melanoma1[k,:]=variance




