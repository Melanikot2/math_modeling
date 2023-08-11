import matplotlib.pyplot as plt 
import numpy as np

phi = np.linspace(0, 8*np.pi, 1000000)

b = 0.1
r = np.exp(b * phi)

x = r * np.cos(phi)
y = r * np.sin(phi)

plt.plot(x, y)
plt.title('Log Spiral')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('log_spiral.png')