import matplotlib.pyplot as plt 
import numpy as np

phi = np.linspace(0, 8*np.pi, 1000000)

k = 3
r = k * phi ** 0.5

x = r * np.cos(phi)
y = r * np.sin(phi)

plt.plot(x, y)
plt.title('Zhezl Spiral')
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('zhezl_spiral.png')