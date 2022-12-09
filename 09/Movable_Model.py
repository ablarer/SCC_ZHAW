# importing modules
from mpl_toolkits import mplot3d
import numpy
from matplotlib import pyplot

# Source:
#
# https://www.geeksforgeeks.org/3d-wireframe-plotting-in-python-using-matplotlib/
#
# Let it run in the terminal.

# assigning coordinates
a = numpy.linspace(-5, 5, 25)
b = numpy.linspace(-5, 5, 25)
x, y = numpy.meshgrid(a, b)
z = numpy.sin(numpy.sqrt(x**2 + y**2))

# creating the visualization
fig = pyplot.figure()
wf = pyplot.axes(projection ='3d')
wf.plot_wireframe(x, y, z, color ='green')

# displaying the visualization
wf.set_title('Example 2')
pyplot.show()