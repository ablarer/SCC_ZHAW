from Wave_PDE_Task1_8 import Wave_PDE_Task1_8
from matplotlib import cm, pyplot as plt, animation
import numpy as np


# Use >>> python3 Task_1_8c.py <<< for a "movie show".
k = 1
L = 1

xmin = 0
xmax = L
tmin = 0
tmax = 4

xrange = np.arange(xmin, xmax + 0.1, 0.1)
nx = len(xrange)
trange = np.arange(tmin, tmax + 0.01, 0.01)
nt = len(trange)

def f(x): return 4. * (x / L) * (1. - x / L)


u_initial = f(xrange)
du_initial = np.ones(u_initial.shape) * 0.2
u0_boundary = np.zeros(nt) # u(0, t) = u(1, t) = 0
uL_boundary = np.zeros(nt) # u(0, t) = u(1, t) = 0

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

x, t = np.meshgrid(xrange, trange)

# Set the z axis limits so they aren't recalculated each frame.
ax.set_zlim(-0.2, 0.2)

# Begin plotting.
wframe = None

u = Wave_PDE_Task1_8(xrange, trange, u_initial, du_initial, u0_boundary, uL_boundary, k)

print(u.T.shape)
print(u.T[2])

for phi in np.linspace(0, 180. / np.pi, 100):
    # If a line collection is already remove it before drawing.
    if wframe:
        wframe.remove()
    # Generate data
    u = Wave_PDE_Task1_8(xrange, trange, u_initial, du_initial, u0_boundary, uL_boundary, k)
    # Plot the new wireframe and pause briefly before continuing.
    wframe = ax.plot_wireframe(x, t, u.T/10 *np.sin(phi), rstride=2, cstride=2)
    plt.pause(0.1)

