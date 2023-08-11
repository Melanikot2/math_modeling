import matplotlib.pyplot as plt 
import numpy as np

phi = np.linspace(0, 20*np.pi, 1000000)

k = 5
r = np.sin(k * phi)

x = r * np.cos(phi)
y = r * np.sin(phi)

plt.plot(x, y)
plt.title('Rose')
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('rose.png')