import numpy as np

c = 1
L = 1

nmax = 40
xmin = 0
xmax = L
tmin = 0
tmax = 4

x = np.arange(xmin, xmax, 0.05)
nx = len(x)

t = np.arange(tmin, tmax, 0.01)
nt = len(t)

u = np.zeros((nx, nt))
a = np.zeros(nmax)
