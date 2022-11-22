from matplotlib import cm, pyplot as plt
import numpy as np
import sympy as sp

sp.init_printing()

x, y = sp.symbols('x y')
f = -((x ** 2 - 1) + (y ** 2 - 4) + (x ** 2 - 1) * (y ** 2 - 4)) / (x ** 2 + y ** 2 + 1) ** 2
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

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
surf = ax.plot_surface(xx, yy, zz, cmap=cm.coolwarm, linewidth=0, antialiased=False)
quiv = ax.quiver(xx, yy, zz, gfx(xx, yy), gfy(xx, yy), (gfx(xx, yy) ** 2 + gfy(xx, yy) ** 2), length=0.1,
                 normalize=True)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('f(x,y)')
plt.show()
