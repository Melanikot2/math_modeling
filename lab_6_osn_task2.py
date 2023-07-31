import matplotlib.pyplot as plt
import numpy as np

def hyperbola(k, N, x_min, x_max):
    x = np.linspace(x_min, x_max, N)
    y = k / x
    plt.plot(x, y, 'o')
    plt.savefig('lab_6_osn_task2.png')

hyperbola(k=1, N=10, x_min=0.001, x_max=2)
