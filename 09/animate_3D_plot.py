import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import matplotlib.animation as animation


Nx = 15
Ny = 15
tol = 1e-3
err = 1
k = 0

Uy0 = 200*np.ones((1,Nx)) # Boundry condition at y=0 # lower boundry
UNy = 200*np.ones((1,Nx)) # Boundry condition at y=Ny # Upper boundary
Ux0 = 200*np.ones(Ny) # Boundry condition at x=0 # left boundry
UNx = 200*np.ones(Ny) # Boundry condition at x=Nx # Right boundary
# initial the whole matrix: the value at the interior nodes
U = np.zeros((Ny,Nx))
#Adding boundry conditions to the matrix
U[0] = UNy
U[Ny-1] = Uy0
U[:,Nx-1] = UNx
U[:,0]= Ux0
# Iterate Jacobi method
UFK=[]
UFK.append(U.copy())
NFK=[]
UF=U.copy()

while True:
    k=k+1
    for i in range (1,Nx-1):
        for j in range (1,Ny-1):
            UF[j,i] = (UF[j+1,i]+UF[j,i+1]+UF[j-1,i]+UF[j,i-1])*0.25 #the matrix i want to plot after each iteration
    UFK.append(UF.copy())
    H = UFK[-1]-UFK[-2]
    N = np.linalg.norm(H)
    NFK.append(N)
    if N <= tol:
        break

def data(t):
    L = UFK[t]
    ax.clear()
    surf = ax.plot_surface(XX, YY, L, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    ax.set_zlim([0,200]) # set zlim to be always the same for every frame


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
X = np.arange(0, Nx)
Y = np.arange(0, Ny)
XX,YY = np.meshgrid(X, Y)
surf = ax.plot_surface(XX, YY, UFK[0],rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax.set_zlim(0, 2)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.set_xlabel('X nodes - Axis')
ax.set_ylabel('Y nodes - Axis')
ax.set_zlabel('Value')
# Figure / Window title: 'Task 1.8 a) Wave equation in 1D - Numerical Solution'

ani = animation.FuncAnimation(fig, data, len(UFK), interval=50, repeat=True )
plt.show()