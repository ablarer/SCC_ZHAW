import matplotlib.pyplot as plt
from fontTools.merge import cmap
from matplotlib import cm
import numpy as np
import scipy.integrate as integrate

c = 1
L = 1

nmax = 40
xmin = 0
xmax = L
tmin = 0
tmax = 4

x = np.arange(xmin, xmax + 0.01, 0.05)
nx = len(x)

t = np.arange(tmin, tmax + 0.01, 0.01)
nt = len(t)

u = np.zeros((nx, nt))
a = np.zeros(nmax)
b = np.zeros(nmax)


#define functions (input can be vectors)
def f(xi): return (xi/L)*(1.-xi/L)
def g(xi): return (xi/L)**2.*(1.-xi/L)
def un(xi, an, bn, n, L, ti):
    return np.sin(n*np.pi*xi/L)*(an*np.cos(n*np.pi*c*ti/L)+bn*np.sin(n*np.pi*c*ti/L))

#calculate the first nmax coefficients an and bn
for ni in np.arange(1, nmax+1) :
    a[ni-1]=2.0/L*integrate.quad(lambda xi: f(xi)*np.sin(ni*np.pi*xi/L),0,L)[0]
    b[ni-1]=2.0/(ni*np.pi*c)*integrate.quad(lambda xi: g(xi)*np.sin(ni*np.pi*xi/L),0,L)[0]

for i in np.arange(0 ,nx):
    for j in np.arange (0,nt) :
        uu = 0.0
        for ni in np.arange (1, nmax+1):
            uu = uu + un(x[i],a[ni-1],b[ni-1],ni,L,t[j])
        u[i,j] = uu

x,t = np.meshgrid(x,t)

fig = plt.figure()
ax = fig.add_subplot (projection= '3d')
surf = ax.plot_surface(x, t, u.T, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Wave Equation - Analytical Solution')
plt.show()