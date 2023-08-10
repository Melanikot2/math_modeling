import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

phi = np.linspace(0, 2*np.pi, 1000)
theta = np.linspace(0, np.pi, 1000)

a = 10
b = 32
c = 15

x = a * np.outer(np.cos(phi), np.sinh(theta))
y = b * np.outer(np.sin(phi), np.sinh(theta))
z = np.outer(c, np.sinh(theta))

ax.plot_surface(x, y, z)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_title('Hyperboloid')

plt.savefig('Hyperboloid.png')