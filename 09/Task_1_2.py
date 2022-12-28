import sympy as sym
import numpy as np
from matplotlib import pyplot as plt, cm
from sympy import sin, cos, exp, ln, Pow
import sympy as sp

x, y = sym.symbols('x, y')

# Equation 1
f = Pow(x, 2) * Pow(y, 4) + exp(x) * cos(y) + 10 * x-2 * Pow(y, 2) + 3
f = sp.Matrix([f])
X = sp.Matrix([x, y])

# Calculates the Jacobian matrix (derivative of a vector-valued function).
# Returns derivativ of x and y
Df = f.jacobian(X)
print(Df)

# Lambdify:
# Convert a SymPy expression into a function that allows for fast numeric evaluation.
ff = sp.lambdify((x, y), f)
gfx = sp.lambdify((x, y), Df[0])
gfy = sp.lambdify((x, y), Df[1])

ran = np.arange(-3, 3.1, .2)
[xx, yy] = np.meshgrid(ran, ran)
zz = ff(xx, yy).reshape(len(ran), len(ran))

# Print slope a x0, y0
print(ff(0,0))

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
surf = ax.plot_surface(xx, yy, zz, cmap=cm.coolwarm, linewidth=0, antialiased=False)
# quiv = ax.quiver(xx, yy, zz, gfx(xx, yy), gfy(xx, yy), 1, length=0.1, normalize=True)
plt.xlabel('X')
plt.ylabel('Y')
plt.title(Df)
plt.show()


# Equation 2
f = x * Pow(y, 2) * (sin(x) + sin(y))
f = sp.Matrix([f])
X = sp.Matrix([x, y])

Df = f.jacobian(X)
print(Df)

ff = sp.lambdify((x, y), f)
gfx = sp.lambdify((x, y), Df[0])
gfy = sp.lambdify((x, y), Df[1])

ran = np.arange(-3, 3.1, .2)
[xx, yy] = np.meshgrid(ran, ran)
zz = ff(xx, yy).reshape(len(ran), len(ran))

# Print slope a x0, y0
print(ff(0,0))

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
surf = ax.plot_surface(xx, yy, zz, cmap=cm.coolwarm, linewidth=0, antialiased=False)
# quiv = ax.quiver(xx, yy, zz, gfx(xx, yy), gfy(xx, yy), 1, length=0.1, normalize=True)
plt.xlabel('X')
plt.ylabel('Y')
plt.title(Df)
plt.show()


# Equation 3
f  = ln(x + Pow(y, 2)) - exp(2 * x * y) + 3 * x
f = sp.Matrix([f])
X = sp.Matrix([x, y])

Df = f.jacobian(X)
print(Df)

ff = sp.lambdify((x, y), f)
gfx = sp.lambdify((x, y), Df[0])
gfy = sp.lambdify((x, y), Df[1])

ran = np.arange(-3, 3.1, .2)
[xx, yy] = np.meshgrid(ran, ran)
zz = ff(xx, yy).reshape(len(ran), len(ran))

# Print slope a x0, y0
print(ff(0,0))

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
surf = ax.plot_surface(xx, yy, zz, linewidth=0, antialiased=False)
# quiv = ax.quiver(xx, yy, zz, gfx(xx, yy), gfy(xx, yy), 1, length=0.1, normalize=True)
plt.xlabel('X')
plt.ylabel('Y')
plt.title(Df[0])
plt.show()

