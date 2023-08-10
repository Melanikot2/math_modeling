import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

phi = np.linspace(0, 2*np.pi, 1000)
theta = np.linspace(0, 4*np.pi, 1000)

a = 780
b = 570
h = 1000

x = a * np.outer(phi, np.cos(theta))
y = b * np.outer(phi, np.sin(theta))
z = np.outer(h, theta)

ax.plot_surface(x, y, z)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_title('Helicoid')

plt.savefig('Helicoid.png')