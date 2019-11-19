import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  

'''
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
'''


########## EVOLVE A

data = np.loadtxt("evolve_A.dat")

plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
plt.imshow(data, aspect="auto")
plt.xlabel("Indice x")
plt.ylabel("Indice t")
plt.title("Nx = 30   Ntc")
plt.colorbar(label="$\psi$")

n_datos_t = len(data[:,0])

plt.subplot(1,3,2)
for i in range(0,n_datos_t,n_datos_t//8):
	leyenda = round(i*(1/n_datos_t),2)
	plt.plot(data[i,:], label="t = " + str(leyenda))
	plt.legend(loc='upper right')

plt.savefig("evolve_A.png")



########## EVOLVE B

data = np.loadtxt("evolve_B.dat")

plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
plt.imshow(data, aspect="auto")
plt.xlabel("Indice x")
plt.ylabel("Indice t")
plt.title("Nx = 31   Ntc")
plt.colorbar(label="$\psi$")

n_datos_t = len(data[:,0])

plt.subplot(1,3,2)
for i in range(0,n_datos_t,n_datos_t//8):
	leyenda = round(i*(1/n_datos_t),2)
	plt.plot(data[i,:], label="t = " + str(leyenda))
	plt.legend(loc='upper right')

plt.savefig("evolve_B.png")




########## EVOLVE C

data = np.loadtxt("evolve_C.dat")

plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
plt.imshow(data, aspect="auto")
plt.xlabel("Indice x")
plt.ylabel("Indice t")
plt.title("Nx = 29   Ntc")
plt.colorbar(label="$\psi$")

n_datos_t = len(data[:,0])

plt.subplot(1,3,2)
for i in range(0,n_datos_t,n_datos_t//8):
	leyenda = round(i*(1/n_datos_t),2)
	plt.plot(data[i,:], label="t = " + str(leyenda))
	plt.legend(loc='upper right')

plt.savefig("evolve_C.png")



########## EVOLVE D

data = np.loadtxt("evolve_D.dat")

plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
plt.imshow(data, aspect="auto")
plt.xlabel("Indice x")
plt.ylabel("Indice t")
plt.title("Nx = 29   Ntc-10")
plt.colorbar(label="$\psi$")

n_datos_t = len(data[:,0])

plt.subplot(1,3,2)
for i in range(0,n_datos_t,n_datos_t//8):
	leyenda = round(i*(1/n_datos_t),2)
	plt.plot(data[i,:], label="t = " + str(leyenda))
	plt.legend(loc='upper right')

plt.savefig("evolve_D.png")
