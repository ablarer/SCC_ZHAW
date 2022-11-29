def Wave_PDE_Task1_8(xrange, trange, u_initial, du_initial, u0_boundary, uL_boundary, k):
    import numpy as np
    n = len(xrange)
    m = len(trange)
    u = np.zeros((n, m))

    delta_x = (xrange[-1] - xrange[0]) / (n - 1)
    delta_t = (trange[-1] - trange[0]) / (m - 1)

    u[:, 0] = u_initial
    u[:, 1] = du_initial
    u[0, :] = u0_boundary
    u[-1, :] = uL_boundary
    alpha = k * delta_t / delta_x

    if alpha ** 2 < 1.0:
        Exception('Stability requires alpha < 0.5')

    for j in np.arange(0, m - 1):
        for i in np.arange(1, n - 1):
            if (j==2):
                u[i, j] = ((alpha ** 2)/2 * (u[i - 1, 1] + u[i + 1, 1]) + ((1- (alpha ** 2)) * (u[i,1])) + (delta_t * du_initial[i]))
            u[i, j+1] = (alpha ** 2 * (u[i - 1, j] + u[i + 1, j])) + (2 * (1 - (alpha ** 2)) * u[i, j]) - u[i, j - 1]

    return u