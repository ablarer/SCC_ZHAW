def calculate_polar_coordinates_task4(x_center, y_center, border):

    """
    This function does the following:
    1) calculates polar coordinates (i.e. radius r, angle alpha) of the 
       boundaries of an area with the centroid defined by (x_center,y_center)
       and the border defined by an array of cartesian x and y coordinates
    2) sorts the polar coordinates in ascending order with respect to alpha
    3) averages the radii over bins of 1 deg in alpha (i.e. 360 bins)
      Input : x_center         : x coordinate of centroid (center of mass)
              y_center         : y coordinate of centroid (center of mass)
              border           : array of size (n,2) with x and y coordinates
                                 of the border in its columns
     Output : r                : vector of size (n,1) containing the radii 
              alpha            : vector of size (n,1) containing the angles
              r_sort           : sorted r with respect to increasing angles
                                 alpha
              alpha_sort       : vector with sorted angles in increasng order
              alpha_index      : vector with index of alpha_sort in the 
                                 unsorted vecotr alpha 
              r_bin            : vector of size (1, 360) containing the
                                 averaged radii over angle bins of 1 deg
              alpha_bin        : vector of size (1, 360) containing the
                                 angle bins of 1 deg in radians, ranging from
                                 -pi to pi
    Remarks: Since images are read as a matrix with the first pixel having
             the coordinates (1,1) in the upper left corner (i.e. row index 
             appears on the y axis, column index on the x axis), coordinates x
             and y in the border do not have to be swapped 
    Example: r, alpha, r_sort, alpha_sort, alpha_index, r_bin, alpha_bin = calculate_polar_coordinates(xc, yc, b)
    Date: November, 12, 2021, knaa
    """

    import numpy as np

# 1) Calculate polar coordinates
    border = np.array(border)
    border = border.reshape(np.shape(border)[1],2)
    r = np.sqrt((border[:,0]-x_center)**2 + (border[:,1]-y_center)**2)
    alpha = np.arctan2(border[:,1]-y_center,border[:,0]-x_center)   
    
# 2) Sort angles in ascending order, sort radii accordingly
    alpha_sort=np.sort(alpha)
    alpha_index=np.argsort(alpha)
    r_sort=r[alpha_index]

# 3) Average the radii in bins of 1 degree in radians
    stepsize=np.pi/180.
    theta = np.arange(-np.pi,np.pi+stepsize,stepsize)
    n = len(theta)-1
    r_bin=np.zeros(n)
    alpha_bin=np.zeros(n)

    for i in np.arange(0,n):
        ind_left = np.argwhere(theta[i] <= alpha_sort) 
        ind_right = np.argwhere(alpha_sort <= theta[i+1])
        ind = np.intersect1d(ind_left,ind_right)
        r_bin[i] = np.mean(r_sort[ind])
        alpha_bin[i] = theta[i]

    return r, alpha, r_sort, alpha_sort, alpha_index, r_bin, alpha_bin