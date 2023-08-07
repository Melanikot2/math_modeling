import matplotlib.pyplot as plt
import numpy as np
import random

def lissazhu(B, t, N, b, a=1, A=1, delta=np.pi/2):
    t = np.linspace(0, t, N)
    X = []
    Y = []
    for i in t:
        x = A * np.sin(a * i + delta)
        y = B * np.sin(b * i)
        X.append(x)
        Y.append(y)
    plt.plot(X, Y)
    plt.title('Lissazhu')
    plt.axis('equal')
    plt.savefig('lissazhu.png')

lissazhu(B=12, t=50, N=500, b=0.6)