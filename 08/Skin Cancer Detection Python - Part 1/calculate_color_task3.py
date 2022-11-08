def calculate_color_task3(cropped_img_cl, cropped_img_mask, color_table, threshold, plot_image):
    """
     This function does the following:
     1) Write the BGR channels of the cropped colour image into separate
        matrices
     2) For each pixel inside the lesion, the euclidian distance to the
        defined colors in color_table is calculated. The minimum distance decides,
        which color the pixel is attributed to
     3) For each color that is present in a certain percentage of all the
        inside pixels (as defined by threshold), the color score is increased by 1
     4) Calculate the euclidian distance between the average pixel inside and
        outside the lesion and write result in average_color_diff
     5) Calculate the variance in B,G,R and write into the vector variance
     6) Plot histograms if required
    
     Input :  cropped_img_cl    : cropped color image as calculated by 
                                  calculate_border.m
              cropped_img_mask  : mask of lesion as calculated by 
                                  calculate_border.m   
              color_table       : (n,3) array of n colors, defined by its RGB colors (see example below)
              threshold         : between 0 and 1, defines the percentage of
                                  pixels that need to be present for each color
                                  to get a point
              plot_image        : 0: no plots are generated
                                  1: plots are generated
     Output : color score       : value between 0 to n (each color present receives
                                  one point)
              count             : percentage of pixels  for each color present
                                : in color_table
              average_color_diff: euclidian distance between the average pixel inside and
                                  outside the lesion
              variance          : (3,1) vector with the variances in R,G,B
     Remarks: The results for the color score differ strongly, if the values
              for the reference colors are changed. It would be necessary to look into
              this more closely and also come up with additional measures, for instance
              the euclidian distance betwenn the average pixel inside the lesion and
              outside the lesion.
     Example: 
     color_table = np.empty([6,3])      # this color table defines the specific colors relevant for the color score in RGB!
     color_table[0,:] = [255, 255, 255] # white
     color_table[1,:] = [204, 51, 51]   # red
     color_table[2,:] = [153, 102, 0]   # light brown
     color_table[3,:] = [51, 0, 0]      # dark brown
     color_table[4,:] = [51, 153, 255]  # blue gray
     color_table[5,:] = [0, 0, 0]       # black
     color_threshold = 0.01
     plot_image = 1
     color_score, count, average_color_diff,variance = calculate_color_task3(cropped_img_cl,cropped_img_mask,color_table,color_threshold,plot_image);
     Date: October,23, 2016; knaa
    """
    import numpy as np
    import matplotlib.pyplot as plt

    # 1) Extract BGR color channels and flatten them (makes it easier)
    B = cropped_img_cl[:, :, 0].astype(np.float64).flatten()
    G = cropped_img_cl[:, :, 1].astype(np.float64).flatten()
    R = cropped_img_cl[:, :, 2].astype(np.float64).flatten()

    # 2) Calculate euclidian distance (using np.linalg.norm())) from the defined colors for each pixel
    #    inside the lesion and count the closest pixels. Don't forget to turn the arrays R[inside[i]] etc.
    #    into float(R[inside[i]]) etc., otherwise np.linalg.norm() will give wrong results

    inside = np.argwhere(cropped_img_mask.flatten() == 255)
    outside = np.argwhere(cropped_img_mask.flatten() != 255)
    num_pix_in = np.shape(inside)[0]
    num_color = np.shape(color_table)[0]
    eucl_diff = np.empty([num_color, 1])
    count = np.zeros([num_color, 1])

    for i in np.arange(0, num_pix_in):
        for j in np.arange(0, num_color):
            """ ... YOUR CODE COMES HERE ... """
            eucl_diff[j] = np.linalg.norm(
                [float(R[inside[i]]), float(R[inside[i]]), float(R[inside[i]])] - color_table[j, :])
            ind_min = np.argmin(eucl_diff)
            count[ind_min] = count[ind_min] + 1

    # 3) For each color, that is represented in more than the percantage of
    #    the pixels (defined by threshold), a point is given for the color score

    """ ... YOUR CODE COMES HERE ... """
    count = count / num_pix_in
    occurence = count >= threshold
    color_score = np.sum(occurence)

    # 4) Calculate the euclidian distance between the average pixel inside and
    #    outside the lesion

    average_inside = [np.mean(R[inside]), np.mean(G[inside]), np.mean(B[inside])]
    average_outside = [np.mean(R[outside]), np.mean(G[outside]), np.mean(B[outside])]
    average_color_diff = np.linalg.norm(np.array(average_inside) - np.array(average_outside))

    # 5) Calculate the variance of the R,G,B channels inside the lesion using np.var()

    """ ... YOUR CODE COMES HERE ... """
    variance = [np.var(R[inside]), np.var(G[inside]),np.var(B[inside])]

    # 6) Do plots if plot_image is set to 1
    if plot_image:
        plt.figure(10)
        plt.subplot(221), plt.imshow(cropped_img_cl[:, :, 0], cmap='Blues'), plt.axis('off'), plt.colorbar(), plt.title(
            'Blue Channel')
        plt.subplot(222), plt.hist(B, bins=50), plt.title('Histogram All')
        plt.subplot(223), plt.hist(B[inside], bins=50), plt.title('Histogram Inside')
        plt.subplot(224), plt.hist(B[outside], bins=50), plt.title('Histogram Outside')

        plt.figure(11)
        plt.subplot(221), plt.imshow(cropped_img_cl[:, :, 1], cmap='Greens'), plt.axis(
            'off'), plt.colorbar(), plt.title('Green Channel')
        plt.subplot(222), plt.hist(G, bins=50), plt.title('Histogram All')
        plt.subplot(223), plt.hist(G[inside], bins=50), plt.title('Histogram Inside')
        plt.subplot(224), plt.hist(G[outside], bins=50), plt.title('Histogram Outside')

        plt.figure(12)
        plt.subplot(221), plt.imshow(cropped_img_cl[:, :, 1], cmap='Reds'), plt.axis('off'), plt.colorbar(), plt.title(
            'Red Channel')
        plt.subplot(222), plt.hist(R, bins=50), plt.title('Histogram All')
        plt.subplot(223), plt.hist(R[inside], bins=50), plt.title('Histogram Inside')
        plt.subplot(224), plt.hist(R[outside], bins=50), plt.title('Histogram Outside')
        plt.show()

    # 7) Return values

    return color_score, count, average_color_diff, variance
