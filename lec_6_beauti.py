import matplotlib.pyplot as plt
import numpy as np

x = [3, 4, 5]
y = [40, 10, 30]

plt.plot(x, y, color='g', label='luchte', marker='>', ms=5)

plt.xlabel('Coord: x')
plt.ylabel('Coord: y')
plt.legend()
plt.title('Base')
plt.grid()
plt.savefig('pic_2.png')