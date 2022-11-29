from Wave_PDE_Task1_8 import Wave_PDE_Task1_8
import matplotlib.pyplot as pit
from matplotlib import cm, pyplot as plt
import numpy as np

k = 1
L = 1

xmin = 0
xmax = L
tmin = 0
tmax = 9

xrange = np.arange(xmin, xmax + 0.1, 0.1)
nx = len(xrange)
trange = np.arange(tmin, tmax + 0.01, 0.01)
nt = len(trange)


def f(x): return 4. * (x / L) * (1. - x / L)


u_initial = f(xrange)
du_initial = np.ones(u_initial.shape) * 0.2
u0_boundary = np.zeros(nt)
uL_boundary = np.zeros(nt)

u = Wave_PDE_Task1_8(xrange, trange, u_initial, du_initial, u0_boundary, uL_boundary, k)

x, t = np.meshgrid(xrange, trange)
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
surf = ax.plot_surface(x, t, u.T, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.xlabel('x')
plt.ylabel('t')
plt.title('Task 1.8 a) Wave equation in 1D - Numerical Solution')
plt.show()

