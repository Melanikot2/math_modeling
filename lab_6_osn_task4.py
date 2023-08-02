import matplotlib.pyplot as plt 
import numpy as np

def arh_spiral(k, N):
    f = np.linspace(0, 8 * np.pi, N)
    x = []
    y = []
    f_xy = []
    for i in range(0, N):
        x.append(k * f[i] * np.cos(f[i]))
        y.append(k * f[i] * np.sin(f[i]))
        X, Y = np.meshgrid(x, y)

        f_xy.append(X ** 2 + Y ** 2 - (k * f[i]) ** 2)

    plt.contour(X, Y, f_xy)
    plt.axis('equal')
    plt.savefig('arh_spiral.png')

arh_spiral(k=1, N=500)

