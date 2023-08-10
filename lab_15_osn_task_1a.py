import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

phi = np.linspace(0, 2*np.pi, 10000)
theta = np.linspace(0, np.pi, 10000)

x = np.outer(phi, np.cos(theta))
y = np.outer(phi, np.sin(theta))
z = np.outer(phi, phi)

ax.plot_surface(x, y, z)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_title('Paraboloid')

plt.savefig('Paraboloid.png')