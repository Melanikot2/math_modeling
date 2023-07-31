import matplotlib.pyplot as plt
import numpy as np

def hyperbola(k, a, N, x_min, x_max):
    x = np.linspace(x_min, x_max, N)
    y = k / x + a

    plt.plot(x, y, color='teal', marker='$f$', ms=20)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Hyperbola')
    plt.savefig('lab_6_osn_task2.png')

hyperbola(k=1, a=5, N=10, x_min=1, x_max=2)
