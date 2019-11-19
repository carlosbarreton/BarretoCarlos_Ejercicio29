import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  

data = np.loadtxt("ejercicio5.dat")
n_datos_x = len(data[0,:])
n_datos_t = len(data[:,0])
x = np.linspace(-1,1,n_datos_x)
t = np.linspace(0,1,n_datos_t)
X, T = np.meshgrid(x, t)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, T, data)

ax.set_xlabel('x')
ax.set_ylabel('t')
ax.set_zlabel('$\psi$')

plt.savefig("pde.png")