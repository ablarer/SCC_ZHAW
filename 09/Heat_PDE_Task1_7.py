def Heat_PDE_Task1_7(xrange, trange, u_initial, u0_boundary, uL_boundary, k):
    import numpy as np
    n = len(xrange)
    m = len(trange)
    u = np.zeros((n, m))

    delta_x = (xrange[-1] - xrange[0]) / (n - 1)
    delta_t = (trange[-1] - trange[0]) / (m - 1)

    u[:, 0] = u_initial
    u[0, :] = u0_boundary
    u[-1, :] = uL_boundary
    alpha = k * delta_t / delta_x ** 2

    if (alpha >= 0.5):
        Exception('Stability requires alpha < 0.5')

    for j in np.arange(0, m - 1):
        for i in np.arange(1, n - 1):
            u[i, j + 1] = u[i, j] + alpha * (u[i + 1, j] - 2 * u[i, j] + u[i - 1, j])
    return u
