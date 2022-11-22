import matplotlib.pyplot as plt
from fontTools.merge import cmap
from matplotlib import cm
import numpy as np
import scipy.integrate as integrate

k=1
L=1

nmax = 40
xmin = 0
xmax = L
tmin = 0
tmax = 0.25

x = np. arange(xmin, xmax, 0.05)
nx = len(x)

t = np. arange (tmin, tmax, 0.01)
nt = len(t)

u = np.zeros ((nx, nt))
b = np.zeros (nmax)

#define functions
def f(xi): return 4. *(xi/L)*(1.-xi/L)
def un(xi,bn,n,L,ti): return bn*np.sin(n*np.pi*xi/L)*np.exp(-n**2* np.pi**2*k*ti/L**2)

#calculate the first nmax coefficients bn
for ni in np.arange (1, nmax+1) :
    def integrand(xi): return f(xi)*np.sin(ni*np.pi*xi/L)
    b[ni-1]=2./L*integrate.quad(integrand,0,L)[0]

for i in np.arange(0, nx) :
    for j in np.arange (0, nt) :
        uu = 0.
        for ni in np.arange (1, nmax+1) :
            uu = uu + un(x[i],b[ni-1],ni,L,t[j])
        u[i,j]=uu

x,t = np.meshgrid(x,t)

fig = plt. figure()
ax = fig.add_subplot (projection= '3d')
surf = ax.plot_surface(x, t, u.T, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.xlabel('X')
plt.ylabel('t')
plt.title('Heat Conduction')
plt.show()