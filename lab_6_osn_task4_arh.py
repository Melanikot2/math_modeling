import matplotlib.pyplot as plt 
import numpy as np

phi = np.linspace(0, 8*np.pi, 1000000)

k = 3
r = k * phi

x = r * np.cos(phi)
y = r * np.sin(phi)

plt.plot(x, y)
plt.title('Arh Spiral')
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('arh_spiral.png')