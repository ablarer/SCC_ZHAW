"""
 This script does the following:
 1) Define the path to the images of melanocytic nevi and melanoma
 2) Defines the input parameters for the sub-functions to be called
 3) Define cell array with file names of melanocytic nevi, and remove
    those images for which the image segmentation does not work
 4) Define cell array with file names of melanoma, and remove
    those images for which the image segmentation does not work
 5) Define arrays for the asymmetry and colour score for nevi and melanoma
 6) Runs a loop for nevi,
    calling the subfunctions calculate_border.m, calculate_polar_coordinates.m,
    calculate_asymmetry.m,calculate_color.m. 
    (optional: these subfunctions can be summarized in asubfunction calculate_all.m)
 7) Runs a loop for melanoma,
    calling the subfunctions calculate_border.m, calculate_polar_coordinates.m,
    calculate_asymmetry.m,calculate_color.m. 
    (optional: these subfunctions can be summarized in asubfunction calculate_all.m)
 8) Plots the histograms of the asymmetry score, color score, and variance
    for the nevi and the melanoma
 9) Creates a training and a target vector for analysis with neural networks,
    keep only as many nevi as melanoma. Use the surplus nevi as an
    additional validation set
10) Create a similar training and a target vector for analysis with SVM (only required for Matlab)
11) Use scikit-learn for classification (call calculate_classifiers_task6_solution.py) 

 Date: November, 16, 2022, knaa
"""""

import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

# os.chdir('./Solutions')

from calculate_border_task1_solution import calculate_border_task1_solution
from calculate_color_task3_solution import calculate_color_task3_solution
from calculate_polar_coordinates_task4 import calculate_polar_coordinates_task4
from calculate_asymmetry_task4_solution import calculate_asymmetry_task4_solution

# 1) Define paths
path_nevi = 'Images Nevi/Melanocytic_Nevus(mole)_Images'
path_melanoma = 'Images Melanoma/Malignant_Melanoma_Images'

# 2) Defines the input parameters for the sub-functions to be called
crop_factor_nevi = 0.01         # 1% of the edges of nevi images is cut away
crop_factor_melanoma = 0.1     # 10% of the edges of nevi images is cut away
sigma = 5                      # sigma for imgaussfilt.m
rel_diff = 0.1                 # the relative difference between radii to increase the SFA index for the asymmetry calculation
sfa_thresh = 140               # SFA index value used for the asymmetry score
color_threshold = 0.01         # trheshold for the color calculation
plot_image = 0                 # if set to 1, plots are generated

color_table = np.empty([6,3])      # this color table defines the specific colors relevant for the color score in RGB!
color_table[0,:] = [255, 255, 255] # white
color_table[1,:] = [204, 51, 51]   # red
color_table[2,:] = [153, 102, 0]   # light brown
color_table[3,:] = [51, 0, 0]      # dark brown
color_table[4,:] = [51, 153, 255]  # blue gray
color_table[5,:] = [0, 0, 0]       # black

# 3) Define cell array with file names of melanocytic nevi, and remove
#    those images for which the image segmentation does not work
NEVI_all = ['A102a.png', 'A112b.png', 'A121a.png','A121c.png','A123.png','A21b.png',
       'A25b.png',	'A27.png','A2b.png','A7g.png','A8a.png','A8b.png',
        'A8c.png',	'A8d.png','A8e.png','A90.png','A91b.png','A97.png',
        'B102a.png','B102d.png','B122.png','B124.png','B125c.png','B13.png',
        'B139.png',	'B145b.png','B152b.png','B152c.png','B157.png','B169a.png',
        'B17a.png',	'B17b.png',	'B17c.png',	'B17f.png','B183.png','B197c.png',
        'B197d.png','B202b.png','B237.png',	'B24.png','B247b.png','B275a.png',
        'B275b.png','B277.png',	'B288.png',	'B292.png','B293b.png','B293d.png',
        'B293e.png','B311c.png','B315.png',	'B328b.png','B336b.png','B339a.png',
        'B339b.png','B350a.png','B350b.png','B350c.png','B350d.png','B354b.png',
        'B355a.png','B355b.png','B355c.png','B356.png','B357.png','B359.png',
        'B361a.png','B371.png',	'B379a.png','B379b.png','B402b.png','B429b.png',
        'B444.png','B447a.png',	'B447b.png','B454b.png','B457a.png','B468.png',
        'B471.png',	'B472b.png','B477a.png','B485.png',	'B489.png',	'B508.png',
        'B513a.png','B522b.png','B52a.png',	'B52b.png',	'B52c.png',	'B543.png',
        'B549c.png','B554c.png','B561.png',	'B564.png',	'B567.png',	'B569a.png',
        'B574.png',	'B578.png',	'B580.png',	'B585.png',	'B591a.png','B591b.png',
        'B598a.png','B598c.png','B607.png',	'B610b.png','B610c.png','B612b.png',
        'B654a.png','B654c.png','B669b.png','B66c.png',	'B672b.png','B676a.png',
        'B676b.png','B69a.png',	'B69b.png',	'B706a.png','B721a.png','B721b.png',
        'B721c.png','B774a.png','B89c.png',	'B89e.png',	'B91a.png',	'B91b.png',
        'B91c.png',	'B98.png',	'D105.png',	'D107.png',	'D112.png',	'D124.png',
        'D133b.png','D144.png',	'D155b.png','D169a.png','D169b.png','D176b.png',
        'D193a.png','D209.png',	'D226b.png','D226c.png','D227.png',	'D239a.png',
        'D239b.png','D244.png',	'D249b.png','D262a.png','D262b.png','D271a.png',
        'D284a.png','D284b.png','D291a.png','D291b.png','D324.png',	'D339.png',
        'D340b.png','D354b.png','D374.png',	'D384.png',	'D385.png',	'D386.png',
        'D395.png',	'D401.png',	'D404.png',	'D412a.png','D419.png',	'D426.png',
        'D427a.png','D427b.png','D463.png',	'D492.png',	'D526a.png','D526b.png',
        'D561.png',	'D564.png',	'D567a.png','D567b.png','D572.png',	'D596.png',
        'D604.png',	'D607.png',	'D626.png',	'D651.png',	'D671.png',	'D682a.png',
        'D684a.png','D684c.png','D686.png',	'D715.png',	'D720.png',	'D721.png',
        'D722.png',	'D723a.png','D724.png',	'D726a.png','D726b.png','D726c.png',
        'D726d.png','D726e.png','D732.png',	'P103a.png','P115.png',	'P125.png',
        'P126b.png','P130a.png','P144.png',	'P174.png',	'P177a.png','P179a.png',
        'P18.png',	'P180a.png','P180b.png','P196.png',	'P199.png',	'P2.png',
        'P20.png',	'P209a.png','P237a.png','P237b.png','P238.png',	'P249a.png',
        'P256a.png','P256b.png','P257.png',	'P265a.png','P271d.png','P271e.png',
        'P271f.png','P273c.png','P273d.png','P273e.png','P275a.png','P275b.png',
        'P275d.png','P275e.png','P277a.png','P277b.png','P291.png',	'P29b.png',
        'P304a.png','P304c.png','P306a.png','P306b.png','P306c.png','P306f.png',
        'P30a.png',	'P30b.png',	'P337a.png','P337b.png','P337c.png','P337d.png',
        'P337e.png','P337f.png','P341a.png','P342.png',	'P347b.png','P347c.png',
        'P354a.png','P354b.png','P359b.png','P363a.png','P365d.png','P365e.png',
        'P365f.png','P367a.png','P367e.png','P373a.png','P373c.png','P376a.png',
        'P376b.png','P376d.png','P382a.png','P382b.png','P384a.png','P384b.png',
        'P384c.png','P392.png',	'P399.png',	'P404a.png','P404b.png','P404c.png',
        'P404d.png','P407a.png','P407b.png','P407c.png','P407d.png','P407e.png',
        'P417.png',	'P432.png',	'P435a.png','P435b.png','P436.png',	'P454a.png',
        'P454b.png','P454c.png','P454d.png','P454f.png','P45a.png',	'P45b.png',
        'P45c.png',	'P472.png',	'P475.png',	'P477.png',	'P487c.png','P487d.png',
        'P489.png',	'P49.png',	'P4a.png',	'P4b.png',	'P502.png',	'P505a.png',
        'P505b.png','P505c.png','P505e.png','P509c.png','P53b.png',	'P54.png',
        'P55.png',	'P56b.png',	'P57.png',	'P58.png',	'P63.png',	'P67a.png',
        'P75a.png',	'P75b.png',	'P79.png',	'P81b.png',	'P88b.png',	'P92.png',
        'P97b.png']

# for these nevi, the image segmentation does not work
NEVI_problematic = ['A25b.png', 'B237.png', 'B24.png', 'B315.png', 'B564.png', 'B774a.png',
                'D155b.png', 'D291a.png', 'D291b.png', 'D567a.png', 'D567b.png', 'D572.png',
                'D607.png', 'D671.png', 'P180a.png', 'P399.png', 'P4a.png',
                'P67a.png', 'P75b.png', 'P81b.png']

# create an array NEVI only with pictures for which the segmentation works;

NEVI = NEVI_all
for dum in NEVI_problematic:
    NEVI.remove(dum)

## 4) Define cell array with file names of melanoma, and remove
#     those images for which the image segmentation does not work

MELANOMA_all = ['A92.png', 'A96.png', 'B1052.png', 'B1067.png', 'B1075.png', 'B1086a.png' ,
 'B1139.png', 'B1154.png', 'B241.png', 'B28.png',  'B284.png', 'B287.png', 'B289.png' ,
 'B302.png', 'B314.png', 'B353a.png', 'B40.png', 'B455.png', 'B472a.png', 'B496a.png' ,
 'B548.png', 'B621.png', 'B65.png', 'B759.png', 'B8.png', 'B960.png', 'B964.png',
 'B981.png', 'C11.png', 'C143.png', 'C145.png', 'C146.png', 'C149.png', 'C152.png' ,
 'C158.png', 'C159a.png', 'C161.png', 'C201.png', 'C227a.png', 'C227b.png', 'C263a.png',
 'C279.png', 'C309.png', 'C311b.png', 'C312.png', 'C350.png', 'C359.png', 'C367.png' ,
 'C377a.png',  'C382.png', 'C46.png', 'C76.png','D143.png', 'D177.png', 'D186.png' ,
 'D265b.png', 'D332.png', 'D39.png', 'D574c.png', 'D630.png', 'D678.png', 'D717.png' ,
 'D718.png', 'G55.png', 'P346.png', 'P352a.png', 'P352b.png', 'P413.png', 'P446.png' ,
 'P494.png', 'T201c.png', 'T233a.png', 'T33.png', 'T80a.png', 'T86b.png', 'T87.png']

# for these melanoma, the image segmentation does not work
MELANOMA_problematic = ['A96.png', 'B1067.png', 'B1154.png', 'B289.png', 'B621.png', 'C227b.png',
                'C312.png', 'C350.png', 'C377a.png', 'D265b.png', 'D332.png', 'G55.png',
                'P494.png']

# create an array MELANOMA only with pictures for which the segmentation works;
# for this to work, the 'bad' pictures in MELANOMA_problematic must appear in the same order as in
# the original array MELANOMA_all

MELANOMA = MELANOMA_all
for dum in MELANOMA_problematic:
    MELANOMA.remove(dum)


# 5) Define arrays for the SFA index, asymmetry score, colour score
#     and variance in RGB for nevi and melanoma
num_pic_nevi = len(NEVI)
sfa_all_nevi=np.empty(num_pic_nevi)
asymmetry_all_nevi=np.empty(num_pic_nevi)
color_score_all_nevi=np.empty(num_pic_nevi)
variance_all_nevi=np.empty((num_pic_nevi,3))

num_pic_melanoma = len(MELANOMA)
sfa_all_melanoma=np.empty(num_pic_melanoma)
asymmetry_all_melanoma=np.empty(num_pic_melanoma)
color_score_all_melanoma=np.empty(num_pic_melanoma)
variance_all_melanoma=np.empty((num_pic_melanoma, 3))

# 6) Runs a loop for all nevi,
#    calling the subfunctions calculate_border_task1.m, calculate_polar_coordinates(),
#    calculate_color_task3(), calculate_polar_coordinates_task4(),calculate_asymmetry_task4()
#    The results are written to the arrays sfa_all_nevi,
#    asymmetry_all_nevi, color_score_all_nevi, variance_all_nevi.


for k in np.arange(0,num_pic_nevi):
    img =NEVI[k]
    path_img = path_nevi+'/'+img
    print('Processed Picture:',img)

    # Read Image and calculate border of lesion
    [cropped_img_cl,cropped_img_gs,cropped_img_mask,border] = calculate_border_task1_solution(path_img, crop_factor_nevi, sigma)

    #Calculate the centroid (center of mass) and bounding box
    for c in border:
        M = cv2.moments(c)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        else:
            cX, cY = 0, 0

    #Calculate the color score and the variance of all the pixels inside the lesion in the R,G,B channels
    color_score, count, average_color_diff,variance = calculate_color_task3_solution(cropped_img_cl,cropped_img_mask,color_table,color_threshold,plot_image)

    #Calculate polar coordinates (radii and angles), sort in ascending order
    r, alpha, r_sort, alpha_sort, alpha_index, r_bin, alpha_bin = calculate_polar_coordinates_task4(cX,cY,border)

    #Calculate asymmetry score and the sum of the SFA index divided by its length (360)
    sfa,sfa_major_axis,ind_major_axis,sfa_minor_axis,ind_minor_axis,asymmetry = calculate_asymmetry_task4_solution(r_bin,rel_diff, sfa_thresh)

    #Display results
    print('asymmetry score: ',asymmetry)
    print('color score: ',color_score)
    print('variance: ',variance[0],variance[1],variance[2])

    #Write results into arrays (sfa is summed up and devided by its length 360)
    sfa_all_nevi[k]=np.sum(sfa)/len(sfa)
    asymmetry_all_nevi[k]=asymmetry
    color_score_all_nevi[k]=color_score
    variance_all_nevi[k,:]=variance



# 7) Runs a loop for all melanoma,
#    calling the subfunctions calculate_border_task1.m, calculate_polar_coordinates(),
#    calculate_color_task3(), calculate_polar_coordinates_task4(),calculate_asymmetry_task4()
#    The results are written to the arrays sfa_all_melanoma,
#    asymmetry_all_melanoma, color_score_all_melanoma, variance_all_melanoma.

for k in np.arange(0,num_pic_melanoma):
    img =MELANOMA[k]
    path_img = path_melanoma+'/'+img
    print('Processed Picture:',img)

    # Read Image and calculate border of lesion
    [cropped_img_cl,cropped_img_gs,cropped_img_mask,border] = calculate_border_task1_solution(path_img, crop_factor_nevi, sigma)

    #Calculate the centroid (center of mass) and bounding box
    for c in border:
        M = cv2.moments(c)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        else:
            cX, cY = 0, 0

    #Calculate the color score and the variance of all the pixels inside the lesion in the R,G,B channels
    color_score, count, average_color_diff,variance = calculate_color_task3_solution(cropped_img_cl,cropped_img_mask,color_table,color_threshold,plot_image)

    #Calculate polar coordinates (radii and angles), sort in ascending order
    r, alpha, r_sort, alpha_sort, alpha_index, r_bin, alpha_bin = calculate_polar_coordinates_task4(cX,cY,border)

    #Calculate asymmetry score and the sum of the SFA index divided by its length (360)
    sfa,sfa_major_axis,ind_major_axis,sfa_minor_axis,ind_minor_axis,asymmetry = calculate_asymmetry_task4_solution(r_bin,rel_diff, sfa_thresh)
    
    #Display results
    print('asymmetry score: ',asymmetry)
    print('color score: ',color_score)
    print('variance: ',variance[0],variance[1],variance[2])

    #Write results into arrays (sfa is summed up and devided by its length 360)
    sfa_all_melanoma[k]=np.sum(sfa)/len(sfa)
    asymmetry_all_melanoma[k]=asymmetry
    color_score_all_melanoma[k]=color_score
    variance_all_melanoma[k,:]=variance


# 8) Plot the histograms of the asymmetry score, color score, and variance
#    in RGB for the nevi and the melanoma
fig = plt.figure(20)
ax = fig.add_subplot(221)
ax.hist(color_score_all_nevi,bins=range(1,7),align='left')
ax.set_xticks(range(1,7))
ax.title.set_text('Hist. Color Score Nevi')
ax = fig.add_subplot(222)
ax.hist(color_score_all_melanoma,bins=range(1,7),align='left')
ax.set_xticks(range(1,7))
ax.title.set_text('Hist. Color Score Melanoma')
ax = fig.add_subplot(223)
ax.hist(asymmetry_all_nevi,bins=range(0,4),align='left')
ax.set_xticks(range(0,3))
ax.title.set_text('Hist. Asymmetry Score Nevi')
ax = fig.add_subplot(224)
ax.hist(asymmetry_all_melanoma,bins=range(0,4),align='left')
ax.set_xticks(range(0,3))
ax.title.set_text('Hist. Asymmetry Score Melanoma')
plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)

plt.show()

fig = plt.figure(21)
ax = fig.add_subplot(221)
ax.hist(variance_all_nevi[:,0],bins=np.arange(0,1600,200))
ax.set_xticks(np.arange(0,1600,400))
ax.title.set_text('Hist. Nevi Variance in R')
ax.grid('minor')
ax = fig.add_subplot(222)
ax.hist(variance_all_nevi[:,1],bins=np.arange(0,1600,200))
ax.set_xticks(np.arange(0,1600,400))
ax.title.set_text('Hist. Nevi Variance in G')
ax.grid('minor')
ax = fig.add_subplot(223)
ax.hist(variance_all_nevi[:,1],bins=np.arange(0,1600,200))
ax.set_xticks(np.arange(0,1600,400))
ax.title.set_text('Hist. Nevi Variance in B')
ax.grid('minor')
ax = fig.add_subplot(224)
ax.hist(np.sum(variance_all_nevi[:,:],axis=1),bins=np.arange(0,4500,300))
ax.set_xticks(np.arange(0,5000,1000))
ax.title.set_text('Hist. Nevi Sum Variance')
ax.grid('minor')
plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)
plt.show()

fig = plt.figure(22)
ax = fig.add_subplot(221)
ax.hist(variance_all_melanoma[:,0],bins=np.arange(0,1600,200))
ax.set_xticks(np.arange(0,1600,400))
ax.title.set_text('Hist. Melanoma Variance in R')
ax.grid('minor')
ax = fig.add_subplot(222)
ax.hist(variance_all_melanoma[:,1],bins=np.arange(0,1600,200))
ax.set_xticks(np.arange(0,1600,400))
ax.title.set_text('Hist. Melanoma Variance in G')
ax.grid('minor')
ax = fig.add_subplot(223)
ax.hist(variance_all_melanoma[:,1],bins=np.arange(0,1600,200))
ax.set_xticks(np.arange(0,1600,400))
ax.title.set_text('Hist. Melanoma Variance in B')
ax.grid('minor')
ax = fig.add_subplot(224)
ax.hist(np.sum(variance_all_melanoma[:,:],axis=1),bins=np.arange(0,4500,300))
ax.set_xticks(np.arange(0,5000,1000))
ax.title.set_text('Hist. Melanoma Sum Variance')
ax.grid('minor')
plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)

plt.show()

fig = plt.figure(23)
plt.plot(sfa_all_melanoma,np.sum(variance_all_melanoma[:,:],axis=1),'rx', 
     sfa_all_nevi,np.sum(variance_all_nevi[:,:],axis = 1),'bx')
plt.legend(['Melanoma','Nevi'])
plt.xlabel('SFA'),plt.ylabel('Sum of Variance'), plt.title('Nevi vs. Melanoma')

plt.show()

fig = plt.figure(24)
ax = plt.axes(projection='3d')
ax.scatter3D(variance_all_melanoma[:,0],variance_all_melanoma[:,1],variance_all_melanoma[:,2], 'ro',label='Melanoma')
ax.scatter3D(variance_all_nevi[:,0],variance_all_nevi[:,1],variance_all_nevi[:,2], 'gx',label='Nevi')
plt.legend()
plt.xlabel('R'),plt.ylabel('G'),ax.set_zlabel('B'), plt.title('Nevi vs. Melanoma'), plt.grid('minor')

plt.show()

fig = plt.figure(25)
plt.plot(np.sum(variance_all_melanoma[:,:],axis=1),variance_all_melanoma[:,0],'rx',np.sum(variance_all_nevi[:,:],axis=1),variance_all_nevi[:,0], 'bx')
plt.xlabel('Sum of Variance'),plt.ylabel('Variance in R'), plt.title('Nevi vs. Melanoma'), plt.grid('minor')
plt.legend(['Melanoma','Nevi'])

plt.show()

fig = plt.figure(26)
ax = plt.axes(projection='3d')
ax.scatter3D(np.sum(variance_all_melanoma[:,:],axis=1),variance_all_melanoma[:,0],sfa_all_melanoma, 'ro',label='Melanoma')
ax.scatter3D(np.sum(variance_all_nevi[:,:],axis=1),variance_all_nevi[:,0],sfa_all_nevi, 'ro',label='Nevi')
plt.legend()
plt.xlabel('Sum of Variance'),plt.ylabel('Variance in R'),ax.set_zlabel('SFA'), plt.title('Nevi vs. Melanoma'), plt.grid('minor')

plt.show()

# 9) Create a training and a target vector for analysis with neural networks,
#    keep only as many nevi as melanoma

# training data is an array with all the calculated quantities in one row per 
# image
nn_training_data = np.empty([2*num_pic_melanoma,6])
nn_training_data[:,0]=np.array([sfa_all_nevi[0:num_pic_melanoma],sfa_all_melanoma]).reshape(2*num_pic_melanoma)
nn_training_data[:,1]=np.array([asymmetry_all_nevi[0:num_pic_melanoma],asymmetry_all_melanoma]).reshape(2*num_pic_melanoma)
nn_training_data[:,2]=np.array([color_score_all_nevi[0:num_pic_melanoma],color_score_all_melanoma]).reshape(2*num_pic_melanoma)
nn_training_data[:,3:]=np.array([variance_all_nevi[0:num_pic_melanoma,:],variance_all_melanoma]).reshape(2*num_pic_melanoma,3)

# target_data[:,0] is 1 for nevi, target_data[:,1] is 1 for melanoma
nn_target_data=np.zeros([2*num_pic_melanoma,2])
nn_target_data[0:num_pic_melanoma, 0] = 1
nn_target_data[num_pic_melanoma:,1]= 1

# Use the surplus nevi as additional validation set
nn_add_validation_data = np.empty([num_pic_nevi-num_pic_melanoma,6])
nn_add_validation_data[:,0]=sfa_all_nevi[num_pic_melanoma:].reshape(num_pic_nevi-num_pic_melanoma)
nn_add_validation_data[:,1]=asymmetry_all_nevi[num_pic_melanoma:].reshape(num_pic_nevi-num_pic_melanoma)
nn_add_validation_data[:,2]=color_score_all_nevi[num_pic_melanoma:].reshape(num_pic_nevi-num_pic_melanoma)
nn_add_validation_data[:,3:]=variance_all_nevi[num_pic_melanoma:,:].reshape(num_pic_nevi-num_pic_melanoma,3)

# add_target_data:[:,0] is 1 for nevi 
nn_add_target_data=np.zeros([num_pic_nevi-num_pic_melanoma,2])
nn_add_target_data[:,0] = 1.

# 10) Create a similar training and a target vector for analysis with SVM and other classifiers (only required for Matlab)
# svm_training_data = np.empty([2*num_pic_melanoma,7])
# svm_training_data[:,0:6]=nn_training_data
# svm_training_data[:,6]=nn_target_data[:,1]

# svm_add_validation_data = np.empty([num_pic_nevi-num_pic_melanoma,7])
# svm_add_validation_data[:,0:6] = nn_add_validation_data
# svm_add_validation_data[:,6] = nn_add_target_data[:,0]

# 11) MATLAB provides a Classification Learner App (classificationLearner) for easy comparison 
# of multiple classifiers. In Python, unfortnately, each classifier has to be called separately.
# See for instance: https://scikit-learn.org/stable/ and https://stackabuse.com/overview-of-classification-methods-in-python-with-scikit-learn/

from calculate_classifiers_task6_solution import calculate_classifiers_task6_solution
calculate_classifiers_task6_solution(nn_training_data,nn_target_data,nn_add_validation_data,nn_add_target_data)