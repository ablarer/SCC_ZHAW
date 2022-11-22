import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

x = np.arange(-np.pi, np.pi + 0.01, 0.1)
y = np.arange(-np.pi, np.pi + 0.01, 0.1)
x, y = np.meshgrid(x, y)
z1 = x ** 2 - y ** 2
z2 = x * y ** 2. * (np.sin(x) + np.sin(y))

fig1 = plt.figure()
ax1 = fig1.add_subplot(projection='3d')
surf = ax1.plot_surface(x, y, z1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('f(x,y) = x ** 2 - y ** 2')
plt.show()

fig2 = plt.figure()
ax2 = fig2.add_subplot(projection='3d')
surf = ax2.plot_surface(x,y, z2, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('x * y ** 2 * (math.sin(x) + math.sin(y))')
plt.show()

