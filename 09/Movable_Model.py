# importing modules
from mpl_toolkits import mplot3d
import numpy
from matplotlib import pyplot, pyplot as plt

# Source:
# https://www.geeksforgeeks.org/3d-wireframe-plotting-in-python-using-matplotlib/
# With some changes to the code.
# Let it run in the terminal.

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# assigning coordinates
a = numpy.linspace(-5, 5, 25)
b = numpy.linspace(-5, 5, 25)
x, y = numpy.meshgrid(a, b)

# Set the z axis limits so they aren't recalculated each frame.
ax.set_zlim(-1, 1)


# Begin plotting.
wframe = None

for phi in  numpy.linspace(0, 180. / numpy.pi, 100):
    # If a line collection is already remove it before drawing.
    if wframe:
        wframe.remove()
    # Generate data.
    z = numpy.sin(numpy.sqrt(x**2 + y**2) + phi)
    # Plot the new wireframe and pause briefly before continuing.
    wframe = ax.plot_wireframe(x, y, z, rstride=2, cstride=2)
    plt.pause(0.1)