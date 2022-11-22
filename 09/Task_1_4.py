import numpy as np
from matplotlib import pyplot as plt, cm
from sympy import sin, cos, exp, ln, Pow

x = np.arange(-3, 3.1, .2)
y = np.arange(1, 5.1, 0.1)
x, y = np.meshgrid(x, y)
u1 = np.cos(x ** 2 + 1.0 / (y ** 2))
u2 = (x ** 2 + 1 / (y ** 2)) ** 2

fig1 = plt.figure()
ax1 = fig1.add_subplot(projection='3d')
surf = ax1.plot_surface(x, y, u1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('f(x,y) = cos(x ** 2 + 1.0 / (y ** 2)')
plt.show()

fig2 = plt.figure()
ax2 = fig2.add_subplot(projection='3d')
surf = ax2.plot_surface(x,y, u2, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('(x ** 2 + 1 / (y ** 2)) ** 2')
plt.show()



from matplotlib import cm, pyplot as plt
import numpy as np
import sympy as sp

sp.init_printing()

x, y = sp.symbols('x y')
f = cos(x ** 2 + 1.0 / (y ** 2))
f = sp.Matrix([f])
X = sp.Matrix([x, y])

Df = f.jacobian(X)
print(Df)

# Show that the linear, homogenous PDE of first order is equal to 0:
Df_1 = 1 / x * Df[0] + Pow(y, 3) * Df[1]
print(Df_1)

ff = sp.lambdify((x, y), f)
gfx = sp.lambdify((x, y), Df[0])
gfy = sp.lambdify((x, y), Df[1])

ran = np.arange(-3, 3.1, .2)
[xx, yy] = np.meshgrid(ran, ran)
zz = ff(xx, yy).reshape(len(ran), len(ran))

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
surf = ax.plot_surface(xx, yy, zz, cmap=cm.coolwarm, linewidth=0, antialiased=False)
# quiv = ax.quiver(xx, yy, zz, gfx(xx, yy), gfy(xx, yy), (gfx(xx, yy) ** 2 + gfy(xx, yy) ** 2), length=0.1, normalize=True)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('f(x,y)')
plt.show()
