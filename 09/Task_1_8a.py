from Wave_PDE_Task1_8 import Wave_PDE_Task1_8
from matplotlib import cm, pyplot as plt, animation
import numpy as np

c = 1
L = 1

xmin = 0
xmax = L
tmin = 0
tmax = 4

xrange = np.arange(xmin, xmax + 0.1, 0.1)
nx = len(xrange)
trange = np.arange(tmin, tmax + 0.01, 0.01)
nt = len(trange)

def f(x): return x * (1-x)


u_initial = f(xrange)
du_initial = np.ones(u_initial.shape) * 0.2 # du/dt(0,x) = 0.2
u0_boundary = np.zeros(nt) # u(0, t) = u(1, t) = 0
uL_boundary = np.zeros(nt) # u(0, t) = u(1, t) = 0

u = Wave_PDE_Task1_8(xrange, trange, u_initial, du_initial, u0_boundary, uL_boundary, c)

x, t = np.meshgrid(xrange, trange)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
# u.T divided by ten so that the range of u is the same as within task 1.6
surf = ax.plot_surface(x, t, u.T / 10, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.xlabel('x')
plt.ylabel('t')
plt.title('Task 1.8 a) Wave equation in 3D - Numerical Solution')
plt.show()