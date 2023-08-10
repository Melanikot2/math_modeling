import matplotlib.pyplot as plt
import numpy as np

def func(a, b):
    y = []
    x = np.arange(-5, 5, 0.01)
    for i in x:
        if i < a:
            y.append(a**2)
        elif a <= i and i <= b:
            y.append(i**2)
        else:
            y.append(b**2)
    plt.plot(x, y, color='m')
    plt.title('Func')
    plt.axis('equal')
    plt.savefig('func.png')

func(a=0, b=3)
        