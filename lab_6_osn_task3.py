import matplotlib.pyplot as plt
import numpy as np

def ellips(N, a, b):
    x = np.linspace(-a, a, N)
    y = np.linspace(-b, b, N)

    X, Y = np.meshgrid(x, y)

    f_xy = X ** 2 / a ** 2 + Y ** 2 / b ** 2 - 1

    plt.contour(X, Y, f_xy, levels=0)
    plt.axis('equal')
    plt.savefig('lab_6_osn_task3.png')

ellips(N=40, a=10, b=3)