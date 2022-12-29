import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

N = 50
fps = 250
frn = 75

x = np.linspace(-4, 4, N + 1)
x, y = np.meshgrid(x, x)
zarray = np.zeros((N + 1, N + 1, frn))

f = lambda x, y, sig: 1 / np.sqrt(sig) * np.exp(-(x ** 2 + y ** 2) / sig ** 2)

for i in range(frn):
   zarray[:, :, i] = f(x, y, 1.5 + np.sin(i * 2 * np.pi / frn))

def change_plot(frame_number, zarray, plot):
   plot[0].remove()
   plot[0] = ax.plot_surface(x, y, zarray[:, :, frame_number], cmap="afmhot_r")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plot = [ax.plot_surface(x, y, zarray[:, :, 0], color='0.75', rstride=1, cstride=1)]

ax.set_zlim(0, 1.1)
ani = animation.FuncAnimation(fig, change_plot, frn, fargs=(zarray, plot), interval=1000 / fps)

ax.axis('off')

plt.show()