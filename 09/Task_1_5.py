import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import scipy.integrate as integrate

# Use values of ...
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
#Initial conditions
# u(x, 0) = f(x) = 4 * (x/L) * (1-x/L)
# for x in range  [0, L]
def f(xi): return 4. *(xi/L)*(1.-xi/L)

# u(x, t) = bn * sin((n*pi*x)/L) * e^(-n^2*pi^2*k*t/L**2)
# for x in range  [0, L]
# for t in range [0, 0.25]
# u(x,t) ohne Summe
def un(xi,bn,n,L,ti): return bn*np.sin(n*np.pi*xi/L)*np.exp(-n**2* np.pi**2*k*ti/L**2)

#calculate the first nmax coefficients bn in the range n = 1,...,40
# bn = 2/L * Integrant of f(x) * sin(n*pi*x/L)dx
for ni in np.arange (1, nmax+1) :
    # Integrant of f(x) * sin(n*pi*x/L)dx
    def integrand(xi): return f(xi)*np.sin(ni*np.pi*xi/L)
    # Integrate func from 0 to L
    # 2/L * Integrant
    b[ni-1]=2./L*integrate.quad(integrand,0,L)[0]

# Sum of bn * sin((n*pi*x)/L) * e^(-n^2*pi^2*k*t/L**2)
for i in np.arange(0, nx) :
    for j in np.arange (0, nt) :
        uu = 0.
        for ni in np.arange (1, nmax+1) :
            # u(x,t) = un(...) mit Summe
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