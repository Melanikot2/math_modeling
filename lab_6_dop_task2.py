import matplotlib.pyplot as plt
import numpy as np
import random

def ell(e, p):
    f = np.linspace(0, 360, 500)
    X = []
    Y = []
    for i in f:
        x = np.cos(p / (1 + e * np.cos(i)))
        y = np.sin(p / (1 + e * np.cos(i)))
        X.append(x)
        Y.append(y)
    
    plt.contour(X, Y)
    plt.axis('equal')
    plt.savefig('ell.png')

ell(e=0.9, p=10)