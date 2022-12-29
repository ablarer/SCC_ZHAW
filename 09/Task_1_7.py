import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

from Heat_PDE_Task1_7 import Heat_PDE_Task1_7

# 1.7a
k = 1
L = 1

xmin = 0
xmax = L
tmin = 0
tmax = 0.25

xrange = np.arange(xmin, xmax + 0.1, 0.1)
nx = len(xrange)
trange = np.arange(tmin, tmax + 0.005, 0.005)
nt = len(trange)


def f(x): return 4. * (x / L) * (1. - x / L)


u_initial = f(xrange)
u0_boundary = np.zeros(nt)
uL_boundary = np.zeros(nt)

u = Heat_PDE_Task1_7(xrange, trange, u_initial, u0_boundary, uL_boundary, k)

x, t = np.meshgrid(xrange, trange)
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
surf = ax.plot_surface(x, t, u.T, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.xlabel('x')
plt.ylabel('t')
plt.title('Task 1.7 a) Heat Conduction - Numerical Solution')
plt.show()

# 1.7b
k = 1
L = 2

xmin = 0
xmax = L
tmin = 0
tmax = 1.5

xrange = np.arange(xmin, xmax + 0.1, 0.1)
nx = len(xrange)

trange = np.arange(tmin, tmax + 0.005, 0.005)
nt = len(trange)


def f(x): return np.zeros((1, nx))


u_initial = f(xrange)
u0_boundary = np.exp(-2 * trange) * np.sin(50 * trange)
uL_boundary = np.exp(-3 * trange) * np.cos(50 * trange)

u = Heat_PDE_Task1_7(xrange, trange, u_initial, u0_boundary, uL_boundary, k)

x, t = np.meshgrid(xrange, trange)
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
surf = ax.plot_surface(x, t, u.T, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.xlabel('x')
plt.ylabel('t')
plt.title('Task 1.7 b) Heat Conduction - Numerical Solution')
plt.show()
